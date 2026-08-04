from __future__ import annotations

import unittest

import numpy as np

from foundations_lab import DATA, dataset_digest, run_lab, train_classifier


class FoundationsLabTests(unittest.TestCase):
    def test_training_beats_declared_baseline(self):
        result = run_lab()
        self.assertTrue(result["acceptance"])
        self.assertGreater(result["accuracy"], result["baseline_accuracy"])
        self.assertLess(result["final_loss"], result["initial_loss"])

    def test_run_is_deterministic(self):
        self.assertEqual(run_lab(), run_lab())

    def test_dataset_contract_rejects_wrong_shape(self):
        with self.assertRaises(ValueError):
            dataset_digest(np.zeros((3, 2), dtype=np.float64))

    def test_invalid_training_configuration_is_rejected(self):
        with self.assertRaises(ValueError):
            train_classifier(DATA, steps=0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
