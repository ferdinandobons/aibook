"""Test per gli snippet del Capitolo 1."""

from __future__ import annotations

import unittest

from snip_ai_001_training_inference import run_demo


class TrainingInferenceTests(unittest.TestCase):
    def test_training_reduces_loss_and_updates_parameters(self) -> None:
        result = run_demo()
        self.assertLess(result.final_loss, result.initial_loss)
        self.assertTrue(result.training_parameters_changed)

    def test_inference_keeps_parameters_fixed(self) -> None:
        result = run_demo()
        self.assertFalse(result.inference_parameters_changed)

    def test_inference_output_contract(self) -> None:
        result = run_demo()
        self.assertEqual(tuple(result.inference_logits.shape), (1, 2))
        self.assertEqual(result.predicted_class, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
