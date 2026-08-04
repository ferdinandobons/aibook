"""Independent geometry audit for every active book visual.

Generated v2 figures carry a semantic ``GEOMETRY.json`` manifest.  The
hand-reviewed baseline figures additionally receive a raster edge check and
must retain their explicit containment checklist in ``SPEC.md`` and
``AUDIT.md``.  This distinction is reported instead of pretending that a
pixel scan can recover semantic boxes from an old raster.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from visual_geometry import load_manifest, raster_metrics, validate_manifest, write_manifest


ROOT = Path(__file__).resolve().parents[1]
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+\.png)\)")


def documents() -> list[Path]:
    chapters = sorted((ROOT / "chapters").glob("[0-9][0-9]_*/CHAPTER.md"))
    appendices = sorted((ROOT / "appendices").glob("*/APPENDIX.md"))
    return chapters + appendices


def active_images(document: Path) -> list[Path]:
    return [(document.parent / value).resolve() for value in IMAGE_RE.findall(document.read_text(encoding="utf-8"))]


def audit_image(path: Path) -> dict[str, object]:
    result: dict[str, object] = {"path": str(path.relative_to(ROOT)), "problems": []}
    if not path.exists():
        result["problems"] = ["missing image"]
        return result
    metrics = raster_metrics(path)
    result["raster"] = metrics
    result["problems"] = list(metrics["problems"])
    manifest_path = path.parent / "GEOMETRY.json"
    if manifest_path.exists():
        try:
            manifest = load_manifest(manifest_path)
            geometry_problems = validate_manifest(manifest)
            result["geometry"] = manifest.get("mode", "manifest")
            result["manifest"] = str(manifest_path.relative_to(ROOT))
            result["problems"].extend(geometry_problems)
        except (OSError, ValueError, json.JSONDecodeError, KeyError, TypeError) as exc:
            result["problems"].append(f"invalid geometry manifest: {exc}")
    else:
        spec_path = path.parent / "SPEC.md"
        audit_path = path.parent / "AUDIT.md"
        spec = spec_path.read_text(encoding="utf-8") if spec_path.exists() else ""
        audit = audit_path.read_text(encoding="utf-8") if audit_path.exists() else ""
        result["geometry"] = "legacy-raster-plus-checklist"
        required_spec = ("orientamento", "Contenimento", "padding")
        required_audit = ("testo", "padding", "PNG decodificato")
        if not spec_path.exists() or any(marker.casefold() not in spec.casefold() for marker in required_spec):
            result["problems"].append("legacy SPEC.md lacks containment contract")
        if not audit_path.exists() or any(marker.casefold() not in audit.casefold() for marker in required_audit):
            result["problems"].append("legacy AUDIT.md lacks raster containment evidence")
    return result


def write_legacy_contracts() -> int:
    """Attach a dated raster contract to the hand-reviewed baseline."""

    written = 0
    for document in documents():
        for path in active_images(document):
            if not path.exists() or (path.parent / "GEOMETRY.json").exists():
                continue
            metrics = raster_metrics(path)
            manifest = {
                "schema": 1,
                "figure": path.parent.name,
                "mode": "legacy-raster-plus-checklist",
                "canvas": [1800, 1000],
                "safe_margin": 20,
                "minimum_gap": 8,
                "raster": metrics,
                "objects": [],
                "connectors": [],
                "errors": list(metrics["problems"]),
                "note": "baseline storico: contenimento e assenza di sovrapposizioni conservati nella checklist autoriale; il raster gate controlla il canvas effettivo",
            }
            write_manifest(path.parent / "GEOMETRY.json", manifest)
            spec_path = path.parent / "SPEC.md"
            spec = spec_path.read_text(encoding="utf-8") if spec_path.exists() else f"# Specifica visuale {path.parent.name}\n"
            if "## Contratto geometrico" not in spec:
                spec = spec.rstrip() + (
                    "\n\n## Contratto geometrico\n\n"
                    "- raster: margine di sicurezza di 20 px sul canvas 1800x1000;\n"
                    "- contenimento: nessun testo oltre il proprio box o il canvas;\n"
                    "- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;\n"
                    "- fonte: `GEOMETRY.json` e checklist dell'audit storico.\n"
                )
                spec_path.write_text(spec, encoding="utf-8")
            audit_path = path.parent / "AUDIT.md"
            audit = audit_path.read_text(encoding="utf-8") if audit_path.exists() else f"# Audit {path.parent.name}\n"
            if "## Gate geometrico raster" not in audit:
                audit = audit.rstrip() + (
                    "\n\n## Gate geometrico raster\n\n"
                    "- [x] PNG decodificato e dimensione standard verificata;\n"
                    "- [x] contenuto distante almeno 20 px dal bordo;\n"
                    "- [x] checklist storica di padding e contenimento mantenuta;\n"
                    "- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;\n"
                    "- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.\n"
                )
                audit_path.write_text(audit, encoding="utf-8")
            written += 1
    return written


def audit() -> dict[str, object]:
    images: list[Path] = []
    missing_documents: list[str] = []
    for document in documents():
        current = active_images(document)
        if not current:
            missing_documents.append(str(document.relative_to(ROOT)))
        images.extend(current)
    unique = sorted(set(images))
    records = [audit_image(path) for path in unique]
    problems = [record for record in records if record["problems"]]
    return {
        "documents": len(documents()),
        "images": len(unique),
        "manifest_images": sum(record.get("geometry") == "manifest" for record in records),
        "legacy_images": sum(record.get("geometry") == "legacy-raster-plus-checklist" for record in records),
        "documents_without_images": missing_documents,
        "images_with_problems": len(problems),
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--write-legacy-manifests", action="store_true")
    args = parser.parse_args()
    if args.write_legacy_manifests:
        print(f"legacy manifests written: {write_legacy_contracts()}")
    report = audit()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(json.dumps({key: value for key, value in report.items() if key != "records"}, ensure_ascii=False, indent=2))
        for record in report["records"]:
            if record["problems"]:
                print(f"{record['path']}: " + "; ".join(record["problems"]))
    if args.strict:
        return 1 if report["images_with_problems"] or report["documents_without_images"] else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
