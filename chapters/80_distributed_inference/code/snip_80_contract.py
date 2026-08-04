from __future__ import annotations

import json

CHAPTER = 80
TITLE = 'Serving disaggregato e inference distribuita'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    workers = {"w1": {"tokens": 2, "network_ms": 3}, "w2": {"tokens": 2, "network_ms": 4}}
    end_to_end_ms = max(worker["network_ms"] for worker in workers.values()) + 2
    return {"workers": len(workers), "end_to_end_ms": end_to_end_ms, "invariant": "distributed inference includes communication in end-to-end latency"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
