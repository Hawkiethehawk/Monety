#!/usr/bin/env python3
"""Dry-run or execute one allowlisted read-only call from a TopOn collection plan."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests


SKILL_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = SKILL_ROOT / "references" / "open-api-capabilities.json"
ALLOWED_HOSTS = {"api.toponad.net", "api.toponad.com", "openapi.toponad.com"}


def uppercase_md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest().upper()


def encode_body(payload: dict[str, Any] | None, method: str) -> bytes:
    if method.upper() == "GET":
        return b""
    return json.dumps(payload or {}, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")


def build_headers(method: str, resource_path: str, body: bytes, publisher_key: str, timestamp_ms: int) -> dict[str, str]:
    method = method.upper()
    content_type = "application/json"
    public_headers = {
        "X-Up-Key": publisher_key,
        "X-Up-Timestamp": str(timestamp_ms),
    }
    header_lines = "\n".join(f"{key}:{public_headers[key]}" for key in sorted(public_headers))
    sign_string = "\n".join([
        method,
        uppercase_md5(body),
        content_type,
        header_lines,
        resource_path,
    ])
    return {
        **public_headers,
        "X-Up-Signature": uppercase_md5(sign_string.encode("utf-8")),
        "Content-Type": content_type,
    }


def path_pattern(path: str) -> re.Pattern[str]:
    escaped = re.escape(path)
    escaped = re.sub(r":[A-Za-z0-9_]+", r"[^/]+", escaped)
    return re.compile(f"^{escaped}$")


def allowlisted_operations(catalog: dict[str, Any]) -> list[tuple[str, re.Pattern[str]]]:
    operations: list[tuple[str, re.Pattern[str]]] = []
    for item in catalog["reporting_datasets"].values():
        operations.append((item["method"].upper(), path_pattern(item["path"])))
    for item in catalog["configuration_reads"].values():
        operations.append((item["method"].upper(), path_pattern(item["path"])))
    return operations


def is_allowlisted(method: str, path: str, catalog: dict[str, Any]) -> bool:
    return any(method.upper() == allowed_method and pattern.fullmatch(path) for allowed_method, pattern in allowlisted_operations(catalog))


def unresolved(value: Any) -> bool:
    if isinstance(value, str):
        return "<" in value or ">" in value or bool(re.search(r"(?:^|/):[A-Za-z0-9_]", value))
    if isinstance(value, dict):
        return any(unresolved(item) for item in value.values())
    if isinstance(value, list):
        return any(unresolved(item) for item in value)
    return False


def select_call(plan: dict[str, Any], call_id: str) -> dict[str, Any]:
    matches = [item for item in plan.get("calls", []) if item.get("id") == call_id]
    if len(matches) != 1:
        raise ValueError(f"计划中未找到唯一调用项：{call_id}")
    return matches[0]


def validate_call(call: dict[str, Any], catalog: dict[str, Any]) -> None:
    method = str(call.get("method", "")).upper()
    path = str(call.get("path", ""))
    if not call.get("read_only"):
        raise ValueError("执行器只接受 read_only=true 的计划项")
    if method not in {"GET", "POST"}:
        raise ValueError(f"执行器拒绝可能修改状态的方法：{method}")
    if not is_allowlisted(method, path, catalog):
        raise ValueError(f"接口未登记为只读能力：{method} {path}")
    if not call.get("enabled"):
        reasons = "；".join(call.get("blocked_by") or ["计划项未启用"])
        raise ValueError(f"计划项仍被阻塞：{reasons}")
    if unresolved({"path": path, "payload": call.get("payload"), "query": call.get("query")}):
        raise ValueError("计划项仍含占位符，拒绝执行")


def safe_base_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS or parsed.path not in {"", "/"}:
        raise ValueError(f"base URL 必须是已登记的 TopOn HTTPS 主机：{sorted(ALLOWED_HOSTS)}")
    return value.rstrip("/")


def dry_run_summary(call: dict[str, Any], base_url: str, key_env: str) -> dict[str, Any]:
    return {
        "mode": "dry_run",
        "call_id": call["id"],
        "method": call["method"],
        "url": f"{base_url}{call['path']}",
        "query": call.get("query"),
        "payload": call.get("payload"),
        "key_env": key_env,
        "publisher_key_available": bool(os.environ.get(key_env)),
        "credentials_printed": False,
        "network_called": False,
    }


def execute_call(call: dict[str, Any], base_url: str, publisher_key: str, timeout_seconds: int) -> tuple[dict[str, Any], Any]:
    method = call["method"].upper()
    path = call["path"]
    body = encode_body(call.get("payload"), method)
    timestamp_ms = int(time.time() * 1000)
    headers = build_headers(method, path, body, publisher_key, timestamp_ms)
    response = requests.request(
        method,
        f"{base_url}{path}",
        headers=headers,
        params=call.get("query"),
        data=body,
        timeout=timeout_seconds,
    )
    try:
        response_body: Any = response.json()
    except ValueError:
        response_body = response.text
    metadata = {
        "call_id": call["id"],
        "method": method,
        "resource_path": path,
        "query": call.get("query"),
        "payload": call.get("payload"),
        "requested_at_ms": timestamp_ms,
        "http_status": response.status_code,
        "publisher_key_logged": False,
        "signature_logged": False,
    }
    return metadata, response_body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--call", required=True, dest="call_id")
    parser.add_argument("--base-url", default="https://api.toponad.net")
    parser.add_argument("--key-env", help="默认按数据集选择 TOPON_REPORT_PUBLISHER_KEY 或 TOPON_MANAGEMENT_PUBLISHER_KEY")
    parser.add_argument("--execute", action="store_true", help="默认只 dry-run；显式传入才访问网络")
    parser.add_argument("--output", type=Path, help="执行时必传，保存脱敏请求摘要和原始响应")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()

    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    call = select_call(plan, args.call_id)
    validate_call(call, catalog)
    base_url = safe_base_url(args.base_url)
    key_env = args.key_env or ("TOPON_REPORT_PUBLISHER_KEY" if call["dataset"] in catalog["reporting_datasets"] else "TOPON_MANAGEMENT_PUBLISHER_KEY")

    if not args.execute:
        print(json.dumps(dry_run_summary(call, base_url, key_env), ensure_ascii=False, indent=2))
        return 0

    if not args.output:
        raise ValueError("执行请求时必须使用 --output 保存审计记录")
    publisher_key = os.environ.get(key_env, "")
    if not publisher_key:
        raise ValueError(f"环境变量 {key_env} 未设置")
    metadata, response_body = execute_call(call, base_url, publisher_key, args.timeout)
    result = {"request": metadata, "response": response_body}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"ok": metadata["http_status"] == 200, "http_status": metadata["http_status"], "output": str(args.output)}, ensure_ascii=False))
    return 0 if metadata["http_status"] == 200 else 1


if __name__ == "__main__":
    raise SystemExit(main())
