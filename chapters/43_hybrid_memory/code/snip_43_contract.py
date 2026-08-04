from __future__ import annotations

import json

CHAPTER = 43
TITLE = 'Architetture ibride e memoria interna'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    local = ["recent-a", "recent-b"]
    long_term = ["stable-fact"]
    read = local[-1] if local else long_term[0]
    return {"local_size": len(local), "long_term_size": len(long_term), "read": read, "invariant": "local and long-term memory have separate lifetimes"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
