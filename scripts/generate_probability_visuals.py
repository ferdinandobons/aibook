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


def make_prob01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "PROB-01 · Dal prior al posterior",
        "Bayes seleziona la massa compatibile con l'evidenza e la normalizza",
        width,
    )

    rounded(draw, (65, 190, 430, 760), 24, C["white"], C["blue"], 3)
    draw_centered_multiline(draw, (90, 205, 405, 270), "1 · MODELLO PRIMA DEI DATI", font(18, True), C["blue"], max_lines=2)
    rounded(draw, (100, 295, 395, 400), 16, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(draw, (120, 305, 375, 390), "Prior\nP(H) = 0,20\nP(¬H) = 0,80", font(18, True), C["text"], spacing=5, max_lines=3)
    rounded(draw, (100, 440, 395, 585), 16, C["purple_fill"], C["purple"], 2)
    draw_centered_multiline(
        draw,
        (120, 450, 375, 575),
        "Likelihood del segnale E₁\nP(E₁|H) = 0,80\nP(E₁|¬H) = 0,10",
        font(17, True),
        C["text"],
        spacing=5,
        max_lines=3,
    )
    rounded(draw, (100, 625, 395, 720), 16, C["neutral_fill"], C["neutral"], 2)
    draw_centered_multiline(draw, (120, 635, 375, 710), "H = problema reale\nE₁ = segnale nel testo", font(16, True), C["text"], spacing=4, max_lines=2)
    arrow(draw, (445, 475), (535, 475), fill=C["blue"], width=5, head=14)

    rounded(draw, (545, 190, 1160, 760), 24, C["white"], C["purple"], 3)
    draw_centered_multiline(draw, (570, 205, 1135, 270), "2 · DISTRIBUZIONE CONGIUNTA", font(18, True), C["purple"], max_lines=2)
    x0, y0 = 600, 315
    widths = [170, 145, 145, 145]
    xs = [x0]
    for cell_width in widths:
        xs.append(xs[-1] + cell_width)
    headers = ["Stato", "E₁ osservato", "¬E₁", "Totale"]
    for index, heading in enumerate(headers):
        fill = C["amber_fill"] if index == 1 else C["neutral_fill"]
        outline = C["amber"] if index == 1 else C["neutral"]
        text_color = C["amber"] if index == 1 else C["muted"]
        rounded(draw, (xs[index], y0, xs[index + 1], y0 + 70), 8, fill, outline, 2)
        draw_centered_multiline(draw, (xs[index] + 5, y0 + 5, xs[index + 1] - 5, y0 + 65), heading, font(15, True), text_color, max_lines=2)

    rows = [
        ("H", "0,16", "0,04", "0,20"),
        ("¬H", "0,08", "0,72", "0,80"),
        ("Totale", "0,24", "0,76", "1,00"),
    ]
    for row_index, row in enumerate(rows):
        y = y0 + 80 + row_index * 95
        for column_index, value in enumerate(row):
            fill = C["amber_fill"] if column_index == 1 else C["white"]
            outline = C["amber"] if column_index == 1 else C["neutral"]
            rounded(draw, (xs[column_index], y, xs[column_index + 1], y + 80), 8, fill, outline, 2)
            draw_centered_multiline(draw, (xs[column_index] + 5, y + 5, xs[column_index + 1] - 5, y + 75), value, font(20, True), C["text"], max_lines=1)
    draw_centered_multiline(draw, (590, 640, 1115, 720), "P(E₁) = 0,16 + 0,08 = 0,24", font(18, True), C["amber"], max_lines=1)
    arrow(draw, (1175, 475), (1265, 475), fill=C["amber"], width=5, head=14)

    rounded(draw, (1275, 190, 1735, 760), 24, C["white"], C["green"], 3)
    draw_centered_multiline(draw, (1300, 205, 1710, 270), "3 · NORMALIZZAZIONE", font(18, True), C["green"], max_lines=2)
    rounded(draw, (1320, 300, 1690, 405), 16, C["amber_fill"], C["amber"], 2)
    draw_centered_multiline(draw, (1340, 310, 1670, 395), "Numeratore\nP(H,E₁) = 0,16", font(18, True), C["text"], spacing=5, max_lines=2)
    draw_centered_multiline(draw, (1320, 435, 1690, 465), "diviso", font(16, True), C["muted"], max_lines=1)
    rounded(draw, (1320, 485, 1690, 590), 16, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(draw, (1340, 495, 1670, 580), "Evidenza\nP(E₁) = 0,24", font(18, True), C["text"], spacing=5, max_lines=2)
    rounded(draw, (1320, 630, 1690, 720), 16, C["green_fill"], C["green"], 3)
    draw_centered_multiline(draw, (1340, 640, 1670, 710), "Posterior\nP(H|E₁) = 0,6667", font(20, True), C["green"], spacing=5, max_lines=2)

    rounded(draw, (190, 825, 1610, 935), 20, C["amber_fill"], C["amber"], 2)
    draw_centered_multiline(
        draw,
        (220, 840, 1580, 920),
        "Il posterior è corretto rispetto al modello usato. Se prior o likelihood non descrivono bene il processo reale, anche l'aggiornamento può risultare mal calibrato.",
        font(19, True),
        C["text"],
        spacing=5,
        max_lines=3,
    )

    return save_png(image, ROOT / "assets/chapters/07_probability/PROB-01/candidate-v1.png")


def sample_card(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    heading: str,
    size_text: str,
    success_text: str,
    mean_text: str,
    deviation_text: str,
    color: str,
    fill: str,
    successes: int,
    sample_size: int,
) -> None:
    x0, y0, x1, y1 = rect
    rounded(draw, rect, 24, C["white"], color, 3)
    draw_centered_multiline(draw, (x0 + 20, y0 + 20, x1 - 20, y0 + 65), heading, font(20, True), color, max_lines=1)
    rounded(draw, (x0 + 35, y0 + 90, x1 - 35, y0 + 210), 16, fill, color, 2)
    draw_centered_multiline(draw, (x0 + 55, y0 + 100, x1 - 55, y0 + 200), f"{size_text}\n{success_text}", font(18, True), C["text"], spacing=7, max_lines=2)

    bar = (x0 + 45, y0 + 260, x1 - 45, y0 + 320)
    rounded(draw, bar, 12, C["neutral_fill"], C["neutral"], 2)
    inner_width = (bar[2] - bar[0] - 8) * successes / sample_size
    draw.rounded_rectangle((bar[0] + 4, bar[1] + 4, bar[0] + 4 + inner_width, bar[3] - 4), radius=8, fill=color)
    draw_centered_multiline(draw, (x0 + 35, y0 + 350, x1 - 35, y0 + 430), mean_text, font(24, True), color, max_lines=1)
    rounded(draw, (x0 + 35, y0 + 470, x1 - 35, y0 + 565), 16, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(draw, (x0 + 50, y0 + 480, x1 - 50, y0 + 555), deviation_text, font(16, True), C["text"], spacing=4, max_lines=2)
    draw_centered_multiline(
        draw,
        (x0 + 35, y0 + 600, x1 - 35, y0 + 680),
        "La media è una statistica\ncalcolata sugli esiti osservati",
        font(16, True),
        C["text"],
        spacing=5,
        max_lines=2,
    )


def make_prob02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "PROB-02 · Distribuzione, campione e stimatore",
        "Il parametro resta fisso; la statistica cambia da un campione all'altro",
        width,
    )

    rounded(draw, (65, 190, 430, 820), 24, C["white"], C["purple"], 3)
    draw_centered_multiline(draw, (90, 210, 405, 260), "DISTRIBUZIONE", font(21, True), C["purple"], max_lines=1)
    rounded(draw, (110, 300, 385, 440), 18, C["purple_fill"], C["purple"], 2)
    draw_centered_multiline(draw, (130, 315, 365, 425), "Bernoulli\np = 0,30", font(25, True), C["text"], spacing=8, max_lines=2)
    draw_centered_multiline(draw, (100, 485, 395, 525), "Momenti teorici", font(18, True), C["muted"], max_lines=1)
    rounded(draw, (105, 550, 390, 690), 16, C["neutral_fill"], C["neutral"], 2)
    draw_centered_multiline(draw, (125, 565, 370, 675), "E[X] = 0,30\nVar(X) = 0,21", font(20, True), C["text"], spacing=10, max_lines=2)
    rounded(draw, (105, 725, 390, 785), 14, C["amber_fill"], C["amber"], 2)
    draw_centered_multiline(draw, (120, 732, 375, 778), "Parametro non osservato direttamente", font(15, True), C["amber"], max_lines=2)
    arrow(draw, (445, 500), (525, 500), fill=C["purple"], width=5, head=14)

    sample_card(draw, (540, 190, 885, 820), "CAMPIONE A", "n = 10", "successi = 6", "media = 0,6000", "deviazione della media\n≈ 0,1449", C["red"], C["red_fill"], 6, 10)
    sample_card(draw, (920, 190, 1265, 820), "CAMPIONE B", "n = 100", "successi = 32", "media = 0,3200", "deviazione della media\n≈ 0,0458", C["amber"], C["amber_fill"], 32, 100)
    sample_card(draw, (1300, 190, 1735, 820), "CAMPIONE C", "n = 10 000", "successi = 3 042", "media = 0,3042", "deviazione della media\n≈ 0,0046", C["green"], C["green_fill"], 3042, 10_000)

    rounded(draw, (210, 860, 1590, 950), 20, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(
        draw,
        (240, 873, 1560, 935),
        "La legge dei grandi numeri descrive l'avvicinamento della media al valore atteso sotto condizioni precise. Non obbliga ogni campione più grande a essere più vicino del precedente.",
        font(18, True),
        C["text"],
        spacing=4,
        max_lines=3,
    )

    return save_png(image, ROOT / "assets/chapters/07_probability/PROB-02/candidate-v1.png")


def main() -> None:
    for path in [make_prob01(), make_prob02()]:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
