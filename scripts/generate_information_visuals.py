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


def probability_bars(
    draw: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    probabilities: list[float],
    colors: list[str],
    labels: list[str],
) -> None:
    x0, y0, x1, y1 = rect
    max_height = y1 - y0 - 65
    bar_width = 70
    gap = (x1 - x0 - 3 * bar_width) / 4
    for index, (probability, color, label) in enumerate(
        zip(probabilities, colors, labels)
    ):
        x = x0 + gap + (bar_width + gap) * index
        height = max_height * probability
        draw.rounded_rectangle(
            (x, y1 - 45 - height, x + bar_width, y1 - 45),
            radius=8,
            fill=color,
        )
        draw_centered_multiline(
            draw,
            (x - 10, y1 - 40, x + bar_width + 10, y1),
            label,
            font(14, True),
            C["muted"],
            max_lines=1,
        )
        draw_centered_multiline(
            draw,
            (x - 15, y0, x + bar_width + 15, y0 + 45),
            f"{probability:.4f}".replace(".", ","),
            font(14, True),
            color,
            max_lines=1,
        )


def prediction_row(
    draw: ImageDraw.ImageDraw,
    y: int,
    heading: str,
    color: str,
    fill: str,
    logits: str,
    probabilities: list[float],
    target_probability: float,
    loss: float,
) -> None:
    rounded(draw, (70, y, 1730, y + 295), 24, C["white"], color, 3)
    rounded(draw, (90, y + 25, 340, y + 270), 18, fill, color, 2)
    draw_centered_multiline(draw, (110, y + 35, 320, y + 85), heading, font(22, True), color, max_lines=2)
    draw_centered_multiline(draw, (110, y + 105, 320, y + 245), "Target\nclasse 0", font(20, True), C["text"], spacing=10, max_lines=2)

    rounded(draw, (385, y + 40, 700, y + 255), 18, C["neutral_fill"], C["neutral"], 2)
    draw_centered_multiline(draw, (405, y + 50, 680, y + 90), "LOGITS", font(18, True), C["muted"], max_lines=1)
    draw_centered_multiline(draw, (405, y + 105, 680, y + 220), logits, font(23, True), C["text"], spacing=10, max_lines=3)
    arrow(draw, (715, y + 147), (790, y + 147), fill=C["purple"], width=5, head=14)

    rounded(draw, (805, y + 40, 1180, y + 255), 18, C["white"], C["purple"], 2)
    draw_centered_multiline(draw, (825, y + 50, 1160, y + 90), "SOFTMAX", font(18, True), C["purple"], max_lines=1)
    probability_bars(
        draw,
        (835, y + 95, 1150, y + 235),
        probabilities,
        [C["blue"], C["amber"], C["red"]],
        ["c0", "c1", "c2"],
    )
    arrow(draw, (1195, y + 147), (1270, y + 147), fill=C["amber"], width=5, head=14)

    rounded(draw, (1285, y + 40, 1500, y + 255), 18, C["amber_fill"], C["amber"], 2)
    draw_centered_multiline(draw, (1300, y + 55, 1485, y + 105), "p(target)", font(18, True), C["amber"], max_lines=1)
    draw_centered_multiline(
        draw,
        (1300, y + 120, 1485, y + 225),
        f"{target_probability:.6f}".replace(".", ","),
        font(25, True),
        C["text"],
        max_lines=1,
    )
    loss_color = C["green"] if loss < 1 else C["red"]
    loss_fill = C["green_fill"] if loss < 1 else C["red_fill"]
    arrow(draw, (1515, y + 147), (1570, y + 147), fill=loss_color, width=5, head=14)
    rounded(draw, (1585, y + 40, 1710, y + 255), 18, loss_fill, loss_color, 2)
    draw_centered_multiline(draw, (1595, y + 55, 1700, y + 105), "NLL", font(18, True), loss_color, max_lines=1)
    draw_centered_multiline(
        draw,
        (1595, y + 120, 1700, y + 225),
        f"{loss:.6f}".replace(".", ","),
        font(21, True),
        C["text"],
        max_lines=1,
    )


