from __future__ import annotations

import json

CHAPTER = 17
TITLE = 'Convolutional network e apprendimento geometrico'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    image = [[1.0, 2.0, 0.0], [0.0, 1.0, 2.0], [2.0, 0.0, 1.0]]
    kernel = [[1.0, 0.0], [0.0, -1.0]]
    output = [
        [
            sum(image[i + u][j + v] * kernel[u][v] for u in range(2) for v in range(2))
            for j in range(2)
        ]
        for i in range(2)
    ]
    return {
        "output": output,
        "shape": [2, 2],
        "invariant": "the same kernel is reused at every position",
    }


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
