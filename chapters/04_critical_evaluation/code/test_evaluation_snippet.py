from __future__ import annotations

import unittest

from snip_eval_001_paired_comparison import (
    EXAMPLES,
    accuracy,
    accuracy_by_group,
    paired_bootstrap_difference,
    weighted_error_cost,
)


class EvaluationSnippetTests(unittest.TestCase):
    def test_overall_accuracy_prefers_model_b(self) -> None:
        self.assertAlmostEqual(accuracy(EXAMPLES, "A"), 19 / 24)
        self.assertAlmostEqual(accuracy(EXAMPLES, "B"), 20 / 24)

    def test_urgent_group_prefers_model_a(self) -> None:
        self.assertAlmostEqual(accuracy_by_group(EXAMPLES, "A")["urgent"], 7 / 8)
        self.assertAlmostEqual(accuracy_by_group(EXAMPLES, "B")["urgent"], 5 / 8)

    def test_weighted_cost_prefers_model_a(self) -> None:
        self.assertEqual(weighted_error_cost(EXAMPLES, "A"), 8.0)
        self.assertEqual(weighted_error_cost(EXAMPLES, "B"), 13.0)

    def test_paired_interval_is_deterministic_and_contains_zero(self) -> None:
        observed, lower, upper = paired_bootstrap_difference(EXAMPLES)
        self.assertAlmostEqual(observed, 1 / 24)
        self.assertEqual((round(lower, 3), round(upper, 3)), (-0.208, 0.292))
        self.assertLessEqual(lower, 0.0)
        self.assertGreaterEqual(upper, 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
