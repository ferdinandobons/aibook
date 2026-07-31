from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]

C = {
    "white": "#FFFFFF",
    "text": "#0F172A",
    "muted": "#475569",
    "neutral": "#CBD5E1",
    "neutral_fill": "#F8FAFC",
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
}

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size=size)


def rounded(draw, box, radius, fill, outline, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text_bbox(draw, text, f):
    box = draw.textbbox((0, 0), text, font=f)
    return box[2] - box[0], box[3] - box[1]


def centered(draw, box, text, f, fill, spacing=4, max_lines=4):
    x0, y0, x1, y1 = box
    lines = text.split("\n")
    if len(lines) > max_lines:
        raise ValueError(text)
    total = sum(text_bbox(draw, line, f)[1] for line in lines) + spacing * (len(lines) - 1)
    y = y0 + ((y1 - y0) - total) / 2
    for line in lines:
        w, h = text_bbox(draw, line, f)
        if w > (x1 - x0):
            raise ValueError(f"overflow: {line}")
        draw.text((x0 + (x1 - x0 - w) / 2, y), line, font=f, fill=fill)
        y += h + spacing


def arrow(draw, start, end, fill="#0F172A", width=5, head=14):
    import math

    x0, y0 = start
    x1, y1 = end
    draw.line((x0, y0, x1, y1), fill=fill, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    left = (x1 - head * math.cos(angle - 0.55), y1 - head * math.sin(angle - 0.55))
    right = (x1 - head * math.cos(angle + 0.55), y1 - head * math.sin(angle + 0.55))
    draw.polygon((end, left, right), fill=fill)


def title(draw, main, sub, width):
    centered(draw, (60, 20, width - 60, 85), main, font(34, True), C["text"], max_lines=1)
    centered(draw, (100, 82, width - 100, 130), sub, font(20), C["muted"], max_lines=2)


def save(image, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format="PNG", optimize=True)
    return path


def make_eval01():
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title(
        draw,
        "EVAL-01 · Dal risultato al claim sostenibile",
        "Un punteggio diventa evidenza soltanto dentro un protocollo ricostruibile",
        width,
    )
    steps = [
        ("1", "Domanda", "Quale decisione\ndeve sostenere?", C["blue"], C["blue_fill"]),
        ("2", "Protocollo", "Quali dati, split\ne condizioni?", C["purple"], C["purple_fill"]),
        ("3", "Baseline", "Rispetto a quale\nriferimento?", C["green"], C["green_fill"]),
        ("4", "Metrica", "Che cosa misura\ne che cosa omette?", C["amber"], C["amber_fill"]),
        ("5", "Slice e costi", "Dove cambiano gli\nerrori importanti?", C["red"], C["red_fill"]),
        ("6", "Variabilità", "Quanto dipende da\ncampione e run?", C["purple"], C["purple_fill"]),
        ("7", "Controlli", "Leakage, ablation,\ncontaminazione?", C["blue"], C["blue_fill"]),
        ("8", "Claim", "Che cosa possiamo\naffermare davvero?", C["green"], C["green_fill"]),
    ]
    xs = [55, 485, 915, 1345]
    top_y, bottom_y, card_width, card_height = 180, 525, 370, 245
    top_boxes = []
    for index, (number, heading, body, color, fill) in enumerate(steps[:4]):
        box = (xs[index], top_y, xs[index] + card_width, top_y + card_height)
        top_boxes.append(box)
        rounded(draw, box, 22, C["white"], color, 3)
        rounded(draw, (box[0] + 15, box[1] + 15, box[2] - 15, box[1] + 78), 16, fill, color, 2)
        draw.ellipse((box[0] + 28, box[1] + 27, box[0] + 76, box[1] + 75), fill=color)
        centered(draw, (box[0] + 28, box[1] + 26, box[0] + 76, box[1] + 76), number, font(19, True), C["white"], max_lines=1)
        centered(draw, (box[0] + 88, box[1] + 22, box[2] - 22, box[1] + 76), heading, font(20, True), color, max_lines=1)
        centered(draw, (box[0] + 35, box[1] + 105, box[2] - 35, box[3] - 28), body, font(22, True), C["text"], spacing=7, max_lines=3)

    bottom_boxes = []
    for index, (number, heading, body, color, fill) in enumerate(reversed(steps[4:])):
        box = (xs[index], bottom_y, xs[index] + card_width, bottom_y + card_height)
        bottom_boxes.append(box)
        rounded(draw, box, 22, C["white"], color, 3)
        rounded(draw, (box[0] + 15, box[1] + 15, box[2] - 15, box[1] + 78), 16, fill, color, 2)
        draw.ellipse((box[0] + 28, box[1] + 27, box[0] + 76, box[1] + 75), fill=color)
        centered(draw, (box[0] + 28, box[1] + 26, box[0] + 76, box[1] + 76), number, font(19, True), C["white"], max_lines=1)
        centered(draw, (box[0] + 88, box[1] + 22, box[2] - 22, box[1] + 76), heading, font(20, True), color, max_lines=1)
        centered(draw, (box[0] + 35, box[1] + 105, box[2] - 35, box[3] - 28), body, font(22, True), C["text"], spacing=7, max_lines=3)

    for first, second in zip(top_boxes, top_boxes[1:]):
        arrow(draw, (first[2] + 5, (first[1] + first[3]) / 2), (second[0] - 8, (second[1] + second[3]) / 2), width=5)
    arrow(
        draw,
        ((top_boxes[-1][0] + top_boxes[-1][2]) / 2, top_boxes[-1][3] + 8),
        ((bottom_boxes[-1][0] + bottom_boxes[-1][2]) / 2, bottom_boxes[-1][1] - 8),
        width=5,
    )
    for first, second in zip(reversed(bottom_boxes[1:]), reversed(bottom_boxes[:-1])):
        arrow(draw, (first[0] - 5, (first[1] + first[3]) / 2), (second[2] + 8, (second[1] + second[3]) / 2), width=5)

    footer = (210, 820, 1590, 940)
    rounded(draw, footer, 24, C["amber_fill"], C["amber"], 3)
    centered(
        draw,
        (260, 835, 1540, 925),
        "Se manca un collegamento, il punteggio può essere corretto\nma il claim può risultare troppo ampio.",
        font(23, True),
        C["text"],
        spacing=5,
        max_lines=2,
    )
    return save(image, ROOT / "assets/chapters/04_critical_evaluation/EVAL-01/candidate-v1.png")


def metric_bar(draw, x, y, label, value_a, value_b, max_value=1.0):
    draw.text((x, y), label, font=font(18, True), fill=C["text"])
    base_y = y + 38
    draw.text((x, base_y + 2), "A", font=font(16, True), fill=C["blue"])
    rounded(draw, (x + 35, base_y, x + 455, base_y + 25), 10, C["neutral_fill"], C["neutral"], 1)
    rounded(draw, (x + 35, base_y, x + 35 + 420 * (value_a / max_value), base_y + 25), 10, C["blue_fill"], C["blue"], 2)
    draw.text((x + 470, base_y + 1), f"{value_a:.3f}", font=font(16, True), fill=C["blue"])
    base_y += 42
    draw.text((x, base_y + 2), "B", font=font(16, True), fill=C["purple"])
    rounded(draw, (x + 35, base_y, x + 455, base_y + 25), 10, C["neutral_fill"], C["neutral"], 1)
    rounded(draw, (x + 35, base_y, x + 35 + 420 * (value_b / max_value), base_y + 25), 10, C["purple_fill"], C["purple"], 2)
    draw.text((x + 470, base_y + 1), f"{value_b:.3f}", font=font(16, True), fill=C["purple"])


def make_eval02():
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title(
        draw,
        "EVAL-02 · La media non basta",
        "Gli stessi due modelli cambiano ordine quando cambiano slice, costo e incertezza",
        width,
    )
    left = (70, 155, 900, 790)
    right = (950, 155, 1730, 790)
    rounded(draw, left, 26, C["white"], C["neutral"], 3)
    rounded(draw, right, 26, C["white"], C["neutral"], 3)
    centered(draw, (100, 175, 870, 225), "Prestazioni sugli stessi 24 esempi", font(24, True), C["text"], max_lines=1)
    metric_bar(draw, 125, 255, "Accuratezza complessiva", 0.792, 0.833)
    metric_bar(draw, 125, 385, "Slice standard", 0.750, 0.938)
    metric_bar(draw, 125, 515, "Slice urgente", 0.875, 0.625)
    draw.line((120, 650, 850, 650), fill=C["neutral"], width=2)
    draw.text((125, 675), "Somma pesata degli errori", font=font(19, True), fill=C["text"])
    rounded(draw, (125, 720, 390, 765), 14, C["blue_fill"], C["blue"], 2)
    centered(draw, (135, 724, 380, 761), "A = 8,0", font(20, True), C["blue"], max_lines=1)
    rounded(draw, (430, 720, 695, 765), 14, C["red_fill"], C["red"], 2)
    centered(draw, (440, 724, 685, 761), "B = 13,0", font(20, True), C["red"], max_lines=1)

    centered(draw, (990, 175, 1690, 225), "Differenza B - A e incertezza", font(24, True), C["text"], max_lines=1)
    x0, x1, axis_y = 1040, 1630, 400

    def px(value):
        return x0 + (value + 0.35) / 0.70 * (x1 - x0)

    draw.line((x0, axis_y, x1, axis_y), fill=C["text"], width=4)
    for value in (-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3):
        x = px(value)
        draw.line((x, axis_y - 10, x, axis_y + 10), fill=C["text"], width=2)
        width_text, _ = text_bbox(draw, f"{value:+.1f}", font(14))
        draw.text((x - width_text / 2, axis_y + 18), f"{value:+.1f}", font=font(14), fill=C["muted"])

    zero = px(0)
    draw.line((zero, 280, zero, 560), fill=C["red"], width=3)
    centered(draw, (zero - 100, 245, zero + 100, 278), "nessuna differenza", font(15, True), C["red"], max_lines=1)
    lower, observed, upper = -0.208, 0.042, 0.292
    draw.line((px(lower), axis_y, px(upper), axis_y), fill=C["purple"], width=15)
    draw.ellipse((px(observed) - 13, axis_y - 13, px(observed) + 13, axis_y + 13), fill=C["purple"], outline=C["text"], width=2)
    centered(
        draw,
        (1010, 500, 1660, 580),
        "Differenza osservata: +0,042\nIntervallo bootstrap 95%: [-0,208, +0,292]",
        font(20, True),
        C["text"],
        spacing=7,
        max_lines=2,
    )
    rounded(draw, (1010, 620, 1670, 750), 20, C["amber_fill"], C["amber"], 3)
    centered(
        draw,
        (1040, 638, 1640, 734),
        "L'intervallo include zero.\nNon dimostra equivalenza.\nLa slice urgente resta peggiore per B.",
        font(20, True),
        C["text"],
        spacing=6,
        max_lines=3,
    )
    footer = (250, 835, 1550, 945)
    rounded(draw, footer, 24, C["green_fill"], C["green"], 3)
    centered(
        draw,
        (290, 850, 1510, 930),
        "La scelta dipende dalla domanda: media, casi critici, costo degli errori\ne incertezza rispondono a domande diverse.",
        font(22, True),
        C["text"],
        spacing=5,
        max_lines=2,
    )
    return save(image, ROOT / "assets/chapters/04_critical_evaluation/EVAL-02/candidate-v1.png")


def main():
    for path in (make_eval01(), make_eval02()):
        with Image.open(path) as image:
            print(path.relative_to(ROOT), image.size, path.stat().st_size)


if __name__ == "__main__":
    main()
