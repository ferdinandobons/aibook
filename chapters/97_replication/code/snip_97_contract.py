from __future__ import annotations

import json

CHAPTER = 97
TITLE = 'Riprodurre e leggere un paper'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    original = {"metric": 0.80, "seed": 1, "split": "fixed"}
    replica = {"metric": 0.78, "seed": 2, "split": "fixed"}
    difference = replica["metric"] - original["metric"]
    return {"difference": difference, "same_split": replica["split"] == original["split"], "invariant": "a replication records setup differences before interpreting outcome differences"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
