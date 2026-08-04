from __future__ import annotations

import json

CHAPTER = 57
TITLE = 'Generazione e modifica delle immagini'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    noisy = [0.9, 0.1]
    denoised = [0.7 * noisy[0] + 0.3 * 0.5, 0.7 * noisy[1] + 0.3 * 0.5]
    return {"denoised": denoised, "steps": 1, "invariant": "a generation step declares its noise level and update"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
