"""Audit the qualities that structural checks cannot prove.

The book intentionally allows different lesson shapes.  This audit therefore
does not require a fixed number of headings, figures, formulas, or code blocks.
It checks the contracts that must hold across those different shapes:

* prose must not contain the historical generated scaffold;
* long paragraphs must not be recycled across chapters;
* figures in one lesson must answer different pedagogical questions;
* lessons marked ``reference`` must show Python and the captured output;
* lessons that omit code must record a concrete reason;
* appendices must contain substantive, appendix-specific material.

The audit is deliberately conservative.  It catches strong signals of a bad
draft, but it never calls a chapter "author approved".
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER_ROOT = ROOT / "chapters"
APPENDIX_ROOT = ROOT / "appendices"

CHAPTER_RE = re.compile(r"^# Capitolo (\d+)\. (.+)$", re.MULTILINE)
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+\.png)\)")
PYTHON_BLOCK_RE = re.compile(r"```python\s*\n(.+?)\n```", re.DOTALL)
OUTPUT_BLOCK_RE = re.compile(r"```(?:text|console)\s*\n(.+?)\n```", re.DOTALL)
META_RE = re.compile(r"<!--\s*(.+?)\s*-->", re.DOTALL)

# These openings came from the superseded bulk generator.  Their presence is
# a reliable signal that a lesson has not yet received an individual rewrite.
SCAFFOLD_MARKERS = (
    "Prima del nome tecnico fissiamo la situazione",
    "Per ricostruire «",
    "Il punto didattico di «",
    "La prova di «",
    "La lettura va fatta in ordine",
    "Se cambiamo una premessa, dobbiamo riaprire l'interpretazione",
    "Il caso intero parte dall'input",
    "Ricostruisci l'oggetto continuo a partire da",
)

GENERIC_APPENDIX_SENTENCE = (
    "Il lettore può usarlo per ricostruire esempi, controlli e convenzioni del libro."
)


def public_text(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def metadata(text: str) -> dict[str, str]:
    match = META_RE.search(text)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def prose_paragraphs(text: str) -> list[str]:
    clean = public_text(text)
    clean = re.sub(r"```.*?```", "", clean, flags=re.DOTALL)
    clean = re.sub(r"\$\$.*?\$\$", "", clean, flags=re.DOTALL)
    paragraphs = []
    for part in re.split(r"\n\s*\n", clean):
        value = re.sub(r"\s+", " ", part).strip()
        if not value or value.startswith(("#", "![", "|", "1. ", "2. ", "3. ", "4. ", "5. ")):
            continue
        if len(value.split()) >= 28:
            paragraphs.append(value)
    return paragraphs


def normalize_paragraph(value: str) -> str:
    value = value.casefold()
    value = re.sub(r"\[src-[^\]]+\]", "[src]", value)
    value = re.sub(r"`[^`]+`", "`code`", value)
    value = re.sub(r"\b\d+(?:[.,]\d+)?\b", "N", value)
    value = re.sub(r"capitolo\s+n", "capitolo N", value)
    return re.sub(r"\s+", " ", value).strip()


def image_questions(chapter_file: Path, images: list[tuple[str, str]]) -> tuple[list[str], list[str]]:
    questions: list[str] = []
    problems: list[str] = []
    for _alt, raw in images:
        path = (chapter_file.parent / raw).resolve()
        if not path.is_file():
            problems.append(f"immagine mancante: {raw}")
            continue
        spec = path.parent / "SPEC.md"
        alt_file = path.parent / "ALT_TEXT.md"
        audit = path.parent / "AUDIT.md"
        for required in (spec, alt_file, audit):
            if not required.is_file():
                problems.append(f"metadata visuale mancante: {required.relative_to(ROOT)}")
        if spec.is_file():
            match = re.search(r"^- domanda principale:\s*(.+)$", spec.read_text(encoding="utf-8"), re.MULTILINE)
            if match:
                questions.append(re.sub(r"\s+", " ", match.group(1).casefold()).strip())
            else:
                problems.append(f"domanda visuale assente: {spec.relative_to(ROOT)}")
    duplicates = [question for question, count in Counter(questions).items() if count > 1]
    if duplicates:
        problems.append("figure della stessa lezione con domanda pedagogica duplicata")
    return questions, problems


@dataclass
class ChapterRecord:
    number: int
    title: str
    words: int
    paragraphs: list[str]
    problems: list[str]


def audit_chapter(path: Path) -> ChapterRecord:
    raw = path.read_text(encoding="utf-8")
    public = public_text(raw)
    heading = CHAPTER_RE.search(raw)
    if not heading:
        return ChapterRecord(0, path.parent.name, 0, [], ["titolo capitolo non riconosciuto"])
    number = int(heading.group(1))
    title = heading.group(2)
    meta = metadata(raw)
    problems: list[str] = []

    words = len(re.findall(r"\b[\wÀ-ÿ][\wÀ-ÿ'’-]*\b", public))
    if words < 850:
        problems.append(f"spiegazione troppo breve per il contratto corrente: {words} parole")
    for marker in SCAFFOLD_MARKERS:
        count = public.count(marker)
        if count:
            problems.append(f"scaffold storico presente: {marker!r} ({count})")
    if number >= 14 and public.count("Il pacco non è arrivato") > 2:
        problems.append("esempio del pacco ripetuto oltre il suo eventuale valore locale")

    images = IMAGE_RE.findall(raw)
    if not images:
        problems.append("nessuna visuale attiva")
    _, visual_problems = image_questions(path, images)
    problems.extend(visual_problems)

    code_policy = meta.get("code_policy")
    python_blocks = PYTHON_BLOCK_RE.findall(public)
    output_blocks = OUTPUT_BLOCK_RE.findall(public)
    if code_policy == "reference":
        if not python_blocks:
            problems.append("code_policy reference senza blocco Python inline")
        if not output_blocks:
            problems.append("code_policy reference senza output inline")
        code_dir = path.parent / "code"
        if not list(code_dir.glob("test_*.py")):
            problems.append("code_policy reference senza test locale")
        if not list((code_dir / "outputs").glob("SNIP-*.txt")):
            problems.append("code_policy reference senza output versionato")
    elif code_policy == "exception":
        reason = meta.get("code_exception")
        if not reason or len(reason.split()) < 5:
            problems.append("eccezione Python priva di motivazione concreta")
    elif number >= 14:
        problems.append("code_policy non dichiarata")

    return ChapterRecord(number, title, words, prose_paragraphs(raw), problems)


def audit_appendix(path: Path) -> dict[str, object]:
    raw = path.read_text(encoding="utf-8")
    words = len(re.findall(r"\b[\wÀ-ÿ][\wÀ-ÿ'’-]*\b", public_text(raw)))
    problems: list[str] = []
    if words < 650:
        problems.append(f"appendice troppo breve: {words} parole")
    if GENERIC_APPENDIX_SENTENCE in raw:
        problems.append("frase segnaposto della prima materializzazione ancora presente")
    if len(re.findall(r"^## ", raw, re.MULTILINE)) < 3:
        problems.append("meno di tre sezioni sostanziali")
    return {"path": str(path.relative_to(ROOT)), "words": words, "problems": problems}


def audit() -> dict[str, object]:
    chapter_files = sorted(CHAPTER_ROOT.glob("[0-9][0-9]_*/CHAPTER.md"))
    records = [audit_chapter(path) for path in chapter_files]

    owners: dict[str, list[int]] = defaultdict(list)
    originals: dict[str, str] = {}
    for record in records:
        for paragraph in record.paragraphs:
            key = normalize_paragraph(paragraph)
            owners[key].append(record.number)
            originals.setdefault(key, paragraph)
    repeated = {
        key: sorted(set(numbers))
        for key, numbers in owners.items()
        if len(set(numbers)) >= 3 and len(key.split()) >= 32
    }
    for key, numbers in repeated.items():
        excerpt = originals[key][:120]
        for number in numbers:
            record = next(item for item in records if item.number == number)
            record.problems.append(
                f"paragrafo condiviso con i capitoli {', '.join(map(str, numbers))}: {excerpt!r}"
            )

    appendices = [audit_appendix(path) for path in sorted(APPENDIX_ROOT.glob("*/APPENDIX.md"))]
    chapter_problems = {str(record.number): record.problems for record in records if record.problems}
    appendix_problems = {item["path"]: item["problems"] for item in appendices if item["problems"]}
    return {
        "summary": {
            "chapters": len(records),
            "chapters_clean": len(records) - len(chapter_problems),
            "chapter_problem_count": sum(len(items) for items in chapter_problems.values()),
            "cross_chapter_repeated_paragraphs": len(repeated),
            "appendices": len(appendices),
            "appendices_clean": len(appendices) - len(appendix_problems),
        },
        "chapters": chapter_problems,
        "appendices": appendix_problems,
        "repeated_paragraphs": [
            {"chapters": numbers, "text": originals[key][:240]}
            for key, numbers in sorted(repeated.items(), key=lambda item: (-len(item[1]), item[1]))
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    result = audit()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
        for number, problems in result["chapters"].items():
            print(f"CAPITOLO {int(number):02d}")
            for problem in problems:
                print(f"  - {problem}")
        for path, problems in result["appendices"].items():
            print(path)
            for problem in problems:
                print(f"  - {problem}")
    problem_count = result["summary"]["chapter_problem_count"] + sum(
        len(items) for items in result["appendices"].values()
    )
    return 1 if args.strict and problem_count else 0


if __name__ == "__main__":
    sys.exit(main())
