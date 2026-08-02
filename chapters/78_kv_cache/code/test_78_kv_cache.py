from __future__ import annotations

import unittest
from snip_78_contract import stable_softmax, weighted_combine

class ContractTests(unittest.TestCase):
    def test_weights_sum_to_one(self):
        self.assertAlmostEqual(sum(stable_softmax([1.0, 0.0, -1.0])), 1.0)

    def test_output_dimension(self):
        self.assertEqual(len(weighted_combine([0.0, 0.0], [[1.0, 2.0], [3.0, 4.0]])), 2)

    def test_invalid_shapes_are_rejected(self):
        with self.assertRaises(ValueError):
            weighted_combine([0.0], [[1.0], [2.0]])

if __name__ == "__main__":
    unittest.main(verbosity=2)
