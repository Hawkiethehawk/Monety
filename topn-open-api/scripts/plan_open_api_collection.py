#!/usr/bin/env python3
"""Build a read-only TopOn Open API collection plan without using credentials."""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = SKILL_ROOT / "references" / "open-api-capabilities.json"


def parse_day(value: str) -> date:
    compact = value.replace("-", "")
    try:
        return datetime.strptime(compact, "%Y%m%d").date()
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"日期必须是 YYYY-MM-DD 或 YYYYMMDD：{value}") from exc


def compact_day(value: date) -> int:
    return int(value.strftime("%Y%m%d"))


def load_context(project_dir: Path) -> dict[str, Any]:
    context_path = project_dir / "context.json"
    if not context_path.exists():
        return {}
    return json.loads(context_path.read_text(encoding="utf-8"))


def context_app_ids(context: dict[str, Any]) -> list[str]:
    result: list[str] = []
    for item in context.get("apps", []):
        if isinstance(item, str):
            value = item
        elif isinstance(item, dict):
            value = item.get("app_id") or item.get("id") or ""
        else:
            value = ""
        if value and value not in result:
            result.append(value)
    return result


def append_call(
    calls: list[dict[str, Any]],
    *,
    call_id: str,
    dataset: str,
    purpose: str,
    method: str,
    path: str,
    payload: dict[str, Any] | None = None,
    query: dict[str, Any] | None = None,
    enabled: bool = True,
    blocked_by: list[str] | None = None,
) -> None:
    calls.append({
        "id": call_id,
        "dataset": dataset,
        "purpose": purpose,
        "method": method,
        "path": path,
        "payload": payload,
        "query": query,
        "enabled": enabled,
        "blocked_by": blocked_by or [],
        "read_only": True,
    })


