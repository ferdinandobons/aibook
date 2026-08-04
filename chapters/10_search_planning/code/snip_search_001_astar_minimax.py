from __future__ import annotations

from dataclasses import dataclass
import heapq
import itertools
import math
from typing import Mapping


@dataclass(frozen=True)
class Edge:
    destination: str
    action: str
    cost: float


GRAPH: dict[str, tuple[Edge, ...]] = {
    "message_received": (
        Edge("order_identified", "identify_order", 1.0),
        Edge("payment_inspected", "inspect_payment", 1.0),
        Edge("agent_asked", "ask_agent", 2.0),
        Edge("ticket_opened", "open_generic_ticket", 7.0),
    ),
    "order_identified": (
        Edge("tracking_checked", "check_tracking", 2.0),
        Edge("ticket_opened", "open_ticket_without_tracking", 6.0),
    ),
    "tracking_checked": (
        Edge("delay_confirmed", "confirm_delay", 1.0),
        Edge("ticket_opened", "open_ticket_after_tracking", 5.0),
    ),
    "delay_confirmed": (Edge("ticket_opened", "open_delay_ticket", 2.0),),
    "payment_inspected": (
        Edge("payment_ok", "confirm_payment_ok", 1.0),
        Edge("ticket_opened", "open_payment_ticket", 12.0),
    ),
    "payment_ok": (Edge("ticket_opened", "redirect_to_delivery", 10.0),),
    "agent_asked": (Edge("ticket_opened", "agent_opens_ticket", 8.0),),
    "ticket_opened": (),
}


HEURISTIC = {
    "message_received": 5.0,
    "order_identified": 4.0,
    "tracking_checked": 3.0,
    "delay_confirmed": 2.0,
    "payment_inspected": 9.0,
    "payment_ok": 10.0,
    "agent_asked": 8.0,
    "ticket_opened": 0.0,
}


@dataclass(frozen=True)
class SearchResult:
    states: tuple[str, ...]
    actions: tuple[str, ...]
    cost: float
    expanded: tuple[str, ...]


def astar(
    start: str,
    goal: str,
    heuristic: Mapping[str, float],
) -> SearchResult:
    counter = itertools.count()
    frontier = [(heuristic[start], 0.0, next(counter), start)]
    best_cost = {start: 0.0}
    parent: dict[str, str | None] = {start: None}
    action_to: dict[str, str] = {}
    expanded: list[str] = []

    while frontier:
        _, cost_so_far, _, state = heapq.heappop(frontier)
        if cost_so_far != best_cost.get(state):
            continue

        expanded.append(state)
        if state == goal:
            states: list[str] = []
            actions: list[str] = []
            current: str | None = state
            while current is not None:
                states.append(current)
                previous = parent[current]
                if previous is not None:
                    actions.append(action_to[current])
                current = previous
            return SearchResult(
                states=tuple(reversed(states)),
                actions=tuple(reversed(actions)),
                cost=cost_so_far,
                expanded=tuple(expanded),
            )

        for edge in GRAPH[state]:
            if edge.cost < 0:
                raise ValueError("A* example requires non-negative costs")
            candidate = cost_so_far + edge.cost
            if candidate < best_cost.get(edge.destination, math.inf):
                best_cost[edge.destination] = candidate
                parent[edge.destination] = state
                action_to[edge.destination] = edge.action
                priority = candidate + heuristic[edge.destination]
                heapq.heappush(
                    frontier,
                    (priority, candidate, next(counter), edge.destination),
                )

    raise ValueError(f"Goal {goal!r} is unreachable from {start!r}")


GAME_TREE: dict[str, tuple[str | int, ...]] = {
    "root": ("A", "B", "C"),
    "A": (3, 5),
    "B": (2, 9),
    "C": (4, 4),
}


def minimax(node: str | int, maximizing: bool = True) -> tuple[float, int]:
    if isinstance(node, int):
        return float(node), 1

    values: list[float] = []
    visited_leaves = 0
    for child in GAME_TREE[node]:
        value, leaves = minimax(child, not maximizing)
        values.append(value)
        visited_leaves += leaves

    result = max(values) if maximizing else min(values)
    return result, visited_leaves


def alpha_beta(
    node: str | int,
    alpha: float = -math.inf,
    beta: float = math.inf,
    maximizing: bool = True,
) -> tuple[float, int]:
    if isinstance(node, int):
        return float(node), 1

    visited_leaves = 0
    if maximizing:
        value = -math.inf
        for child in GAME_TREE[node]:
            child_value, leaves = alpha_beta(child, alpha, beta, False)
            visited_leaves += leaves
            value = max(value, child_value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, visited_leaves

    value = math.inf
    for child in GAME_TREE[node]:
        child_value, leaves = alpha_beta(child, alpha, beta, True)
        visited_leaves += leaves
        value = min(value, child_value)
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value, visited_leaves


def main() -> None:
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

    print("uniform_cost")
    print(f"states: {uniform_cost.states}")
    print(f"actions: {uniform_cost.actions}")
    print(f"cost: {uniform_cost.cost}")
    print(f"expanded: {uniform_cost.expanded}")
    print()

    print("astar")
    print(f"states: {informed.states}")
    print(f"actions: {informed.actions}")
    print(f"cost: {informed.cost}")
    print(f"expanded: {informed.expanded}")
    print()

    minimax_value, minimax_leaves = minimax("root")
    alpha_beta_value, alpha_beta_leaves = alpha_beta("root")
    print("game_tree")
    print(f"minimax_value: {minimax_value}")
    print(f"minimax_leaves: {minimax_leaves}")
    print(f"alpha_beta_value: {alpha_beta_value}")
    print(f"alpha_beta_leaves: {alpha_beta_leaves}")


if __name__ == "__main__":
    main()
