from __future__ import annotations

import json

CHAPTER = 96
TITLE = 'Progetto di produzione completo'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    release = {"version": "v2", "offline_gate": True, "canary": True, "rollback": True}
    ready = all(release[key] for key in ("offline_gate", "canary", "rollback"))
    return {"version": release["version"], "ready_for_review": ready, "invariant": "production readiness requires independent gates and a rollback path"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
