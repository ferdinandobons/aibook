"""Audit the formula and schema contracts used by generated lessons.

The check is intentionally modest but stronger than a regular-expression
presence check: every generated formula must be present in its lesson, every
displayed block must have balanced delimiters and a nearby explanation, and
schema-like expressions must be explicitly labelled as schemas rather than
being presented as measured laws.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import revise_book_completeness as base  # noqa: E402


FORMULA_BLOCK_RE = re.compile(r"\$\$\s*\n(.+?)\n\s*\$\$", re.DOTALL)
SCHEMA_MARKER = "**Schema concettuale.**"


def compact(value: str) -> str:
    return re.sub(r"\s+", "", value.casefold())


def balanced_delimiters(value: str) -> bool:
    pairs = {"(": ")", "[": "]", "{": "}"}
    closing = set(pairs.values())
    stack: list[str] = []
    escaped = False
    for char in value:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char in pairs:
            stack.append(pairs[char])
        elif char in closing:
            if not stack or stack.pop() != char:
                return False
    return not stack and not escaped


def nearby_explanation(text: str, end: int) -> bool:
    tail = text[end : end + 420]
    tail = re.sub(r"\s+", " ", tail).strip()
    if not tail:
        return False
    sentence = re.split(r"(?<=[.!?])\s+", tail, maxsplit=1)[0]
    return len(sentence.split()) >= 6


def audit() -> dict[str, object]:
    records: list[dict[str, object]] = []
    problems: list[str] = []
    displayed_blocks = 0
    for number, (expected, explanation) in sorted(base.FORMULAS.items()):
        chapter_files = sorted((ROOT / "chapters").glob(f"{number:02d}_*/CHAPTER.md"))
        record: dict[str, object] = {
            "chapter": number,
            "expected": expected,
            "schema": number in base.FORMULA_SCHEMA_NUMBERS,
            "present": False,
            "explained": False,
            "balanced_blocks": True,
            "problems": [],
        }
        if not chapter_files:
            record["problems"].append("CHAPTER.md assente")
            records.append(record)
            continue
        text = chapter_files[0].read_text(encoding="utf-8")
        public = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
        prose = re.sub(r"```.*?```", "", public, flags=re.DOTALL)
        present = compact(expected) in compact(prose)
        record["present"] = present
        if not present:
            record["problems"].append("formula o schema non rintracciabile")
        if number in base.FORMULA_SCHEMA_NUMBERS and SCHEMA_MARKER not in public:
            record["problems"].append("schema non etichettato")
        blocks = list(FORMULA_BLOCK_RE.finditer(public))
        displayed_blocks += len(blocks)
        for block in blocks:
            if not balanced_delimiters(block.group(1)):
                record["balanced_blocks"] = False
                record["problems"].append("delimitatori non bilanciati")
            if not nearby_explanation(public, block.end()):
                record["problems"].append("blocco senza spiegazione vicina")
        record["explained"] = bool(blocks and all(nearby_explanation(public, block.end()) for block in blocks)) or (
            number in base.FORMULA_SCHEMA_NUMBERS and SCHEMA_MARKER in public
        )
        if record["problems"]:
            for problem in record["problems"]:
                problems.append(f"capitolo {number}: {problem}")
        records.append(record)
    return {
        "summary": {
            "formulas": len(records),
            "formula_contracts_clean": sum(not record["problems"] for record in records),
            "formula_contracts_with_problems": sum(bool(record["problems"]) for record in records),
            "displayed_blocks": displayed_blocks,
        },
        "problems": problems,
        "records": records,
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
        for problem in result["problems"]:
            print(f"- {problem}")
    return 1 if args.strict and result["problems"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
