from __future__ import annotations

import json

CHAPTER = 45
TITLE = 'Byte, predizione multi-token e language diffusion'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    payload = "AI"
    encoded = list(payload.encode("utf-8"))
    groups = [encoded[index:index + 2] for index in range(0, len(encoded), 2)]
    return {"bytes": encoded, "groups": groups, "invariant": "byte grouping is explicit before any higher-level prediction"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
