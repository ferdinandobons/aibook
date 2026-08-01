from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

from generate_book_visuals import C, ROOT, arrow, font, rounded, text_size


def centered_lines(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    size: int,
    *,
    bold: bool = False,
    fill: str = C["text"],
    spacing: int = 5,
) -> None:
    selected_font = font(size, bold)
    x0, y0, x1, y1 = box
    lines = text.split("\n")
    heights = [text_size(draw, line, selected_font)[1] for line in lines]
    total = sum(heights) + spacing * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total) / 2
    for line, height in zip(lines, heights):
        width, _ = text_size(draw, line, selected_font)
        if width > x1 - x0:
            raise ValueError(f"Text overflow: {line!r}")
        draw.text((x0 + (x1 - x0 - width) / 2, y), line, font=selected_font, fill=fill)
        y += height + spacing


def matrix(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    values: list[list[str | int]],
    *,
    size: int = 18,
) -> None:
    x0, y0, x1, y1 = box
    rows = len(values)
    cols = len(values[0])
    cell_width = (x1 - x0) / cols
    cell_height = (y1 - y0) / rows
    for row_index, row in enumerate(values):
        if len(row) != cols:
            raise ValueError("Matrix rows must have equal length")
        for col_index, value in enumerate(row):
            cell = (
                x0 + col_index * cell_width,
                y0 + row_index * cell_height,
                x0 + (col_index + 1) * cell_width,
                y0 + (row_index + 1) * cell_height,
            )
            draw.rectangle(cell, outline=C["neutral"], width=1)
            centered_lines(
                draw,
                (int(cell[0] + 3), int(cell[1] + 2), int(cell[2] - 3), int(cell[3] - 2)),
                str(value),
                size,
            )
    draw.line((x0 - 10, y0, x0 - 10, y1), fill=C["text"], width=3)
    draw.line((x0 - 10, y0, x0, y0), fill=C["text"], width=3)
    draw.line((x0 - 10, y1, x0, y1), fill=C["text"], width=3)
    draw.line((x1 + 10, y0, x1 + 10, y1), fill=C["text"], width=3)
    draw.line((x1, y0, x1 + 10, y0), fill=C["text"], width=3)
    draw.line((x1, y1, x1 + 10, y1), fill=C["text"], width=3)


def save(image: Image.Image, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format="PNG", optimize=True)
    with Image.open(path) as decoded:
        decoded.load()
        if decoded.mode != "RGB":
            raise ValueError(f"Unexpected mode: {decoded.mode}")
    return path


