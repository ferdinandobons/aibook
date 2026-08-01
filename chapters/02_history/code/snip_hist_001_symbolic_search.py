from __future__ import annotations

from collections import deque
from collections.abc import Mapping, Sequence

Transition = tuple[str, str]
Graph = Mapping[str, Sequence[Transition]]

TRANSITIONS: dict[str, list[Transition]] = {
    "request_received": [
        ("ask_order_id", "order_identified"),
    ],
    "order_identified": [
        ("check_shipment", "shipment_checked"),
        ("open_ticket_immediately", "ticket_opened"),
    ],
    "shipment_checked": [
        ("open_ticket", "ticket_opened"),
    ],
    "ticket_opened": [],
}


def shortest_plan(graph: Graph, start: str, goal: str) -> list[Transition]:
    """Return a shortest action/state path in an explicitly represented graph."""
    if start not in graph:
        raise KeyError(f"Unknown start state: {start}")
    if goal not in graph:
        raise KeyError(f"Unknown goal state: {goal}")

    queue: deque[tuple[str, list[Transition]]] = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        for action, next_state in graph[state]:
            if next_state not in graph:
                raise KeyError(f"Transition points to unknown state: {next_state}")
            if next_state in visited:
                continue
            visited.add(next_state)
            queue.append((next_state, [*path, (action, next_state)]))

    raise ValueError(f"Goal not reachable: {goal}")


def main() -> None:
    plan = shortest_plan(TRANSITIONS, "request_received", "ticket_opened")
    print("start: request_received")
    for step, (action, state) in enumerate(plan, start=1):
        print(f"step_{step}: {action} -> {state}")
    print(f"plan_length: {len(plan)}")


if __name__ == "__main__":
    main()
