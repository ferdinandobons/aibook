from __future__ import annotations

import unittest

from snip_search_001_astar_minimax import (
    GAME_TREE,
    GRAPH,
    HEURISTIC,
    alpha_beta,
    astar,
    minimax,
)


class SearchPlanningTests(unittest.TestCase):
    def test_astar_and_uniform_cost_find_same_optimal_plan(self) -> None:
        uniform_cost = astar(
            "message_received",
            "ticket_opened",
            {state: 0.0 for state in GRAPH},
        )
        informed = astar(
            "message_received",
            "ticket_opened",
            HEURISTIC,
        )
        self.assertEqual(uniform_cost.cost, 6.0)
        self.assertEqual(informed.cost, 6.0)
        self.assertEqual(uniform_cost.states, informed.states)
        self.assertEqual(uniform_cost.actions, informed.actions)

    def test_heuristic_is_admissible_and_consistent_for_example(self) -> None:
        true_remaining = {
            state: astar(state, "ticket_opened", {s: 0.0 for s in GRAPH}).cost
            for state in GRAPH
        }
        for state, estimate in HEURISTIC.items():
            self.assertLessEqual(estimate, true_remaining[state])
            for edge in GRAPH[state]:
                self.assertLessEqual(
                    estimate,
                    edge.cost + HEURISTIC[edge.destination],
                )

    def test_astar_expands_fewer_states_in_the_fixed_example(self) -> None:
        uniform_cost = astar(
            "message_received",
            "ticket_opened",
            {state: 0.0 for state in GRAPH},
        )
        informed = astar(
            "message_received",
            "ticket_opened",
            HEURISTIC,
        )
        self.assertEqual(len(uniform_cost.expanded), 8)
        self.assertEqual(len(informed.expanded), 5)

    def test_negative_cost_is_rejected(self) -> None:
        original = GRAPH["delay_confirmed"]
        try:
            GRAPH["delay_confirmed"] = (
                type(original[0])("ticket_opened", "invalid", -1.0),
            )
            with self.assertRaises(ValueError):
                astar("delay_confirmed", "ticket_opened", HEURISTIC)
        finally:
            GRAPH["delay_confirmed"] = original

    def test_alpha_beta_preserves_minimax_value(self) -> None:
        minimax_value, minimax_leaves = minimax("root")
        alpha_beta_value, alpha_beta_leaves = alpha_beta("root")
        self.assertEqual(minimax_value, 4.0)
        self.assertEqual(alpha_beta_value, minimax_value)
        self.assertEqual(minimax_leaves, 6)
        self.assertEqual(alpha_beta_leaves, 5)

    def test_game_tree_has_three_min_children(self) -> None:
        self.assertEqual(GAME_TREE["root"], ("A", "B", "C"))
        self.assertEqual(GAME_TREE["A"], (3, 5))
        self.assertEqual(GAME_TREE["B"], (2, 9))
        self.assertEqual(GAME_TREE["C"], (4, 4))


if __name__ == "__main__":
    unittest.main(verbosity=2)
