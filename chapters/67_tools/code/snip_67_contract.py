from __future__ import annotations

import json

CHAPTER = 67
TITLE = 'Output strutturato e uso degli strumenti'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    request = {"tool": "lookup_order", "order_id": "A1"}
    allowlist = {"lookup_order"}
    allowed = request["tool"] in allowlist and bool(request["order_id"])
    return {"allowed": allowed, "request": request, "invariant": "tool execution requires validation outside generated text"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
