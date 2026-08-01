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
    text_size,
    title_block,
    wrap_text,
)

ROOT = Path(__file__).resolve().parents[1]


def draw_left_wrapped(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    size: int,
    *,
    bold: bool = False,
    fill: str = C["text"],
    spacing: int = 5,
    max_lines: int = 4,
) -> None:
    x0, y0, x1, _ = box
    selected_font = font(size, bold)
    lines = wrap_text(draw, text, selected_font, x1 - x0)
    if len(lines) > max_lines:
        raise ValueError(f"Text exceeds box: {text!r} -> {lines!r}")
    y = y0
    for line in lines:
        draw.text((x0, y), line, font=selected_font, fill=fill)
        y += text_size(draw, line, selected_font)[1] + spacing


def make_hist01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "HIST-01 · Cinque transizioni, diversi colli di bottiglia",
        "Le fasi si sovrappongono: cambia ciò che il progettista deve rappresentare, acquisire, addestrare o integrare",
        width,
    )

    columns = [
        (
            "1",
            "SIMBOLI E RICERCA",
            "anni 1950-1970",
            C["blue"],
            C["blue_fill"],
            "Stati, simboli, regole e funzioni di transizione.",
            "Rappresentare il problema e contenere lo spazio di ricerca.",
            ["Turing e Dartmouth", "problem solving", "physical symbol system"],
        ),
        (
            "2",
            "SISTEMI ESPERTI E STATISTICA",
            "anni 1970-2000",
            C["purple"],
            C["purple_fill"],
            "Knowledge base, feature progettate e modelli statistici.",
            "Acquisire conoscenza, mantenere regole e scegliere feature utili.",
            ["MYCIN", "knowledge engineering", "support vector network"],
        ),
        (
            "3",
            "RAPPRESENTAZIONI APPRESE",
            "anni 1980-2010",
            C["green"],
            C["green_fill"],
            "Pesi multilivello, backpropagation e feature apprese.",
            "Rendere stabile il training e disporre di dati e calcolo adeguati.",
            ["backpropagation", "reti convoluzionali", "ImageNet e GPU"],
        ),
        (
            "4",
            "TRANSFORMER E PRETRAINING",
            "dal 2017",
            C["amber"],
            C["amber_fill"],
            "Attention, pretraining ampio e adattamento ai task.",
            "Costruire corpora, obiettivi, compute e valutazioni trasferibili.",
            ["Transformer", "BERT", "scaling e few-shot"],
        ),
        (
            "5",
            "FOUNDATION MODEL E SISTEMI",
            "dal 2021",
            C["red"],
            C["red_fill"],
            "Modello di base, adattamento, retrieval, strumenti e policy.",
            "Integrare capacità, costi, aggiornamento, sicurezza e governance.",
            ["base riutilizzabile", "sistemi multimodali", "agenti e tool"],
        ),
    ]

    x0 = 35
    gap = 18
    card_width = 332
    top = 155
    bottom = 815
    for index, item in enumerate(columns):
        number, heading, period, color, fill, representation, bottleneck, examples = item
        x = x0 + index * (card_width + gap)
        card = (x, top, x + card_width, bottom)
        rounded(draw, card, 24, C["white"], color, 4)
        rounded(draw, (x + 16, top + 16, x + card_width - 16, top + 112), 18, fill, color, 3)
        draw.ellipse((x + 30, top + 33, x + 82, top + 85), fill=color)
        number_font = font(23, True)
        number_width, number_height = text_size(draw, number, number_font)
        draw.text((x + 56 - number_width / 2, top + 59 - number_height / 2), number, font=number_font, fill=C["white"])
        draw_centered_multiline(
            draw,
            (x + 95, top + 26, x + card_width - 25, top + 78),
            heading,
            font(19, True),
            color,
            spacing=2,
            max_lines=3,
        )
        draw_centered_multiline(
            draw,
            (x + 95, top + 78, x + card_width - 25, top + 105),
            period,
            font(15, True),
            C["muted"],
            spacing=1,
            max_lines=1,
        )

        draw.text((x + 28, top + 145), "RAPPRESENTAZIONE", font=font(16, True), fill=color)
        rounded(draw, (x + 24, top + 176, x + card_width - 24, top + 275), 16, fill, color, 2)
        draw_centered_multiline(
            draw,
            (x + 42, top + 188, x + card_width - 42, top + 263),
            representation,
            font(17),
            C["text"],
            spacing=4,
            max_lines=4,
        )

        draw.text((x + 28, top + 310), "COLLO DI BOTTIGLIA DOMINANTE", font=font(15, True), fill=color)
        rounded(draw, (x + 24, top + 340, x + card_width - 24, top + 460), 16, C["neutral_fill"], C["neutral"], 2)
        draw_centered_multiline(
            draw,
            (x + 42, top + 352, x + card_width - 42, top + 448),
            bottleneck,
            font(17, True),
            C["text"],
            spacing=4,
            max_lines=5,
        )

        draw.text((x + 28, top + 497), "ESEMPI PORTANTI", font=font(15, True), fill=color)
        example_y = top + 530
        for example in examples:
            rounded(draw, (x + 26, example_y, x + card_width - 26, example_y + 45), 14, fill, color, 2)
            draw_centered_multiline(
                draw,
                (x + 39, example_y + 5, x + card_width - 39, example_y + 40),
                example,
                font(15, True),
                C["text"],
                spacing=2,
                max_lines=2,
            )
            example_y += 55

    footer = (180, 850, 1620, 950)
    rounded(draw, footer, 24, C["amber_fill"], C["amber"], 3)
    draw.ellipse((215, 870, 275, 930), fill="#F59E0B")
    draw.text((237, 881), "i", font=font(31, True), fill=C["white"])
    draw_centered_multiline(
        draw,
        (305, 865, 1580, 938),
        "Le date orientano la lettura, ma le famiglie si sovrappongono e continuano a convivere nei sistemi moderni.",
        font(23, True),
        C["text"],
        spacing=4,
        max_lines=2,
    )

    return save_png(image, ROOT / "assets/chapters/02_history/HIST-01/candidate-v1.png")


