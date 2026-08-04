"""Ensure inline Python and captured output are the executed artefacts."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
CHAPTER_RE = re.compile(r"^# Capitolo (\d+)\. ", re.MULTILINE)
PYTHON_RE = re.compile(r"```python\s*\n(.+?)\n```", re.DOTALL)
TEXT_RE = re.compile(r"```text\s*\n(.+?)\n```", re.DOTALL)


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def audit_chapter(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    match = CHAPTER_RE.search(text)
    if not match:
        return ["titolo capitolo non riconosciuto"]
    number = int(match.group(1))
    meta = re.search(r"^code_policy:\s*(\w+)", text, re.MULTILINE)
    policy = meta.group(1) if meta else "undeclared"
    if policy != "reference" or number <= 13 or number == 28:
        return []
    problems: list[str] = []
    code_dir = path.parent / "code"
    source = code_dir / f"snip_{number:02d}_contract.py"
    output = code_dir / "outputs" / f"SNIP-{number:02d}-001.txt"
    if not source.exists():
        problems.append(f"modulo assente: {source.relative_to(ROOT)}")
    if not output.exists():
        problems.append(f"output assente: {output.relative_to(ROOT)}")
    python_blocks = PYTHON_RE.findall(text)
    text_blocks = TEXT_RE.findall(text)
    if not python_blocks:
        problems.append("nessun blocco Python inline")
    if not text_blocks:
        problems.append("nessun output inline")
    if source.exists():
        source_texts = [normalized(source.read_text(encoding="utf-8"))]
        source_texts.extend(
            normalized(candidate.read_text(encoding="utf-8"))
            for candidate in code_dir.glob("*.py")
            if not candidate.name.startswith("test_") and candidate != source
        )
        for index, block in enumerate(python_blocks, 1):
            if not any(normalized(block) in candidate for candidate in source_texts):
                problems.append(f"blocco Python {index} non contenuto nel file eseguito")
    if output.exists():
        output_text = normalized(output.read_text(encoding="utf-8"))
        if not any(normalized(block) in output_text for block in text_blocks):
            problems.append("nessun output inline coincide con l'artefatto versionato")
    return problems


def audit() -> dict[str, object]:
    records = {}
    reference_count = 0
    for path in sorted(CHAPTERS.glob("[0-9][0-9]_*/CHAPTER.md")):
        match = CHAPTER_RE.search(path.read_text(encoding="utf-8"))
        if not match:
            continue
        if re.search(r"^code_policy:\s*reference", path.read_text(encoding="utf-8"), re.MULTILINE) and int(match.group(1)) > 13 and int(match.group(1)) != 28:
            reference_count += 1
        problems = audit_chapter(path)
        records[match.group(1)] = problems
    problems = {number: values for number, values in records.items() if values}
    return {
        "summary": {
            "reference_chapters": reference_count,
            "chapters_checked": len(records),
            "chapters_with_problems": len(problems),
            "problem_count": sum(len(values) for values in problems.values()),
        },
        "problems": problems,
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
        for number, values in result["problems"].items():
            print(f"CAPITOLO {number}: " + "; ".join(values))
    return 1 if args.strict and result["problems"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
