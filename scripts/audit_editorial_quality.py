"""Audit editoriale profondo del libro senza modificare gli artefatti.

Questo controllo non sostituisce la lettura autoriale. Verifica però i difetti
che una revisione strutturale può facilmente nascondere: costruzioni italiane
malformate, didascalie ambigue, formule schematiche non etichettate, prosa
duplicata, dossier con riferimenti troppo generici e codice non collegato agli
artefatti eseguiti.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
COMMON_EXAMPLE = "Il pacco non è arrivato"
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
FORMULA_RE = re.compile(r"\$\$\s*\n(.+?)\n\$\$", re.DOTALL)
CHAPTER_RE = re.compile(r"^# Capitolo (\d+)\. (.+)$", re.MULTILINE)
HEADING_RE = re.compile(r"^#{2,3} (.+)$", re.MULTILINE)
SOURCE_ID_RE = re.compile(r"\bSRC-\d{2}-\d{3}\b")

MALFORMED_PATTERNS = {
    "article_a_la": re.compile(r"\ba la\b", re.IGNORECASE),
    "article_a_il": re.compile(r"\ba il\b", re.IGNORECASE),
    "article_a_i": re.compile(r"\ba i\b", re.IGNORECASE),
    "fino_a_article": re.compile(r"\bfino a (?:la|il|i|gli)\b", re.IGNORECASE),
    "question_period": re.compile(r"\?\."),
    "figure_colon_caption": re.compile(r"^La figura [^\n:]+ usa la famiglia [^\n:.]+:", re.MULTILINE),
    "mechanical_reading": re.compile(
        r"\b(?:La lettura di|Per non saltare dalla definizione|La sequenza si può|"
        r"Il caso diventa trasferibile|Il valore didattico del caso|La distinzione utile è|"
        r"Il termine tecnico indica una relazione)\b"
    ),
}

SCHEMA_MARKERS = ("schema compatto", "schema concettuale", "notazione di interfaccia", "schema mnemonico")
SCHEMATIC_FORMULA_HINTS = ("claim =", "attention = tiles", "tool_call =", "trajectory =", "system =", "result = run(")


def chapter_dirs() -> list[Path]:
    return sorted(
        (p for p in CHAPTERS.iterdir() if p.is_dir() and re.match(r"^\d+_", p.name)),
        key=lambda p: int(p.name.split("_", 1)[0]),
    )


def public_text(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return text


def paragraphs(text: str) -> list[str]:
    return [
        re.sub(r"\s+", " ", part).strip()
        for part in public_text(text).split("\n\n")
        if part.strip() and not part.lstrip().startswith(("#", "![]", "1. ", "2. ", "3. ", "4. ", "5. "))
    ]


def normalize_paragraph(value: str) -> str:
    value = re.sub(r"\[SRC-[^\]]+\]", "[SRC]", value)
    value = re.sub(r"\b(?:14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98)\b", "N", value)
    return re.sub(r"\s+", " ", value.lower()).strip()


def image_record(path: Path) -> dict[str, object]:
    record: dict[str, object] = {"path": str(path.relative_to(ROOT)), "problems": []}
    try:
        with Image.open(path) as image:
            image.load()
            record["size"] = list(image.size)
            record["mode"] = image.mode
            rgb = image.convert("RGB")
            width, height = image.size
            nonwhite = rgb.point(lambda value: 0 if value > 248 else 255)
            bbox = nonwhite.getbbox()
            record["bbox"] = list(bbox) if bbox else None
            if image.size != (1800, 1000):
                record["problems"].append("dimensione diversa da 1800x1000")
            if image.mode != "RGB":
                record["problems"].append("modalita diversa da RGB")
            if bbox and (bbox[0] <= 2 or bbox[1] <= 2 or bbox[2] >= width - 2 or bbox[3] >= height - 2):
                record["problems"].append("contenuto troppo vicino al bordo")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            record["sha256"] = digest
    except Exception as exc:  # pragma: no cover - defensive audit path
        record["problems"].append(f"immagine non leggibile: {exc}")
    return record


def audit_chapter(chapter: Path) -> dict[str, object]:
    path = chapter / "CHAPTER.md"
    text = path.read_text(encoding="utf-8")
    public = public_text(text)
    heading = CHAPTER_RE.search(text)
    number = int(chapter.name.split("_", 1)[0])
    title = heading.group(2) if heading else chapter.name
    section_titles = [m.group(1) for m in HEADING_RE.finditer(public) if not m.group(1).startswith(("Capitolo", "Fonti", "Dossier", "Materiali"))]
    image_paths = [((chapter / link).resolve()) for link in IMAGE_RE.findall(text)]
    images = [image_record(image) for image in image_paths if image.exists()]
    missing_images = [str(image.relative_to(ROOT)) for image in image_paths if not image.exists()]
    formula_blocks = FORMULA_RE.findall(public)
    formula_problems = []
    for formula in formula_blocks:
        if any(hint in formula.lower() for hint in SCHEMATIC_FORMULA_HINTS):
            window_start = public.find(formula)
            preceding = public[max(0, window_start - 180):window_start].lower()
            if not any(marker in preceding for marker in SCHEMA_MARKERS):
                formula_problems.append(f"schema non etichettato: {formula.strip()}")
    para = paragraphs(public)
    normalized = Counter(normalize_paragraph(p) for p in para)
    duplicate_paragraphs = [value for value, count in normalized.items() if count >= 2 and len(value) > 90]
    malformed = {
        name: pattern.findall(public)
        for name, pattern in MALFORMED_PATTERNS.items()
        if pattern.search(public)
    }
    source_file = chapter / "FONTI_PRIMARIE.md"
    claims_file = chapter / "CLAIMS.md"
    sources = source_file.read_text(encoding="utf-8") if source_file.exists() else ""
    claims = claims_file.read_text(encoding="utf-8") if claims_file.exists() else ""
    generic_source_lines = [line for line in sources.splitlines() if "riferimento sostiene la definizione o il meccanismo" in line]
    generic_claim_lines = [line for line in claims.splitlines() if "riferimento alla sezione rilevante" in line]
    code_dir = chapter / "code"
    code_modules = sorted(code_dir.glob("*.py")) if code_dir.exists() else []
    tests = sorted(code_dir.glob("test_*.py")) if code_dir.exists() else []
    outputs = sorted((code_dir / "outputs").glob("SNIP-*.txt")) if (code_dir / "outputs").exists() else []
    problems: list[str] = []
    if COMMON_EXAMPLE not in public:
        problems.append("esempio comune assente")
    if len(section_titles) < 3:
        problems.append("meno di tre sezioni pubbliche")
    if len(para) < 15:
        problems.append(f"prosa pubblica corta: {len(para)} paragrafi")
    if missing_images:
        problems.append(f"immagini mancanti: {len(missing_images)}")
    problems.extend(f"{key}: {len(values)} occorrenze" for key, values in malformed.items())
    problems.extend(f"immagine: {issue}" for image in images for issue in image["problems"])
    problems.extend(formula_problems)
    if duplicate_paragraphs:
        problems.append(f"paragrafi ripetuti dopo normalizzazione: {len(duplicate_paragraphs)}")
    if not code_modules or not tests or not outputs:
        problems.append("evidenza codice incompleta")
    return {
        "number": number,
        "title": title,
        "words": len(re.findall(r"\b[\wÀ-ÿ][\wÀ-ÿ'’-]*\b", public)),
        "paragraphs": len(para),
        "sections": len(section_titles),
        "sources_cited": len(set(SOURCE_ID_RE.findall(public))),
        "images": images,
        "missing_images": missing_images,
        "formulas": formula_blocks,
        "formula_problems": formula_problems,
        "malformed": {key: len(values) for key, values in malformed.items()},
        "duplicate_paragraphs": len(duplicate_paragraphs),
        "generic_source_lines": len(generic_source_lines),
        "generic_claim_lines": len(generic_claim_lines),
        "code": {"modules": len(code_modules), "tests": len(tests), "outputs": len(outputs)},
        "problems": problems,
    }


def audit() -> dict[str, object]:
    records = [audit_chapter(chapter) for chapter in chapter_dirs()]
    images = [image for record in records for image in record["images"]]
    hashes = Counter(image.get("sha256") for image in images if image.get("sha256"))
    duplicate_images = {digest: count for digest, count in hashes.items() if count > 1}
    malformed_count = sum(sum(record["malformed"].values()) for record in records)
    formula_count = sum(len(record["formulas"]) for record in records)
    summary = {
        "chapters": len(records),
        "chapters_with_problems": sum(bool(record["problems"]) for record in records),
        "words_min": min((record["words"] for record in records), default=0),
        "words_max": max((record["words"] for record in records), default=0),
        "images": len(images),
        "image_problems": sum(len(image["problems"]) for image in images),
        "duplicate_image_files": len(duplicate_images),
        "formulas": formula_count,
        "unlabelled_formula_schemas": sum(len(record["formula_problems"]) for record in records),
        "malformed_occurrences": malformed_count,
        "duplicate_paragraph_records": sum(record["duplicate_paragraphs"] for record in records),
        "generic_source_records": sum(record["generic_source_lines"] for record in records),
        "generic_claim_records": sum(record["generic_claim_lines"] for record in records),
        "missing_images": sum(len(record["missing_images"]) for record in records),
    }
    return {"summary": summary, "duplicate_images": duplicate_images, "chapters": records}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="stampa il rapporto in JSON")
    parser.add_argument("--strict", action="store_true", help="fallisce se restano problemi editoriali automatici")
    args = parser.parse_args()
    report = audit()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
        for record in report["chapters"]:
            if record["problems"]:
                print(f"CAPITOLO {record['number']:02d}: {record['title']}")
                for problem in record["problems"]:
                    print(f"  - {problem}")
    if args.strict:
        return 1 if report["summary"]["chapters_with_problems"] else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
