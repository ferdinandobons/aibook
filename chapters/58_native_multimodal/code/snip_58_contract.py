from __future__ import annotations

import json

CHAPTER = 58
TITLE = 'Modelli multimodali nativi e any-to-any'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    sequence = [("text", 1), ("image", 7), ("text", 2)]
    vocabulary = {"text": {1, 2}, "image": {7}}
    valid = all(token in vocabulary[modality] for modality, token in sequence)
    return {"valid": valid, "length": len(sequence), "invariant": "native multimodal serialization keeps modality and token identity"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
