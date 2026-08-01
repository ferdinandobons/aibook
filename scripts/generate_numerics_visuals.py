from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

from generate_book_visuals import (
    C,
    arrow,
    draw_centered_multiline,
    font,
    rounded,
    save_png,
    title_block,
)

ROOT = Path(__file__).resolve().parents[1]


def dtype_card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    name: str,
    bits: str,
    byte_count: str,
    eps: str,
    maximum: str,
    color: str,
    fill: str,
) -> None:
    x0, y0, x1, y1 = box
    rounded(draw, box, 24, C["white"], color, 3)
    rounded(draw, (x0 + 18, y0 + 18, x1 - 18, y0 + 84), 16, fill, color, 2)
    draw_centered_multiline(
        draw,
        (x0 + 30, y0 + 25, x1 - 30, y0 + 78),
        name,
        font(24, True),
        color,
        max_lines=1,
    )

    draw_centered_multiline(
        draw,
        (x0 + 30, y0 + 105, x1 - 30, y0 + 145),
        f"{byte_count} per elemento",
        font(16, True),
        C["muted"],
        max_lines=1,
    )

    labels = ["segno", "esponente", "significando"]
    widths = [62, 120, 198]
    colors = [C["red"], C["blue"], C["purple"]]
    fills = [C["red_fill"], C["blue_fill"], C["purple_fill"]]
    cursor = x0 + 28
    for label, width, section_color, section_fill in zip(labels, widths, colors, fills):
        rounded(
            draw,
            (cursor, y0 + 170, cursor + width, y0 + 270),
            10,
            section_fill,
            section_color,
            2,
        )
        draw_centered_multiline(
            draw,
            (cursor + 5, y0 + 180, cursor + width - 5, y0 + 225),
            label,
            font(12, True),
            section_color,
            max_lines=2,
        )
        cursor += width + 8

    draw_centered_multiline(
        draw,
        (x0 + 35, y0 + 285, x1 - 35, y0 + 345),
        bits,
        font(19, True),
        C["text"],
        max_lines=1,
    )

    rounded(draw, (x0 + 28, y0 + 370, x1 - 28, y0 + 455), 14, C["neutral_fill"], C["neutral"], 2)
    draw_centered_multiline(
        draw,
        (x0 + 45, y0 + 380, x1 - 45, y0 + 445),
        f"eps vicino a 1\n{eps}",
        font(16, True),
        C["text"],
        spacing=5,
        max_lines=2,
    )

    rounded(draw, (x0 + 28, y0 + 475, x1 - 28, y0 + 560), 14, fill, color, 2)
    draw_centered_multiline(
        draw,
        (x0 + 45, y0 + 485, x1 - 45, y0 + 550),
        f"massimo finito\n{maximum}",
        font(16, True),
        C["text"],
        spacing=5,
        max_lines=2,
    )


def make_num01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "NUM-01 · Range e precisione dei dtype",
        "Lo stesso numero di bit non implica lo stesso compromesso tra valori estremi e dettagli vicini",
        width,
    )

    specs = [
        ("float16", "1 | 5 | 10 bit", "2 byte", "9,765625e-4", "65504", C["amber"], C["amber_fill"]),
        ("bfloat16", "1 | 8 | 7 bit", "2 byte", "7,8125e-3", "3,3895e38", C["purple"], C["purple_fill"]),
        ("float32", "1 | 8 | 23 bit", "4 byte", "1,1921e-7", "3,4028e38", C["blue"], C["blue_fill"]),
        ("float64", "1 | 11 | 52 bit", "8 byte", "2,2204e-16", "1,7977e308", C["green"], C["green_fill"]),
    ]
    x_positions = [45, 480, 915, 1350]
    for x, spec in zip(x_positions, specs):
        dtype_card(draw, (x, 165, x + 405, 755), *spec)

    rounded(draw, (115, 800, 1685, 955), 24, C["amber_fill"], C["amber"], 3)
    draw_centered_multiline(
        draw,
        (150, 820, 1650, 935),
        "Float16 conserva più dettaglio di bfloat16 vicino a 1, ma bfloat16 conserva un range simile a float32. Il formato migliore dipende dall'operazione e dal contratto numerico.",
        font(20, True),
        C["text"],
        spacing=6,
        max_lines=3,
    )

    return save_png(image, ROOT / "assets/chapters/09_numerics_hardware/NUM-01/candidate-v1.png")


def stage_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    subtitle: str,
    color: str,
    fill: str,
) -> None:
    rounded(draw, box, 20, fill, color, 3)
    x0, y0, x1, y1 = box
    draw_centered_multiline(
        draw,
        (x0 + 16, y0 + 14, x1 - 16, y0 + 65),
        title,
        font(18, True),
        color,
        max_lines=2,
    )
    draw_centered_multiline(
        draw,
        (x0 + 18, y0 + 78, x1 - 18, y1 - 18),
        subtitle,
        font(15),
        C["text"],
        spacing=4,
        max_lines=4,
    )


def make_num02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "NUM-02 · Contratto della mixed precision",
        "Storage, calcolo, accumulo e aggiornamento possono usare dtype differenti",
        width,
    )

    boxes = [
        ((45, 245, 300, 490), "Input e pesi", "storage fp32 oppure precisione ridotta, secondo il modello", C["blue"], C["blue_fill"]),
        ((355, 245, 610, 490), "Autocast", "sceglie il dtype per ogni operatore in base a device e policy", C["purple"], C["purple_fill"]),
        ((665, 245, 920, 490), "Matmul e conv", "operatori idonei possono usare fp16 o bfloat16", C["green"], C["green_fill"]),
        ((975, 245, 1230, 490), "Riduzioni e loss", "operazioni sensibili possono restare o accumulare in fp32", C["amber"], C["amber_fill"]),
        ((1285, 245, 1540, 490), "Backward", "gradienti; loss scaling opzionale nel training fp16", C["red"], C["red_fill"]),
    ]
    for box, title, subtitle, color, fill in boxes:
        stage_box(draw, box, title, subtitle, color, fill)
    for first, second in zip(boxes, boxes[1:]):
        arrow(
            draw,
            (first[0][2] + 7, (first[0][1] + first[0][3]) / 2),
            (second[0][0] - 10, (second[0][1] + second[0][3]) / 2),
            width=5,
            head=13,
        )

    optimizer = (550, 610, 1250, 790)
    rounded(draw, optimizer, 24, C["neutral_fill"], C["neutral"], 3)
    draw_centered_multiline(
        draw,
        (590, 630, 1210, 680),
        "OPTIMIZER E MASTER WEIGHTS",
        font(20, True),
        C["text"],
        max_lines=1,
    )
    draw_centered_multiline(
        draw,
        (600, 700, 1200, 765),
        "aggiornamenti e stati sensibili possono restare in float32",
        font(18, True),
        C["muted"],
        max_lines=2,
    )
    arrow(draw, (1412, 505), (1170, 600), fill=C["red"], width=5, head=13)
    arrow(draw, (550, 700), (180, 505), fill=C["blue"], width=5, head=13)

    rounded(draw, (100, 840, 1700, 960), 22, C["amber_fill"], C["amber"], 3)
    draw_centered_multiline(
        draw,
        (135, 855, 1665, 945),
        "Contratto tipico, non universale: l'operatore effettivo, il dtype interno e l'accumulatore dipendono da hardware, backend, shape e versione.",
        font(19, True),
        C["text"],
        spacing=5,
        max_lines=3,
    )

    return save_png(image, ROOT / "assets/chapters/09_numerics_hardware/NUM-02/candidate-v1.png")


def main() -> None:
    for path in [make_num01(), make_num02()]:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
