from __future__ import annotations

import json

CHAPTER = 35
TITLE = 'La ricetta di pretraining'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    base_lr = 0.001
    warmup_steps = 4
    steps = [0, 1, 4, 8]
    rates = [round(base_lr * min(1.0, step / warmup_steps), 6) for step in steps]
    return {"learning_rates": rates, "invariant": "the scheduler is indexed by the declared step counter"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
