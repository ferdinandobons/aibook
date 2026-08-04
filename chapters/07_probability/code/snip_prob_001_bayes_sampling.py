from __future__ import annotations

from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class BayesResult:
    prior: float
    likelihood_if_h: float
    likelihood_if_not_h: float
    evidence_probability: float
    posterior: float


def bayes_update(
    prior: float,
    likelihood_if_h: float,
    likelihood_if_not_h: float,
) -> BayesResult:
    if not 0.0 <= prior <= 1.0:
        raise ValueError("prior must be in [0, 1]")
    if not 0.0 <= likelihood_if_h <= 1.0:
        raise ValueError("likelihood_if_h must be in [0, 1]")
    if not 0.0 <= likelihood_if_not_h <= 1.0:
        raise ValueError("likelihood_if_not_h must be in [0, 1]")

    numerator = prior * likelihood_if_h
    evidence_probability = numerator + (1.0 - prior) * likelihood_if_not_h
    if evidence_probability == 0.0:
        raise ValueError("the observed evidence has zero probability under the model")
    posterior = numerator / evidence_probability
    return BayesResult(
        prior=prior,
        likelihood_if_h=likelihood_if_h,
        likelihood_if_not_h=likelihood_if_not_h,
        evidence_probability=evidence_probability,
        posterior=posterior,
    )


def delivery_example() -> tuple[BayesResult, BayesResult]:
    first = bayes_update(
        prior=0.20,
        likelihood_if_h=0.80,
        likelihood_if_not_h=0.10,
    )
    second = bayes_update(
        prior=first.posterior,
        likelihood_if_h=0.70,
        likelihood_if_not_h=0.20,
    )
    return first, second


def bernoulli_mle(observations: torch.Tensor) -> float:
    if observations.ndim != 1:
        raise ValueError("observations must be a one-dimensional tensor")
    if observations.numel() == 0:
        raise ValueError("observations cannot be empty")
    if not torch.all((observations == 0) | (observations == 1)):
        raise ValueError("Bernoulli observations must be 0 or 1")
    return observations.to(torch.float64).mean().item()


def bernoulli_log_likelihood(observations: torch.Tensor, probability: float) -> float:
    if not 0.0 < probability < 1.0:
        raise ValueError("probability must be strictly between 0 and 1")
    distribution = torch.distributions.Bernoulli(
        probs=torch.tensor(probability, dtype=torch.float64)
    )
    return distribution.log_prob(observations.to(torch.float64)).sum().item()


def sampling_summary(
    probability: float = 0.30,
    sample_sizes: tuple[int, ...] = (10, 100, 10_000),
    seed: int = 2026,
) -> list[tuple[int, float, float]]:
    torch.manual_seed(seed)
    distribution = torch.distributions.Bernoulli(
        probs=torch.tensor(probability, dtype=torch.float64)
    )
    summaries: list[tuple[int, float, float]] = []
    for sample_size in sample_sizes:
        sample = distribution.sample((sample_size,))
        summaries.append(
            (
                sample_size,
                sample.mean().item(),
                sample.var(unbiased=False).item(),
            )
        )
    return summaries


def main() -> None:
    first, second = delivery_example()
    print(f"prior_delivery_issue: {first.prior:.6f}")
    print(f"probability_first_evidence: {first.evidence_probability:.6f}")
    print(f"posterior_after_text_evidence: {first.posterior:.6f}")
    print(f"posterior_after_tracking_evidence: {second.posterior:.6f}")

    observations = torch.tensor(
        [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        dtype=torch.float64,
    )
    estimate = bernoulli_mle(observations)
    print(f"bernoulli_positives: {int(observations.sum().item())}")
    print(f"bernoulli_trials: {observations.numel()}")
    print(f"bernoulli_mle: {estimate:.6f}")
    print(
        f"log_likelihood_at_mle: {bernoulli_log_likelihood(observations, estimate):.6f}"
    )

    distribution = torch.distributions.Bernoulli(
        probs=torch.tensor(0.30, dtype=torch.float64)
    )
    print(f"theoretical_mean: {distribution.mean.item():.6f}")
    print(f"theoretical_variance: {distribution.variance.item():.6f}")
    for sample_size, sample_mean, sample_variance in sampling_summary():
        print(
            f"sample_size={sample_size}: "
            f"sample_mean={sample_mean:.6f}, "
            f"sample_variance={sample_variance:.6f}"
        )


if __name__ == "__main__":
    main()
