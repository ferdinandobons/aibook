from __future__ import annotations

import json
import math
import unittest

from snip_66_contract import contract


class LessonExampleTests(unittest.TestCase):
    def test_expected_result(self):
        self.assertEqual(contract(), {'short_term': ['ultimo evento'], 'recalled': 'fatto stabile', 'invariant': 'memory scope and retrieval source remain explicit'})

    def test_example_is_deterministic(self):
        self.assertEqual(contract(), contract())

    def test_result_is_serializable_and_finite(self):
        encoded = json.dumps(contract(), sort_keys=True)
        self.assertTrue(encoded)
        for value in contract().values():
            if isinstance(value, float):
                self.assertTrue(math.isfinite(value))

    def test_interpretation_boundary_is_explicit(self):
        self.assertIsInstance(contract().get('invariant'), str)
        self.assertGreaterEqual(len(contract()['invariant'].split()), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
