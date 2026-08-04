from __future__ import annotations

import json

CHAPTER = 81
TITLE = 'Compiler, kernel e runtime'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    graph = ["matmul", "add", "relu"]
    fused = ["matmul_add", "relu"]
    return {"original_ops": len(graph), "fused_ops": len(fused), "invariant": "compiler optimization preserves the declared operator result"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
