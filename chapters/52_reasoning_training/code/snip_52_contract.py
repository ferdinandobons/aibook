from __future__ import annotations

import json

CHAPTER = 52
TITLE = 'Addestrare e distillare il reasoning'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    traces = [("4", 0.9), ("4", 0.7), ("5", 0.8)]
    counts = {}
    for answer, _score in traces:
        counts[answer] = counts.get(answer, 0) + 1
    selected = max(counts, key=counts.__getitem__)
    return {"trace_count": len(traces), "selected": selected, "invariant": "self-consistency selects among traces and does not prove their faithfulness"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
