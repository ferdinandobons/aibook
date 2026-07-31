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


def node(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    label: str,
    color: str,
    fill: str,
    width: int,
    height: int,
) -> tuple[int, int, int, int]:
    x, y = center
    box = (x - width // 2, y - height // 2, x + width // 2, y + height // 2)
    rounded(draw, box, 16, fill, color, 3)
    draw_centered_multiline(
        draw,
        (box[0] + 10, box[1] + 8, box[2] - 10, box[3] - 8),
        label,
        font(15, True),
        color,
        spacing=3,
        max_lines=2,
    )
    return box


def make_know01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "KNOW-01 · Dai fatti alle conclusioni",
        "Il forward chaining applica regole positive finché non compaiono nuovi fatti",
        width,
    )

    rounded(draw, (45, 160, 535, 820), 28, C["white"], C["blue"], 3)
    draw_centered_multiline(
        draw,
        (70, 178, 510, 235),
        "FATTI INIZIALI",
        font(22, True),
        C["blue"],
        max_lines=1,
    )
    facts = [
        ("F1", "message_mentions_\nmissing_delivery(order_42)"),
        ("F2", "tracking_stalled(order_42)"),
        ("F3", "delivery_date_passed(order_42)"),
    ]
    for (tag, text), y in zip(facts, [275, 445, 615]):
        rounded(draw, (85, y, 495, y + 115), 18, C["blue_fill"], C["blue"], 2)
        rounded(draw, (100, y + 22, 155, y + 77), 14, C["white"], C["blue"], 2)
        draw_centered_multiline(
            draw,
            (107, y + 28, 148, y + 70),
            tag,
            font(16, True),
            C["blue"],
            max_lines=1,
        )
        draw_centered_multiline(
            draw,
            (180, y + 12, 475, y + 103),
            text,
            font(14, True),
            C["text"],
            spacing=5,
            max_lines=3,
        )

    rounded(draw, (655, 160, 1145, 820), 28, C["white"], C["purple"], 3)
    draw_centered_multiline(
        draw,
        (680, 178, 1120, 235),
        "REGOLE DI HORN",
        font(22, True),
        C["purple"],
        max_lines=1,
    )
    rules = [
        (
            "R1",
            "tracking_stalled(?ordine)\nAND delivery_date_passed(?ordine)\n→ possible_delay(?ordine)",
        ),
        (
            "R2",
            "message_mentions_\nmissing_delivery(?ordine)\nAND possible_delay(?ordine)\n→ needs_review(?ordine)",
        ),
        (
            "R3",
            "needs_review(?ordine)\n→ eligible_for_delay_\nworkflow(?ordine)",
        ),
    ]
    for (tag, text), y, box_height, max_lines in zip(
        rules,
        [270, 470, 670],
        [145, 155, 105],
        [3, 4, 3],
    ):
        rounded(
            draw,
            (695, y, 1105, y + box_height),
            18,
            C["purple_fill"],
            C["purple"],
            2,
        )
        rounded(draw, (710, y + 20, 765, y + 75), 14, C["white"], C["purple"], 2)
        draw_centered_multiline(
            draw,
            (717, y + 26, 758, y + 68),
            tag,
            font(16, True),
            C["purple"],
            max_lines=1,
        )
        draw_centered_multiline(
            draw,
            (800, y + 10, 1085, y + box_height - 10),
            text,
            font(13, True),
            C["text"],
            spacing=4,
            max_lines=max_lines,
        )

    rounded(draw, (1265, 160, 1755, 820), 28, C["white"], C["green"], 3)
    draw_centered_multiline(
        draw,
        (1290, 178, 1730, 235),
        "FATTI DERIVATI",
        font(22, True),
        C["green"],
        max_lines=1,
    )
    derived = [
        ("D1", "possible_delay(order_42)"),
        ("D2", "needs_review(order_42)"),
        ("D3", "eligible_for_delay_\nworkflow(order_42)"),
    ]
    for (tag, text), y in zip(derived, [285, 485, 685]):
        rounded(draw, (1305, y, 1715, y + 105), 18, C["green_fill"], C["green"], 2)
        rounded(draw, (1320, y + 20, 1375, y + 75), 14, C["white"], C["green"], 2)
        draw_centered_multiline(
            draw,
            (1327, y + 26, 1368, y + 68),
            tag,
            font(16, True),
            C["green"],
            max_lines=1,
        )
        draw_centered_multiline(
            draw,
            (1400, y + 10, 1695, y + 95),
            text,
            font(14, True),
            C["text"],
            spacing=5,
            max_lines=2,
        )

    for y, color, label in [
        (340, C["blue"], "1"),
        (540, C["purple"], "2"),
        (740, C["green"], "3"),
    ]:
        arrow(draw, (540, y), (645, y), fill=color, width=5, head=14)
        arrow(draw, (1155, y), (1255, y), fill=color, width=5, head=14)
        rounded(draw, (565, y - 30, 635, y + 30), 14, C["white"], color, 2)
        draw_centered_multiline(
            draw,
            (575, y - 22, 625, y + 22),
            label,
            font(18, True),
            color,
            max_lines=1,
        )

    rounded(draw, (190, 850, 1610, 955), 22, C["amber_fill"], C["amber"], 3)
    draw_centered_multiline(
        draw,
        (220, 864, 1580, 941),
        "Assenza ≠ negazione: se delivered(order_42) non compare, questo sistema non deriva not_delivered(order_42). Servirebbe una regola o una semantica esplicita della negazione.",
        font(18, True),
        C["text"],
        spacing=5,
        max_lines=3,
    )

    return save_png(
        image,
        ROOT / "assets/chapters/11_knowledge_logic/KNOW-01/candidate-v2.png",
    )


