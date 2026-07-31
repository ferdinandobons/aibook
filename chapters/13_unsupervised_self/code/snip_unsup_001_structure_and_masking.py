from __future__ import annotations

from dataclasses import dataclass
import math

import torch
from torch import nn
import torch.nn.functional as F


DTYPE = torch.float64
CENTERS = torch.tensor(
    [
        [-2.0, -2.0, 0.0, 0.0],
        [2.0, 0.0, 2.0, 0.0],
        [0.0, 2.0, 0.0, 2.0],
    ],
    dtype=DTYPE,
)


@dataclass(frozen=True)
class SyntheticData:
    features: torch.Tensor
    hidden_group: torch.Tensor


@dataclass(frozen=True)
class KMeansResult:
    centroids: torch.Tensor
    assignments: torch.Tensor
    objective_history: tuple[float, ...]


@dataclass(frozen=True)
class ReconstructionResult:
    model: nn.Module
    initial_loss: float
    final_loss: float
    test_loss: float
    mean_baseline_loss: float
    embedding_shape: tuple[int, int]


def make_data(n_per_group: int, seed: int) -> SyntheticData:
    generator = torch.Generator().manual_seed(seed)
    blocks = []
    labels = []
    for group, center in enumerate(CENTERS):
        noise = 0.35 * torch.randn(
            n_per_group,
            center.numel(),
            generator=generator,
            dtype=DTYPE,
        )
        blocks.append(center + noise)
        labels.append(torch.full((n_per_group,), group, dtype=torch.int64))
    features = torch.cat(blocks, dim=0)
    hidden_group = torch.cat(labels, dim=0)
    permutation = torch.randperm(features.shape[0], generator=generator)
    return SyntheticData(features[permutation], hidden_group[permutation])


def farthest_first_initialization(features: torch.Tensor, k: int) -> torch.Tensor:
    """Select centroids from geometry only, without using hidden group ids."""
    first = torch.argmin(features.square().sum(dim=1))
    chosen = [int(first)]
    while len(chosen) < k:
        current = features[chosen]
        distances = torch.cdist(features, current).square()
        nearest = distances.min(dim=1).values
        nearest[chosen] = -math.inf
        chosen.append(int(torch.argmax(nearest)))
    return features[chosen].clone()


def kmeans(features: torch.Tensor, k: int = 3, max_steps: int = 30) -> KMeansResult:
    centroids = farthest_first_initialization(features, k)
    history: list[float] = []

    for _ in range(max_steps):
        squared_distances = torch.cdist(features, centroids).square()
        assignments = squared_distances.argmin(dim=1)
        objective = squared_distances[
            torch.arange(features.shape[0]), assignments
        ].sum()
        history.append(float(objective))

        new_centroids = []
        for cluster in range(k):
            members = features[assignments == cluster]
            if members.numel() == 0:
                raise RuntimeError("Empty cluster in the fixed example")
            new_centroids.append(members.mean(dim=0))
        updated = torch.stack(new_centroids)
        if torch.allclose(updated, centroids, atol=1e-10, rtol=0.0):
            centroids = updated
            break
        centroids = updated

    squared_distances = torch.cdist(features, centroids).square()
    assignments = squared_distances.argmin(dim=1)
    final_objective = squared_distances[
        torch.arange(features.shape[0]), assignments
    ].sum()
    if not history or not math.isclose(
        history[-1], float(final_objective), rel_tol=0, abs_tol=1e-10
    ):
        history.append(float(final_objective))
    return KMeansResult(centroids, assignments, tuple(history))