def build_plan(
    project_dir: Path,
    start_day: date,
    end_day: date,
    app_ids: list[str],
    profile: str,
    currency: str,
    timezone_name: str,
    include_config: bool,
) -> dict[str, Any]:
    if end_day < start_day:
        raise ValueError("end_date 不能早于 start_date")
    if currency not in {"USD", "CNY"}:
        raise ValueError("TopOn 文档只列出 USD、CNY 两种请求币种")
    if timezone_name not in {"UTC-8", "UTC+0", "UTC+8"}:
        raise ValueError("TopOn 报表 API 时区必须是 UTC-8、UTC+0 或 UTC+8")

    apps_known = bool(app_ids)
    app_blocker = [] if apps_known else ["缺少 app_id；先执行配置读取 apps 或在 context.json 登记应用"]
    start_value = compact_day(start_day)
    end_value = compact_day(end_day)
    base_full = {
        "startdate": start_value,
        "enddate": end_value,
        "app_id_list": app_ids,
        "time_zone": timezone_name,
        "metric": ["all"],
        "start": 0,
        "limit": 1000,
    }
    calls: list[dict[str, Any]] = []

    if profile in {"daily", "all"}:
        slices = [
            ("core", ["date", "app", "area"], "用户、收入、流量请求、广告请求、展示、点击、Ready 与竞价的日级主表"),
            ("placement", ["date", "app", "placement", "adformat", "area"], "按广告位和广告样式拆解收入与漏斗"),
            ("supply", ["date", "app", "placement", "network_firm_id", "adsource", "area"], "按广告平台和广告源拆解收入、请求、竞价与 GAP"),
            ("scenario", ["date", "app", "placement", "scenario", "area"], "按广告场景观察到达和 Ready；文档限制下部分请求/API 指标不会返回"),
            ("traffic_group", ["date", "app", "placement", "traffic_group", "area"], "按流量分组观察 TopOn 侧表现；第三方 API 与 Ready 指标受限"),
            ("channel", ["date", "app", "area", "channel"], "按渠道观察新用户、用户与 TopOn 侧变现"),
            ("version", ["date", "app", "sdk_version", "app_version", "area"], "按 SDK 和应用版本定位版本相关变化"),
            ("abtest", ["date", "app", "placement", "abtest", "area"], "按 A/B 测试分组比较表现"),
        ]
        for suffix, group_by, purpose in slices:
            payload = dict(base_full)
            payload["group_by"] = group_by
            append_call(
                calls,
                call_id=f"fullreport_{suffix}",
                dataset="comprehensive",
                purpose=purpose,
                method="POST",
                path="/v2/fullreport",
                payload=payload,
                enabled=apps_known,
                blocked_by=app_blocker,
            )

    if profile in {"hourly", "all"}:
        span_days = (end_day - start_day).days + 1
        append_call(
            calls,
            call_id="hourly_intraday",
            dataset="hourly",
            purpose="小时级请求、填充、展示、点击、预估收益和启动趋势",
            method="POST",
            path="/v3/report/tk_hour",
            payload={
                "start_date": start_value,
                "end_date": end_value,
                "currency": currency,
                "time_zone": timezone_name,
                "app_id_list": app_ids,
                "start": 0,
                "limit": 1000,
            },
            enabled=apps_known and span_days <= 10,
            blocked_by=app_blocker + (["小时报表单次日期跨度不能超过 10 天，执行器需切片"] if span_days > 10 else []),
        )

    if profile in {"cohort", "all"}:
        cohort_common = {
            "start_date": start_value,
            "end_date": end_value,
            "appid_list": app_ids,
            "time_zone": timezone_name,
            "group_by": ["date", "app", "area", "channel"],
            "metric": ["all"],
            "start": 0,
            "limit": 1000,
        }
        append_call(calls, call_id="ltv_1_60", dataset="ltv_1_60", purpose="新增用户 cohort 的第 1-60 天总收益", method="POST", path="/v3/ltvreport", payload=cohort_common, enabled=apps_known, blocked_by=app_blocker)
        append_call(calls, call_id="retention_2_60", dataset="retention_2_60", purpose="新增用户 cohort 的第 2-60 天留存人数", method="POST", path="/v3/retentionreport", payload=cohort_common, enabled=apps_known, blocked_by=app_blocker)
        for index, app_id in enumerate(app_ids, start=1):
            append_call(
                calls,
                call_id=f"new_user_impressions_{index}",
                dataset="new_user_impressions_1_60",
                purpose="单应用新增用户 cohort 的第 1-60 天人均展示",
                method="POST",
                path="/v3/impnewuserreport",
                payload={
                    "start_date": start_value,
                    "end_date": end_value,
                    "app_id_list": [app_id],
                    "time_zone": timezone_name,
                    "group_by": ["date_time", "app_id", "geo_short", "channel"],
                    "start": 0,
                    "limit": 1000,
                },
            )
        if not app_ids:
            append_call(calls, call_id="new_user_impressions", dataset="new_user_impressions_1_60", purpose="单应用新增用户 cohort 的第 1-60 天人均展示", method="POST", path="/v3/impnewuserreport", enabled=False, blocked_by=app_blocker)

    if profile in {"device", "all"}:
        append_call(
            calls,
            call_id="device_report_template",
            dataset="device_impression_click",
            purpose="按应用和日期取得设备级 CSV；执行器需展开为一天一个应用一个请求",
            method="GET",
            path="/v3/devicereport",
            query={"day": "<YYYYMMDD; one day per request>", "app_id": app_ids or ["<app_id>"], "timezone": int(timezone_name.replace("UTC", ""))},
            enabled=False,
            blocked_by=app_blocker + ["需要 TopOn 单独开通设备报表权限", "包含敏感设备标识，需先确认最小化和保留策略"],
        )

    if include_config:
        config_calls = [
            ("config_apps", "apps", "POST", "/v1/apps", "应用主数据", {"start": 0, "limit": 100}),
            ("config_placements", "placements", "POST", "/v1/placements", "广告位主数据", {"start": 0, "limit": 100}),
            ("config_networks", "network_accounts", "GET", "/v1/networks", "广告平台账号及报表 API 配置", None),
            ("config_units", "ad_sources", "GET", "/v3/units/list", "广告源主数据", {"start": 0, "limit": 200}),
            ("config_abtests", "abtests", "GET", "/v3/abtest", "A/B 测试配置快照", {"start": 0, "limit": 100}),
        ]
        for call_id, dataset, method, path, purpose, params in config_calls:
            append_call(calls, call_id=call_id, dataset=dataset, purpose=purpose, method=method, path=path, payload=params if method == "POST" else None, query=params if method == "GET" else None)
        append_call(calls, call_id="config_mediation_template", dataset="mediation_groups", purpose="按广告位展开聚合分组、流量分组和 Waterfall 配置", method="GET", path="/v3/mediation_group/:placement_id", enabled=False, blocked_by=["依赖广告位列表；执行器取得 placement_id 后展开"])

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return {
        "schema_version": "1.0.0",
        "generated_at": now,
        "project_dir": str(project_dir.resolve()),
        "mode": "planning_only_no_network",
        "defaults": {"currency": currency, "timezone": timezone_name},
        "range": {"start_date": start_day.isoformat(), "end_date": end_day.isoformat()},
        "app_ids": app_ids,
        "profile": profile,
        "source_policy": "Open API reporting is primary; manual exports are supplemental and used for reconciliation or unavailable dimensions.",
        "catalog": str(CATALOG_PATH),
        "calls": calls,
        "summary": {
            "total": len(calls),
            "enabled": sum(1 for call in calls if call["enabled"]),
            "blocked": sum(1 for call in calls if not call["enabled"]),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--start-date", type=parse_day, required=True)
    parser.add_argument("--end-date", type=parse_day, required=True)
    parser.add_argument("--app-id", action="append", default=[], help="可重复传入；未传时读取 context.json 的 apps")
    parser.add_argument("--profile", choices=["daily", "hourly", "cohort", "device", "all"], default="all")
    parser.add_argument("--currency", choices=["USD", "CNY"])
    parser.add_argument("--timezone", choices=["UTC-8", "UTC+0", "UTC+8"])
    parser.add_argument("--include-config", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    project_dir = args.project_dir.resolve()
    context = load_context(project_dir)
    app_ids = list(dict.fromkeys(args.app_id or context_app_ids(context)))
    currency = args.currency or context.get("currency") or "USD"
    timezone_name = args.timezone or context.get("timezone") or "UTC+0"
    plan = build_plan(project_dir, args.start_date, args.end_date, app_ids, args.profile, currency, timezone_name, args.include_config)
    serialized = json.dumps(plan, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8", newline="\n")
    print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
