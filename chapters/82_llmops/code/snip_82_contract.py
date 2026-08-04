from __future__ import annotations

import json

CHAPTER = 82
TITLE = 'LLMOps, edge, costo ed energia'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    request = {"model": "v1", "tokens": 20, "energy_wh": 0.4}
    cost = request["energy_wh"] * 0.30
    return {"model": request["model"], "cost": round(cost, 6), "invariant": "an operational metric records model version and measurement boundary"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
