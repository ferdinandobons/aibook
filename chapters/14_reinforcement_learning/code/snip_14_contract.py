from __future__ import annotations

import json

CHAPTER = 14
TITLE = 'Reinforcement learning'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    gamma = 0.9
    reward = 1.0
    next_value = 0.5
    target = reward + gamma * next_value
    return {
        "target": round(target, 6),
        "invariant": "reward and discounted next value are explicit",
    }


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
