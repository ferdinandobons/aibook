from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

C = {
    "text": "#0F172A",
    "muted": "#475569",
    "blue": "#2563EB",
    "blue_fill": "#EFF6FF",
    "purple": "#7C3AED",
    "purple_fill": "#F5F3FF",
    "green": "#16A34A",
    "green_fill": "#F0FDF4",
    "amber": "#D97706",
    "amber_fill": "#FFFBEB",
    "red": "#DC2626",
    "red_fill": "#FEF2F2",
    "neutral": "#CBD5E1",
    "neutral_fill": "#F8FAFC",
    "white": "#FFFFFF",
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def text_size(
    draw: ImageDraw.ImageDraw,
    text: str,
    selected_font: ImageFont.FreeTypeFont,
) -> tuple[int, int]:
    left, top, right, bottom = draw.textbbox((0, 0), text, font=selected_font)
    return right - left, bottom - top


def wrap(
    draw: ImageDraw.ImageDraw,
    text: str,
    selected_font: ImageFont.FreeTypeFont,
    max_width: int,
) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        current = ""
        for word in paragraph.split():
            candidate = word if not current else f"{current} {word}"
            if text_size(draw, candidate, selected_font)[0] <= max_width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def centered(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    selected_font: ImageFont.FreeTypeFont,
    fill: str | None = None,
    spacing: int = 6,
    max_lines: int | None = None,
) -> None:
    fill = fill or C["text"]
    x0, y0, x1, y1 = box
    lines = wrap(draw, text, selected_font, x1 - x0)
    if max_lines is not None and len(lines) > max_lines:
        raise ValueError((text, lines, box))
    heights = [
        text_size(draw, line, selected_font)[1]
        if line
        else selected_font.size
        for line in lines
    ]
    total = sum(heights) + spacing * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    for line, height in zip(lines, heights):
        width, _ = (
            text_size(draw, line, selected_font)
            if line
            else (0, height)
        )
        draw.text(
            (x0 + (x1 - x0 - width) / 2, y),
            line,
            font=selected_font,
            fill=fill,
        )
        y += height + spacing


def rounded(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: str,
    outline: str,
    width: int = 3,
    radius: int = 20,
) -> None:
    draw.rounded_rectangle(
        box,
        radius=radius,
        fill=fill,
        outline=outline,
        width=width,
    )


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str,
    width: int = 5,
    head: int = 14,
) -> None:
    x0, y0 = start
    x1, y1 = end
    draw.line((x0, y0, x1, y1), fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    point_1 = (
        x1 + head * math.cos(angle + math.pi * 0.82),
        y1 + head * math.sin(angle + math.pi * 0.82),
    )
    point_2 = (
        x1 + head * math.cos(angle - math.pi * 0.82),
        y1 + head * math.sin(angle - math.pi * 0.82),
    )
    draw.polygon([end, point_1, point_2], fill=color)


def title(
    draw: ImageDraw.ImageDraw,
    heading: str,
    subtitle: str,
    width: int,
) -> None:
    centered(
        draw,
        (70, 25, width - 70, 82),
        heading,
        font(32, True),
        max_lines=1,
    )
    centered(
        draw,
        (100, 88, width - 100, 140),
        subtitle,
        font(18),
        C["muted"],
        max_lines=2,
    )


def save(image: Image.Image, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, optimize=True)
    with Image.open(path) as check:
        check.verify()
    return path


def draw_points(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
) -> None:
    x0, y0, x1, y1 = box
    groups = [
        (
            C["blue"],
            [(0.18, 0.25), (0.25, 0.32), (0.20, 0.43), (0.32, 0.25), (0.29, 0.47)],
        ),
        (
            C["purple"],
            [(0.55, 0.26), (0.65, 0.20), (0.69, 0.35), (0.57, 0.41), (0.73, 0.46)],
        ),
        (
            C["green"],
            [(0.38, 0.69), (0.50, 0.73), (0.57, 0.64), (0.46, 0.57), (0.31, 0.62)],
        ),
    ]
    for color, points in groups:
        for point_x, point_y in points:
            x = x0 + point_x * (x1 - x0)
            y = y0 + point_y * (y1 - y0)
            draw.ellipse(
                (x - 9, y - 9, x + 9, y + 9),
                fill=color,
                outline=C["text"],
                width=1,
            )


def make_unsup01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title(
        draw,
        "UNSUP-01 · Tre modi di costruire un segnale senza label esterne",
        "L'obiettivo scelto decide quali regolarità diventano utili nella rappresentazione",
        width,
    )

    panels = [
        (55, 180, 580, 825, "CLUSTERING", C["blue"]),
        (638, 180, 1162, 825, "RICOSTRUZIONE MASCHERATA", C["purple"]),
        (1220, 180, 1745, 825, "CONTRASTO O PREDIZIONE", C["green"]),
    ]
    for x0, y0, x1, y1, heading, color in panels:
        rounded(draw, (x0, y0, x1, y1), C["white"], color)
        centered(
            draw,
            (x0 + 25, y0 + 20, x1 - 25, y0 + 75),
            heading,
            font(20, True),
            color,
            max_lines=2,
        )

    draw_points(draw, (100, 290, 535, 455))
    arrow(draw, (315, 475), (315, 535), C["blue"])
    rounded(draw, (120, 545, 515, 650), C["blue_fill"], C["blue"], 2, 16)
    centered(
        draw,
        (140, 557, 495, 638),
        "Minimizza la distanza\ntra esempi e centroidi",
        font(17, True),
        max_lines=2,
    )
    arrow(draw, (315, 665), (315, 715), C["blue"])
    rounded(draw, (120, 725, 515, 790), C["neutral_fill"], C["neutral"], 2, 14)
    centered(
        draw,
        (140, 733, 495, 782),
        "Output: gruppi e centroidi",
        font(16, True),
        max_lines=1,
    )

    rounded(draw, (690, 285, 860, 390), C["neutral_fill"], C["neutral"], 2, 14)
    centered(draw, (705, 297, 845, 378), "x = [a,b,c,d]", font(17, True), max_lines=1)
    arrow(draw, (875, 337), (945, 337), C["purple"])
    rounded(draw, (960, 270, 1110, 405), C["purple_fill"], C["purple"], 2, 14)
    centered(
        draw,
        (975, 282, 1095, 393),
        "maschera\n[b,d]\n→ [a,0,c,0]",
        font(16, True),
        max_lines=3,
    )
    arrow(draw, (900, 425), (900, 495), C["purple"])
    rounded(draw, (710, 510, 1090, 625), C["purple_fill"], C["purple"], 2, 16)
    centered(
        draw,
        (730, 522, 1070, 613),
        "Predice le coordinate nascoste\ncon target ricavato da x",
        font(17, True),
        max_lines=2,
    )
    arrow(draw, (900, 640), (900, 700), C["purple"])
    rounded(draw, (710, 715, 1090, 790), C["neutral_fill"], C["neutral"], 2, 14)
    centered(
        draw,
        (730, 724, 1070, 781),
        "Output: embedding + ricostruzione",
        font(16, True),
        max_lines=1,
    )

    rounded(draw, (1270, 280, 1435, 405), C["green_fill"], C["green"], 2, 14)
    centered(
        draw,
        (1285, 292, 1420, 393),
        "vista 1\nstesso dato",
        font(15, True),
        max_lines=2,
    )
    rounded(draw, (1530, 280, 1695, 405), C["green_fill"], C["green"], 2, 14)
    centered(
        draw,
        (1545, 292, 1680, 393),
        "vista 2\no parte futura",
        font(15, True),
        max_lines=3,
    )
    arrow(draw, (1448, 340), (1517, 340), C["green"])
    centered(draw, (1445, 300, 1520, 326), "coppia", font(13, True), C["muted"], max_lines=1)
    arrow(draw, (1482, 425), (1482, 495), C["green"])
    rounded(draw, (1290, 510, 1675, 635), C["green_fill"], C["green"], 2, 16)
    centered(
        draw,
        (1310, 522, 1655, 623),
        "Avvicina rappresentazioni correlate\no predice una parte dal contesto",
        font(17, True),
        max_lines=3,
    )
    arrow(draw, (1482, 650), (1482, 710), C["green"])
    rounded(draw, (1290, 725, 1675, 790), C["neutral_fill"], C["neutral"], 2, 14)
    centered(
        draw,
        (1310, 733, 1655, 782),
        "Output: rappresentazione trasferibile",
        font(16, True),
        max_lines=1,
    )

    rounded(draw, (155, 860, 1645, 950), C["amber_fill"], C["amber"], 2, 18)
    centered(
        draw,
        (185, 872, 1615, 938),
        "Senza label esterne non significa senza obiettivo. Distanza, maschera, augmentazione, contesto e campioni negativi determinano ciò che il modello è incentivato a conservare.",
        font(18, True),
        max_lines=3,
    )
    return save(
        image,
        ROOT / "assets/chapters/13_unsupervised_self/UNSUP-01/candidate-v1.png",
    )


def make_unsup02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title(
        draw,
        "UNSUP-02 · La label nasce dal dato stesso",
        "Nel masked modeling il target è la parte nascosta dell'input originale, non una categoria assegnata da una persona",
        width,
    )

    x_positions = [60, 355, 660, 965, 1270, 1535]
    boxes = []
    labels = [
        ("DATO ORIGINALE", "x = [a, b, c, d]", C["blue"], C["blue_fill"]),
        ("MASCHERA", "m = [0, 1, 0, 1]", C["amber"], C["amber_fill"]),
        ("INPUT CORROTTO", "x̃ = [a, 0, c, 0]\n+ maschera m", C["purple"], C["purple_fill"]),
        ("ENCODER", "z = fθ(x̃,m)\nshape [2]", C["purple"], C["purple_fill"]),
        ("DECODER", "x̂ = gφ(z)\nshape [4]", C["green"], C["green_fill"]),
        ("LOSS", "solo su b e d\nMSE(x̂m, xm)", C["red"], C["red_fill"]),
    ]
    widths = [250, 250, 250, 250, 220, 205]
    y0, y1 = 250, 500
    for x, width, (heading, body, color, fill) in zip(x_positions, widths, labels):
        box = (x, y0, x + width, y1)
        boxes.append(box)
        rounded(draw, box, C["white"], color)
        centered(
            draw,
            (x + 15, y0 + 22, x + width - 15, y0 + 72),
            heading,
            font(18, True),
            color,
            max_lines=2,
        )
        rounded(
            draw,
            (x + 25, y0 + 105, x + width - 25, y1 - 30),
            fill,
            color,
            2,
            15,
        )
        centered(
            draw,
            (x + 40, y0 + 118, x + width - 40, y1 - 43),
            body,
            font(17, True),
            max_lines=3,
        )
    for left_box, right_box in zip(boxes, boxes[1:]):
        arrow(
            draw,
            (left_box[2] + 5, (left_box[1] + left_box[3]) // 2),
            (right_box[0] - 8, (right_box[1] + right_box[3]) // 2),
            C["text"],
            4,
            12,
        )

    target_y = 650
    draw.line((185, 510, 185, target_y), fill=C["blue"], width=4)
    draw.line((185, target_y, 1635, target_y), fill=C["blue"], width=4)
    arrow(draw, (1635, target_y), (1635, 515), C["blue"], 4, 12)
    rounded(draw, (525, 605, 1135, 700), C["blue_fill"], C["blue"], 2, 16)
    centered(
        draw,
        (545, 618, 1115, 685),
        "TARGET AUTOGENERATO: valori originali nelle posizioni mascherate",
        font(17, True),
        C["blue"],
        max_lines=2,
    )

    rounded(draw, (210, 760, 770, 880), C["neutral_fill"], C["neutral"], 2, 18)
    centered(
        draw,
        (235, 775, 745, 865),
        "La maschera dice dove calcolare la loss. Non dice quale gruppo, categoria o significato umano possiede l'esempio.",
        font(17, True),
        max_lines=3,
    )
    rounded(draw, (1030, 760, 1590, 880), C["green_fill"], C["green"], 2, 18)
    centered(
        draw,
        (1055, 775, 1565, 865),
        "Dopo il pretraining, l'encoder può essere valutato con linear probe, fine-tuning o task downstream separati.",
        font(17, True),
        max_lines=3,
    )
    return save(
        image,
        ROOT / "assets/chapters/13_unsupervised_self/UNSUP-02/candidate-v1.png",
    )


def main() -> None:
    for path in [make_unsup01(), make_unsup02()]:
        with Image.open(path) as image:
            print(
                f"{path.relative_to(ROOT)}: "
                f"{image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes"
            )


if __name__ == "__main__":
    main()
