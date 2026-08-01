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
    left, top, right, bottom = draw.textbbox((0, 0), text, font=selected_font)
    return right - left, bottom - top


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    selected_font: ImageFont.FreeTypeFont,
    max_width: int,
) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if text_size(draw, candidate, selected_font)[0] <= max_width:
            current = candidate
            continue
        if current:
            lines.append(current)
        if text_size(draw, word, selected_font)[0] <= max_width:
            current = word
            continue
        fragment = ""
        for character in word:
            candidate = fragment + character
            if text_size(draw, candidate, selected_font)[0] <= max_width:
                fragment = candidate
            else:
                if fragment:
                    lines.append(fragment)
                fragment = character
        current = fragment
    if current:
        lines.append(current)
    return lines


def draw_centered_multiline(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    selected_font: ImageFont.FreeTypeFont,
    fill: str = C["text"],
    spacing: int = 8,
    max_lines: int | None = None,
) -> None:
    x0, y0, x1, y1 = box
    lines = wrap_text(draw, text, selected_font, x1 - x0)
    if max_lines is not None and len(lines) > max_lines:
        raise ValueError(f"Text exceeds box: {text!r} -> {lines!r}")
    heights = [text_size(draw, line, selected_font)[1] for line in lines]
    total_height = sum(heights) + spacing * max(0, len(lines) - 1)
    y = y0 + (y1 - y0 - total_height) / 2
    for line, line_height in zip(lines, heights):
        line_width, _ = text_size(draw, line, selected_font)
        draw.text((x0 + (x1 - x0 - line_width) / 2, y), line, font=selected_font, fill=fill)
        y += line_height + spacing


def rounded(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    radius: int,
    fill: str,
    outline: str,
    width: int = 3,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[float, float],
    end: tuple[float, float],
    fill: str = C["text"],
    width: int = 5,
    head: int = 14,
) -> None:
    x0, y0 = start
    x1, y1 = end
    draw.line((x0, y0, x1, y1), fill=fill, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    point_1 = (x1 + head * math.cos(angle + math.pi * 0.82), y1 + head * math.sin(angle + math.pi * 0.82))
    point_2 = (x1 + head * math.cos(angle - math.pi * 0.82), y1 + head * math.sin(angle - math.pi * 0.82))
    draw.polygon([end, point_1, point_2], fill=fill)


def elbow_arrow(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[float, float]],
    fill: str = C["text"],
    width: int = 5,
    head: int = 14,
) -> None:
    for first, second in zip(points, points[1:]):
        draw.line((*first, *second), fill=fill, width=width)
    arrow(draw, points[-2], points[-1], fill=fill, width=width, head=head)


def title_block(draw: ImageDraw.ImageDraw, title: str, subtitle: str, width: int) -> None:
    title_font = font(44, True)
    subtitle_font = font(25)
    title_width, _ = text_size(draw, title, title_font)
    subtitle_width, _ = text_size(draw, subtitle, subtitle_font)
    draw.text(((width - title_width) / 2, 25), title, font=title_font, fill=C["text"])
    draw.text(((width - subtitle_width) / 2, 82), subtitle, font=subtitle_font, fill=C["muted"])


