from __future__ import annotations

import unittest

from snip_55_contract import contract, weighted_state


class ContractTests(unittest.TestCase):
    def test_contract_is_deterministic(self):
        self.assertEqual(contract(), contract())

    def test_contract_has_invariant(self):
        self.assertIn("invariant", contract())

    def test_contract_has_observable_output(self):
        self.assertGreaterEqual(len(contract()), 2)

    def test_contract_rejects_incoherent_shape(self):
        with self.assertRaises(ValueError):
            weighted_state([0.0], [[1.0, 2.0], [3.0]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
