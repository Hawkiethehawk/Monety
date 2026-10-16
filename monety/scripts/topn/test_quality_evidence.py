from __future__ import annotations

import csv
import json
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

from audit_topn_data import audit
from evaluate_evidence import evaluate
from report_io import parse_date_range_from_filename


class QualityAndEvidenceTests(unittest.TestCase):
    def make_dataset(self, root: Path, trust_status: str = "observed", days: int = 28) -> tuple[Path, Path]:
        csv_path = root / "normalized.csv"
        rows = []
        start = date(2026, 1, 1)
        change_at = max(days // 2, 1)
        for offset in range(days):
            value = 100 if offset < change_at else 200
            rows.append({
                "date": (start + timedelta(days=offset)).isoformat(),
                "estimated_revenue": value,
                "impressions": value * 100,
                "estimated_ecpm": 10,
            })
        with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        definitions = {
            "date": {"kind": "dimension", "data_type": "date"},
            "estimated_revenue": {"kind": "metric", "data_type": "currency", "aggregation": "sum_same_currency_mutually_exclusive_grain"},
            "impressions": {"kind": "metric", "data_type": "number", "aggregation": "sum_mutually_exclusive_grain", "unit": "impressions"},
            "estimated_ecpm": {"kind": "metric", "data_type": "currency_per_thousand_impressions", "aggregation": "recompute_from_estimated_revenue_and_impressions", "formula": "estimated_revenue / impressions * 1000"},
        }
        metadata = {
            "normalized_data_path": str(csv_path),
            "normalized_fields": list(rows[0]),
            "normalized_row_count": len(rows),
            "metric_definitions": definitions,
            "trust_status": trust_status,
            "report_type": {"id": "comprehensive_report", "name": "综合报表"},
            "date_range": {"start": rows[0]["date"], "end": rows[-1]["date"], "distinct_days": days},
            "formula_reconciliation": {"checked_values": 28, "mismatched_values": 0},
            "issues": [],
        }
        metadata_path = root / "metadata.json"
        metadata_path.write_text(json.dumps(metadata, ensure_ascii=False), encoding="utf-8")
        return csv_path, metadata_path

    def test_filename_date_range_is_generic(self) -> None:
        self.assertEqual(
            parse_date_range_from_filename("TopOn_聚合管理_20250102-20250304 (2).xlsx"),
            {"start": "2025-01-02", "end": "2025-03-04"},
        )
        self.assertEqual(
            parse_date_range_from_filename("TopOn_聚合管理_20260908.xlsx"),
            {"start": "2026-09-08", "end": "2026-09-08"},
        )

    def test_quality_profile_is_usable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, metadata = self.make_dataset(Path(tmp))
            result = audit(metadata)
            self.assertEqual(result["quality_status"], "usable")
            self.assertEqual(result["dataset_profile"]["candidate_grain"], ["date"])

    def test_adaptive_engine_detects_stable_change(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _, metadata = self.make_dataset(root)
            quality_path = root / "quality.json"
            quality_path.write_text(json.dumps(audit(metadata), ensure_ascii=False), encoding="utf-8")
            result = evaluate(metadata, quality_path, [7, 14], 300, 0.05)
            revenue = next(item for item in result["metric_results"] if item["metric"] == "estimated_revenue")
            self.assertEqual(revenue["selected"]["grade"], "A")
            self.assertTrue(result["method"]["no_fixed_dau_threshold"])

    def test_fixture_is_never_actionable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _, metadata = self.make_dataset(root, "fixture")
            quality_path = root / "quality.json"
            quality_path.write_text(json.dumps(audit(metadata), ensure_ascii=False), encoding="utf-8")
            result = evaluate(metadata, quality_path, [7], 100, 0)
            self.assertEqual(result["overall_grade"], "D")
            self.assertEqual(result["status"], "not_actionable")

    def test_short_windows_are_available_for_test_observation(self) -> None:
        for days in (2, 4, 7):
            with self.subTest(days=days), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                _, metadata = self.make_dataset(root, days=days)
                quality_path = root / "quality.json"
                quality_path.write_text(json.dumps(audit(metadata), ensure_ascii=False), encoding="utf-8")
                result = evaluate(metadata, quality_path, [2, 4, 7], 100, 0)
                self.assertEqual(result["status"], "short_window")
                self.assertEqual(result["overall_grade"], "C")
                revenue = next(item for item in result["metric_results"] if item["metric"] == "estimated_revenue")
                self.assertEqual(revenue["selected"]["window_days"], days)
                self.assertIn(revenue["selected"]["analysis_mode"], {
                    "short_window_descriptive", "short_window_paired_comparison",
                })

    def test_mediation_snapshot_accepts_bidding_price_and_sparse_rows(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            csv_path = root / "normalized_mediation_management.csv"
            rows = [
                {
                    "network": "Admob", "ad_source_id": "1", "sort_price": "竞价",
                    "fill_latency_seconds": "0.75", "estimated_revenue": "1.00", "impressions": "2",
                },
                {
                    "network": "Pangle", "ad_source_id": "2", "sort_price": "3",
                    "fill_latency_seconds": "", "estimated_revenue": "", "impressions": "",
                },
            ]
            with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)
            metadata = root / "metadata.json"
            metadata.write_text(json.dumps({
                "normalized_data_path": str(csv_path),
                "normalized_fields": list(rows[0]),
                "metric_definitions": {
                    "network": {"kind": "dimension", "data_type": "string"},
                    "ad_source_id": {"kind": "dimension", "data_type": "string"},
                    "sort_price": {"kind": "metric", "data_type": "currency_per_thousand_impressions_or_bidding_label", "aggregation": "none"},
                    "fill_latency_seconds": {"kind": "metric", "data_type": "number", "unit": "seconds", "aggregation": "weighted_average_requires_successful_fill_count"},
                    "estimated_revenue": {"kind": "metric", "data_type": "currency", "aggregation": "sum_same_currency_mutually_exclusive_grain"},
                    "impressions": {"kind": "metric", "data_type": "number", "unit": "impressions", "aggregation": "sum_mutually_exclusive_grain"},
                },
                "trust_status": "observed",
                "report_type": {"id": "mediation_management_report", "name": "聚合管理报表"},
                "report_period_from_filename": {"start": "2026-09-08", "end": "2026-09-08"},
                "issues": [],
            }, ensure_ascii=False), encoding="utf-8")
            result = audit(metadata)
            codes = {item["code"] for item in result["findings"]}
            self.assertEqual(result["quality_status"], "usable")
            self.assertNotIn("numeric_parse_failures", codes)
            self.assertNotIn("non_integer_count_metric", codes)
            self.assertIn("expected_sparse_mediation_metrics", codes)


if __name__ == "__main__":
    unittest.main()
