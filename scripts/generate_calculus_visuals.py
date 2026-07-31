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


def panel(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    heading: str,
    body: str,
    outline: str,
    fill: str,
    *,
    body_lines: int = 4,
) -> None:
    rounded(draw, rect, 20, fill, outline, 3)
    x0, y0, x1, y1 = rect
    draw_centered_multiline(
        draw,
        (x0 + 14, y0 + 12, x1 - 14, y0 + 52),
        heading,
        font(18, True),
        outline,
        spacing=2,
        max_lines=1,
    )
    draw_centered_multiline(
        draw,
        (x0 + 18, y0 + 58, x1 - 18, y1 - 16),
        body,
        font(17, True),
        C["text"],
        spacing=5,
        max_lines=body_lines,
    )


def make_calc01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "CALC-01 · Forward e backward sullo stesso grafo",
        "Il forward calcola i valori; il backward compone sensibilità locali",
        width,
    )

    nodes = [
        (70, 210, 285, 360, "Input", "x = 2,0\nw₁ = 1,5\nb₁ = −0,5", C["blue"], C["blue_fill"]),
        (365, 210, 615, 360, "Affine 1", "z = w₁x + b₁\nz = 2,500000", C["purple"], C["purple_fill"]),
        (695, 210, 935, 360, "Attivazione", "h = tanh(z)\nh = 0,986614", C["purple"], C["purple_fill"]),
        (1015, 210, 1265, 360, "Affine 2", "ŷ = w₂h + b₂\nw₂ = −0,7\nb₂ = 0,2\nŷ = −0,490630", C["purple"], C["purple_fill"]),
        (1345, 210, 1710, 360, "Loss", "y = 0,4\nL = 1/2(ŷ − y)²\nL = 0,396611", C["green"], C["green_fill"]),
    ]
    for node in nodes:
        panel(draw, node[:4], node[4], node[5], node[6], node[7])
    for first, second in zip(nodes, nodes[1:]):
        arrow(
            draw,
            (first[2] + 8, (first[1] + first[3]) / 2),
            (second[0] - 10, (second[1] + second[3]) / 2),
            C["blue"],
            width=5,
            head=14,
        )
    draw_centered_multiline(
        draw,
        (70, 155, 1710, 195),
        "FORWARD · valori da sinistra a destra",
        font(20, True),
        C["blue"],
        max_lines=1,
    )

    local = [
        (365, 480, 615, 630, "∂z/∂w₁ = x = 2,0\n∂z/∂b₁ = 1"),
        (695, 480, 935, 630, "∂h/∂z = 1 − h²\n= 0,026592"),
        (1015, 480, 1265, 630, "∂ŷ/∂h = w₂ = −0,7\n∂ŷ/∂w₂ = h"),
        (1345, 480, 1710, 630, "∂L/∂ŷ = ŷ − y\n= −0,890630"),
    ]
    for x0, y0, x1, y1, text in local:
        rounded(draw, (x0, y0, x1, y1), 16, C["amber_fill"], C["amber"], 2)
        draw_centered_multiline(
            draw,
            (x0 + 15, y0 + 10, x1 - 15, y1 - 10),
            text,
            font(16, True),
            C["text"],
            spacing=5,
            max_lines=3,
        )
    draw_centered_multiline(
        draw,
        (70, 425, 1710, 465),
        "DERIVATE LOCALI · ogni nodo conserva il proprio contratto",
        font(20, True),
        C["amber"],
        max_lines=1,
    )

    gradients = [
        (70, 745, 285, 875, "∂L/∂w₁ = 0,033157\n∂L/∂b₁ = 0,016579"),
        (365, 745, 615, 875, "∂L/∂z = 0,016579"),
        (695, 745, 935, 875, "∂L/∂h = 0,623441"),
        (1015, 745, 1265, 875, "∂L/∂w₂ = −0,878708\n∂L/∂b₂ = −0,890630"),
        (1345, 745, 1710, 875, "seme iniziale\n∂L/∂L = 1"),
    ]
    for x0, y0, x1, y1, text in gradients:
        rounded(draw, (x0, y0, x1, y1), 16, C["neutral_fill"], C["amber"], 2)
        draw_centered_multiline(
            draw,
            (x0 + 14, y0 + 10, x1 - 14, y1 - 10),
            text,
            font(16, True),
            C["text"],
            spacing=5,
            max_lines=2,
        )
    for first, second in zip(reversed(gradients), reversed(gradients[:-1])):
        arrow(
            draw,
            (first[0] - 8, (first[1] + first[3]) / 2),
            (second[2] + 10, (second[1] + second[3]) / 2),
            C["amber"],
            width=5,
            head=14,
        )
    draw_centered_multiline(
        draw,
        (70, 665, 1710, 715),
        "BACKWARD · gradienti da destra a sinistra, senza modificare i valori del forward",
        font(20, True),
        C["amber"],
        max_lines=1,
    )

    rounded(draw, (250, 915, 1550, 970), 18, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(
        draw,
        (270, 922, 1530, 963),
        "Backpropagation calcola gradienti. L'optimizer, trattato separatamente, decide come usare quei gradienti per aggiornare i parametri.",
        font(17, True),
        C["text"],
        spacing=3,
        max_lines=2,
    )

    return save_png(image, ROOT / "assets/chapters/06_calculus_backprop/CALC-01/candidate-v1.png")


def reverse_card(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    heading: str,
    formula: str,
    incoming: str,
    local: str,
    outgoing: str,
    color: str,
    fill: str,
) -> None:
    x0, y0, x1, y1 = rect
    rounded(draw, rect, 22, C["white"], color, 3)
    rounded(draw, (x0 + 18, y0 + 18, x1 - 18, y0 + 88), 16, fill, color, 2)
    draw_centered_multiline(draw, (x0 + 30, y0 + 22, x1 - 30, y0 + 52), heading, font(21, True), color, max_lines=1)
    draw_centered_multiline(draw, (x0 + 30, y0 + 51, x1 - 30, y0 + 84), formula, font(18, True), C["text"], max_lines=1)

    sections = [
        ("1 · IN ARRIVO", incoming, C["blue_fill"], C["blue"], 130),
        ("2 · LOCALE", local, C["amber_fill"], C["amber"], 165),
        ("3 · IN USCITA", outgoing, C["green_fill"], C["green"], 170),
    ]
    y = y0 + 108
    for label, text, section_fill, section_color, section_height in sections:
        rounded(draw, (x0 + 28, y, x1 - 28, y + section_height), 14, section_fill, section_color, 2)
        draw_centered_multiline(draw, (x0 + 42, y + 8, x1 - 42, y + 36), label, font(15, True), section_color, max_lines=1)
        draw_centered_multiline(
            draw,
            (x0 + 42, y + 38, x1 - 42, y + section_height - 10),
            text,
            font(16, True),
            C["text"],
            spacing=4,
            max_lines=4,
        )
        y += section_height + 12


def make_calc02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "CALC-02 · Reverse mode come composizione di derivate locali",
        "Un gradiente in arrivo viene moltiplicato per la derivata locale e distribuito agli input del nodo",
        width,
    )

    reverse_card(
        draw,
        (80, 190, 545, 735),
        "Nodo loss",
        "L = 1/2(ŷ − y)²",
        "gradiente in arrivo\n1",
        "derivata locale\n∂L/∂ŷ = ŷ − y",
        "gradiente in uscita\n∂L/∂ŷ = −0,890630",
        C["green"],
        C["green_fill"],
    )
    reverse_card(
        draw,
        (665, 190, 1130, 735),
        "Nodo affine",
        "ŷ = w₂h + b₂",
        "gradiente in arrivo\n−0,890630",
        "derivate locali\n∂ŷ/∂h = w₂\n∂ŷ/∂w₂ = h\n∂ŷ/∂b₂ = 1",
        "gradienti in uscita\n∂L/∂h = 0,623441\n∂L/∂w₂ = −0,878708\n∂L/∂b₂ = −0,890630",
        C["purple"],
        C["purple_fill"],
    )
    reverse_card(
        draw,
        (1250, 190, 1720, 735),
        "Nodo tanh",
        "h = tanh(z)",
        "gradiente in arrivo\n0,623441",
        "derivata locale\n∂h/∂z = 1 − h²\n= 0,026592",
        "gradiente in uscita\n∂L/∂z = 0,016579",
        C["amber"],
        C["amber_fill"],
    )

    arrow(draw, (555, 440), (655, 440), C["amber"], width=5, head=15)
    arrow(draw, (1140, 440), (1240, 440), C["amber"], width=5, head=15)
    draw_centered_multiline(draw, (550, 392, 660, 425), "VJP", font(15, True), C["amber"], max_lines=1)
    draw_centered_multiline(draw, (1135, 392, 1245, 425), "VJP", font(15, True), C["amber"], max_lines=1)

    rounded(draw, (120, 790, 1680, 940), 22, C["neutral_fill"], C["neutral"], 2)
    draw_centered_multiline(draw, (160, 810, 720, 855), "DIFFERENZIAZIONE", font(20, True), C["purple"], max_lines=1)
    draw_centered_multiline(draw, (160, 855, 720, 915), "calcola ∂L/∂θ\nsul grafo eseguito", font(18, True), C["text"], max_lines=2)
    arrow(draw, (760, 865), (1030, 865), C["text"], width=5, head=15)
    draw_centered_multiline(draw, (755, 815, 1035, 850), "gradienti disponibili", font(16, True), C["muted"], max_lines=1)
    draw_centered_multiline(draw, (1070, 810, 1640, 855), "OPTIMIZER STEP", font(20, True), C["red"], max_lines=1)
    draw_centered_multiline(
        draw,
        (1070, 855, 1640, 915),
        "usa i gradienti per proporre\nun aggiornamento dei parametri",
        font(18, True),
        C["text"],
        max_lines=2,
    )

    return save_png(image, ROOT / "assets/chapters/06_calculus_backprop/CALC-02/candidate-v2.png")


def main() -> None:
    for path in [make_calc01(), make_calc02()]:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