def make_hist02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "HIST-02 · La stessa richiesta attraverso paradigmi diversi",
        "L’input esterno resta uguale; cambiano rappresentazione, conoscenza appresa e componenti del sistema",
        width,
    )

    case = (540, 135, 1260, 235)
    rounded(draw, case, 24, C["neutral_fill"], C["neutral"], 3)
    draw.text((580, 157), "INPUT COMUNE", font=font(19, True), fill=C["muted"])
    draw_centered_multiline(
        draw,
        (600, 178, 1200, 225),
        "«Il pacco non è arrivato»",
        font(28, True),
        max_lines=2,
    )

    panel_specs = [
        (
            "1",
            "REGOLE E RICERCA",
            C["blue"],
            C["blue_fill"],
            [
                ("Rappresentazione", "stati e transizioni scritti a mano"),
                ("Calcolo", "ricerca di un percorso valido"),
                ("Output", "azione prevista dalla procedura"),
            ],
            "Se una regola manca, il sistema non la inventa.",
        ),
        (
            "2",
            "SISTEMA ESPERTO",
            C["purple"],
            C["purple_fill"],
            [
                ("Rappresentazione", "knowledge base di regole di dominio"),
                ("Calcolo", "motore di inferenza"),
                ("Output", "raccomandazione motivata dalle regole"),
            ],
            "Il costo si sposta sulla knowledge engineering.",
        ),
        (
            "3",
            "MODELLO APPRESO",
            C["green"],
            C["green_fill"],
            [
                ("Rappresentazione", "feature o vettori appresi dai dati"),
                ("Calcolo", "parametri scelti durante il training"),
                ("Output", "categoria o predizione"),
            ],
            "La qualità dipende da dati, obiettivo e valutazione.",
        ),
        (
            "4",
            "SISTEMA CON FOUNDATION MODEL",
            C["amber"],
            C["amber_fill"],
            [
                ("Rappresentazione", "modello preaddestrato e contesto"),
                ("Calcolo", "modello, retrieval, strumenti e policy"),
                ("Output", "risposta o azione controllata"),
            ],
            "Il modello è una base; il comportamento appartiene al sistema.",
        ),
    ]

    x_positions = [45, 485, 925, 1365]
    panel_width = 390
    top = 315
    bottom = 830
    for start_x, specification in zip(x_positions, panel_specs):
        number, heading, color, fill, rows, note = specification
        panel = (start_x, top, start_x + panel_width, bottom)
        rounded(draw, panel, 24, C["white"], color, 4)
        rounded(draw, (start_x + 16, top + 16, start_x + panel_width - 16, top + 90), 18, fill, color, 3)
        draw.ellipse((start_x + 30, top + 28, start_x + 80, top + 78), fill=color)
        number_font = font(22, True)
        number_width, number_height = text_size(draw, number, number_font)
        draw.text((start_x + 55 - number_width / 2, top + 53 - number_height / 2), number, font=number_font, fill=C["white"])
        draw_centered_multiline(
            draw,
            (start_x + 92, top + 25, start_x + panel_width - 24, top + 82),
            heading,
            font(19, True),
            color,
            spacing=2,
            max_lines=3,
        )

        row_y = top + 125
        for row_title, row_text in rows:
            rounded(draw, (start_x + 24, row_y, start_x + panel_width - 24, row_y + 92), 16, fill, color, 2)
            draw.text((start_x + 42, row_y + 12), row_title, font=font(16, True), fill=color)
            draw_left_wrapped(
                draw,
                (start_x + 42, row_y + 39, start_x + panel_width - 42, row_y + 84),
                row_text,
                15,
                fill=C["text"],
                spacing=2,
                max_lines=3,
            )
            row_y += 108

        note_box = (start_x + 24, bottom - 82, start_x + panel_width - 24, bottom - 22)
        rounded(draw, note_box, 16, C["white"], color, 2)
        draw_centered_multiline(
            draw,
            (note_box[0] + 12, note_box[1] + 6, note_box[2] - 12, note_box[3] - 6),
            note,
            font(15, True),
            color,
            spacing=2,
            max_lines=3,
        )
        arrow(draw, (900, 235), (start_x + panel_width / 2, top - 8), fill=color, width=4, head=12)

    footer = (215, 865, 1585, 955)
    rounded(draw, footer, 22, C["amber_fill"], C["amber"], 3)
    draw.ellipse((250, 880, 306, 936), fill="#F59E0B")
    draw.text((271, 891), "i", font=font(29, True), fill=C["white"])
    draw_centered_multiline(
        draw,
        (335, 878, 1545, 940),
        "I paradigmi non si escludono: una sola applicazione può usare un modello appreso, ricerca, regole, retrieval e strumenti.",
        font(22, True),
        C["text"],
        spacing=4,
        max_lines=2,
    )

    return save_png(image, ROOT / "assets/chapters/02_history/HIST-02/candidate-v1.png")


def main() -> None:
    for path in [make_hist01(), make_hist02()]:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
