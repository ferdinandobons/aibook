from __future__ import annotations

import json

CHAPTER = 32
TITLE = 'Il ciclo di vita dei dati'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    records = [{"id": "a", "source": "mail", "text": "pacco"}, {"id": "b", "source": "crm", "text": "ritardo"}]
    manifest = {"ids": [record["id"] for record in records], "sources": sorted({record["source"] for record in records})}
    return {"manifest": manifest, "invariant": "data transformations retain provenance and a stable record identity"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
