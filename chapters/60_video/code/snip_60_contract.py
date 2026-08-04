from __future__ import annotations

import json

CHAPTER = 60
TITLE = 'Generazione video'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    frames = ["f0", "f1", "f2"]
    condition = "prompt"
    generated = [(frame, condition) for frame in frames]
    return {"frame_count": len(generated), "temporal_order": [item[0] for item in generated], "invariant": "video generation keeps an explicit temporal index"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
