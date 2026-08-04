"""Replica indipendente di una stima Bernoulli con protocollo dichiarato."""

from __future__ import annotations

import hashlib
import json
import math
import random
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Protocol:
    probability: float
    samples: int
    tolerance: float

    def validate(self) -> None:
        if not 0.0 < self.probability < 1.0:
            raise ValueError("probability deve essere compresa tra 0 e 1")
        if self.samples < 30:
            raise ValueError("samples deve essere almeno 30 per questo esempio")
        if self.tolerance <= 0.0:
            raise ValueError("tolerance deve essere positiva")


def protocol_digest(protocol: Protocol) -> str:
    payload = json.dumps(asdict(protocol), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def run_trial(protocol: Protocol, seed: int) -> dict[str, object]:
    protocol.validate()
    rng = random.Random(seed)
    successes = sum(
        rng.random() < protocol.probability for _ in range(protocol.samples)
    )
    estimate = successes / protocol.samples
    standard_error = math.sqrt(estimate * (1.0 - estimate) / protocol.samples)
    return {
        "seed": seed,
        "successes": successes,
        "estimate": round(estimate, 6),
        "ci95": [
            round(max(0.0, estimate - 1.96 * standard_error), 6),
            round(min(1.0, estimate + 1.96 * standard_error), 6),
        ],
    }


# BOOK-EXCERPT-START
def replicate(
    protocol: Protocol, original_seed: int = 11, replica_seed: int = 29
) -> dict[str, object]:
    original = run_trial(protocol, original_seed)
    replica = run_trial(protocol, replica_seed)
    difference = abs(float(replica["estimate"]) - float(original["estimate"]))
    return {
        "protocol_sha256": protocol_digest(protocol),
        "original": original,
        "replica": replica,
        "absolute_difference": round(difference, 6),
        "within_declared_tolerance": difference <= protocol.tolerance,
        "interpretation": "stesso protocollo, campione indipendente; la tolleranza non prova equivalenza universale",
    }


# BOOK-EXCERPT-END


if __name__ == "__main__":
    result = replicate(Protocol(probability=0.70, samples=1000, tolerance=0.05))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
