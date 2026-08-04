from __future__ import annotations

import json

CHAPTER = 62
TITLE = 'World model, embodied AI e vision-language-action'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    state = {"position": 0, "battery": 2}
    action = "move"
    next_state = dict(state)
    next_state["position"] += 1
    next_state["battery"] -= 1
    return {"action": action, "next_state": next_state, "invariant": "the world transition exposes state and action consequences"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
