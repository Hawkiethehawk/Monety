#!/usr/bin/env python3
"""Regression tests for the TopOn Open API collection planner."""

from __future__ import annotations

import json
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

from plan_open_api_collection import CATALOG_PATH, build_plan, context_app_ids
from execute_open_api_call import build_headers, encode_body, is_allowlisted, unresolved


class OpenApiPlanTests(unittest.TestCase):
    def test_catalog_is_machine_readable_and_open_api_first(self) -> None:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        self.assertEqual(catalog["source_precedence"][0]["source"], "open_api_reporting")
        self.assertIn("comprehensive", catalog["reporting_datasets"])
        self.assertIn("waterfall_units", catalog["configuration_reads"])
        self.assertEqual(catalog["defaults"]["currency"], "USD")
        self.assertEqual(catalog["defaults"]["timezone"], "UTC+0")

    def test_daily_plan_has_separate_dimension_slices(self) -> None:
        with TemporaryDirectory() as temp_dir:
            plan = build_plan(Path(temp_dir), date(2026, 7, 1), date(2026, 7, 20), ["app-1"], "daily", "USD", "UTC+0", False)
        ids = {call["id"] for call in plan["calls"]}
        self.assertIn("fullreport_core", ids)
        self.assertIn("fullreport_supply", ids)
        self.assertIn("fullreport_traffic_group", ids)
        self.assertTrue(all(call["read_only"] for call in plan["calls"]))

    def test_missing_app_blocks_report_calls_but_allows_config_discovery(self) -> None:
        with TemporaryDirectory() as temp_dir:
            plan = build_plan(Path(temp_dir), date(2026, 7, 1), date(2026, 7, 2), [], "daily", "USD", "UTC+0", True)
        by_id = {call["id"]: call for call in plan["calls"]}
        self.assertFalse(by_id["fullreport_core"]["enabled"])
        self.assertTrue(by_id["config_apps"]["enabled"])

    def test_hourly_span_over_ten_days_is_explicitly_blocked(self) -> None:
        with TemporaryDirectory() as temp_dir:
            plan = build_plan(Path(temp_dir), date(2026, 7, 1), date(2026, 7, 20), ["app-1"], "hourly", "USD", "UTC+0", False)
        call = plan["calls"][0]
        self.assertFalse(call["enabled"])
        self.assertTrue(any("10 天" in reason for reason in call["blocked_by"]))

    def test_context_app_shapes(self) -> None:
        apps = context_app_ids({"apps": ["a", {"app_id": "b"}, {"id": "c"}, "a"]})
        self.assertEqual(apps, ["a", "b", "c"])

    def test_signature_is_deterministic_and_query_is_not_in_resource(self) -> None:
        body = encode_body({"enddate": 20260720, "startdate": 20260701}, "POST")
        headers = build_headers("POST", "/v2/fullreport", body, "fixture-key", 1700000000000)
        self.assertEqual(headers["X-Up-Signature"], "92706F1E1D41D56E9008575A6547E95E")
        self.assertNotIn("fixture-key", headers["X-Up-Signature"])

    def test_executor_allowlist_blocks_write_surface(self) -> None:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        self.assertTrue(is_allowlisted("POST", "/v2/fullreport", catalog))
        self.assertTrue(is_allowlisted("GET", "/v3/mediation_group/demo-placement", catalog))
        self.assertFalse(is_allowlisted("PUT", "/v3/waterfall/units", catalog))
        self.assertFalse(is_allowlisted("POST", "/v3/units", catalog))
        self.assertTrue(unresolved({"path": "/v3/mediation_group/:placement_id"}))


if __name__ == "__main__":
    unittest.main()
