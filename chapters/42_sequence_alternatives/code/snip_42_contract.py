from __future__ import annotations

import json

CHAPTER = 42
TITLE = 'State-space model, recurrence e long convolution'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    state = 0.0
    inputs = [1.0, 0.0, -1.0]
    outputs = []
    for value in inputs:
        state = 0.8 * state + 0.4 * value
        outputs.append(round(state, 6))
    return {"outputs": outputs, "invariant": "the state update is explicit before each emitted value"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
