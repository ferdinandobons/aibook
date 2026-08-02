from __future__ import annotations

import unittest
from snip_30_contract import normalize, weighted_state

class ContractTests(unittest.TestCase):
    def test_weights_sum_to_one(self):
        self.assertAlmostEqual(sum(normalize([1.0, 0.0, -1.0])), 1.0)

    def test_output_dimension(self):
        self.assertEqual(len(weighted_state([0.0, 0.0], [[1.0, 2.0], [3.0, 4.0]])), 2)

    def test_invalid_shapes_are_rejected(self):
        with self.assertRaises(ValueError):
            weighted_state([0.0], [[1.0], [2.0]])

if __name__ == "__main__":
    unittest.main(verbosity=2)
