from __future__ import annotations

import json

CHAPTER = 70
TITLE = 'Multi-agent, browser, computer e code agents'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    messages = [("planner", "lookup"), ("executor", "done"), ("critic", "pass")]
    roles = [role for role, _message in messages]
    return {"roles": roles, "message_count": len(messages), "invariant": "multi-agent coordination exposes role and message boundaries"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
