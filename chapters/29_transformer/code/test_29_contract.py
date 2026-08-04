from __future__ import annotations

import json
import math
import unittest

from snip_29_contract import contract


def assert_finite(testcase, value):
    if isinstance(value, float):
        testcase.assertTrue(math.isfinite(value))
    elif isinstance(value, dict):
        for nested in value.values():
            assert_finite(testcase, nested)
    elif isinstance(value, (list, tuple)):
        for nested in value:
            assert_finite(testcase, nested)


class LessonExampleTests(unittest.TestCase):
    def test_expected_result(self):
        self.assertEqual(contract(), {'scores': [[1.0, 0.0], [0.0, 1.0]], 'output': [[1.462117, 0.806824], [0.537883, 2.193176]], 'invariant': 'queries read keys and values through the declared attention matrix'})

    def test_example_is_deterministic(self):
        self.assertEqual(contract(), contract())

    def test_result_is_serializable_and_finite(self):
        result = contract()
        self.assertTrue(json.dumps(result, sort_keys=True))
        assert_finite(self, result)

    def test_contract_shape_is_explicit(self):
        result = contract()
        self.assertIsInstance(result, dict)
        self.assertIsInstance(result.get('invariant'), str)
        self.assertGreaterEqual(len(result['invariant'].split()), 4)

    def test_unsupported_case_fails_before_interpretation(self):
        with self.assertRaises(ValueError):
            contract('unsupported')


if __name__ == '__main__':
    unittest.main(verbosity=2)
