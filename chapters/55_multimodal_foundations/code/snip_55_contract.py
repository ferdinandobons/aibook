from __future__ import annotations

import json

CHAPTER = 55
TITLE = 'Fondamenti della multimodalità'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    text = [0.2, 0.4]
    image = [0.6, 0.1]
    shared = [(a + b) / 2 for a, b in zip(text, image)]
    return {"shared": shared, "modalities": 2, "invariant": "modalities meet in a declared shared representation"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
