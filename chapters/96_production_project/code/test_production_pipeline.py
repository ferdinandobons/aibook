from __future__ import annotations

import unittest

from production_pipeline import ReleaseCandidate, evaluate_release, run_project


class ProductionPipelineTests(unittest.TestCase):
    def test_healthy_candidate_is_promoted(self):
        self.assertEqual(run_project()["healthy"]["decision"], "promote")

    def test_canary_regression_triggers_rollback(self):
        result = run_project()["regressed_canary"]
        self.assertEqual(result["decision"], "rollback")
        self.assertEqual(result["rollback_target"], "v2")

    def test_offline_slice_regression_blocks_canary_promotion(self):
        candidate = ReleaseCandidate("v4", "ml-platform", 0.90, 0.60, 0.01, "v2")
        self.assertEqual(evaluate_release(candidate)["decision"], "reject_offline")

    def test_missing_owner_is_rejected(self):
        candidate = ReleaseCandidate("v4", "", 0.90, 0.90, 0.01, "v2")
        with self.assertRaises(ValueError):
            evaluate_release(candidate)

    def test_manifest_is_deterministic(self):
        self.assertEqual(run_project(), run_project())


if __name__ == "__main__":
    unittest.main(verbosity=2)
