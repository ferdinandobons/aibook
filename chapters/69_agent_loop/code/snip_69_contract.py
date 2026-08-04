from __future__ import annotations

import json

CHAPTER = 69
TITLE = 'Ciclo agentico, pianificazione e verifica'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    events = ["observe", "plan", "tool", "verify"]
    valid = events == ["observe", "plan", "tool", "verify"]
    return {"events": events, "valid": valid, "invariant": "an agent loop records observation, action and verification"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
