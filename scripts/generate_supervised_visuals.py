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


def text_size(draw: ImageDraw.ImageDraw, text: str, selected_font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=selected_font)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, selected_font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = ""
        if not words:
            lines.append("")
            continue
        for word in words:
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
    heights = [text_size(draw, line, selected_font)[1] if line else selected_font.size for line in lines]
    total = sum(heights) + spacing * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    for line, height in zip(lines, heights):
        width, _ = text_size(draw, line, selected_font) if line else (0, height)
        draw.text((x0 + (x1 - x0 - width) / 2, y), line, font=selected_font, fill=fill)
        y += height + spacing


def rounded(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: str,
    outline: str,
    width: int = 3,
    radius: int = 20,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    color: str | None = None,
    width: int = 5,
    head: int = 14,
) -> None:
    color = color or C["text"]
    x0, y0 = start
    x1, y1 = end
    draw.line((x0, y0, x1, y1), fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    p1 = (x1 + head * math.cos(angle + math.pi * 0.82), y1 + head * math.sin(angle + math.pi * 0.82))
    p2 = (x1 + head * math.cos(angle - math.pi * 0.82), y1 + head * math.sin(angle - math.pi * 0.82))
    draw.polygon([end, p1, p2], fill=color)


def title(draw: ImageDraw.ImageDraw, heading: str, subtitle: str, width: int) -> None:
    centered(draw, (80, 28, width - 80, 88), heading, font(34, True), C["text"], max_lines=1)
    centered(draw, (120, 92, width - 120, 140), subtitle, font(19), C["muted"], max_lines=2)


def save(image: Image.Image, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, optimize=True)
    with Image.open(path) as check:
        check.verify()
    return path


def make_sup01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title(
        draw,
        "SUP-01 · Dal dataset al risultato di test",
        "Training, validation e test hanno ruoli diversi e non intercambiabili",
        width,
    )

    rounded(draw, (70, 190, 350, 785), C["white"], C["blue"])
    centered(draw, (95, 210, 325, 270), "DATASET ETICHETTATO", font(20, True), C["blue"], max_lines=2)
    rounded(draw, (110, 315, 310, 430), C["blue_fill"], C["blue"], 2, 16)
    centered(draw, (122, 325, 298, 420), "coppie (x, y)\nrichieste + target", font(16, True), max_lines=3)
    centered(
        draw,
        (105, 480, 315, 640),
        "Il target è una label osservata secondo una procedura. Non coincide automaticamente con la realtà completa.",
        font(16),
        C["text"],
        max_lines=5,
    )
    rounded(draw, (105, 675, 315, 745), C["neutral_fill"], C["neutral"], 2, 14)
    centered(draw, (120, 684, 300, 736), "split dichiarato\nprima del tuning", font(15, True), C["muted"], max_lines=2)

    arrow(draw, (365, 485), (450, 485), C["blue"])
    rounded(draw, (465, 205, 760, 780), C["white"], C["neutral"])
    centered(draw, (490, 220, 735, 270), "TRE SOTTOINSIEMI", font(20, True), C["text"], max_lines=1)
    lanes = [
        (315, "TRAIN\n120 esempi", C["blue"], C["blue_fill"], "aggiorna i parametri"),
        (485, "VALIDATION\n50 esempi", C["purple"], C["purple_fill"], "sceglie soglia e configurazione"),
        (655, "TEST\n50 esempi", C["green"], C["green_fill"], "stima finale del protocollo"),
    ]
    for y, label, color, fill, explanation in lanes:
        rounded(draw, (510, y - 55, 715, y + 55), fill, color, 2, 16)
        centered(draw, (525, y - 46, 700, y + 8), label, font(18, True), color, max_lines=2)
        centered(draw, (490, y + 68, 735, y + 112), explanation, font(14, True), C["muted"], max_lines=2)

    arrow(draw, (775, 315), (875, 315), C["blue"])
    rounded(draw, (890, 220, 1175, 410), C["blue_fill"], C["blue"])
    centered(draw, (915, 235, 1150, 285), "TRAINING", font(20, True), C["blue"], max_lines=1)
    centered(draw, (915, 305, 1150, 375), "BCE + L2\ngradienti → optimizer", font(18, True), max_lines=2)
    arrow(draw, (1190, 315), (1285, 315), C["blue"])
    rounded(draw, (1300, 220, 1715, 410), C["white"], C["blue"])
    centered(draw, (1325, 235, 1690, 285), "MODELLO APPRESO", font(20, True), C["blue"], max_lines=1)
    centered(draw, (1335, 305, 1680, 375), "p(y=1|x)=σ(wᵀx+b)\nparametri fissati dopo il training", font(18, True), max_lines=2)

    arrow(draw, (775, 485), (875, 485), C["purple"])
    rounded(draw, (890, 435, 1175, 625), C["purple_fill"], C["purple"])
    centered(draw, (915, 450, 1150, 500), "SELEZIONE", font(20, True), C["purple"], max_lines=1)
    centered(draw, (915, 520, 1150, 590), "costo FN = 5\ncosto FP = 1", font(18, True), max_lines=2)
    arrow(draw, (1190, 530), (1285, 530), C["purple"])
    rounded(draw, (1300, 435, 1715, 625), C["white"], C["purple"])
    centered(draw, (1325, 450, 1690, 500), "SOGLIA SCELTA", font(20, True), C["purple"], max_lines=1)
    centered(draw, (1335, 520, 1680, 590), "threshold = 0,30\nscelta solo sulla validation", font(19, True), max_lines=2)
    arrow(draw, (1507, 415), (1507, 430), C["purple"], width=4, head=10)

    arrow(draw, (775, 655), (875, 655), C["green"])
    rounded(draw, (890, 650, 1175, 840), C["green_fill"], C["green"])
    centered(draw, (915, 665, 1150, 715), "VALUTAZIONE", font(20, True), C["green"], max_lines=1)
    centered(draw, (915, 735, 1150, 805), "modello + soglia fissati\nnessun nuovo tuning", font(17, True), max_lines=2)
    arrow(draw, (1190, 745), (1285, 745), C["green"])
    rounded(draw, (1300, 650, 1715, 840), C["white"], C["green"])
    centered(draw, (1325, 665, 1690, 715), "TEST FINALE", font(20, True), C["green"], max_lines=1)
    centered(draw, (1335, 730, 1680, 810), "accuracy = 0,900\nrecall = 0,913\ncosto = 13", font(18, True), max_lines=3)
    arrow(draw, (1507, 630), (1507, 645), C["green"], width=4, head=10)

    rounded(draw, (180, 880, 1620, 955), C["amber_fill"], C["amber"], 2, 18)
    centered(
        draw,
        (210, 890, 1590, 945),
        "Il test non sceglie il modello, la soglia o la regolarizzazione. Se viene consultato durante il tuning, il suo ruolo cambia e il claim deve essere ristretto.",
        font(18, True),
        max_lines=3,
    )
    return save(image, ROOT / "assets/chapters/12_supervised/SUP-01/candidate-v1.png")


def confusion_grid(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    heading: str,
    color: str,
    tp: int,
    tn: int,
    fp: int,
    fn: int,
    cost: int,
) -> None:
    rounded(draw, (x, y, x + 720, y + 560), C["white"], color)
    centered(draw, (x + 25, y + 20, x + 695, y + 75), heading, font(22, True), color, max_lines=1)
    centered(draw, (x + 95, y + 105, x + 675, y + 145), "PREDIZIONE", font(16, True), C["muted"], max_lines=1)
    centered(draw, (x + 15, y + 210, x + 80, y + 420), "TARGET", font(16, True), C["muted"], max_lines=1)
    centered(draw, (x + 165, y + 150, x + 375, y + 195), "positivo", font(16, True), C["muted"], max_lines=1)
    centered(draw, (x + 420, y + 150, x + 630, y + 195), "negativo", font(16, True), C["muted"], max_lines=1)
    centered(draw, (x + 85, y + 220, x + 155, y + 295), "positivo", font(15, True), C["muted"], max_lines=1)
    centered(draw, (x + 85, y + 345, x + 155, y + 420), "negativo", font(15, True), C["muted"], max_lines=1)
    cells = [
        (x + 165, y + 205, x + 375, y + 315, "TP", tp, C["green"], C["green_fill"]),
        (x + 420, y + 205, x + 630, y + 315, "FN", fn, C["red"], C["red_fill"]),
        (x + 165, y + 335, x + 375, y + 445, "FP", fp, C["amber"], C["amber_fill"]),
        (x + 420, y + 335, x + 630, y + 445, "TN", tn, C["blue"], C["blue_fill"]),
    ]
    for x0, y0, x1, y1, label, value, cell_color, cell_fill in cells:
        rounded(draw, (x0, y0, x1, y1), cell_fill, cell_color, 2, 14)
        centered(draw, (x0 + 10, y0 + 10, x1 - 10, y1 - 10), f"{label}\n{value}", font(23, True), cell_color, max_lines=2)
    centered(draw, (x + 100, y + 475, x + 620, y + 535), f"accuracy = 0,900   ·   costo pesato = {cost}", font(19, True), color, max_lines=1)


def make_sup02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title(
        draw,
        "SUP-02 · Stessa accuracy, decisioni diverse",
        "La soglia cambia falsi positivi, falsi negativi e costo anche quando la media resta uguale",
        width,
    )
    confusion_grid(draw, 65, 185, "SOGLIA 0,30 · scelta sulla validation", C["purple"], 21, 24, 3, 2, 13)
    confusion_grid(draw, 1015, 185, "SOGLIA 0,50 · valore predefinito", C["blue"], 19, 26, 1, 4, 21)

    rounded(draw, (780, 295, 1015, 620), C["amber_fill"], C["amber"], 3, 24)
    centered(draw, (800, 315, 995, 375), "STESSA MEDIA", font(19, True), C["amber"], max_lines=1)
    centered(draw, (795, 390, 1000, 515), "45 predizioni\ncorrette su 50", font(20, True), C["text"], max_lines=3)
    centered(draw, (805, 535, 990, 595), "ma errori diversi", font(17, True), C["red"], max_lines=1)

    rounded(draw, (150, 790, 1650, 940), C["neutral_fill"], C["neutral"], 2, 20)
    centered(draw, (180, 800, 1620, 837), "LETTURA PER SLICE CON SOGLIA 0,30", font(18, True), C["text"], max_lines=1)
    centered(draw, (180, 838, 1620, 862), "costo: falso negativo = 5, falso positivo = 1", font(13, True), C["muted"], max_lines=1)
    rounded(draw, (210, 870, 820, 925), C["green_fill"], C["green"], 2, 14)
    centered(draw, (225, 876, 805, 919), "tracking disponibile · 34 casi · recall 1,000 · costo 3", font(16, True), C["green"], max_lines=1)
    rounded(draw, (980, 870, 1590, 925), C["amber_fill"], C["amber"], 2, 14)
    centered(draw, (995, 876, 1575, 919), "tracking mancante · 16 casi · recall 0,778 · costo 10", font(16, True), C["amber"], max_lines=1)
    return save(image, ROOT / "assets/chapters/12_supervised/SUP-02/candidate-v1.png")


def main() -> None:
    for path in [make_sup01(), make_sup02()]:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
