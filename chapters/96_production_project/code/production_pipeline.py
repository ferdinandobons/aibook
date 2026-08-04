"""Simulazione verificabile di gate offline, canary e rollback."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ReleaseCandidate:
    version: str
    owner: str
    overall_accuracy: float
    critical_slice_accuracy: float
    canary_error_rate: float
    rollback_version: str

    def validate(self) -> None:
        if not self.version or not self.owner or not self.rollback_version:
            raise ValueError("version, owner e rollback_version sono obbligatori")
        for value in (
            self.overall_accuracy,
            self.critical_slice_accuracy,
            self.canary_error_rate,
        ):
            if not 0.0 <= value <= 1.0:
                raise ValueError("le metriche devono essere comprese tra 0 e 1")


@dataclass(frozen=True)
class GatePolicy:
    minimum_overall_accuracy: float = 0.85
    minimum_critical_slice_accuracy: float = 0.80
    maximum_canary_error_rate: float = 0.03


def manifest_digest(candidate: ReleaseCandidate, policy: GatePolicy) -> str:
    payload = json.dumps(
        {"candidate": asdict(candidate), "policy": asdict(policy)},
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


# BOOK-EXCERPT-START
def evaluate_release(
    candidate: ReleaseCandidate, policy: GatePolicy = GatePolicy()
) -> dict[str, object]:
    candidate.validate()
    offline_checks = {
        "overall": candidate.overall_accuracy >= policy.minimum_overall_accuracy,
        "critical_slice": candidate.critical_slice_accuracy
        >= policy.minimum_critical_slice_accuracy,
    }
    offline_passed = all(offline_checks.values())
    canary_passed = candidate.canary_error_rate <= policy.maximum_canary_error_rate

    promoted = offline_passed and canary_passed
    rollback = offline_passed and not canary_passed
    decision = "promote" if promoted else ("rollback" if rollback else "reject_offline")
    return {
        "version": candidate.version,
        "decision": decision,
        "offline_checks": offline_checks,
        "canary_passed": canary_passed,
        "rollback_target": candidate.rollback_version if rollback else None,
        "manifest_sha256": manifest_digest(candidate, policy),
    }


# BOOK-EXCERPT-END


def run_project() -> dict[str, object]:
    healthy = ReleaseCandidate("v2", "ml-platform", 0.90, 0.84, 0.02, "v1")
    regressed_canary = ReleaseCandidate("v3", "ml-platform", 0.91, 0.85, 0.08, "v2")
    return {
        "healthy": evaluate_release(healthy),
        "regressed_canary": evaluate_release(regressed_canary),
    }


if __name__ == "__main__":
    print(json.dumps(run_project(), ensure_ascii=False, sort_keys=True))
