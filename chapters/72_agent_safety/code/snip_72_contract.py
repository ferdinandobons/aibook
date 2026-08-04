from __future__ import annotations

import json

CHAPTER = 72
TITLE = 'Sicurezza operativa degli agenti'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    request = {"tool": "refund", "scope": "order:A1"}
    policy = {"allowed_tools": {"lookup_order"}, "requires_approval": {"refund"}}
    allowed = request["tool"] in policy["allowed_tools"]
    return {"allowed": allowed, "approval_required": request["tool"] in policy["requires_approval"], "invariant": "authorization and rollback live outside the model text"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
