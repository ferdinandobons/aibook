from __future__ import annotations

import json

CHAPTER = 66
TITLE = 'Contesto lungo, retrieval e memoria'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    short_term = ["ultimo evento"]
    long_term = ["fatto stabile"]
    recalled = long_term[0]
    return {"short_term": short_term, "recalled": recalled, "invariant": "memory scope and retrieval source remain explicit"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
