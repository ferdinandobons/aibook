from __future__ import annotations

import unittest

from snip_hist_001_symbolic_search import TRANSITIONS, shortest_plan


class SymbolicSearchTests(unittest.TestCase):
    def test_finds_known_shortest_plan(self) -> None:
        plan = shortest_plan(TRANSITIONS, "request_received", "ticket_opened")
        self.assertEqual(
            plan,
            [
                ("ask_order_id", "order_identified"),
                ("open_ticket_immediately", "ticket_opened"),
            ],
        )

    def test_reaches_goal_without_repeating_states(self) -> None:
        plan = shortest_plan(TRANSITIONS, "request_received", "ticket_opened")
        states = ["request_received", *(state for _, state in plan)]
        self.assertEqual(states[-1], "ticket_opened")
        self.assertEqual(len(states), len(set(states)))

    def test_unreachable_goal_raises(self) -> None:
        graph = {
            "start": [("wait", "middle")],
            "middle": [],
            "goal": [],
        }
        with self.assertRaises(ValueError):
            shortest_plan(graph, "start", "goal")


if __name__ == "__main__":
    unittest.main()
