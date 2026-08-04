from __future__ import annotations

import json

CHAPTER = 54
TITLE = 'Aggiornamento, merging ed editing del modello'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    original = {"pacco": "in_transito", "ritardo": 1}
    edited = dict(original)
    edited["ritardo"] = 0
    changed = [key for key in original if original[key] != edited[key]]
    return {"changed_keys": changed, "rollback": original == {"pacco": "in_transito", "ritardo": 1}, "invariant": "an edit needs a targeted diff and a regression check"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
