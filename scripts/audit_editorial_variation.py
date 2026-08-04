"""Catch large-scale prose repetition without imposing one lesson template.

The course keeps a small canonical vocabulary for contracts and verification,
but a sentence copied across most generated chapters is a compiler defect.
This audit measures sentence ownership by chapter and reports only repetition
that crosses a deliberately high threshold.  It also keeps the historical
scaffold markers out of the active book.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
MAX_SHARED_CHAPTERS = 20
MIN_WORDS = 9

SCAFFOLD_MARKERS = (
    "La domanda guida di questa lezione",
    "Il frammento seguente è volutamente",
    "La regola generale viene poi letta dentro il componente",
    "Il caso guida è questo",
)


def public_text(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    return text


def sentences(text: str):
    for raw in re.split(r"(?<=[.!?])\s+", public_text(text)):
        value = re.sub(r"\s+", " ", raw).strip(" -")
        if len(value.split()) < MIN_WORDS:
            continue
        if value.startswith(("#", "!", "|", "1. ", "2. ", "3. ", "4. ", "5. ")):
            continue
        yield value


def normalize(value: str) -> str:
    value = value.casefold()
    value = re.sub(r"\[[^\]]*SRC-[^\]]*\]", "[SRC]", value)
    value = re.sub(r"`[^`]+`", "`code`", value)
    value = re.sub(r"\b\d+(?:[.,]\d+)?\b", "N", value)
    return re.sub(r"\s+", " ", value).strip()


def audit() -> dict[str, object]:
    owners: dict[str, set[int]] = defaultdict(set)
    originals: dict[str, str] = {}
    scaffold: list[dict[str, object]] = []
    chapter_files = sorted(CHAPTERS.glob("[0-9][0-9]_*/CHAPTER.md"))
    for chapter_file in chapter_files:
        number = int(chapter_file.parent.name.split("_", 1)[0])
        text = chapter_file.read_text(encoding="utf-8")
        for marker in SCAFFOLD_MARKERS:
            if marker in text:
                scaffold.append({"chapter": number, "marker": marker})
        for sentence in sentences(text):
            key = normalize(sentence)
            owners[key].add(number)
            originals.setdefault(key, sentence)
    repeated = [
        {
            "chapters": sorted(chapters),
            "count": len(chapters),
            "text": originals[key][:240],
        }
        for key, chapters in owners.items()
        if len(chapters) > MAX_SHARED_CHAPTERS
    ]
    repeated.sort(key=lambda item: (-item["count"], item["text"]))
    problems = [
        f"frase condivisa da {item['count']} capitoli: {item['text']}"
        for item in repeated
    ]
    problems.extend(
        f"scaffold storico nel capitolo {item['chapter']}: {item['marker']}" for item in scaffold
    )
    return {
        "summary": {
            "chapters": len(chapter_files),
            "sentences_indexed": len(owners),
            "max_shared_chapters": max((len(chapters) for chapters in owners.values()), default=0),
            "repeated_over_threshold": len(repeated),
            "scaffold_markers": len(scaffold),
        },
        "problems": problems,
        "repeated": repeated,
        "scaffold": scaffold,
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
