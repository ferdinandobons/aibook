from __future__ import annotations

import json

CHAPTER = 27
TITLE = 'Embedding e spazio semantico'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    embedding_table = {1: [1.0, 0.0], 2: [0.0, 1.0]}
    static = embedding_table[1]
    contextual = [static[0] + 0.2, static[1] + 0.8]
    return {"static": static, "contextual": contextual, "invariant": "an embedding lookup is distinct from later contextualization"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