class MaskedAutoencoder(nn.Module):
    """Tiny masked autoencoder.

    The model receives the corrupted values and the binary mask. The mask is
    not an external label; it only states which coordinates were hidden by the
    self-supervised corruption process.
    """

    def __init__(self) -> None:
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(8, 16, dtype=DTYPE),
            nn.Tanh(),
            nn.Linear(16, 4, dtype=DTYPE),
            nn.Tanh(),
            nn.Linear(4, 2, dtype=DTYPE),
        )
        self.decoder = nn.Sequential(
            nn.Linear(2, 8, dtype=DTYPE),
            nn.Tanh(),
            nn.Linear(8, 16, dtype=DTYPE),
            nn.Tanh(),
            nn.Linear(16, 4, dtype=DTYPE),
        )

    def forward(
        self,
        corrupted: torch.Tensor,
        mask: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        model_input = torch.cat((corrupted, mask.to(DTYPE)), dim=1)
        embedding = self.encoder(model_input)
        reconstruction = self.decoder(embedding)
        return reconstruction, embedding


def fixed_mask(n: int, seed: int, probability: float = 0.50) -> torch.Tensor:
    generator = torch.Generator().manual_seed(seed)
    mask = torch.rand(n, 4, generator=generator, dtype=DTYPE) < probability
    empty_rows = ~mask.any(dim=1)
    mask[empty_rows, 0] = True
    full_rows = mask.all(dim=1)
    mask[full_rows, 0] = False
    return mask


def random_mask(
    n: int,
    generator: torch.Generator,
    probability: float = 0.50,
) -> torch.Tensor:
    mask = torch.rand(n, 4, generator=generator, dtype=DTYPE) < probability
    empty_rows = ~mask.any(dim=1)
    mask[empty_rows, 0] = True
    full_rows = mask.all(dim=1)
    mask[full_rows, 0] = False
    return mask


def masked_loss(
    model: MaskedAutoencoder,
    features: torch.Tensor,
    mask: torch.Tensor,
) -> torch.Tensor:
    corrupted = features.masked_fill(mask, 0.0)
    reconstruction, _ = model(corrupted, mask)
    return F.mse_loss(reconstruction[mask], features[mask])


def train_masked_autoencoder(
    train_features: torch.Tensor,
    test_features: torch.Tensor,
    *,
    seed: int = 17,
    steps: int = 1800,
    learning_rate: float = 0.01,
) -> ReconstructionResult:
    torch.manual_seed(seed)
    model = MaskedAutoencoder()
    training_generator = torch.Generator().manual_seed(303)
    initial_mask = fixed_mask(train_features.shape[0], seed=101)
    test_mask = fixed_mask(test_features.shape[0], seed=202)

    initial_loss = float(masked_loss(model, train_features, initial_mask).detach())
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    for _ in range(steps):
        train_mask = random_mask(
            train_features.shape[0],
            training_generator,
            probability=0.50,
        )
        optimizer.zero_grad()
        loss = masked_loss(model, train_features, train_mask)
        loss.backward()
        optimizer.step()

    final_loss = float(masked_loss(model, train_features, initial_mask).detach())

    with torch.inference_mode():
        test_loss = float(masked_loss(model, test_features, test_mask))
        feature_mean = train_features.mean(dim=0)
        baseline = feature_mean.unsqueeze(0).expand_as(test_features)
        mean_baseline_loss = float(
            F.mse_loss(baseline[test_mask], test_features[test_mask])
        )
        corrupted_test = test_features.masked_fill(test_mask, 0.0)
        _, embedding = model(corrupted_test, test_mask)

    return ReconstructionResult(
        model=model,
        initial_loss=initial_loss,
        final_loss=final_loss,
        test_loss=test_loss,
        mean_baseline_loss=mean_baseline_loss,
        embedding_shape=tuple(embedding.shape),
    )


def run_experiment() -> dict[str, object]:
    train = make_data(40, seed=11)
    test = make_data(20, seed=12)
    clusters = kmeans(train.features, k=3)
    reconstruction = train_masked_autoencoder(train.features, test.features)
    cluster_counts = torch.bincount(clusters.assignments, minlength=3)
    return {
        "train": train,
        "test": test,
        "clusters": clusters,
        "cluster_counts": cluster_counts,
        "reconstruction": reconstruction,
    }


def main() -> None:
    result = run_experiment()
    clusters = result["clusters"]
    reconstruction = result["reconstruction"]
    assert isinstance(clusters, KMeansResult)
    assert isinstance(reconstruction, ReconstructionResult)

    print(f"train_shape: {tuple(result['train'].features.shape)}")
    print(f"test_shape: {tuple(result['test'].features.shape)}")
    print(f"cluster_counts: {result['cluster_counts'].tolist()}")
    print(
        "kmeans_objective_history: "
        + str([round(value, 6) for value in clusters.objective_history])
    )
    print(f"masked_train_initial_loss: {reconstruction.initial_loss:.6f}")
    print(f"masked_train_final_loss: {reconstruction.final_loss:.6f}")
    print(f"masked_test_loss: {reconstruction.test_loss:.6f}")
    print(f"mean_baseline_test_loss: {reconstruction.mean_baseline_loss:.6f}")
    print(f"embedding_shape: {reconstruction.embedding_shape}")


if __name__ == "__main__":
    main()
