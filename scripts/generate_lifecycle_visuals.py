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
)

ROOT = Path(__file__).resolve().parents[1]


def phase_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    number: str,
    title: str,
    artifact: str,
    color: str,
    fill: str,
) -> None:
    rounded(draw, box, 20, C["white"], color, 3)
    x0, y0, x1, y1 = box
    rounded(draw, (x0 + 14, y0 + 14, x1 - 14, y0 + 74), 16, fill, color, 2)
    draw.ellipse((x0 + 26, y0 + 25, x0 + 68, y0 + 67), fill=color)
    number_font = font(18, True)
    number_width, number_height = text_size(draw, number, number_font)
    draw.text((x0 + 47 - number_width / 2, y0 + 46 - number_height / 2), number, font=number_font, fill=C["white"])
    draw_centered_multiline(
        draw,
        (x0 + 82, y0 + 20, x1 - 22, y0 + 68),
        title,
        font(19, True),
        color,
        spacing=2,
        max_lines=2,
    )
    draw.text((x0 + 24, y0 + 97), "ARTEFATTO", font=font(14, True), fill=C["muted"])
    rounded(draw, (x0 + 20, y0 + 125, x1 - 20, y1 - 20), 15, C["neutral_fill"], C["neutral"], 2)
    draw_centered_multiline(
        draw,
        (x0 + 36, y0 + 135, x1 - 36, y1 - 30),
        artifact,
        font(16, True),
        C["text"],
        spacing=3,
        max_lines=4,
    )


def make_life01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "LIFE-01 · Ciclo di vita e artefatti verificabili",
        "Ogni fase produce decisioni e versioni; il deployment non conclude il processo",
        width,
    )

    card_width = 370
    card_height = 235
    top_y = 175
    bottom_y = 520
    x_positions = [55, 485, 915, 1345]
    top_specs = [
        ("1", "Definire il problema", "specifica, utenti, azioni consentite", C["blue"], C["blue_fill"]),
        ("2", "Costruire i dati", "dataset, schema, datasheet e versione", C["purple"], C["purple_fill"]),
        ("3", "Addestrare", "configurazione, log, ambiente e checkpoint", C["green"], C["green_fill"]),
        ("4", "Valutare", "baseline, metriche, slice e model card", C["amber"], C["amber_fill"]),
    ]
    bottom_specs = [
        ("8", "Aggiornare o ritirare", "rollback, nuova versione o record di ritiro", C["red"], C["red_fill"]),
        ("7", "Monitorare", "telemetria, feedback, incidenti e soglie", C["purple"], C["purple_fill"]),
        ("6", "Distribuire", "release identificabile e configurazione", C["blue"], C["blue_fill"]),
        ("5", "Integrare il sistema", "prompt, retrieval, tool, policy e interfacce", C["green"], C["green_fill"]),
    ]

    top_boxes = []
    bottom_boxes = []
    for x, spec in zip(x_positions, top_specs):
        box = (x, top_y, x + card_width, top_y + card_height)
        phase_box(draw, box, *spec)
        top_boxes.append(box)
    for x, spec in zip(x_positions, bottom_specs):
        box = (x, bottom_y, x + card_width, bottom_y + card_height)
        phase_box(draw, box, *spec)
        bottom_boxes.append(box)

    for first, second in zip(top_boxes, top_boxes[1:]):
        arrow(draw, (first[2] + 5, (first[1] + first[3]) / 2), (second[0] - 8, (second[1] + second[3]) / 2), width=5, head=13)
    arrow(draw, ((top_boxes[-1][0] + top_boxes[-1][2]) / 2, top_boxes[-1][3] + 6), ((bottom_boxes[-1][0] + bottom_boxes[-1][2]) / 2, bottom_boxes[-1][1] - 8), width=5, head=13)
    for first, second in zip(reversed(bottom_boxes[1:]), reversed(bottom_boxes[:-1])):
        arrow(draw, (first[0] - 5, (first[1] + first[3]) / 2), (second[2] + 8, (second[1] + second[3]) / 2), width=5, head=13)
    arrow(draw, ((bottom_boxes[0][0] + bottom_boxes[0][2]) / 2, bottom_boxes[0][1] - 8), ((top_boxes[0][0] + top_boxes[0][2]) / 2, top_boxes[0][3] + 8), fill=C["red"], width=5, head=13)

    footer = (190, 805, 1610, 945)
    rounded(draw, footer, 24, C["amber_fill"], C["amber"], 3)
    draw.ellipse((225, 835, 285, 895), fill="#F59E0B")
    draw.text((247, 846), "i", font=font(31, True), fill=C["white"])
    draw_centered_multiline(
        draw,
        (315, 820, 1570, 920),
        "Il feedback osservato in produzione non diventa automaticamente dato di training: deve essere verificato, versionato e ricondotto al problema corretto.",
        font(22, True),
        C["text"],
        spacing=4,
        max_lines=3,
    )

    return save_png(image, ROOT / "assets/chapters/03_lifecycle/LIFE-01/candidate-v1.png")


