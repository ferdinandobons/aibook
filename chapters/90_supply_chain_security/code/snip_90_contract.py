from __future__ import annotations

import json

CHAPTER = 90
TITLE = 'Poisoning, backdoor, extraction e supply chain'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    artifact = {"name": "checkpoint", "digest": "abc123", "owner": "team-a"}
    trusted_owners = {"team-a"}
    decision = artifact["owner"] in trusted_owners and bool(artifact["digest"])
    return {"release": decision, "invariant": "artifact integrity and content trust are separate checks"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
