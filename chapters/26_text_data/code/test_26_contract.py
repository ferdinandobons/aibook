from __future__ import annotations

import json
import math
import unittest

from snip_26_contract import contract


class LessonExampleTests(unittest.TestCase):
    def test_expected_result(self):
        self.assertEqual(contract(), {'code_points': ['p', 'a', 'c', 'c', 'o'], 'token_ids': [112, 97, 99, 99, 111], 'invariant': 'tokenization preserves an explicit mapping from text to ids'})

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
