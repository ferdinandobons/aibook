from __future__ import annotations

import json

CHAPTER = 64
TITLE = 'Retrieval-Augmented Generation'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    retrieved = [("d1", 0.9), ("d2", 0.4)]
    answer = "Il pacco è in transito"
    cited = retrieved[0][0]
    return {"answer": answer, "citation": cited, "invariant": "RAG keeps retrieved evidence and generated answer as separate records"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
