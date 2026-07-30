from __future__ import annotations

import unittest

import torch

from snip_att_001_single_query import single_query_attention
from snip_att_002_matrix_api import matrix_attention
from snip_att_003_causal_mask import causal_attention
from snip_att_004_multihead_shapes import multihead_shapes


class AttentionSnippetTests(unittest.TestCase):
    def test_single_query_values(self) -> None:
        scores, weights, output = single_query_attention()
        torch.testing.assert_close(scores, torch.tensor([0.70710678, 0.0, 0.70710678], dtype=torch.float64))
        torch.testing.assert_close(weights, torch.tensor([0.40111209, 0.19777581, 0.40111209], dtype=torch.float64))
        torch.testing.assert_close(output, torch.tensor([0.80222418, 0.59888791], dtype=torch.float64))

    def test_matrix_invariants(self) -> None:
        scores, weights, output = matrix_attention()
        self.assertEqual(tuple(scores.shape), (1, 1, 3, 3))
        self.assertEqual(tuple(weights.shape), (1, 1, 3, 3))
        self.assertEqual(tuple(output.shape), (1, 1, 3, 2))

    def test_causal_mask(self) -> None:
        allowed, weights, output = causal_attention()
        self.assertEqual(tuple(allowed.shape), (3, 3))
        self.assertEqual(tuple(output.shape), (1, 1, 3, 2))
        self.assertEqual(torch.count_nonzero(weights[..., ~allowed]).item(), 0)

    def test_multihead_shapes(self) -> None:
        output, weights = multihead_shapes()
        self.assertEqual(tuple(output.shape), (1, 3, 4))
        self.assertEqual(tuple(weights.shape), (1, 2, 3, 3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
