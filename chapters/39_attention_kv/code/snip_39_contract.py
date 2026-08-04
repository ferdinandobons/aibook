from __future__ import annotations

import json

CHAPTER = 39
TITLE = "Varianti dell'attention e gestione KV"


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    query_heads = 4
    kv_heads = 2
    group_size = query_heads // kv_heads
    return {"query_heads": query_heads, "kv_heads": kv_heads, "queries_per_kv": group_size, "invariant": "the head grouping is declared before cache accounting"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
