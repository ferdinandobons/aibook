from __future__ import annotations
import unittest
from snip_hybrid_001 import checks, demo


class ContractTests(unittest.TestCase):
    def test_demo_is_deterministic(self):
        self.assertEqual(demo(), demo())

    def test_all_contracts_hold(self):
        results = checks()
        self.assertTrue(results)
        self.assertTrue(all(results.values()), results)

    def test_result_is_observable(self):
        self.assertIsInstance(demo(), dict)


if __name__ == "__main__":
    unittest.main(verbosity=2)
