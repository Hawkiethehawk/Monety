#!/usr/bin/env python3
"""Grade TopOn metric changes with adaptive windows, noise and uncertainty."""

from __future__ import annotations

import argparse
import ast
import csv
import json
import math
import random
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable


SKIP_FORMULA_TOKENS = {"report_total_estimated_revenue", "report_total_impressions", "report_total_clicks", "report_total_revenue_api", "report_total_impressions_api", "fills_at_current_grain"}
SHORT_WINDOW_DAYS = (2, 4, 7)
MIN_PAIRED_HISTORY_DAYS = 14


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def num(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def formula_names(formula: str) -> set[str]:
    if not formula:
        return set()
    try:
        tree = ast.parse(formula, mode="eval")
    except SyntaxError:
        return set()
    return {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}


def evaluate_formula(formula: str, values: dict[str, float]) -> float | None:
    """Evaluate the catalog's arithmetic-only formulas."""
    try:
        tree = ast.parse(formula, mode="eval")
    except SyntaxError:
        return None

    def walk(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.Name):
            return float(values[node.id])
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            left, right = walk(node.left), walk(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if right == 0:
                raise ZeroDivisionError
            return left / right
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = walk(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        raise ValueError("unsupported expression")

    try:
        result = walk(tree)
    except (KeyError, ValueError, ZeroDivisionError, OverflowError):
        return None
    return result if math.isfinite(result) else None


def percentile(values: list[float], probability: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] * (upper - position) + ordered[upper] * (position - lower)


def daily_values(rows: list[dict[str, str]], definitions: dict[str, Any]) -> tuple[list[str], dict[str, dict[str, float]], int]:
    event_rows = [row for row in rows if not row.get("statistic_type") or row.get("statistic_type") == "event_count"]
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in event_rows:
        if row.get("date"):
            grouped[row["date"]].append(row)
    dates = sorted(grouped)
    result: dict[str, dict[str, float]] = {}
    max_rows_per_day = max((len(items) for items in grouped.values()), default=0)
    for day, items in grouped.items():
        aggregates: dict[str, float] = {}
        for field, definition in definitions.items():
            values = [num(row.get(field)) for row in items]
            values = [value for value in values if value is not None]
            if not values or definition.get("kind") != "metric":
                continue
            aggregation = str(definition.get("aggregation", ""))
            dtype = definition.get("data_type")
            if dtype in {"number", "currency"} and ("sum" in aggregation or "depends_on_statistic_type" in aggregation):
                aggregates[field] = sum(values)
            elif len(items) == 1:
                aggregates[field] = values[0]
        for field, definition in definitions.items():
            formula = definition.get("formula") or ""
            names = formula_names(formula)
            if formula and names and not (names & SKIP_FORMULA_TOKENS) and names.issubset(aggregates):
                value = evaluate_formula(formula, aggregates)
                if value is not None:
                    aggregates[field] = value
        result[day] = aggregates
    return dates, result, max_rows_per_day


def aggregate_metric(days: list[str], daily: dict[str, dict[str, float]], metric: str, definition: dict[str, Any]) -> float | None:
    formula = definition.get("formula") or ""
    names = formula_names(formula)
    if formula and names and not (names & SKIP_FORMULA_TOKENS):
        totals: dict[str, float] = {}
        for name in names:
            values = [daily[day].get(name) for day in days]
            if any(value is None for value in values):
                return None
            totals[name] = sum(float(value) for value in values if value is not None)
        return evaluate_formula(formula, totals)
    values = [daily[day].get(metric) for day in days]
    if any(value is None for value in values) or not values:
        return None
    aggregation = str(definition.get("aggregation", ""))
    if definition.get("data_type") in {"number", "currency"} and ("sum" in aggregation or "depends_on_statistic_type" in aggregation):
        return sum(float(value) for value in values if value is not None)
    return statistics.fmean(float(value) for value in values if value is not None)


def bootstrap_deltas(
    baseline_days: list[str], current_days: list[str], daily: dict[str, dict[str, float]],
    metric: str, definition: dict[str, Any], iterations: int, seed: int,
) -> list[float]:
    rng = random.Random(seed)
    deltas: list[float] = []
    for _ in range(iterations):
        before = [rng.choice(baseline_days) for _ in baseline_days]
        after = [rng.choice(current_days) for _ in current_days]
        before_value = aggregate_metric(before, daily, metric, definition)
        after_value = aggregate_metric(after, daily, metric, definition)
        if before_value is None or after_value is None:
            continue
        # Equal-length windows: totals and means have the same directional uncertainty.
        deltas.append(after_value - before_value)
    return deltas


def noise_floor(dates: list[str], daily: dict[str, dict[str, float]], metric: str) -> float:
    changes: list[float] = []
    values = [daily[day].get(metric) for day in dates]
    for previous, current in zip(values, values[1:]):
        if previous is None or current is None or previous == 0:
            continue
        changes.append((current - previous) / abs(previous))
    if len(changes) < 4:
        return 0.0
    median = statistics.median(changes)
    mad = statistics.median(abs(value - median) for value in changes)
    return min(5.0, 1.4826 * mad)


def grade_window(
    metric: str, definition: dict[str, Any], baseline_days: list[str], current_days: list[str],
    dates: list[str], daily: dict[str, dict[str, float]], iterations: int,
    minimum_relative_change: float,
) -> dict[str, Any]:
    before = aggregate_metric(baseline_days, daily, metric, definition)
    after = aggregate_metric(current_days, daily, metric, definition)
    if before is None or after is None:
        return {"grade": "D", "reason": "当前窗口缺少连续可计算的字段或公式分母。"}
    delta = after - before
    relative = None if before == 0 else delta / abs(before)
    samples = bootstrap_deltas(baseline_days, current_days, daily, metric, definition, iterations, 20260721 + len(current_days) + sum(map(ord, metric)))
    ci95 = [percentile(samples, 0.025), percentile(samples, 0.975)]
    ci80 = [percentile(samples, 0.10), percentile(samples, 0.90)]
    noise = noise_floor(dates, daily, metric)
    threshold = max(minimum_relative_change, noise)
    effect_ok = relative is not None and abs(relative) >= threshold
    excludes_zero_95 = None not in ci95 and (ci95[0] > 0 or ci95[1] < 0)
    excludes_zero_80 = None not in ci80 and (ci80[0] > 0 or ci80[1] < 0)
    if excludes_zero_95 and effect_ok:
        grade, reason = "A", "95% 自助法区间方向一致，且变化超过历史噪声与业务最小变化。"
    elif excludes_zero_80 and effect_ok:
        grade, reason = "B", "80% 自助法区间方向一致，且变化超过历史噪声与业务最小变化。"
    else:
        grade, reason = "C", "方向、效应大小或不确定性尚未同时通过阈值。"
    return {
        "grade": grade, "reason": reason,
        "baseline_value": before, "current_value": after,
        "absolute_change": delta, "relative_change": relative,
        "confidence_interval_95_for_change": ci95,
        "confidence_interval_80_for_change": ci80,
        "historical_noise_floor": noise,
        "practical_relative_change_threshold": threshold,
        "bootstrap_samples": len(samples),
    }


def short_window_description(
    metric: str, definition: dict[str, Any], window_days: list[str],
    daily: dict[str, dict[str, float]],
) -> dict[str, Any]:
    """Return descriptive statistics for one 2/4/7-day observation window."""
    window_value = aggregate_metric(window_days, daily, metric, definition)
    first_value = aggregate_metric([window_days[0]], daily, metric, definition)
    last_value = aggregate_metric([window_days[-1]], daily, metric, definition)
    absolute_change = None if first_value is None or last_value is None else last_value - first_value
    relative_change = (
        None if absolute_change is None or first_value in (None, 0)
        else absolute_change / abs(first_value)
    )
    if absolute_change is None or absolute_change == 0:
        direction = "flat" if absolute_change == 0 else None
    else:
        direction = "up" if absolute_change > 0 else "down"
    return {
        "grade": "C",
        "reason": "只有一个短观察窗口；输出窗口汇总和首末日变化，不作长期稳定性或因果结论。",
        "analysis_mode": "short_window_descriptive",
        "window_value": window_value,
        "first_day_value": first_value,
        "last_day_value": last_value,
        "absolute_change": absolute_change,
        "relative_change": relative_change,
        "direction": direction,
        "confidence_interval_95_for_change": None,
        "confidence_interval_80_for_change": None,
        "historical_noise_floor": None,
        "practical_relative_change_threshold": None,
        "bootstrap_samples": 0,
    }


def cap_short_comparison(candidate: dict[str, Any]) -> dict[str, Any]:
    """Keep paired short-window calculations, but prevent them from becoming A/B claims."""
    raw_grade = candidate.get("grade")
    output = {**candidate, "grade": "C"}
    if raw_grade and raw_grade != "C":
        output["uncapped_grade"] = raw_grade
    output["reason"] = (
        str(candidate.get("reason") or "")
        + " 该窗口少于 14 个可用日期，最终按短窗口观察级别 C 输出。"
    )
    output["analysis_mode"] = "short_window_paired_comparison"
    return output


def evaluate(metadata_path: Path, quality_path: Path | None, windows: list[int], iterations: int, minimum_relative_change: float) -> dict[str, Any]:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    quality = json.loads(quality_path.read_text(encoding="utf-8")) if quality_path and quality_path.exists() else None
    rows = read_rows(Path(metadata["normalized_data_path"]))
    definitions = metadata.get("metric_definitions", {})
    dates, daily, max_rows_per_day = daily_values(rows, definitions)
    grade_cap = (quality or {}).get("evidence_grade_cap")
    trust = metadata.get("trust_status")
    report_type = metadata.get("report_type") or {}
    report_period = metadata.get("report_period_from_filename") or metadata.get("date_range")

    if trust == "fixture" or grade_cap == "D":
        return {
            "contract_version": 1, "status": "not_actionable", "overall_grade": "D",
            "reason": "数据被标记为结构样例或质量审计阻断，只能测试流程。",
            "source_metadata": str(metadata_path.resolve()), "metric_results": [],
        }
    if not dates:
        if report_type.get("id") == "mediation_management_report" and report_period:
            return {
                "contract_version": 1, "status": "snapshot_only", "overall_grade": "C",
                "reason": "聚合管理报表是按文件日期保存的广告源快照，没有逐行日期；可做横截面结构分析，不构造时间趋势。",
                "source_metadata": str(metadata_path.resolve()), "available_days": 1,
                "analysis_scope": "single_snapshot", "snapshot_period": report_period,
                "metric_results": [],
            }
        return {
            "contract_version": 1, "status": "insufficient_history", "overall_grade": "D",
            "reason": "没有可解析日期，无法形成时间窗口；先补充日期列或文件日期上下文。",
            "source_metadata": str(metadata_path.resolve()), "available_days": len(dates), "metric_results": [],
        }
    if len(dates) == 1:
        return {
            "contract_version": 1, "status": "snapshot_only", "overall_grade": "C",
            "reason": "只有一个可用日期；可做单日观察，不形成趋势或因果结论。",
            "source_metadata": str(metadata_path.resolve()), "available_days": 1,
            "analysis_scope": "single_day", "metric_results": [],
        }

    eligible: list[str] = []
    for field, definition in definitions.items():
        if definition.get("kind") != "metric":
            continue
        formula = definition.get("formula") or ""
        names = formula_names(formula)
        if names & SKIP_FORMULA_TOKENS:
            continue
        aggregation = str(definition.get("aggregation", ""))
        if formula:
            eligible_dates = dates[-min(len(dates), MIN_PAIRED_HISTORY_DAYS):]
            if names and all(all(name in daily[day] for name in names) for day in eligible_dates):
                eligible.append(field)
        elif definition.get("data_type") in {"number", "currency"} and ("sum" in aggregation or "depends_on_statistic_type" in aggregation):
            eligible_dates = dates[-min(len(dates), MIN_PAIRED_HISTORY_DAYS):]
            if all(field in daily[day] for day in eligible_dates):
                eligible.append(field)

    results: list[dict[str, Any]] = []
    rank = {"A": 3, "B": 2, "C": 1, "D": 0}
    requested_windows = sorted({window for window in windows if window > 0})
    short_history = len(dates) < MIN_PAIRED_HISTORY_DAYS
    for metric in eligible:
        candidates: list[dict[str, Any]] = []
        for window in requested_windows:
            if len(dates) < 2 * window:
                if len(dates) >= window:
                    current_days = dates[-window:]
                    candidate = short_window_description(metric, definitions[metric], current_days, daily)
                    candidate.update({
                        "window_days": window,
                        "requested_window_days": window,
                        "current_period": {"start": current_days[0], "end": current_days[-1]},
                    })
                    candidates.append(candidate)
                continue
            baseline_days = dates[-2 * window:-window]
            current_days = dates[-window:]
            candidate = grade_window(metric, definitions[metric], baseline_days, current_days, dates, daily, iterations, minimum_relative_change)
            if short_history:
                candidate = cap_short_comparison(candidate)
            candidate.update({
                "window_days": window,
                "requested_window_days": window,
                "baseline_period": {"start": baseline_days[0], "end": baseline_days[-1]},
                "current_period": {"start": current_days[0], "end": current_days[-1]},
            })
            candidates.append(candidate)
        if not candidates and short_history:
            current_days = dates
            candidate = short_window_description(metric, definitions[metric], current_days, daily)
            candidate.update({
                "window_days": len(current_days),
                "requested_window_days": requested_windows[-1] if requested_windows else None,
                "current_period": {"start": current_days[0], "end": current_days[-1]},
                "window_fallback": True,
            })
            candidates.append(candidate)
        if not candidates:
            continue
        if short_history:
            # For a launch/test snapshot, the requested observation horizon is more useful
            # than selecting a noisy two-day comparison hidden inside a longer short window.
            selected = max(candidates, key=lambda item: item["window_days"])
        else:
            decisive = [item for item in candidates if item["grade"] in {"A", "B"}]
            selected = min(decisive, key=lambda item: item["window_days"]) if decisive else max(candidates, key=lambda item: item["window_days"])
        if grade_cap in rank and rank[selected["grade"]] > rank[grade_cap]:
            selected = {**selected, "uncapped_grade": selected["grade"], "grade": grade_cap,
                        "reason": selected["reason"] + f" 数据质量审计将最终等级限制为 {grade_cap}。"}
        results.append({
            "metric": metric,
            "display_name": definitions[metric].get("display_name", metric),
            "formula": definitions[metric].get("formula"),
            "selected": selected,
            "candidate_windows": candidates,
        })

    overall = min((item["selected"]["grade"] for item in results), key=lambda value: rank[value], default="D")
    if grade_cap in rank and rank.get(overall, 0) > rank[grade_cap]:
        overall = grade_cap
    return {
        "contract_version": 1,
        "status": "short_window" if short_history else "evaluated",
        "overall_grade": overall,
        "reason": (
            "短窗口用于投放测试观察；已输出 2/4/7 日窗口可用范围、窗口汇总和首末日变化，不把结果解释为长期稳定或因果证据。"
            if short_history else None
        ),
        "source_metadata": str(metadata_path.resolve()),
        "quality_audit": str(quality_path.resolve()) if quality_path else None,
        "method": {
            "windows_days": requested_windows, "short_window_days": list(SHORT_WINDOW_DAYS),
            "bootstrap_iterations": iterations,
            "minimum_relative_change": minimum_relative_change,
            "selection": "有独立基线时选择最短的 A/B 级等长窗口；短历史优先保留最长可用的 2/4/7 日观察窗口。",
            "paired_window_rule": "只有至少 2×窗口天数时才做前后周期比较；否则进入单窗口描述模式。",
            "short_window_grade_cap": "可用日期少于 14 天时，短窗口最终等级不超过 C；如存在配对计算，保留 uncapped_grade 供复核。",
            "no_fixed_dau_threshold": True,
            "max_rows_per_day": max_rows_per_day,
        },
        "available_days": len(dates),
        "metric_results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metadata", type=Path)
    parser.add_argument("--quality", type=Path)
    parser.add_argument("--windows", default="2,4,7,14,28,56")
    parser.add_argument("--bootstrap-iterations", type=int, default=2000)
    parser.add_argument("--min-relative-change", type=float, default=0.0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    windows = [int(value) for value in args.windows.split(",") if value.strip()]
    payload = evaluate(args.metadata, args.quality, windows, args.bootstrap_iterations, args.min_relative_change)
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
