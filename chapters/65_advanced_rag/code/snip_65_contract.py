from __future__ import annotations

import json

CHAPTER = 65
TITLE = 'RAG adattivo, correttivo e basato su grafi'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    graph = {"q1": ["d1"], "d1": ["q2"], "q2": ["d2"]}
    frontier = ["q1"]
    visited = []
    while frontier:
        node = frontier.pop(0)
        visited.append(node)
        frontier.extend(neighbor for neighbor in graph.get(node, []) if neighbor not in visited)
    return {"path": visited, "invariant": "multi-hop retrieval records the path rather than only the final context"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
