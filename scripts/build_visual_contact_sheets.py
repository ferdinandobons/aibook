"""Build disposable contact sheets for visual QA of the linked book figures."""

from __future__ import annotations

import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path("/tmp/aibook-visual-qa")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+\.png)\)")
FONT_PATH = next(
    path
    for path in (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    )
    if Path(path).exists()
)


def chapter_images(start: int, end: int):
    result = []
    for number in range(start, end + 1):
        chapter = next((ROOT / "chapters").glob(f"{number:02d}_*/CHAPTER.md"), None)
        if not chapter:
            continue
        for index, (_, relative) in enumerate(IMAGE_RE.findall(chapter.read_text(encoding="utf-8")), 1):
            result.append((f"{number:02d}.{index}", (chapter.parent / relative).resolve()))
    return result


def appendix_images():
    result = []
    for appendix in sorted((ROOT / "appendices").glob("*/APPENDIX.md")):
        for _, relative in IMAGE_RE.findall(appendix.read_text(encoding="utf-8")):
            result.append((appendix.parent.name.split("_", 1)[0], (appendix.parent / relative).resolve()))
    return result


def build(name: str, entries) -> Path:
    columns = 6
    thumb_w, thumb_h, label_h = 300, 167, 30
    rows = (len(entries) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * thumb_w, rows * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    selected_font = ImageFont.truetype(FONT_PATH, 18)
    for index, (label, path) in enumerate(entries):
        row, col = divmod(index, columns)
        x, y = col * thumb_w, row * (thumb_h + label_h)
        with Image.open(path) as source:
            thumb = source.convert("RGB").resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (x, y))
        draw.rectangle((x, y + thumb_h, x + thumb_w, y + thumb_h + label_h), fill="#F8FAFC")
        draw.text((x + 8, y + thumb_h + 5), label, font=selected_font, fill="#0F172A")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    target = OUTPUT / f"{name}.png"
    sheet.save(target, optimize=True)
    return target


def main() -> None:
    groups = ((14, 31), (32, 49), (50, 67), (68, 84), (85, 98))
    for start, end in groups:
        print(build(f"chapters-{start:02d}-{end:02d}", chapter_images(start, end)))
    print(build("appendices", appendix_images()))


if __name__ == "__main__":
    main()
