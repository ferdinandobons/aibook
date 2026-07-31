from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

from generate_book_visuals import C, draw_centered_multiline, font, rounded, save_png
from generate_numerics_visuals import make_num01, make_num02

ROOT = Path(__file__).resolve().parents[1]


def patch_num01() -> Path:
    path = make_num01()
    image = Image.open(path).convert("RGB")
    draw = ImageDraw.Draw(image)

    x_positions = [45, 480, 915, 1350]
    labels = ["segno", "esponente", "significando"]
    widths = [54, 100, 175]
    colors = [C["red"], C["blue"], C["purple"]]
    fills = [C["red_fill"], C["blue_fill"], C["purple_fill"]]

    for x in x_positions:
        draw.rectangle((x + 22, 328, x + 383, 440), fill=C["white"])
        cursor = x + 28
        for label, width, color, fill in zip(labels, widths, colors, fills):
            rounded(draw, (cursor, 335, cursor + width, 430), 10, fill, color, 2)
            draw_centered_multiline(
                draw,
                (cursor + 4, 344, cursor + width - 4, 421),
                label,
                font(11, True),
                color,
                max_lines=2,
            )
            cursor += width + 8

    return save_png(image, path)


def patch_num02() -> Path:
    path = make_num02()
    image = Image.open(path).convert("RGB")
    draw = ImageDraw.Draw(image)

    rounded(draw, (1185, 520, 1375, 565), 12, C["white"], C["red"], 2)
    draw_centered_multiline(
        draw,
        (1195, 526, 1365, 559),
        "gradienti",
        font(14, True),
        C["red"],
        max_lines=1,
    )

    rounded(draw, (270, 570, 500, 615), 12, C["white"], C["blue"], 2)
    draw_centered_multiline(
        draw,
        (280, 576, 490, 609),
        "pesi aggiornati",
        font(14, True),
        C["blue"],
        max_lines=1,
    )

    return save_png(image, path)


def main() -> None:
    for path in [patch_num01(), patch_num02()]:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
