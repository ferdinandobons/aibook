from __future__ import annotations

import json

CHAPTER = 86
TITLE = 'Interpretabilità delle rappresentazioni e dei circuiti'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    baseline = 0.60
    intervened = 0.25
    effect = intervened - baseline
    return {"baseline": baseline, "intervened": intervened, "effect": effect, "invariant": "an intervention is compared with a baseline before causal language"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
