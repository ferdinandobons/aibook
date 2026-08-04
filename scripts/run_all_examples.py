"""Execute every chapter test file in an isolated Python process.

The runner intentionally avoids unittest discovery across the whole tree:
many chapter folders contain modules with the same basename.  A fresh process
per file also catches hidden dependencies on imports or mutable global state.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAN_RE = re.compile(r"Ran (\d+) tests?")


def test_files(include_appendix_a: bool) -> list[Path]:
    files = sorted(ROOT.glob("chapters/[0-9][0-9]_*/code/test_*.py"))
    if include_appendix_a:
        files.append(ROOT / "appendices" / "A_python_numpy_pytorch" / "test_example.py")
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--include-appendix-a", action="store_true")
    args = parser.parse_args()
    files = test_files(args.include_appendix_a)
    total = 0
    failures = []
    for path in files:
        process = subprocess.run(
            [sys.executable, path.name],
            cwd=path.parent,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=180,
            check=False,
        )
        match = RAN_RE.search(process.stdout)
        if process.returncode or not match:
            failures.append((path.relative_to(ROOT), process.returncode, process.stdout[-3000:]))
            continue
        total += int(match.group(1))
    print(f"files={len(files)} tests={total} failures={len(failures)} python={sys.version.split()[0]}")
    for path, returncode, output in failures:
        print(f"\nFAIL {path} (exit {returncode})\n{output}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