def make_la_01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    centered_lines(draw, (60, 18, width - 60, 72), "LA-01 · Contratto delle shape in un layer lineare", 34, bold=True)
    centered_lines(
        draw,
        (120, 75, width - 120, 125),
        "L'asse feature viene combinato; batch e classe restano nell'output",
        20,
        fill=C["muted"],
    )

    boxes = [(55, 180, 390, 640), (455, 180, 790, 640), (875, 180, 1205, 640), (1275, 180, 1745, 640)]
    headers = [
        ("X", "[batch=3, feature=4]", "blue", "blue_fill"),
        ("Wᵀ", "[feature=4, classe=3]", "purple", "purple_fill"),
        ("XWᵀ", "[batch=3, classe=3]", "green", "green_fill"),
    ]
    for box, (title, subtitle, color, fill) in zip(boxes[:3], headers):
        rounded(draw, box, 24, C["white"], C[color], 3)
        rounded(draw, (box[0] + 18, box[1] + 18, box[2] - 18, box[1] + 95), 18, C[fill], C[color], 2)
        centered_lines(draw, (box[0] + 28, box[1] + 25, box[2] - 28, box[1] + 62), title, 28, bold=True, fill=C[color])
        centered_lines(draw, (box[0] + 28, box[1] + 62, box[2] - 28, box[1] + 91), subtitle, 16, bold=True)

    final_box = boxes[3]
    rounded(draw, final_box, 24, C["white"], C["amber"], 3)
    rounded(
        draw,
        (final_box[0] + 18, final_box[1] + 18, final_box[2] - 18, final_box[1] + 125),
        18,
        C["amber_fill"],
        C["amber"],
        2,
    )
    centered_lines(draw, (final_box[0] + 28, final_box[1] + 23, final_box[2] - 28, final_box[1] + 62), "+ b → Y", 28, bold=True, fill=C["amber"])
    centered_lines(
        draw,
        (final_box[0] + 28, final_box[1] + 65, final_box[2] - 28, final_box[1] + 118),
        "b [classe=3]\nY [batch=3, classe=3]",
        16,
        bold=True,
        spacing=2,
    )

    matrix(draw, (105, 315, 335, 545), [[1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]])
    matrix(
        draw,
        (505, 275, 740, 555),
        [["1", "0", "0,5"], ["0", "1", "-0,5"], ["-1", "1", "0"], ["0,5", "-0,5", "1"]],
        size=17,
    )
    matrix(
        draw,
        (925, 315, 1155, 545),
        [["0", "1", "0,5"], ["-1", "2", "-0,5"], ["1,5", "0,5", "1"]],
        size=17,
    )

    bias_y = final_box[1] + 145
    centered_lines(draw, (1315, bias_y, 1410, bias_y + 40), "b =", 18, bold=True, fill=C["amber"])
    matrix(draw, (1425, bias_y, 1660, bias_y + 60), [["0,2", "-0,1", "0,3"]], size=16)
    centered_lines(draw, (1310, bias_y + 85, 1695, bias_y + 125), "broadcast su 3 righe", 18, bold=True, fill=C["amber"])
    matrix(
        draw,
        (1350, bias_y + 155, 1665, bias_y + 295),
        [["0,2", "0,9", "0,8"], ["-0,8", "1,9", "-0,2"], ["1,7", "0,4", "1,3"]],
        size=16,
    )

    for first, second in zip(boxes, boxes[1:]):
        arrow(draw, (first[2] + 10, 410), (second[0] - 12, 410), width=6)
    centered_lines(draw, (797, 330, 870, 385), "@", 28, bold=True)
    centered_lines(draw, (1210, 330, 1270, 385), "+", 28, bold=True)

    rounded(draw, (570, 690, 1230, 790), 22, C["blue_fill"], C["blue"], 3)
    centered_lines(
        draw,
        (600, 705, 1200, 775),
        "Dimensione contratta: feature = 4\nOgni cella dell'output è un prodotto scalare.",
        22,
        bold=True,
        spacing=6,
    )
    arrow(draw, (790, 640), (790, 688), C["blue"], 4, 12)
    arrow(draw, (875, 640), (875, 688), C["blue"], 4, 12)

    rounded(draw, (250, 850, 1550, 950), 22, C["amber_fill"], C["amber"], 3)
    centered_lines(
        draw,
        (290, 866, 1510, 934),
        "Le shape compatibili non sostituiscono il significato degli assi.",
        24,
        bold=True,
    )
    return save(image, ROOT / "assets/chapters/05_linear_algebra/LA-01/candidate-v1.png")


