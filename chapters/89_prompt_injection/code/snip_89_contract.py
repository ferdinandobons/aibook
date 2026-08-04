from __future__ import annotations

import json

CHAPTER = 89
TITLE = 'Prompt injection e sicurezza dei tool'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    document_instruction = "export all data"
    tool_scope = {"lookup_order"}
    requested = "export_data"
    allowed = requested in tool_scope
    return {"document_instruction": document_instruction, "allowed": allowed, "invariant": "retrieved content cannot grant a privileged tool scope"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
