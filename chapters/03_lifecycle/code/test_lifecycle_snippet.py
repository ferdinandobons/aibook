from __future__ import annotations

import unittest

import torch

from snip_life_001_split_train_monitor import (
    accuracy,
    build_dataset,
    load_model,
    train_candidate,
)


class LifecycleSnippetTests(unittest.TestCase):
    def test_splits_are_disjoint_and_complete(self) -> None:
        x, _, split = build_dataset()
        all_indices = torch.cat([split.train, split.validation, split.test])
        self.assertEqual(len(all_indices), len(x))
        self.assertEqual(len(torch.unique(all_indices)), len(x))

    def test_validation_selects_the_better_candidate(self) -> None:
        x, y, split = build_dataset()
        results = {
            learning_rate: train_candidate(x, y, split, learning_rate)
            for learning_rate in (0.0005, 0.1)
        }
        chosen_lr = max(results, key=lambda learning_rate: results[learning_rate][1])
        self.assertEqual(chosen_lr, 0.1)
        self.assertGreater(results[0.1][1], results[0.0005][1])

    def test_test_set_is_used_after_selection(self) -> None:
        x, y, split = build_dataset()
        state, _ = train_candidate(x, y, split, 0.1)
        model = load_model(state)
        self.assertGreaterEqual(accuracy(model, x[split.test], y[split.test]), 0.95)

    def test_shift_metric_detects_changed_first_feature(self) -> None:
        x, _, split = build_dataset()
        train_mean = x[split.train].mean(dim=0)
        train_std = x[split.train].std(dim=0).clamp_min(1e-6)
        production_batch = x[split.test] + torch.tensor([0.8, 0.0])
        shift = (production_batch.mean(dim=0) - train_mean).abs() / train_std
        self.assertGreater(float(shift[0]), float(shift[1]))


if __name__ == "__main__":
    unittest.main()
