from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable


Fact = tuple[str, ...]


@dataclass(frozen=True)
class Rule:
    premises: tuple[Fact, ...]
    conclusion: Fact


def is_variable(token: str) -> bool:
    return token.startswith("?")


def match(
    pattern: Fact,
    fact: Fact,
    environment: dict[str, str],
) -> dict[str, str] | None:
    if len(pattern) != len(fact) or pattern[0] != fact[0]:
        return None

    result = dict(environment)
    for pattern_token, fact_token in zip(pattern[1:], fact[1:]):
        if is_variable(pattern_token):
            bound = result.get(pattern_token)
            if bound is not None and bound != fact_token:
                return None
            result[pattern_token] = fact_token
        elif pattern_token != fact_token:
            return None
    return result


def instantiate(pattern: Fact, environment: dict[str, str]) -> Fact:
    return tuple(environment.get(token, token) for token in pattern)


def satisfy_premises(
    premises: tuple[Fact, ...],
    facts: set[Fact],
) -> list[dict[str, str]]:
    environments: list[dict[str, str]] = [{}]
    for premise in premises:
        next_environments: list[dict[str, str]] = []
        for environment in environments:
            for fact in sorted(facts):
                candidate = match(premise, fact, environment)
                if candidate is not None:
                    next_environments.append(candidate)
        environments = next_environments
    return environments


def forward_chain(
    initial_facts: Iterable[Fact],
    rules: Iterable[Rule],
) -> set[Fact]:
    facts = set(initial_facts)
    changed = True
    while changed:
        changed = False
        for rule in rules:
            for environment in satisfy_premises(rule.premises, facts):
                derived = instantiate(rule.conclusion, environment)
                if derived not in facts:
                    facts.add(derived)
                    changed = True
    return facts


FACTS = {
    ("message_mentions_missing_delivery", "order_42"),
    ("tracking_stalled", "order_42"),
    ("delivery_date_passed", "order_42"),
}


RULES = (
    Rule(
        premises=(
            ("tracking_stalled", "?order"),
            ("delivery_date_passed", "?order"),
        ),
        conclusion=("possible_delay", "?order"),
    ),
    Rule(
        premises=(
            ("message_mentions_missing_delivery", "?order"),
            ("possible_delay", "?order"),
        ),
        conclusion=("needs_review", "?order"),
    ),
    Rule(
        premises=(("needs_review", "?order"),),
        conclusion=("eligible_for_delay_workflow", "?order"),
    ),
)


P_DELAY = 0.20
P_MESSAGE_GIVEN_DELAY = {True: 0.80, False: 0.10}
P_TRACKING_GIVEN_DELAY = {True: 0.70, False: 0.20}


def bernoulli_probability(value: bool, probability_true: float) -> float:
    return probability_true if value else 1.0 - probability_true


def joint_probability(
    real_delay: bool,
    message_signal: bool,
    tracking_stalled: bool,
) -> float:
    probability_delay = bernoulli_probability(real_delay, P_DELAY)
    probability_message = bernoulli_probability(
        message_signal,
        P_MESSAGE_GIVEN_DELAY[real_delay],
    )
    probability_tracking = bernoulli_probability(
        tracking_stalled,
        P_TRACKING_GIVEN_DELAY[real_delay],
    )
    return probability_delay * probability_message * probability_tracking


def posterior_delay(
    message_signal: bool,
    tracking_stalled: bool,
) -> float:
    numerator = joint_probability(True, message_signal, tracking_stalled)
    denominator = sum(
        joint_probability(real_delay, message_signal, tracking_stalled)
        for real_delay in (False, True)
    )
    return numerator / denominator


def joint_total() -> float:
    return sum(
        joint_probability(real_delay, message_signal, tracking_stalled)
        for real_delay, message_signal, tracking_stalled in product(
            (False, True),
            repeat=3,
        )
    )


def main() -> None:
    derived = forward_chain(FACTS, RULES)

    print("forward_chaining")
    for fact in sorted(derived):
        print(fact)
    print(
        "absence_does_not_imply_negation:",
        ("not_delivered", "order_42") not in derived,
    )
    print()

    print("bayesian_network")
    print(f"joint_total: {joint_total():.6f}")
    print(
        "posterior_delay_given_message_and_tracking:",
        f"{posterior_delay(True, True):.6f}",
    )
    print(
        "posterior_delay_given_no_signals:",
        f"{posterior_delay(False, False):.6f}",
    )


if __name__ == "__main__":
    main()
