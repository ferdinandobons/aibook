from __future__ import annotations

import json

CHAPTER = 48
TITLE = 'Preferenze, reward model e RLHF'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    chosen = 0.8
    rejected = 0.2
    reward_margin = chosen - rejected
    return {"reward_margin": round(reward_margin, 6), "invariant": "preference learning compares responses under one prompt"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
