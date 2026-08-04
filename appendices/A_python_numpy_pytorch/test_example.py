from __future__ import annotations

import math
import unittest

from example import run_example


class NumPyPyTorchExampleTests(unittest.TestCase):
    def test_forward_and_shape(self):
        result = run_example()
        self.assertEqual(result["shape"], [2, 2])
        self.assertEqual(result["forward"], [[0.65, -0.3], [-0.15, 0.55]])

    def test_loss_and_gradients_are_finite(self):
        result = run_example()
        self.assertAlmostEqual(result["loss"], 0.209375, places=6)
        values = [value for row in result["weight_grad"] for value in row]
        values.extend(result["bias_grad"])
        self.assertTrue(all(math.isfinite(value) for value in values))

    def test_example_is_deterministic(self):
        self.assertEqual(run_example(), run_example())


if __name__ == "__main__":
    unittest.main(verbosity=2)
