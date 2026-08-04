from __future__ import annotations

import hashlib
import json

CHAPTER = 94
TITLE = 'Percorso pratico dai fondamenti'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    configuration = {"seed": 7, "split": "fixed", "dtype": "float32"}
    digest = hashlib.sha256(json.dumps(configuration, sort_keys=True).encode()).hexdigest()
    return {"configuration_digest": digest[:12], "configuration": configuration, "invariant": "a local run is reproducible only with its declared setup"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
