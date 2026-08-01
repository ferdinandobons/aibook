from __future__ import annotations

import unittest

import torch

from snip_prob_001_bayes_sampling import (
    bayes_update,
    bernoulli_log_likelihood,
    bernoulli_mle,
    delivery_example,
    sampling_summary,
)


class ProbabilityInferenceTests(unittest.TestCase):
    def test_bayes_update_normalizes(self) -> None:
        result = bayes_update(0.20, 0.80, 0.10)
        self.assertAlmostEqual(result.evidence_probability, 0.24)
        self.assertAlmostEqual(result.posterior, 2.0 / 3.0)

    def test_sequential_delivery_update(self) -> None:
        first, second = delivery_example()
        self.assertAlmostEqual(first.posterior, 2.0 / 3.0)
        self.assertAlmostEqual(second.posterior, 0.875)

    def test_bernoulli_mle_is_sample_mean(self) -> None:
        observations = torch.tensor([1, 0, 1, 0, 1, 0, 0, 0], dtype=torch.float64)
        self.assertAlmostEqual(bernoulli_mle(observations), 3.0 / 8.0)

    def test_likelihood_is_maximized_at_sample_mean_on_local_grid(self) -> None:
        observations = torch.tensor([1, 0, 1, 0, 1, 0, 0, 0], dtype=torch.float64)
        candidates = [0.30, 0.35, 0.375, 0.40, 0.45]
        values = [bernoulli_log_likelihood(observations, p) for p in candidates]
        best = candidates[max(range(len(values)), key=values.__getitem__)]
        self.assertEqual(best, 0.375)

    def test_bernoulli_theoretical_moments(self) -> None:
        distribution = torch.distributions.Bernoulli(
            probs=torch.tensor(0.30, dtype=torch.float64)
        )
        self.assertAlmostEqual(distribution.mean.item(), 0.30)
        self.assertAlmostEqual(distribution.variance.item(), 0.21)

    def test_large_sample_is_close_but_not_equal_to_probability(self) -> None:
        summaries = sampling_summary()
        sample_size, sample_mean, sample_variance = summaries[-1]
        self.assertEqual(sample_size, 10_000)
        self.assertLess(abs(sample_mean - 0.30), 0.02)
        self.assertLess(abs(sample_variance - 0.21), 0.02)
        self.assertNotEqual(sample_mean, 0.30)


if __name__ == "__main__":
    unittest.main(verbosity=2)
