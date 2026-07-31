from __future__ import annotations

import unittest

import torch

from snip_unsup_001_structure_and_masking import (
    KMeansResult,
    ReconstructionResult,
    fixed_mask,
    run_experiment,
)


class UnsupervisedSelfSupervisedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_experiment()

    def test_dataset_shapes(self) -> None:
        self.assertEqual(self.result["train"].features.shape, (120, 4))
        self.assertEqual(self.result["test"].features.shape, (60, 4))

    def test_kmeans_objective_is_non_increasing(self) -> None:
        clusters = self.result["clusters"]
        self.assertIsInstance(clusters, KMeansResult)
        for previous, current in zip(
            clusters.objective_history,
            clusters.objective_history[1:],
        ):
            self.assertLessEqual(current, previous + 1e-10)

    def test_kmeans_has_three_nonempty_clusters(self) -> None:
        counts = self.result["cluster_counts"]
        self.assertEqual(counts.shape, (3,))
        self.assertTrue((counts > 0).all())
        self.assertEqual(int(counts.sum()), 120)

    def test_centroids_match_assigned_means(self) -> None:
        clusters = self.result["clusters"]
        features = self.result["train"].features
        for index in range(3):
            expected = features[clusters.assignments == index].mean(dim=0)
            torch.testing.assert_close(
                clusters.centroids[index],
                expected,
                rtol=0,
                atol=1e-12,
            )

    def test_mask_construction_masks_every_example(self) -> None:
        mask = fixed_mask(60, seed=202)
        self.assertTrue(mask.any(dim=1).all())
        self.assertTrue((~mask).any(dim=1).all())

    def test_masked_reconstruction_loss_decreases(self) -> None:
        result = self.result["reconstruction"]
        self.assertIsInstance(result, ReconstructionResult)
        self.assertLess(result.final_loss, result.initial_loss)

    def test_reconstruction_beats_mean_baseline_on_fixed_test(self) -> None:
        result = self.result["reconstruction"]
        self.assertLess(result.test_loss, result.mean_baseline_loss)

    def test_embedding_shape(self) -> None:
        result = self.result["reconstruction"]
        self.assertEqual(result.embedding_shape, (60, 2))

    def test_run_is_deterministic(self) -> None:
        repeated = run_experiment()
        first_clusters = self.result["clusters"]
        second_clusters = repeated["clusters"]
        torch.testing.assert_close(
            first_clusters.centroids,
            second_clusters.centroids,
            rtol=0,
            atol=0,
        )
        self.assertEqual(
            self.result["reconstruction"].test_loss,
            repeated["reconstruction"].test_loss,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