def save_png(image: Image.Image, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    quantized = image.convert("RGB").quantize(colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    quantized.save(path, optimize=True)
    with Image.open(path) as check:
        check.verify()
    return path


def make_ai01() -> Path:
    width, height = 1600, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "AI-01 · Tre domande per descrivere un sistema di AI",
        "Meccanismo, obiettivo e ampiezza rispondono a domande diverse",
        width,
    )

    case = (500, 135, 1100, 250)
    rounded(draw, case, 26, C["neutral_fill"], C["neutral"], 3)
    draw.text((545, 156), "CASO GUIDA", font=font(20, True), fill=C["muted"])
    draw_centered_multiline(
        draw,
        (545, 183, 1055, 232),
        "«Il pacco non è arrivato»",
        font(29, True),
        max_lines=2,
    )

    panel_y0, panel_y1 = 335, 825
    x_positions = [50, 550, 1050]
    panel_width = 500
    specifications = [
        (
            "1",
            "MECCANISMO",
            "Come viene costruito il comportamento?",
            C["blue"],
            C["blue_fill"],
            [
                ("Regole esplicite", "La logica viene scritta da persone."),
                ("Modello appreso dai dati", "I parametri vengono scelti usando esempi."),
                ("Sistema ibrido", "Regole, modelli e strumenti collaborano."),
            ],
            "Le categorie possono combinarsi nello stesso sistema.",
        ),
        (
            "2",
            "OBIETTIVO",
            "Che cosa deve produrre o decidere?",
            C["purple"],
            C["purple_fill"],
            [
                ("Classificare o predire", "Sceglie tra possibilità già definite."),
                ("Decidere", "Seleziona un’azione o una raccomandazione."),
                ("Generare contenuto", "Produce testo, immagini, audio o altri dati."),
            ],
            "L’obiettivo non determina il meccanismo.",
        ),
        (
            "3",
            "AMPIEZZA",
            "Per quanti compiti e contesti è pensato?",
            C["green"],
            C["green_fill"],
            [
                ("Specialistico", "È progettato per un compito ristretto."),
                ("Base adattabile", "Può essere riutilizzato dopo un adattamento."),
                ("Generalista", "È valutato su molti compiti e contesti."),
            ],
            "L’ampiezza dipende dal perimetro valutato.",
        ),
    ]

    panel_centers: list[tuple[float, float]] = []
    for x, specification in zip(x_positions, specifications):
        number, heading, question, color, fill, items, note = specification
        panel = (x, panel_y0, x + panel_width, panel_y1)
        rounded(draw, panel, 28, C["white"], color, 4)
        rounded(draw, (x + 18, panel_y0 + 18, x + panel_width - 18, panel_y0 + 86), 20, fill, color, 3)
        draw.ellipse((x + 35, panel_y0 + 28, x + 85, panel_y0 + 78), fill=color)
        number_font = font(23, True)
        number_width, number_height = text_size(draw, number, number_font)
        draw.text((x + 60 - number_width / 2, panel_y0 + 53 - number_height / 2), number, font=number_font, fill=C["white"])
        draw.text((x + 105, panel_y0 + 34), heading, font=font(24, True), fill=color)

        question_y = panel_y0 + 104
        for line in wrap_text(draw, question, font(19), panel_width - 70):
            line_width, line_height = text_size(draw, line, font(19))
            draw.text((x + (panel_width - line_width) / 2, question_y), line, font=font(19), fill=C["muted"])
            question_y += line_height + 3

        item_y = panel_y0 + 166
        for item_title, description in items:
            box = (x + 32, item_y, x + panel_width - 32, item_y + 68)
            rounded(draw, box, 16, fill, color, 2)
            draw.text((x + 50, item_y + 9), item_title, font=font(19, True), fill=C["text"])
            description_y = item_y + 36
            for line in wrap_text(draw, description, font(15), panel_width - 100)[:2]:
                draw.text((x + 50, description_y), line, font=font(15), fill=C["muted"])
                description_y += 18
            item_y += 80

        note_box = (x + 32, panel_y1 - 72, x + panel_width - 32, panel_y1 - 20)
        rounded(draw, note_box, 16, C["white"], color, 2)
        draw_centered_multiline(
            draw,
            (note_box[0] + 12, note_box[1] + 6, note_box[2] - 12, note_box[3] - 6),
            note,
            font(15, True),
            color,
            spacing=2,
            max_lines=2,
        )
        panel_centers.append((x + panel_width / 2, panel_y0))

    for start, center, color in zip(
        [(620, 250), (800, 250), (980, 250)],
        panel_centers,
        [C["blue"], C["purple"], C["green"]],
    ):
        elbow_arrow(
            draw,
            [start, (start[0], 300), (center[0], 300), (center[0], panel_y0 - 8)],
            fill=color,
            width=5,
            head=14,
        )

    footer = (210, 855, 1390, 955)
    rounded(draw, footer, 24, C["amber_fill"], C["amber"], 3)
    draw.ellipse((245, 875, 305, 935), fill="#F59E0B")
    draw.text((266, 886), "i", font=font(31, True), fill=C["white"])
    draw_centered_multiline(
        draw,
        (335, 870, 1350, 940),
        "I tre aspetti possono combinarsi: nessuno determina automaticamente gli altri.",
        font(24, True),
        max_lines=2,
    )

    return save_png(image, ROOT / "assets/chapters/01_ai_field/AI-01/candidate-v1.png")


def make_ai02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "AI-02 · Training e inference usano il modello in fasi diverse",
        "L’optimizer aggiorna i parametri nel training; l’inference usa il checkpoint disponibile",
        width,
    )

    left = (40, 145, 1195, 825)
    right = (1225, 145, 1760, 825)
    rounded(draw, left, 28, C["white"], C["green"], 4)
    rounded(draw, right, 28, C["white"], C["blue"], 4)

    rounded(draw, (62, 165, 1173, 235), 20, C["green_fill"], C["green"], 3)
    draw.text((92, 183), "TRAINING", font=font(28, True), fill=C["green"])
    draw.text((275, 188), "i parametri cambiano", font=font(21), fill=C["muted"])
    rounded(draw, (1247, 165, 1738, 235), 20, C["blue_fill"], C["blue"], 3)
    draw.text((1277, 183), "INFERENCE", font=font(28, True), fill=C["blue"])
    draw.text((1490, 188), "parametri invariati", font=font(18), fill=C["muted"])

    top_y = 295
    nodes = [
        (75, top_y, 260, top_y + 108, "1", "Dati di training", "input + target", C["blue"], C["blue_fill"]),
        (330, top_y, 515, top_y + 108, "2", "Modello", "parametri θ", C["purple"], C["purple_fill"]),
        (585, top_y, 770, top_y + 108, "3", "Output", "predizioni", C["green"], C["green_fill"]),
        (840, top_y, 1085, top_y + 108, "4", "Loss", "confronto con i target", C["amber"], C["amber_fill"]),
    ]
    centers: list[tuple[float, float]] = []
    for x0, y0, x1, y1, number, title, subtitle, color, fill in nodes:
        rounded(draw, (x0, y0, x1, y1), 18, fill, color, 3)
        draw.ellipse((x0 + 12, y0 + 12, x0 + 54, y0 + 54), fill=color)
        number_font = font(18, True)
        number_width, number_height = text_size(draw, number, number_font)
        draw.text((x0 + 33 - number_width / 2, y0 + 33 - number_height / 2), number, font=number_font, fill=C["white"])
        draw_centered_multiline(draw, (x0 + 20, y0 + 13, x1 - 20, y0 + 62), title, font(20, True), max_lines=2)
        draw_centered_multiline(draw, (x0 + 18, y0 + 61, x1 - 18, y1 - 10), subtitle, font(16), C["muted"], spacing=2, max_lines=2)
        centers.append(((x0 + x1) / 2, (y0 + y1) / 2))
    for first, second in zip(centers, centers[1:]):
        arrow(draw, (first[0] + 93, first[1]), (second[0] - 93, second[1]), width=5, head=13)

    target_box = (865, 450, 1060, 520)
    rounded(draw, target_box, 16, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(draw, (880, 460, 1045, 510), "Target corretti", font(18, True), C["blue"], spacing=2, max_lines=2)
    arrow(draw, (962, 450), (962, 411), fill=C["blue"], width=4, head=12)

    lower_y = 585
    lower_nodes = [
        (625, lower_y, 810, lower_y + 105, "5", "Gradienti", "direzione di modifica", C["amber"], C["amber_fill"]),
        (875, lower_y, 1085, lower_y + 105, "6", "Optimizer step", "aggiorna i parametri", C["amber"], C["amber_fill"]),
        (315, lower_y, 545, lower_y + 105, "θ → θ′", "Parametri aggiornati", "nuovo checkpoint", C["green"], C["green_fill"]),
    ]
    for x0, y0, x1, y1, number, title, subtitle, color, fill in lower_nodes:
        rounded(draw, (x0, y0, x1, y1), 18, fill, color, 3)
        draw.text((x0 + 16, y0 + 12), number, font=font(18, True), fill=color)
        draw_centered_multiline(draw, (x0 + 20, y0 + 28, x1 - 20, y0 + 70), title, font(19, True), max_lines=2)
        draw_centered_multiline(draw, (x0 + 18, y0 + 67, x1 - 18, y1 - 8), subtitle, font(15), C["muted"], spacing=2, max_lines=2)

    elbow_arrow(draw, [(962, 403), (962, 545), (718, 545), (718, 577)], fill=C["amber"], width=5, head=13)
    arrow(draw, (810, 638), (867, 638), fill=C["amber"], width=5, head=13)
    elbow_arrow(draw, [(980, 690), (980, 740), (430, 740), (430, 698)], fill=C["green"], width=5, head=13)
    elbow_arrow(draw, [(430, 585), (430, 535), (423, 535), (423, 411)], fill=C["green"], width=5, head=13)
    draw.text((590, 752), "Solo l’optimizer modifica θ in θ′.", font=font(18, True), fill=C["green"])

    inference_nodes = [
        (1255, 300, 1395, 412, "Nuovo input", "un caso non visto", C["blue"], C["blue_fill"]),
        (1430, 300, 1585, 412, "Modello", "checkpoint θ′ fissato", C["purple"], C["purple_fill"]),
        (1620, 300, 1730, 412, "Output", "predizione", C["green"], C["green_fill"]),
    ]
    for x0, y0, x1, y1, title, subtitle, color, fill in inference_nodes:
        rounded(draw, (x0, y0, x1, y1), 18, fill, color, 3)
        draw_centered_multiline(draw, (x0 + 10, y0 + 12, x1 - 10, y0 + 58), title, font(18, True), max_lines=2)
        draw_centered_multiline(draw, (x0 + 10, y0 + 58, x1 - 10, y1 - 10), subtitle, font(14), C["muted"], spacing=2, max_lines=2)
    arrow(draw, (1395, 356), (1422, 356), width=5, head=11)
    arrow(draw, (1585, 356), (1612, 356), width=5, head=11)

    absent_box = (1260, 475, 1725, 735)
    rounded(draw, absent_box, 20, C["neutral_fill"], C["neutral"], 2)
    draw.text((1290, 500), "Nel caso base non compaiono:", font=font(20, True), fill=C["text"])
    item_y = 548
    for item in ["target", "loss", "gradienti", "optimizer step"]:
        draw.ellipse((1293, item_y + 3, 1313, item_y + 23), fill=C["red_fill"], outline=C["red"], width=2)
        draw.line((1298, item_y + 8, 1308, item_y + 18), fill=C["red"], width=2)
        draw.line((1308, item_y + 8, 1298, item_y + 18), fill=C["red"], width=2)
        draw.text((1328, item_y), item, font=font(18), fill=C["muted"])
        item_y += 38
    draw.text((1290, 704), "Il modello usa ciò che è stato appreso.", font=font(18, True), fill=C["blue"])

    footer = (250, 855, 1550, 950)
    rounded(draw, footer, 24, C["amber_fill"], C["amber"], 3)
    draw.ellipse((285, 873, 345, 933), fill="#F59E0B")
    draw.text((307, 884), "i", font=font(31, True), fill=C["white"])
    draw_centered_multiline(
        draw,
        (375, 870, 1510, 938),
        "PyTorch: eval() e inference_mode() hanno ruoli distinti; nessuno dei due esegue un optimizer step.",
        font(22, True),
        max_lines=2,
    )

    return save_png(image, ROOT / "assets/chapters/01_ai_field/AI-02/candidate-v1.png")


def make_att01_v3() -> Path:
    source = ROOT / "assets/chapters/28_attention/ATT-01/candidate-v2.png"
    image = Image.open(source).convert("RGB")
    draw = ImageDraw.Draw(image)

    draw.rectangle((35, 125, 685, 785), fill=C["white"])
    rounded(draw, (44, 138, 670, 775), 24, C["white"], C["red"], 3)
    rounded(draw, (64, 158, 650, 204), 12, C["red_fill"], C["red"], 2)
    draw_centered_multiline(
        draw,
        (78, 160, 636, 202),
        "1) Contesto fisso (uguale per tutte le posizioni)",
        font(20, True),
        max_lines=2,
    )
    draw_centered_multiline(
        draw,
        (100, 229, 615, 265),
        "Sequenza sorgente (stessi valori per tutti)",
        font(18, True),
        max_lines=2,
    )

    for box, text in [
        ((98, 276, 239, 357), "v₁\nIl"),
        ((281, 276, 422, 357), "v₂\ngatto"),
        ((464, 276, 605, 357), "v₃\ndorme"),
    ]:
        rounded(draw, box, 12, C["blue_fill"], C["blue"], 2)
        draw_centered_multiline(draw, (box[0] + 10, box[1] + 8, box[2] - 10, box[3] - 8), text, font(19, True), spacing=4, max_lines=2)

    rounded(draw, (190, 435, 513, 551), 16, C["purple_fill"], C["purple"], 3)
    draw_centered_multiline(
        draw,
        (215, 448, 488, 538),
        "Vettore di contesto fisso\nc\n(unico e invariato)",
        font(18, True),
        spacing=4,
        max_lines=3,
    )
    arrow(draw, (168, 358), (263, 431), fill=C["muted"], width=4, head=12)
    arrow(draw, (351, 358), (351, 431), fill=C["muted"], width=4, head=12)
    arrow(draw, (534, 358), (441, 431), fill=C["muted"], width=4, head=12)

    for box, label in [
        ((84, 607, 276, 674), "Posizione 1\n(usa c)"),
        ((397, 607, 589, 674), "Posizione 2\n(usa c)"),
    ]:
        rounded(draw, box, 14, C["green_fill"], C["green"], 2)
        draw_centered_multiline(draw, (box[0] + 10, box[1] + 7, box[2] - 10, box[3] - 7), label, font(18, True), spacing=3, max_lines=2)
    arrow(draw, (248, 552), (180, 602), fill="#B91C1C", width=4, head=12)
    arrow(draw, (455, 552), (493, 602), fill="#B91C1C", width=4, head=12)

    rounded(draw, (80, 707, 635, 754), 12, C["red_fill"], C["red"], 2)
    draw_centered_multiline(
        draw,
        (95, 711, 620, 750),
        "Lo stesso vettore c è riutilizzato da tutte le posizioni.",
        font(17, True),
        "#B91C1C",
        spacing=2,
        max_lines=2,
    )

    draw.rectangle((210, 790, 1410, 920), fill=C["white"])
    rounded(draw, (235, 807, 1395, 900), 20, C["amber_fill"], C["amber"], 2)
    draw.ellipse((262, 826, 318, 882), fill="#F59E0B")
    draw.text((283, 837), "i", font=font(30, True), fill=C["white"])
    draw_centered_multiline(
        draw,
        (345, 820, 1360, 886),
        "Invariante: i valori sorgente v₁, v₂, v₃ non cambiano; cambiano soltanto i pesi usati per combinarli.",
        font(22, True),
        max_lines=2,
    )

    return save_png(image, ROOT / "assets/chapters/28_attention/ATT-01/candidate-v3.png")


def main() -> None:
    generated = [make_ai01(), make_ai02(), make_att01_v3()]
    for path in generated:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
