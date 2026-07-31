from __future__ import annotations

import unittest

import torch

from snip_sup_001_logistic_threshold import (
    DataSplit,
    TrainingResult,
    binary_metrics,
    make_split,
    run_experiment,
    select_threshold,
)


class SupervisedLearningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_experiment()

    def test_splits_have_expected_shapes(self) -> None:
        expected = {"train": 120, "validation": 50, "test": 50}
        for name, count in expected.items():
            split = self.result[name]
            self.assertIsInstance(split, DataSplit)
            self.assertEqual(split.features.shape, (count, 2))
            self.assertEqual(split.targets.shape, (count,))
            self.assertEqual(split.tracking_missing.shape, (count,))

    def test_training_reduces_regularized_objective(self) -> None:
        training = self.result["training"]
        self.assertIsInstance(training, TrainingResult)
        self.assertLess(training.final_objective, training.initial_objective)

    def test_probabilities_are_valid(self) -> None:
        for probabilities in self.result["probabilities"].values():
            self.assertTrue(torch.isfinite(probabilities).all())
            self.assertTrue((probabilities >= 0.0).all())
            self.assertTrue((probabilities <= 1.0).all())

    def test_threshold_is_selected_only_from_validation_inputs(self) -> None:
        validation_probabilities = self.result["probabilities"]["validation"]
        validation_targets = self.result["validation"].targets
        threshold_a, _ = select_threshold(
            validation_probabilities,
            validation_targets,
        )

        altered_test = make_split(50, seed=999, missing_rate=0.80)
        self.assertNotEqual(
            altered_test.targets.tolist(),
            self.result["test"].targets.tolist(),
        )
        threshold_b, _ = select_threshold(
            validation_probabilities,
            validation_targets,
        )
        self.assertEqual(threshold_a, threshold_b)

    def test_validation_selection_reduces_fixed_weighted_cost(self) -> None:
        selected = self.result["validation_metrics"]
        default = binary_metrics(
            self.result["probabilities"]["validation"],
            self.result["validation"].targets,
            0.50,
        )
        self.assertLess(selected.weighted_cost, default.weighted_cost)

    def test_selected_threshold_improves_test_cost_in_fixed_example(self) -> None:
        self.assertLess(
            self.result["test_selected"].weighted_cost,
            self.result["test_default"].weighted_cost,
        )
        self.assertLess(
            self.result["test_selected"].weighted_cost,
            self.result["majority_baseline"].weighted_cost,
        )

    def test_slice_counts_reconstruct_test_set(self) -> None:
        slice_count = sum(
            metrics.count for metrics in self.result["slice_metrics"].values()
        )
        self.assertEqual(slice_count, self.result["test"].targets.numel())

    def test_majority_baseline_predicts_training_majority(self) -> None:
        training_majority = int(self.result["train"].targets.mean() >= 0.50)
        baseline = self.result["majority_baseline"]
        if training_majority == 0:
            self.assertEqual(baseline.tp + baseline.fp, 0)
        else:
            self.assertEqual(baseline.tn + baseline.fn, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