def make_know02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "KNOW-02 · Una rete bayesiana fattorizza la congiunta",
        "Nel modello illustrativo, i due segnali sono indipendenti quando lo stato di ritardo è fissato",
        width,
    )

    rounded(draw, (55, 160, 910, 805), 28, C["white"], C["neutral"], 3)
    draw_centered_multiline(
        draw,
        (80, 180, 885, 230),
        "STRUTTURA E TABELLE CONDIZIONALI",
        font(21, True),
        C["text"],
        max_lines=1,
    )
    delay = node(draw, (465, 300), "H · ritardo reale", C["purple"], C["purple_fill"], 250, 85)
    message = node(draw, (245, 535), "M · segnale nel messaggio", C["blue"], C["blue_fill"], 300, 85)
    tracking = node(draw, (685, 535), "T · tracking fermo", C["blue"], C["blue_fill"], 270, 85)

    arrow(draw, (410, delay[3] + 4), (305, message[1] - 6), fill=C["purple"], width=5, head=14)
    arrow(draw, (520, delay[3] + 4), (625, tracking[1] - 6), fill=C["purple"], width=5, head=14)

    rounded(draw, (120, 265, 315, 335), 16, C["purple_fill"], C["purple"], 2)
    draw_centered_multiline(
        draw,
        (135, 275, 300, 325),
        "P(H=1)=0,20",
        font(17, True),
        C["purple"],
        max_lines=1,
    )
    for index in range(6):
        if index % 2:
            continue
        x0 = 315 + (340 - 315) * index / 6
        x1 = 315 + (340 - 315) * (index + 1) / 6
        draw.line((x0, 300, x1, 300), fill=C["purple"], width=3)

    rounded(draw, (100, 655, 390, 760), 16, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(
        draw,
        (115, 665, 375, 750),
        "P(M=1|H=1)=0,80\nP(M=1|H=0)=0,10",
        font(15, True),
        C["text"],
        spacing=6,
        max_lines=2,
    )
    rounded(draw, (530, 655, 820, 760), 16, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(
        draw,
        (545, 665, 805, 750),
        "P(T=1|H=1)=0,70\nP(T=1|H=0)=0,20",
        font(15, True),
        C["text"],
        spacing=6,
        max_lines=2,
    )

    rounded(draw, (965, 160, 1745, 805), 28, C["white"], C["green"], 3)
    draw_centered_multiline(
        draw,
        (990, 180, 1720, 230),
        "FATTORIZZAZIONE E INFERENZA",
        font(21, True),
        C["green"],
        max_lines=1,
    )
    rounded(draw, (1010, 265, 1700, 390), 20, C["neutral_fill"], C["neutral"], 2)
    draw_centered_multiline(
        draw,
        (1035, 280, 1675, 375),
        "P(H,M,T) = P(H) · P(M|H) · P(T|H)",
        font(25, True),
        C["text"],
        max_lines=2,
    )
    rounded(draw, (1010, 430, 1700, 565), 20, C["amber_fill"], C["amber"], 2)
    draw_centered_multiline(
        draw,
        (1035, 445, 1675, 550),
        "Evidenza: M=1, T=1\nnumeratore = 0,20 · 0,80 · 0,70 = 0,112",
        font(20, True),
        C["text"],
        spacing=8,
        max_lines=2,
    )
    rounded(draw, (1010, 605, 1700, 740), 20, C["green_fill"], C["green"], 3)
    draw_centered_multiline(
        draw,
        (1035, 620, 1675, 725),
        "P(H=1|M=1,T=1)\n= 0,112 / (0,112 + 0,016)\n= 0,875",
        font(24, True),
        C["green"],
        spacing=8,
        max_lines=3,
    )

    rounded(draw, (200, 845, 1600, 955), 22, C["amber_fill"], C["amber"], 3)
    draw_centered_multiline(
        draw,
        (230, 860, 1570, 940),
        "L'indipendenza condizionata tra M e T, dato H, è una proprietà del modello. Se i due segnali restano dipendenti anche fissato H, questa fattorizzazione non è valida.",
        font(18, True),
        C["text"],
        spacing=5,
        max_lines=3,
    )

    return save_png(
        image,
        ROOT / "assets/chapters/11_knowledge_logic/KNOW-02/candidate-v3.png",
    )


def main() -> None:
    for path in [make_know01(), make_know02()]:
        with Image.open(path) as image:
            print(
                f"{path.relative_to(ROOT)}: "
                f"{image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes"
            )


if __name__ == "__main__":
    main()