def component_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    subtitle: str,
    color: str,
    fill: str,
) -> None:
    rounded(draw, box, 18, fill, color, 3)
    x0, y0, x1, y1 = box
    draw_centered_multiline(draw, (x0 + 14, y0 + 10, x1 - 14, y0 + 48), title, font(18, True), color, spacing=2, max_lines=2)
    draw_centered_multiline(draw, (x0 + 14, y0 + 47, x1 - 14, y1 - 10), subtitle, font(15), C["text"], spacing=3, max_lines=3)


def make_life02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "LIFE-02 · Il modello è un componente del sistema",
        "Il checkpoint può restare identico mentre cambiano dati, strumenti, regole, interfacce e monitoraggio",
        width,
    )

    system = (120, 145, 1680, 830)
    rounded(draw, system, 32, C["white"], C["neutral"], 4)
    draw.text((160, 168), "CONFINE DEL SISTEMA", font=font(19, True), fill=C["muted"])

    model = (715, 360, 1085, 610)
    rounded(draw, model, 28, C["purple_fill"], C["purple"], 4)
    draw_centered_multiline(draw, (755, 390, 1045, 455), "MODELLO", font(28, True), C["purple"], max_lines=1)
    draw_centered_multiline(draw, (755, 455, 1045, 535), "checkpoint\nparametri θ", font(24, True), C["text"], spacing=6, max_lines=2)
    rounded(draw, (775, 548, 1025, 590), 14, C["white"], C["purple"], 2)
    draw_centered_multiline(draw, (790, 552, 1010, 586), "inference", font(17, True), C["purple"], max_lines=1)

    components = [
        ((180, 270, 470, 385), "Input e validazione", "schema, filtri e normalizzazione", C["blue"], C["blue_fill"]),
        ((180, 465, 470, 580), "Prompt e configurazione", "istruzioni, soglie e template", C["blue"], C["blue_fill"]),
        ((180, 660, 470, 775), "Retrieval e dati esterni", "ordini, documenti e contesto aggiornato", C["green"], C["green_fill"]),
        ((1330, 270, 1620, 385), "Strumenti", "API e azioni su servizi esterni", C["green"], C["green_fill"]),
        ((1330, 465, 1620, 580), "Regole e autorizzazioni", "policy, limiti e intervento umano", C["red"], C["red_fill"]),
        ((1330, 660, 1620, 775), "Output e interfaccia", "post-processing, formato e consegna", C["blue"], C["blue_fill"]),
        ((640, 190, 1160, 290), "Versione distribuita", "codice + configurazione + checkpoint + dipendenze", C["amber"], C["amber_fill"]),
        ((640, 690, 1160, 790), "Telemetria e monitoraggio", "input, output, latenza, costi, feedback e incidenti", C["amber"], C["amber_fill"]),
    ]
    for box, title, subtitle, color, fill in components:
        component_box(draw, box, title, subtitle, color, fill)

    arrow(draw, (470, 327), (705, 420), fill=C["blue"], width=5, head=13)
    arrow(draw, (470, 522), (705, 480), fill=C["blue"], width=5, head=13)
    arrow(draw, (470, 717), (705, 550), fill=C["green"], width=5, head=13)
    arrow(draw, (1095, 420), (1320, 327), fill=C["green"], width=5, head=13)
    arrow(draw, (1095, 480), (1320, 522), fill=C["red"], width=5, head=13)
    arrow(draw, (1095, 550), (1320, 717), fill=C["blue"], width=5, head=13)
    arrow(draw, (900, 300), (900, 350), fill=C["amber"], width=5, head=13)
    arrow(draw, (900, 620), (900, 680), fill=C["amber"], width=5, head=13)

    footer = (250, 860, 1550, 950)
    rounded(draw, footer, 22, C["amber_fill"], C["amber"], 3)
    draw.ellipse((285, 876, 343, 934), fill="#F59E0B")
    draw.text((307, 887), "i", font=font(30, True), fill=C["white"])
    draw_centered_multiline(
        draw,
        (375, 874, 1510, 938),
        "Una modifica fuori dal modello può cambiare il comportamento osservato senza cambiare il checkpoint.",
        font(23, True),
        C["text"],
        spacing=4,
        max_lines=2,
    )

    return save_png(image, ROOT / "assets/chapters/03_lifecycle/LIFE-02/candidate-v1.png")


def main() -> None:
    for path in [make_life01(), make_life02()]:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