def make_la_02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    centered_lines(draw, (60, 18, width - 60, 72), "LA-02 · Rango e SVD come componenti ordinate", 34, bold=True)
    centered_lines(
        draw,
        (120, 75, width - 120, 125),
        "Una dipendenza tra righe appare come un valore singolare numericamente nullo",
        20,
        fill=C["muted"],
    )

    left = (55, 175, 500, 700)
    rounded(draw, left, 24, C["white"], C["blue"], 3)
    rounded(draw, (75, 195, 480, 275), 18, C["blue_fill"], C["blue"], 2)
    centered_lines(draw, (95, 205, 460, 260), "Matrice A [3,3]", 26, bold=True, fill=C["blue"])
    matrix(draw, (145, 335, 410, 545), [[1, 2, 3], [2, 4, 6], [1, 1, 1]], size=20)
    rounded(draw, (105, 580, 450, 660), 16, C["amber_fill"], C["amber"], 2)
    centered_lines(draw, (125, 590, 430, 650), "riga 2 = 2 × riga 1\nrango ≤ 2", 19, bold=True)

    center = (560, 175, 1170, 700)
    rounded(draw, center, 24, C["white"], C["purple"], 3)
    rounded(draw, (580, 195, 1150, 275), 18, C["purple_fill"], C["purple"], 2)
    centered_lines(draw, (600, 205, 1130, 260), "A = U · diag(S) · Vᵀ", 26, bold=True, fill=C["purple"])
    for x, label, shape, color, fill in [
        (610, "U", "[3,3]", "blue", "blue_fill"),
        (800, "diag(S)", "[3,3]", "amber", "amber_fill"),
        (1000, "Vᵀ", "[3,3]", "green", "green_fill"),
    ]:
        rounded(draw, (x, 320, x + 145, 450), 16, C[fill], C[color], 2)
        centered_lines(draw, (x + 10, 335, x + 135, 375), label, 21, bold=True, fill=C[color])
        centered_lines(draw, (x + 10, 390, x + 135, 430), shape, 17, bold=True)
    centered_lines(draw, (760, 350, 800, 420), "·", 30, bold=True)
    centered_lines(draw, (955, 350, 1000, 420), "·", 30, bold=True)
    centered_lines(draw, (620, 485, 1110, 530), "Valori singolari S", 22, bold=True)
    rounded(draw, (635, 540, 1095, 660), 18, C["neutral_fill"], C["neutral"], 2)
    singular_values = [("σ₁ = 8,5198", 1.0, C["purple"]), ("σ₂ = 0,6429", 0.07546, C["blue"]), ("σ₃ ≈ 0", 0.0, C["muted"])]
    for index, (label, fraction, color) in enumerate(singular_values):
        y = 555 + index * 32
        draw.text((655, y), label, font=font(16, True), fill=C["text"])
        bar_width = max(2, 250 * fraction)
        rounded(draw, (815, y + 2, 815 + bar_width, y + 21), 7, color, color, 1)

    arrow(draw, (505, 430), (550, 430), width=6)

    right = (1230, 175, 1745, 700)
    rounded(draw, right, 24, C["white"], C["green"], 3)
    rounded(draw, (1250, 195, 1725, 275), 18, C["green_fill"], C["green"], 2)
    centered_lines(draw, (1270, 205, 1705, 260), "Somma di componenti di rango 1", 23, bold=True, fill=C["green"])
    centered_lines(draw, (1260, 300, 1715, 350), "A = σ₁u₁v₁ᵀ + σ₂u₂v₂ᵀ + σ₃u₃v₃ᵀ", 19, bold=True)

    cards = [(1250, 385, 1405, 575), (1410, 385, 1565, 575), (1570, 385, 1725, 575)]
    card_data = [
        ("purple", "purple_fill", "Componente\n1", "dominante", True),
        ("blue", "blue_fill", "Componente\n2", "secondaria", True),
        ("neutral", "neutral_fill", "Componente\n3", "numericamente\nnulla", False),
    ]
    for card, (color, fill, title, weight, active) in zip(cards, card_data):
        rounded(draw, card, 16, C[fill], C[color], 2)
        centered_lines(draw, (card[0] + 8, card[1] + 12, card[2] - 8, card[1] + 65), title, 15, bold=True, fill=C[color], spacing=2)
        center_x = (card[0] + card[2]) / 2
        draw.line((center_x, card[1] + 83, center_x, card[1] + 135), fill=C[color], width=5)
        draw.line((card[0] + 35, card[1] + 109, card[2] - 35, card[1] + 109), fill=C[color], width=5)
        draw.ellipse((center_x - 9, card[1] + 100, center_x + 9, card[1] + 118), fill=C[color])
        centered_lines(draw, (card[0] + 8, card[1] + 145, card[2] - 8, card[3] - 10), weight, 13, bold=True, spacing=2)
        if not active:
            draw.line((card[0] + 20, card[1] + 20, card[2] - 20, card[3] - 20), fill=C["red"], width=4)
    arrow(draw, (1175, 430), (1220, 430), width=6)

    rounded(draw, (230, 785, 1570, 940), 24, C["amber_fill"], C["amber"], 3)
    centered_lines(
        draw,
        (270, 810, 1530, 915),
        "Rango numerico = 2 nell'esempio.\nIl valore singolare piccolo dipende da scala, precisione e tolleranza;\ntroncare componenti è una scelta del problema, non una regola universale.",
        21,
        bold=True,
        spacing=6,
    )
    return save(image, ROOT / "assets/chapters/05_linear_algebra/LA-02/candidate-v1.png")


def main() -> None:
    for path in (make_la_01(), make_la_02()):
        with Image.open(path) as image:
            print(path.relative_to(ROOT), image.size, path.stat().st_size)


if __name__ == "__main__":
    main()
