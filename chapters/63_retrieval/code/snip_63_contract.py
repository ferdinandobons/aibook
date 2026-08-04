from __future__ import annotations

import json

CHAPTER = 63
TITLE = 'Information retrieval'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    query = {"pacco", "ritardo"}
    documents = [("d1", {"pacco", "ritardo"}), ("d2", {"pacco"}), ("d3", {"carta"})]
    ranking = sorted(((len(query & terms), doc_id) for doc_id, terms in documents), reverse=True)
    return {"ranking": ranking, "invariant": "retrieval exposes document scores before generation"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
