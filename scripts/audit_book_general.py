"""Audit generale del libro, senza modificare gli artefatti del progetto.

Il controllo distingue la copertura automatica dalla revisione autoriale. Non
prova la verità di un claim: verifica che il claim abbia una fonte registrata,
che il codice abbia una prova eseguibile e che la visuale collegata sia
decodificabile e geometricamente contenuta.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
ASSETS = ROOT / "assets" / "chapters"
COMMON_EXAMPLE = "Il pacco non è arrivato"
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
SOURCE_RE = re.compile(r"\bSRC-(?:\d{2}|[A-Z0-9]+)-\d{3}\b")
CHAPTER_RE = re.compile(r"^# Capitolo (\d+)\. (.+)$", re.MULTILINE)
VALID_CLAIM_STATUSES = {"aperta", "verificata", "corretta", "respinta", "rimossa"}


def chapter_number(path: Path) -> int:
    match = re.match(r"^(\d+)_", path.name)
    if not match:
        raise ValueError(f"cartella capitolo non numerata: {path}")
    return int(match.group(1))


def chapter_dirs() -> list[Path]:
    return sorted(
        (path for path in CHAPTERS.iterdir() if path.is_dir() and re.match(r"^\d+_", path.name)),
        key=chapter_number,
    )


def image_paths(text: str, chapter: Path) -> list[Path]:
    paths = []
    for link in IMAGE_RE.findall(text):
        path = (chapter / link).resolve()
        paths.append(path)
    return paths


def image_metrics(path: Path) -> dict[str, object]:
    with Image.open(path) as image:
        image.load()
        rgb_image = image.convert("RGB")
        width, height = image.size
        corners = [rgb_image.getpixel(point) for point in ((0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1))]
        rgb_corners = all(pixel == (255, 255, 255) for pixel in corners)
        nonwhite = rgb_image.point(lambda value: 0 if value > 248 else 255)
        bbox = nonwhite.getbbox()
        return {
            "mode": image.mode,
            "size": [width, height],
            "white_corners": rgb_corners,
            "content_bbox": list(bbox) if bbox else None,
        }


def source_ids(chapter_text: str) -> set[str]:
    return set(SOURCE_RE.findall(chapter_text))


def claim_statuses(claims: str) -> list[str]:
    statuses = []
    for line in claims.splitlines():
        if line.lstrip().startswith("- Esito:"):
            statuses.append(line.split(":", 1)[1].strip().strip("`").lower())
            continue
        if line.startswith("|") and line.rstrip().endswith("|"):
            last_cell = line.rstrip().rstrip("|").split("|")[-1].strip().strip("`").lower()
            if last_cell in {"aperta", "verificata", "verificato", "corretta", "respinta", "rimossa", "eseguito", "eseguita"}:
                statuses.append(last_cell)
    return statuses


def code_evidence(chapter: Path) -> dict[str, object]:
    code = chapter / "code"
    if not code.exists():
        return {"exists": False, "modules": 0, "tests": 0, "outputs": 0, "problems": ["cartella code assente"]}
    modules = sorted(path for path in code.glob("*.py") if not path.name.startswith("test_"))
    tests = sorted(code.glob("test_*.py"))
    outputs = sorted((code / "outputs").glob("SNIP-*.txt")) if (code / "outputs").exists() else []
    problems = []
    if modules and not tests:
        problems.append("moduli Python senza test locali")
    if modules and not outputs:
        problems.append("moduli Python senza output SNIP")
    return {
        "exists": True,
        "modules": len(modules),
        "tests": len(tests),
        "outputs": len(outputs),
        "problems": problems,
    }


def audit() -> dict[str, object]:
    chapters = chapter_dirs()
    records = []
    all_images: list[Path] = []
    missing_images = []
    duplicate_paragraphs: Counter[str] = Counter()
    all_source_problems = []
    all_claim_problems = []
    all_code_problems = []
    common_missing = []

    for chapter in chapters:
        chapter_file = chapter / "CHAPTER.md"
        text = chapter_file.read_text(encoding="utf-8")
        heading = CHAPTER_RE.search(text)
        number = chapter_number(chapter)
        title = heading.group(2) if heading else chapter.name
        images = image_paths(text, chapter)
        all_images.extend(images)
        missing = [str(path.relative_to(ROOT)) for path in images if not path.exists()]
        missing_images.extend(missing)
        source_file = chapter / "FONTI_PRIMARIE.md"
        claim_file = chapter / "CLAIMS.md"
        source_text = source_file.read_text(encoding="utf-8") if source_file.exists() else ""
        claim_text = claim_file.read_text(encoding="utf-8") if claim_file.exists() else ""
        ids = source_ids(text)
        missing_sources = sorted(sid for sid in ids if sid not in source_text)
        if missing_sources:
            all_source_problems.append({"chapter": number, "missing": missing_sources})
        statuses = claim_statuses(claim_text)
        aliases = sorted(status for status in statuses if status in {"verificato", "eseguito", "eseguita"})
        invalid_statuses = sorted(status for status in statuses if status not in VALID_CLAIM_STATUSES and status not in aliases)
        has_status_field = "- Esito:" in claim_text or bool(re.search(r"\|\s*Esito\s*\|", claim_text, re.IGNORECASE))
        if invalid_statuses or aliases or (claim_file.exists() and has_status_field and not statuses):
            all_claim_problems.append({"chapter": number, "invalid": invalid_statuses, "noncanonical": aliases, "count": len(statuses)})
        code = code_evidence(chapter)
        if code["problems"]:
            all_code_problems.append({"chapter": number, "problems": code["problems"]})
        if COMMON_EXAMPLE not in text:
            common_missing.append(number)
        paragraphs = [
            part.strip()
            for part in re.split(r"\n\s*\n", text)
            if len(part.strip().split()) >= 35
            and "Verifica della comprensione" not in part
            and "Esercizi" not in part
            and not re.match(r"^\d+\. ", part.strip())
        ]
        duplicate_paragraphs.update(paragraphs)
        h2 = len(re.findall(r"^## ", text, re.MULTILINE))
        h3 = len(re.findall(r"^### ", text, re.MULTILINE))
        records.append(
            {
                "number": number,
                "title": title,
                "words": len(text.split()),
                "h2": h2,
                "h3": h3,
                "images": len(images),
                "common_example": COMMON_EXAMPLE in text,
                "source_ids": len(ids),
                "code": code,
                "missing_images": missing,
            }
        )

    unique_images = sorted(set(all_images))
    image_issues = []
    image_family_counts: Counter[str] = Counter()
    for path in unique_images:
        if not path.exists():
            continue
        try:
            metrics = image_metrics(path)
        except Exception as exc:  # pragma: no cover - defensive audit path
            image_issues.append({"path": str(path.relative_to(ROOT)), "error": str(exc)})
            continue
        try:
            spec = path.parent / "SPEC.md"
            family_match = re.search(r"^- famiglia: (.+)$", spec.read_text(encoding="utf-8"), re.MULTILINE)
            if family_match:
                image_family_counts[family_match.group(1).strip()] += 1
        except FileNotFoundError:
            image_issues.append({"path": str(path.relative_to(ROOT)), "error": "SPEC.md assente"})
        if metrics["mode"] not in {"RGB", "RGBA"}:
            image_issues.append({"path": str(path.relative_to(ROOT)), "error": f"modalità {metrics['mode']}"})
        if metrics["size"] != [1800, 1000] and path.name.startswith("candidate-v"):
            image_issues.append({"path": str(path.relative_to(ROOT)), "error": f"dimensione {metrics['size']}"})
        if not metrics["white_corners"]:
            image_issues.append({"path": str(path.relative_to(ROOT)), "error": "angoli non bianchi"})

    repeated = [
        {"count": count, "words": len(paragraph.split()), "text": paragraph[:180]}
        for paragraph, count in duplicate_paragraphs.items()
        if count >= 8
    ]
    records.sort(key=lambda item: item["number"])
    return {
        "chapters": records,
        "summary": {
            "chapters": len(records),
            "images_linked": len(all_images),
            "images_unique": len(unique_images),
            "missing_images": len(missing_images),
            "image_issues": len(image_issues),
            "common_example_missing": common_missing,
            "source_problems": len(all_source_problems),
            "claim_problems": len(all_claim_problems),
            "code_problems": len(all_code_problems),
            "repeated_paragraphs_ge8": len(repeated),
            "image_families": dict(sorted(image_family_counts.items())),
            "words_min": min(item["words"] for item in records) if records else 0,
            "words_max": max(item["words"] for item in records) if records else 0,
        },
        "problems": {
            "missing_images": missing_images,
            "image_issues": image_issues,
            "source_problems": all_source_problems,
            "claim_problems": all_claim_problems,
            "code_problems": all_code_problems,
            "repeated_paragraphs": repeated,
        },
    }


def markdown_report(result: dict[str, object]) -> str:
    summary = result["summary"]
    lines = [
        "# Audit generale del libro",
        "",
        "Audit statico e raster eseguito dal verificatore locale. Il controllo non sostituisce la rilettura autoriale e non trasforma una fonte in una garanzia di performance.",
        "",
        "## Risultato sintetico",
        "",
        f"- Capitoli: {summary['chapters']}",
        f"- Immagini collegate: {summary['images_linked']} riferimenti, {summary['images_unique']} file distinti",
        f"- Parole per capitolo: minimo {summary['words_min']}, massimo {summary['words_max']}",
        f"- Immagini mancanti: {summary['missing_images']}",
        f"- Problemi raster automatici: {summary['image_issues']}",
        f"- Problemi di mapping delle fonti: {summary['source_problems']}",
        f"- Problemi nei claim: {summary['claim_problems']}",
        f"- Problemi di copertura del codice: {summary['code_problems']}",
        f"- Paragrafi ripetuti in almeno otto capitoli: {summary['repeated_paragraphs_ge8']}",
        "",
        "## Famiglie visuali",
        "",
    ]
    for family, count in summary["image_families"].items():
        lines.append(f"- `{family}`: {count}")
    lines.extend(["", "## Capitoli con esempio comune assente", ""])
    missing_common = summary["common_example_missing"]
    lines.append("- Nessuno" if not missing_common else "- " + ", ".join(str(number) for number in missing_common))
    lines.extend(["", "## Problemi rilevati", "", "```json", json.dumps(result["problems"], ensure_ascii=False, indent=2), "```", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="stampa il risultato JSON")
    parser.add_argument("--write-report", type=Path, help="scrive un report Markdown nel percorso indicato")
    args = parser.parse_args()
    result = audit()
    if args.write_report:
        args.write_report.write_text(markdown_report(result), encoding="utf-8")
    print(json.dumps(result if args.json else result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
