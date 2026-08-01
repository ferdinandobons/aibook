from __future__ import annotations

import torch


def build_example() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    x = torch.tensor(
        [
            [1.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 1.0, 0.0],
            [1.0, 1.0, 0.0, 1.0],
        ],
        dtype=torch.float64,
    )
    weight = torch.tensor(
        [
            [1.0, 0.0, -1.0, 0.5],
            [0.0, 1.0, 1.0, -0.5],
            [0.5, -0.5, 0.0, 1.0],
        ],
        dtype=torch.float64,
    )
    bias = torch.tensor([0.2, -0.1, 0.3], dtype=torch.float64)
    return x, weight, bias


def linear_scores(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
) -> torch.Tensor:
    return x @ weight.transpose(0, 1) + bias


def gram_matrix(x: torch.Tensor) -> torch.Tensor:
    return x @ x.transpose(0, 1)


def rank_two_svd() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    matrix = torch.tensor(
        [
            [1.0, 2.0, 3.0],
            [2.0, 4.0, 6.0],
            [1.0, 1.0, 1.0],
        ],
        dtype=torch.float64,
    )
    u, singular_values, vh = torch.linalg.svd(matrix, full_matrices=False)
    reconstruction = (u * singular_values) @ vh
    return matrix, singular_values, reconstruction, torch.linalg.matrix_rank(matrix)


def main() -> None:
    x, weight, bias = build_example()
    scores = linear_scores(x, weight, bias)
    gram = gram_matrix(x)
    matrix, singular_values, reconstruction, rank = rank_two_svd()

    print(f"x_shape: {tuple(x.shape)}")
    print(f"weight_shape: {tuple(weight.shape)}")
    print(f"bias_shape: {tuple(bias.shape)}")
    print(f"scores_shape: {tuple(scores.shape)}")
    print("scores:")
    print(scores)
    print("gram_matrix:")
    print(gram)
    print("singular_values:")
    print(singular_values)
    print(f"matrix_rank: {int(rank)}")
    print(
        "svd_reconstruction_max_abs_error: "
        f"{torch.max(torch.abs(reconstruction - matrix)).item():.3e}"
    )


if __name__ == "__main__":
    main()
