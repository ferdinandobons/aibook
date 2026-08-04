from __future__ import annotations

import math
import unittest

from example_jax import run_example


class JaxExampleTests(unittest.TestCase):
    def test_shapes(self):
        result = run_example()
        self.assertEqual(result["shape"], [2, 2])
        self.assertEqual(result["gradient_shapes"], {"weight": [2, 2], "bias": [2]})

    def test_values_are_finite(self):
        result = run_example()
        self.assertTrue(math.isfinite(result["loss"]))
        self.assertTrue(all(math.isfinite(value) for row in result["predictions"] for value in row))

    def test_example_is_deterministic(self):
        self.assertEqual(run_example(), run_example())


if __name__ == "__main__":
    unittest.main(verbosity=2)
