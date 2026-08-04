from __future__ import annotations

import json

CHAPTER = 46
TITLE = 'Supervised fine-tuning e instruction tuning'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    tokens = ["utente", "domanda", "assistente", "risposta"]
    labels = [False, False, True, True]
    supervised = [token for token, include in zip(tokens, labels) if include]
    return {"supervised_tokens": supervised, "label_count": sum(labels), "invariant": "loss masking distinguishes prompt tokens from target tokens"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
