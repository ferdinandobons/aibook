from __future__ import annotations

import json

CHAPTER = 78
TITLE = 'KV cache e riuso del contesto'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    prefix = ["p0", "p1"]
    requests = {"r1": prefix + ["a"], "r2": prefix + ["b"]}
    shared_tokens = len(set(requests["r1"]) & set(requests["r2"]))
    return {"shared_prefix": shared_tokens, "request_lengths": {key: len(value) for key, value in requests.items()}, "invariant": "cache reuse preserves token position and request ownership"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
