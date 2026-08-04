"""Check that generated lesson code can be rebuilt without drift.

The generated examples are public teaching material as well as executable
artifacts. This audit catches a class of regressions that normal tests miss:
the code still runs, but a second compiler pass accumulates guards or changes
the snippet shown in the lesson.
"""

from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER_RE = re.compile(r"^title:\s*(.+)$", re.MULTILINE)
PYTHON_BLOCK_RE = re.compile(r"```python\s*\n(.+?)\n```", re.DOTALL)
GUARD = 'if case != "default":'


def compiler_module():
    path = ROOT / "scripts" / "rebuild_lessons_v2.py"
    spec = importlib.util.spec_from_file_location("rebuild_lessons_v2", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"impossibile caricare {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def chapter_title(chapter: Path) -> str:
    text = (chapter / "CHAPTER.md").read_text(encoding="utf-8")
    match = CHAPTER_RE.search(text)
    if not match:
        raise ValueError(f"titolo mancante: {chapter}")
    return match.group(1).strip()


def audit() -> dict[str, object]:
    compiler = compiler_module()
    non_idempotent: list[dict[str, object]] = []
    duplicate_guards: list[dict[str, object]] = []
    checked = 0

    for code_path in sorted(
        (ROOT / "chapters").glob("[0-9][0-9]_*/code/snip_*_contract.py")
    ):
        number = int(code_path.parent.parent.name[:2])
        if number == 28:
            continue
        checked += 1
        chapter = code_path.parent.parent
        current = code_path.read_text(encoding="utf-8")
        rebuilt = compiler.clean_code_source(number, chapter_title(chapter))
        if rebuilt != current:
            non_idempotent.append(
                {
                    "chapter": number,
                    "path": str(code_path.relative_to(ROOT)),
                    "current_chars": len(current),
                    "rebuilt_chars": len(rebuilt),
                }
            )
        guard_count = current.count(GUARD)
        if guard_count > 1:
            duplicate_guards.append(
                {
                    "chapter": number,
                    "path": str(code_path.relative_to(ROOT)),
                    "count": guard_count,
                }
            )

        chapter_text = (chapter / "CHAPTER.md").read_text(encoding="utf-8")
        for block_index, block in enumerate(
            PYTHON_BLOCK_RE.findall(chapter_text), start=1
        ):
            block_count = block.count(GUARD)
            if block_count > 1:
                duplicate_guards.append(
                    {
                        "chapter": number,
                        "path": str((chapter / "CHAPTER.md").relative_to(ROOT)),
                        "block": block_index,
                        "count": block_count,
                    }
                )

    return {
        "checked_contracts": checked,
        "non_idempotent": non_idempotent,
        "duplicate_guards": duplicate_guards,
        "problems": len(non_idempotent) + len(duplicate_guards),
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    result = audit()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if args.strict and result["problems"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
