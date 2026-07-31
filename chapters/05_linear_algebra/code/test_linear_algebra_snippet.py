from __future__ import annotations

import unittest

import torch

from snip_la_001_shapes_linear_svd import (
    build_example,
    gram_matrix,
    linear_scores,
    rank_two_svd,
)


class LinearAlgebraSnippetTests(unittest.TestCase):
    def test_affine_shape_and_values(self) -> None:
        x, weight, bias = build_example()
        scores = linear_scores(x, weight, bias)
        expected = torch.tensor(
            [
                [0.2, 0.9, 0.8],
                [-0.8, 1.9, -0.2],
                [1.7, 0.4, 1.3],
            ],
            dtype=torch.float64,
        )
        self.assertEqual(tuple(scores.shape), (3, 3))
        torch.testing.assert_close(scores, expected)

    def test_bias_broadcast_matches_explicit_rows(self) -> None:
        x, weight, bias = build_example()
        explicit = x @ weight.transpose(0, 1) + bias.unsqueeze(0).expand(x.size(0), -1)
        torch.testing.assert_close(linear_scores(x, weight, bias), explicit)

    def test_gram_matrix_contains_row_dot_products(self) -> None:
        x, _, _ = build_example()
        gram = gram_matrix(x)
        expected = torch.tensor(
            [[2.0, 1.0, 1.0], [1.0, 2.0, 1.0], [1.0, 1.0, 3.0]],
            dtype=torch.float64,
        )
        torch.testing.assert_close(gram, expected)
        torch.testing.assert_close(gram, gram.transpose(0, 1))

    def test_rank_and_svd_reconstruction(self) -> None:
        matrix, singular_values, reconstruction, rank = rank_two_svd()
        self.assertEqual(int(rank), 2)
        self.assertLess(singular_values[-1].item(), 1e-12)
        torch.testing.assert_close(reconstruction, matrix, rtol=1e-12, atol=1e-12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
