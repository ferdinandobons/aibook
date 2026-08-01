from __future__ import annotations

import math
import unittest

import torch

from snip_num_001_precision_contracts import (
    autocast_example,
    dtype_summary,
    logsumexp_example,
    non_associativity_example,
    range_example,
    representable_step,
    tensor_bytes,
)


class NumericalContractsTests(unittest.TestCase):
    def test_dtype_range_and_precision_contracts(self) -> None:
        fp16 = dtype_summary(torch.float16)
        bf16 = dtype_summary(torch.bfloat16)
        fp32 = dtype_summary(torch.float32)

        self.assertEqual(fp16["bits"], 16)
        self.assertEqual(bf16["bits"], 16)
        self.assertLess(fp16["eps"], bf16["eps"])
        self.assertLess(fp16["max"], bf16["max"])
        self.assertAlmostEqual(bf16["tiny"], fp32["tiny"])

    def test_eps_is_observable_near_one(self) -> None:
        for dtype in (torch.float16, torch.bfloat16, torch.float32, torch.float64):
            half_step, full_step = representable_step(dtype)
            self.assertEqual(half_step, 1.0)
            self.assertGreater(full_step, 1.0)

    def test_float32_addition_is_not_associative_for_constructed_case(self) -> None:
        left_grouping, right_grouping = non_associativity_example()
        self.assertAlmostEqual(left_grouping, 3.14, places=5)
        self.assertEqual(right_grouping, 0.0)

    def test_stable_logsumexp_remains_finite(self) -> None:
        naive, stable = logsumexp_example()
        self.assertTrue(math.isinf(naive))
        self.assertTrue(math.isfinite(stable))
        self.assertAlmostEqual(stable, 1000.4075927734375, places=6)

    def test_fp16_and_bfloat16_have_different_range(self) -> None:
        fp16_value, bf16_value = range_example()
        self.assertTrue(math.isinf(fp16_value))
        self.assertEqual(bf16_value, 70144.0)

    def test_cpu_autocast_uses_bfloat16_for_matmul(self) -> None:
        result = autocast_example()
        self.assertEqual(result["output_dtype"], "torch.bfloat16")
        self.assertGreater(result["max_abs_error"], 0.0)
        self.assertLess(result["max_abs_error"], 0.1)
        self.assertLess(result["median_rel_error"], 0.01)

    def test_storage_bytes_follow_element_size(self) -> None:
        shape = (1024, 1024)
        self.assertEqual(tensor_bytes(shape, torch.float32), 4_194_304)
        self.assertEqual(tensor_bytes(shape, torch.float16), 2_097_152)


if __name__ == "__main__":
    unittest.main(verbosity=2)
