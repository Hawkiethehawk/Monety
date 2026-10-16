#!/usr/bin/env python3
"""Inspect a TopOn CSV/XLSX report before drawing analytical conclusions."""

from __future__ import annotations

import argparse
from pathlib import Path

from report_io import (
    ADDITIVE_METRICS,
    DIMENSIONS,
    RATIO_METRICS,
    SUPPLEMENTAL_COUNT_METRICS,
    SUPPLEMENTAL_NON_ADDITIVE_METRICS,
    SUPPLEMENTAL_RATIO_METRICS,
    canonical_rows,
    detect_mapping,
    detect_report_type,
    is_summary_row,
    is_sort_price_bidding_label,
    load_mapping,
    parse_date_range_from_filename,
    read_report,
    validate_mapping,
    write_json,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--sheet")
    parser.add_argument("--mapping", help="JSON string or path: canonical_field -> source column")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    headers, rows, source_meta = read_report(args.report, args.sheet)
    detected, conflicts = detect_mapping(headers)
    detected.update(load_mapping(args.mapping))
    mapping_errors = validate_mapping(detected, headers)
    canonical = canonical_rows(rows, detected)
    report_type = detect_report_type(headers, args.report.name)
    report_type_id = report_type["id"] if report_type else None
    is_mediation_report = report_type_id == "mediation_management_report"
    report_period = parse_date_range_from_filename(args.report.name)
    mediation_sparse_fields = {
        "estimated_revenue", "revenue_api", "impressions", "impressions_api", "clicks",
        "estimated_revenue_share", "revenue_api_share", "impression_share", "impressions_api_share",
        "click_share", "clicks_api_share", "estimated_ecpm", "ecpm_api", "ctr", "fill_rate",
        "impression_rate", "impression_gap_rate", "bidding_response_rate", "bidding_response_ecpm",
        "bidding_win_rate", "request_or_bid", "requests", "responses", "fill_latency_seconds",
    }
    mediation_expected_partial_fields = mediation_sparse_fields | {
        "third_party_ad_unit_id", "status", "sort_price",
    }
    date_values = sorted({row.get("date") for row in canonical if row.get("date")})
    null_rates = {}
    for field in detected:
        missing = sum(1 for row in canonical if row.get(field) in (None, ""))
        null_rates[field] = round(missing / len(canonical), 6) if canonical else None

    issues: list[dict] = []
    for error in mapping_errors:
        issues.append({"severity": "error", "code": error["code"], "message": error})
    if not rows:
        issues.append({"severity": "error", "code": "empty_report", "message": "报表没有数据行。"})
    if "date" not in detected:
        issues.append({
            "severity": "info" if is_mediation_report and report_period else "warning",
            "code": "missing_date",
            "message": (
                f"聚合管理报表未提供日期列；已从文件名取得 {report_period['start']} 至 {report_period['end']}，按快照读取。"
                if is_mediation_report and report_period
                else "未识别日期列，无法自动做前后周期比较。"
            ),
        })
    if not any(field in detected for field in ADDITIVE_METRICS):
        issues.append({"severity": "error", "code": "missing_additive_metrics", "message": "未识别请求、填充、展示、点击或收入等可加指标。"})
    if "revenue" not in detected and "estimated_revenue" not in detected and "revenue_api" not in detected:
        issues.append({"severity": "warning", "code": "missing_revenue", "message": "未识别收益、预估收益或收益 API 列，不能分析收入变化。"})
    if "impressions" not in detected:
        issues.append({"severity": "warning", "code": "missing_impressions", "message": "未识别展示列，不能重算 eCPM。"})
    if any(field in detected for field in RATIO_METRICS + SUPPLEMENTAL_RATIO_METRICS) and not any(
        {numerator, denominator}.issubset(detected)
        for numerator, denominator in (("revenue", "impressions"), ("estimated_revenue", "impressions"), ("clicks", "impressions"))
    ):
        issues.append({"severity": "warning", "code": "ratio_without_denominator", "message": "报表含比率或 eCPM，但缺少部分原始分子/分母，汇总结果可能不能加权重算。"})
    for conflict in conflicts:
        issues.append({"severity": "warning", "code": "mapping_conflict", "message": conflict})
    expected_sparse_fields = {}
    for field, rate in null_rates.items():
        if rate == 1.0:
            issues.append({"severity": "error", "code": "unparseable_column", "message": f"字段 {field} 的值全部为空或无法解析。"})
        elif rate is not None and rate > 0:
            if is_mediation_report and field in mediation_expected_partial_fields:
                if field in mediation_sparse_fields:
                    expected_sparse_fields[field] = rate
            else:
                issues.append({"severity": "warning", "code": "partial_nulls", "message": f"字段 {field} 有 {rate:.2%} 的值为空或无法解析。"})

    if expected_sparse_fields:
        issues.append({
            "severity": "info",
            "code": "expected_sparse_mediation_metrics",
            "message": "未请求、未填充或未产生展示的广告源，其对应聚合指标为空属于正常结构；空值不自动当作零值。",
            "fields": expected_sparse_fields,
        })

    if is_mediation_report and "sort_price" in detected:
        labels = sorted({
            str(row.get("sort_price")).strip()
            for row in canonical
            if is_sort_price_bidding_label(row.get("sort_price"))
        })
        if labels:
            issues.append({
                "severity": "info",
                "code": "mixed_sort_price_semantics",
                "message": "“价格”列允许数值排序价格与竞价文本标签共存；竞价标签不参与数值价格比较。",
                "labels": labels,
            })

    for field in ("currency", "timezone", "data_source"):
        values = sorted({str(row.get(field)) for row in canonical if row.get(field) not in (None, "")})
        if len(values) > 1:
            severity = "error"
            issues.append({"severity": severity, "code": f"mixed_{field}", "message": {"field": field, "values": values}})

    row_signatures = [tuple(row.get(field) for field in sorted(detected)) for row in canonical]
    duplicate_count = len(row_signatures) - len(set(row_signatures))
    if duplicate_count:
        issues.append({"severity": "warning", "code": "duplicate_rows", "message": f"发现 {duplicate_count} 行完全重复记录。"})
    negative_counts = {
        metric: sum(1 for row in canonical if row.get(metric) is not None and row[metric] < 0)
        for metric in ADDITIVE_METRICS
    }
    negative_counts = {metric: count for metric, count in negative_counts.items() if count}
    if negative_counts:
        issues.append({"severity": "warning", "code": "negative_metrics", "message": negative_counts})
    inverted_funnel = sum(
        1 for row in canonical
        if row.get("impressions") is not None and row.get("responses") is not None
        and row["impressions"] > row["responses"]
    )
    if inverted_funnel:
        issues.append({"severity": "warning", "code": "impressions_gt_responses", "message": f"有 {inverted_funnel} 行展示数大于返回数，请核对粒度和口径。"})
    summary_rows = sum(1 for row in rows if is_summary_row(row))
    if summary_rows:
        issues.append({
            "severity": "info" if report_type_id in {"comprehensive_report", "mediation_management_report"} else "error",
            "code": "summary_rows",
            "message": (
                f"发现 {summary_rows} 行 TopOn 导出汇总；对应标准化适配器会先隔离，不能与明细重复汇总。"
                if report_type_id in {"comprehensive_report", "mediation_management_report"}
                else f"发现 {summary_rows} 行合计或小计，直接汇总会重复计算。"
            ),
        })
    if date_values:
        from datetime import date as date_type, timedelta
        parsed_dates = [date_type.fromisoformat(item) for item in date_values]
        expected = {(parsed_dates[0] + timedelta(days=offset)).isoformat() for offset in range((parsed_dates[-1] - parsed_dates[0]).days + 1)}
        missing_dates = sorted(expected - set(date_values))
        if missing_dates:
            issues.append({"severity": "warning", "code": "date_gaps", "message": missing_dates})
    if "network" in detected and any(metric in detected for metric in ("requests", "responses")):
        issues.append({
            "severity": "info" if is_mediation_report else "warning",
            "code": "network_funnel_non_additive",
            "message": "广告源级请求/返回可能是瀑布尝试，通常不能跨广告源相加为广告位漏斗。",
        })

    payload = {
        "evidence_type": "observed_input_inspection",
        "report": str(args.report.resolve()),
        "source": source_meta,
        "report_type": None if report_type is None else {
            "id": report_type["id"],
            "name": report_type["name"],
            "grain": report_type["grain"],
            "analysis_rule": report_type["analysis_rule"],
        },
        "row_count": len(rows),
        "columns": headers,
        "mapping": detected,
        "unmapped_columns": [header for header in headers if header not in detected.values()],
        "available_dimensions": [field for field in DIMENSIONS if field in detected],
        "available_metrics": [
            field for field in (
                ADDITIVE_METRICS + RATIO_METRICS + SUPPLEMENTAL_COUNT_METRICS
                + SUPPLEMENTAL_RATIO_METRICS + SUPPLEMENTAL_NON_ADDITIVE_METRICS
                + ("dau", "ad_users")
            ) if field in detected
        ],
        "date_range": {"start": date_values[0], "end": date_values[-1], "distinct_days": len(date_values)} if date_values else None,
        "report_period_from_filename": report_period,
        "null_rates": null_rates,
        "issues": issues,
    }
    write_json(payload, args.output)
    return 2 if any(issue["severity"] == "error" for issue in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
