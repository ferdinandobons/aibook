from __future__ import annotations

import json

CHAPTER = 77
TITLE = 'Speculative e parallel decoding'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    draft = ["a", "b", "c"]
    target_accepts = [True, True, False]
    accepted = [token for token, ok in zip(draft, target_accepts) if ok]
    fallback = "target_next" if not target_accepts[-1] else None
    return {"accepted": accepted, "fallback": fallback, "invariant": "speculative decoding verifies draft tokens before committing them"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
