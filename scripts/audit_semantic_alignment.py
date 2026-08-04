"""Audit semantic routing, claim citations, depth, and active visual contracts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import complete_remaining_book as base  # noqa: E402
import lesson_evidence as evidence  # noqa: E402


CHAPTER_RE = re.compile(r"^# Capitolo (\d+)\. ", re.MULTILINE)
SOURCE_RE = re.compile(r"^## (SRC-\d{2}-\d{3})\s*$", re.MULTILINE)
CLAIM_RE = re.compile(r"^## (CL-\d{2}-(?:\d{2}|CODE))\s*$", re.MULTILINE)
SOURCE_LINK_RE = re.compile(r"\[?(SRC-\d{2}-\d{3})\]?\b")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+/assets/chapters/[^)]+/candidate-v\d+\.png)\)")


def norm(text: str) -> str:
    return " ".join(text.casefold().split())


def sections_from_specs(number: int) -> list[tuple[str, str]]:
    if number not in base.SPECS:
        return []
    return list(base.SPECS[number][6])


def source_blocks(text: str) -> dict[str, str]:
    matches = list(SOURCE_RE.finditer(text))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[match.group(1)] = text[match.start():end]
    return result


def claim_blocks(text: str) -> dict[str, str]:
    matches = list(CLAIM_RE.finditer(text))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[match.group(1)] = text[match.start():end]
    return result


def active_image_paths(chapter_file: Path, chapter_number: int) -> list[Path]:
    paths = []
    for raw in IMAGE_RE.findall(chapter_file.read_text(encoding="utf-8")):
        path = (chapter_file.parent / raw).resolve()
        if path not in paths:
            paths.append(path)
    return paths


def audit_chapter(number: int, chapter_file: Path) -> list[str]:
    problems: list[str] = []
    text = chapter_file.read_text(encoding="utf-8")
    source_file = chapter_file.parent / "FONTI_PRIMARIE.md"
    claims_file = chapter_file.parent / "CLAIMS.md"
    source_text = source_file.read_text(encoding="utf-8") if source_file.exists() else ""
    claims_text = claims_file.read_text(encoding="utf-8") if claims_file.exists() else ""
    expected_topic = evidence.topic_for(number, base.profile(number) if number in base.SPECS else "lab")

    if number in evidence.CHAPTER_TOPIC and f"tema `{expected_topic}`" not in source_text:
        problems.append(f"routing assente o disallineato: atteso {expected_topic}")
    if number in evidence.DETAILS:
        detail = evidence.DETAILS[number]
        for label, value in (("oggetto", detail["object"]), ("input", detail["input"]), ("output", detail["output"]), ("invariante", detail["invariant"])):
            if norm(value) not in norm(text):
                problems.append(f"{label} del contratto non rintracciabile")

    headings = [heading for heading, _ in sections_from_specs(number)]
    for heading in headings:
        if f"## {heading}" not in text:
            problems.append(f"sezione mancante: {heading}")
    if len(headings) >= 5 and text.count("## ") < 5:
        problems.append("copertura inferiore ai cinque nuclei semantici previsti")
    if len(text.split()) < 850:
        problems.append(f"testo breve: {len(text.split())} parole")

    chapter_source_ids = set(SOURCE_LINK_RE.findall(text))
    dossier_ids = set(source_blocks(source_text))
    claim_map = claim_blocks(claims_text)
    if not source_text:
        problems.append("FONTI_PRIMARIE.md assente")
    if not claims_text:
        problems.append("CLAIMS.md assente")
    for sid in chapter_source_ids:
        if sid not in dossier_ids:
            problems.append(f"fonte citata senza dossier: {sid}")
    for block_id, block in source_blocks(source_text).items():
        if "URL o identificatore:" not in block:
            problems.append(f"URL assente: {block_id}")
        if "Sezioni rilevanti: ;" in block or "Affermazioni sostenibili: \n" in block:
            problems.append(f"dossier vuoto: {block_id}")
    expected_claims = {f"CL-{number:02d}-{index:02d}" for index in range(1, len(headings) + 1)}
    missing_claims = expected_claims - set(claim_map)
    if missing_claims:
        problems.append(f"claim mancanti: {', '.join(sorted(missing_claims))}")
    for claim_id, block in claim_map.items():
        if claim_id.endswith("CODE"):
            continue
        cited = set(SOURCE_LINK_RE.findall(block))
        if not cited:
            problems.append(f"claim senza fonte: {claim_id}")
        elif not cited <= dossier_ids:
            problems.append(f"claim con fonte non dossier: {claim_id}")
        if "Esito: verificata" not in block and "Esito: corretta" not in block:
            problems.append(f"claim non chiuso: {claim_id}")

    active_images = active_image_paths(chapter_file, number)
    if not active_images:
        problems.append("nessuna figura attiva")
    for image in active_images:
        if not image.exists():
            problems.append(f"immagine assente: {image}")
            continue
        figure_dir = image.parent
        spec = figure_dir / "SPEC.md"
        audit = figure_dir / "AUDIT.md"
        alt = figure_dir / "ALT_TEXT.md"
        for metadata in (spec, audit, alt):
            if not metadata.exists():
                problems.append(f"metadata assente: {metadata.relative_to(ROOT)}")
        if spec.exists() and number in evidence.CHAPTER_TOPIC:
            spec_text = spec.read_text(encoding="utf-8")
            if "formato: PNG raster 1800x1000" not in spec_text:
                problems.append(f"formato visuale non dichiarato: {image.relative_to(ROOT)}")
            if "domanda principale:" not in spec_text:
                problems.append(f"domanda visuale assente: {image.relative_to(ROOT)}")
        if audit.exists() and number in evidence.CHAPTER_TOPIC and "approvazione autoriale: aperta" not in audit.read_text(encoding="utf-8"):
            problems.append(f"audit visuale non riaperto: {image.relative_to(ROOT)}")

    # Known bad profile routings are kept as hard guards.  They make a generic
    # fallback impossible to mistake for topic validation.
    forbidden = {
        "governance": ("Universal and Transferable Adversarial", "Not What You’ve Signed Up For", "OWASP, Top 10"),
        "small_lm": ("Artifact Review and Badging", "Python Documentation"),
        "interpretability": ("Holistic Evaluation", "Measuring Massive Multitask"),
        "sae": ("AI Risk Management Framework", "Model Cards for Model Reporting"),
        "privacy_fairness": ("Universal and Transferable Adversarial", "Not What You’ve Signed Up For"),
    }
    for token in forbidden.get(expected_topic, ()):
        if token in source_text:
            problems.append(f"fonte di profilo non pertinente: {token}")
    return problems


def run() -> dict:
    chapters = sorted(ROOT.glob("chapters/*/CHAPTER.md"))
    details = {}
    for chapter_file in chapters:
        match = CHAPTER_RE.search(chapter_file.read_text(encoding="utf-8"))
        if not match:
            continue
        number = int(match.group(1))
        details[str(number)] = audit_chapter(number, chapter_file)
    problems = {number: issues for number, issues in details.items() if issues}
    return {
        "chapters": len(details),
        "chapters_clean": len(details) - len(problems),
        "chapters_with_problems": len(problems),
        "problem_count": sum(len(items) for items in problems.values()),
        "problems": problems,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"chapters={result['chapters']} clean={result['chapters_clean']} problems={result['problem_count']}")
        for number, issues in result["problems"].items():
            print(f"{number}: " + "; ".join(issues))
    raise SystemExit(1 if result["problem_count"] else 0)


if __name__ == "__main__":
    main()
