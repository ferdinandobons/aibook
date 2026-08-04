from __future__ import annotations

import hashlib
import json

CHAPTER = 92
TITLE = 'Watermarking e provenienza dei contenuti'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    payload = "Il pacco non è arrivato"
    manifest = {"payload": payload, "creator": "local-test", "version": "v1"}
    digest = hashlib.sha256(json.dumps(manifest, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    tampered = dict(manifest, payload="Il pacco è arrivato")
    tampered_digest = hashlib.sha256(json.dumps(tampered, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    return {"digest_prefix": digest[:12], "tamper_detected": digest != tampered_digest, "invariant": "provenance detects a changed record but does not certify its truth"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
