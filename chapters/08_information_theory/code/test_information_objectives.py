from __future__ import annotations

import unittest

import torch
import torch.nn.functional as F

from snip_info_001_cross_entropy import cross_entropy, entropy, kl_divergence


class InformationObjectivesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.logits = torch.tensor([2.0, 0.5, -1.0], dtype=torch.float64)
        self.target_index = torch.tensor(0)
        self.probabilities = torch.softmax(self.logits, dim=0)

    def test_probabilities_sum_to_one(self) -> None:
        self.assertAlmostEqual(self.probabilities.sum().item(), 1.0)

    def test_manual_nll_matches_cross_entropy(self) -> None:
        manual = -torch.log_softmax(self.logits, dim=0)[0]
        api = F.cross_entropy(
            self.logits.unsqueeze(0),
            self.target_index.unsqueeze(0),
        )
        torch.testing.assert_close(manual, api, rtol=0.0, atol=1e-12)

    def test_cross_entropy_decomposes_into_entropy_plus_kl(self) -> None:
        target = torch.tensor([0.90, 0.05, 0.05], dtype=torch.float64)
        ce = cross_entropy(target, self.probabilities)
        h = entropy(target)
        kl = kl_divergence(target, self.probabilities)
        torch.testing.assert_close(ce, h + kl, rtol=0.0, atol=1e-12)

    def test_one_hot_cross_entropy_equals_kl(self) -> None:
        target = torch.tensor([1.0, 0.0, 0.0], dtype=torch.float64)
        ce = cross_entropy(target, self.probabilities)
        kl = kl_divergence(target, self.probabilities)
        torch.testing.assert_close(ce, kl, rtol=0.0, atol=1e-12)

    def test_gradient_is_probability_minus_one_hot_target(self) -> None:
        logits = self.logits.clone().requires_grad_(True)
        loss = F.cross_entropy(
            logits.unsqueeze(0),
            self.target_index.unsqueeze(0),
        )
        loss.backward()
        expected = torch.softmax(logits.detach(), dim=0) - torch.tensor(
            [1.0, 0.0, 0.0],
            dtype=torch.float64,
        )
        torch.testing.assert_close(logits.grad, expected, rtol=0.0, atol=1e-12)

    def test_wrong_confident_prediction_has_larger_loss(self) -> None:
        correct = F.cross_entropy(
            self.logits.unsqueeze(0),
            self.target_index.unsqueeze(0),
        )
        wrong_logits = torch.tensor([-1.0, 0.5, 2.0], dtype=torch.float64)
        wrong = F.cross_entropy(
            wrong_logits.unsqueeze(0),
            self.target_index.unsqueeze(0),
        )
        self.assertGreater(wrong.item(), correct.item())
        self.assertAlmostEqual(wrong.item() - correct.item(), 3.0)

    def test_log_softmax_stays_finite_for_large_logits(self) -> None:
        large = torch.tensor([1000.0, 999.0, 998.0], dtype=torch.float64)
        naive = torch.exp(large) / torch.exp(large).sum()
        stable = torch.log_softmax(large, dim=0)
        self.assertTrue(torch.isnan(naive).all())
        self.assertTrue(torch.isfinite(stable).all())


if __name__ == "__main__":
    unittest.main(verbosity=2)