def make_info01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "INFO-01 · Dai logits alla cross-entropy",
        "La loss dipende dalla probabilità assegnata alla classe osservata",
        width,
    )
    prediction_row(
        draw,
        180,
        "PREVISIONE\nCORRETTA",
        C["green"],
        C["green_fill"],
        "[ 2,0 ]\n[ 0,5 ]\n[−1,0 ]",
        [0.785597, 0.175290, 0.039113],
        0.785597,
        0.241311,
    )
    prediction_row(
        draw,
        515,
        "PREVISIONE\nERRATA",
        C["red"],
        C["red_fill"],
        "[−1,0 ]\n[ 0,5 ]\n[ 2,0 ]",
        [0.039113, 0.175290, 0.785597],
        0.039113,
        3.241311,
    )
    rounded(draw, (240, 845, 1560, 950), 20, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(
        draw,
        (270, 858, 1530, 935),
        "Le due distribuzioni hanno la stessa entropia perché sono permutazioni. La cross-entropy cambia perché il target resta la classe 0.",
        font(19, True),
        C["text"],
        spacing=5,
        max_lines=3,
    )
    return save_png(image, ROOT / "assets/chapters/08_information_theory/INFO-01/candidate-v1.png")


def make_info02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "INFO-02 · Entropia, cross-entropy e KL",
        "La cross-entropy contiene l'incertezza del target più il divario tra target e previsione",
        width,
    )

    rounded(draw, (80, 190, 600, 560), 24, C["white"], C["purple"], 3)
    draw_centered_multiline(draw, (105, 210, 575, 260), "TARGET q", font(22, True), C["purple"], max_lines=1)
    probability_bars(draw, (150, 285, 530, 500), [0.90, 0.05, 0.05], [C["purple"], C["amber"], C["amber"]], ["c0", "c1", "c2"])
    draw_centered_multiline(draw, (120, 500, 560, 545), "q = [0,90; 0,05; 0,05]", font(18, True), C["text"], max_lines=1)

    rounded(draw, (1200, 190, 1720, 560), 24, C["white"], C["blue"], 3)
    draw_centered_multiline(draw, (1225, 210, 1695, 260), "PREDIZIONE p", font(22, True), C["blue"], max_lines=1)
    probability_bars(draw, (1270, 285, 1650, 500), [0.785597, 0.175290, 0.039113], [C["blue"], C["amber"], C["red"]], ["c0", "c1", "c2"])
    draw_centered_multiline(draw, (1240, 500, 1680, 545), "p = [0,7856; 0,1753; 0,0391]", font(18, True), C["text"], max_lines=1)

    arrow(draw, (615, 375), (760, 375), fill=C["purple"], width=5, head=14)
    arrow(draw, (1185, 375), (1040, 375), fill=C["blue"], width=5, head=14)
    rounded(draw, (775, 235, 1025, 510), 22, C["amber_fill"], C["amber"], 3)
    draw_centered_multiline(draw, (795, 255, 1005, 310), "CROSS-ENTROPY", font(18, True), C["amber"], max_lines=2)
    draw_centered_multiline(draw, (795, 330, 1005, 475), "H(q,p)\n= −Σ q_i log p_i\n= 0,466311", font(20, True), C["text"], spacing=10, max_lines=3)

    rounded(draw, (120, 650, 540, 855), 20, C["purple_fill"], C["purple"], 3)
    draw_centered_multiline(draw, (145, 670, 515, 720), "ENTROPIA DEL TARGET", font(18, True), C["purple"], max_lines=2)
    draw_centered_multiline(draw, (145, 740, 515, 825), "H(q)\n= 0,394398", font(23, True), C["text"], spacing=8, max_lines=2)
    draw_centered_multiline(draw, (565, 715, 650, 790), "+", font(40, True), C["text"], max_lines=1)

    rounded(draw, (675, 650, 1095, 855), 20, C["amber_fill"], C["amber"], 3)
    draw_centered_multiline(draw, (700, 670, 1070, 720), "DIVERGENZA", font(18, True), C["amber"], max_lines=1)
    draw_centered_multiline(draw, (700, 740, 1070, 825), "KL(q||p)\n= 0,071914", font(23, True), C["text"], spacing=8, max_lines=2)
    draw_centered_multiline(draw, (1120, 715, 1205, 790), "=", font(40, True), C["text"], max_lines=1)

    rounded(draw, (1230, 650, 1680, 855), 20, C["green_fill"], C["green"], 3)
    draw_centered_multiline(draw, (1255, 670, 1655, 720), "CROSS-ENTROPY", font(18, True), C["green"], max_lines=1)
    draw_centered_multiline(draw, (1255, 740, 1655, 825), "H(q,p)\n= 0,466311", font(23, True), C["text"], spacing=8, max_lines=2)

    rounded(draw, (360, 895, 1440, 965), 18, C["neutral_fill"], C["neutral"], 2)
    draw_centered_multiline(
        draw,
        (390, 903, 1410, 955),
        "Caso one-hot: H(q)=0, quindi cross-entropy = KL = negative log-likelihood.",
        font(17, True),
        C["text"],
        max_lines=2,
    )
    return save_png(image, ROOT / "assets/chapters/08_information_theory/INFO-02/candidate-v1.png")


def main() -> None:
    for path in [make_info01(), make_info02()]:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
