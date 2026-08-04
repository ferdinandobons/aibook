from __future__ import annotations

import json

CHAPTER = 71
TITLE = 'Training e valutazione degli agenti'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    traces = [{"success": True, "violations": 0}, {"success": True, "violations": 1}]
    safe_success = sum(trace["success"] and trace["violations"] == 0 for trace in traces)
    return {"task_success": sum(trace["success"] for trace in traces), "safe_success": safe_success, "invariant": "task completion and policy compliance are separate metrics"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
