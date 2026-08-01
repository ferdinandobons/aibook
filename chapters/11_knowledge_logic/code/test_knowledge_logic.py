from __future__ import annotations

import unittest

from snip_knowledge_001_rules_bayes import (
    FACTS,
    P_DELAY,
    P_MESSAGE_GIVEN_DELAY,
    P_TRACKING_GIVEN_DELAY,
    RULES,
    bernoulli_probability,
    forward_chain,
    joint_probability,
    joint_total,
    posterior_delay,
)


class KnowledgeLogicTests(unittest.TestCase):
    def test_forward_chain_derives_expected_facts(self) -> None:
        facts = forward_chain(FACTS, RULES)
        self.assertIn(("possible_delay", "order_42"), facts)
        self.assertIn(("needs_review", "order_42"), facts)
        self.assertIn(("eligible_for_delay_workflow", "order_42"), facts)

    def test_forward_chain_is_idempotent(self) -> None:
        once = forward_chain(FACTS, RULES)
        twice = forward_chain(once, RULES)
        self.assertEqual(once, twice)

    def test_absence_does_not_create_negation(self) -> None:
        facts = forward_chain(FACTS, RULES)
        self.assertNotIn(("delivered", "order_42"), facts)
        self.assertNotIn(("not_delivered", "order_42"), facts)

    def test_joint_distribution_normalizes(self) -> None:
        self.assertAlmostEqual(joint_total(), 1.0)

    def test_posterior_with_two_positive_signals(self) -> None:
        self.assertAlmostEqual(posterior_delay(True, True), 0.875)

    def test_absent_signals_reduce_posterior(self) -> None:
        self.assertLess(posterior_delay(False, False), P_DELAY)

    def test_conditional_factorization_is_explicit(self) -> None:
        for real_delay in (False, True):
            product_probability = (
                bernoulli_probability(
                    True,
                    P_MESSAGE_GIVEN_DELAY[real_delay],
                )
                * bernoulli_probability(
                    True,
                    P_TRACKING_GIVEN_DELAY[real_delay],
                )
            )
            normalized = (
                joint_probability(real_delay, True, True)
                / bernoulli_probability(real_delay, P_DELAY)
            )
            self.assertAlmostEqual(normalized, product_probability)


if __name__ == "__main__":
    unittest.main(verbosity=2)
