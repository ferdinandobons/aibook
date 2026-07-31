from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw

from generate_book_visuals import C, arrow, draw_centered_multiline, font, rounded, save_png, title_block

ROOT = Path(__file__).resolve().parents[1]


def node(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    label: str,
    *,
    color: str = C["blue"],
    fill: str = C["blue_fill"],
    width: int = 210,
    height: int = 72,
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


def edge(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    cost: str,
    *,
    color: str = C["neutral"],
    width: int = 3,
    label_offset: tuple[int, int] = (0, 0),
) -> None:
    arrow(draw, start, end, fill=color, width=width, head=11)
    mx = int((start[0] + end[0]) / 2 + label_offset[0])
    my = int((start[1] + end[1]) / 2 + label_offset[1])
    rounded(draw, (mx - 24, my - 18, mx + 24, my + 18), 9, C["white"], color, 2)
    draw_centered_multiline(draw, (mx - 18, my - 13, mx + 18, my + 13), cost, font(13, True), C["text"], max_lines=1)


def make_search01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "SEARCH-01 · Uniform-cost e A* sullo stesso grafo",
        "Stesso piano ottimo di costo 6; la euristica consistente evita tre espansioni nel caso illustrativo",
        width,
    )

    rounded(draw, (35, 145, 1400, 925), 28, C["white"], C["neutral"], 3)
    draw.text((65, 165), "SPAZIO DEGLI STATI", font=font(18, True), fill=C["muted"])

    positions = {
        "message_received": (145, 505),
        "order_identified": (425, 250),
        "payment_inspected": (425, 505),
        "agent_asked": (425, 760),
        "tracking_checked": (720, 250),
        "payment_ok": (720, 505),
        "delay_confirmed": (1015, 250),
        "ticket_opened": (1280, 505),
    }

    optimal = {"message_received", "order_identified", "tracking_checked", "delay_confirmed", "ticket_opened"}
    boxes = {}
    for state, center in positions.items():
        if state == "ticket_opened":
            boxes[state] = node(draw, center, state, color=C["green"], fill=C["green_fill"])
        elif state in optimal:
            boxes[state] = node(draw, center, state, color=C["blue"], fill=C["blue_fill"])
        else:
            boxes[state] = node(draw, center, state, color=C["muted"], fill=C["neutral_fill"])

    def right(state: str) -> tuple[int, int]:
        b = boxes[state]
        return b[2] + 4, int((b[1] + b[3]) / 2)

    def left(state: str) -> tuple[int, int]:
        b = boxes[state]
        return b[0] - 4, int((b[1] + b[3]) / 2)

    def top(state: str) -> tuple[int, int]:
        b = boxes[state]
        return int((b[0] + b[2]) / 2), b[1] - 4

    edges = [
        ("message_received", "order_identified", "1", C["green"], (0, -14)),
        ("message_received", "payment_inspected", "1", C["neutral"], (0, -16)),
        ("message_received", "agent_asked", "2", C["neutral"], (0, 14)),
        ("order_identified", "tracking_checked", "2", C["green"], (0, -16)),
        ("tracking_checked", "delay_confirmed", "1", C["green"], (0, -16)),
        ("delay_confirmed", "ticket_opened", "2", C["green"], (0, -18)),
        ("payment_inspected", "payment_ok", "1", C["neutral"], (0, -16)),
        ("payment_ok", "ticket_opened", "10", C["neutral"], (0, 18)),
        ("agent_asked", "ticket_opened", "8", C["neutral"], (0, 18)),
    ]
    for source, destination, cost, color, offset in edges:
        edge(draw, right(source), left(destination), cost, color=color, width=5 if color == C["green"] else 3, label_offset=offset)

    edge(draw, right("message_received"), left("ticket_opened"), "7", color=C["amber"], width=3, label_offset=(0, 40))
    edge(draw, right("order_identified"), left("ticket_opened"), "6", color=C["neutral"], width=3, label_offset=(0, -55))
    edge(draw, right("tracking_checked"), left("ticket_opened"), "5", color=C["neutral"], width=3, label_offset=(0, -38))
    edge(draw, right("payment_inspected"), left("ticket_opened"), "12", color=C["neutral"], width=3, label_offset=(0, 50))

    rounded(draw, (65, 840, 1345, 900), 15, C["green_fill"], C["green"], 2)
    draw_centered_multiline(
        draw,
        (90, 848, 1320, 892),
        "Piano ottimo: identify_order → check_tracking → confirm_delay → open_delay_ticket · costo 6",
        font(16, True),
        C["green"],
        max_lines=1,
    )

    rounded(draw, (1430, 145, 1765, 925), 28, C["white"], C["neutral"], 3)
    draw_centered_multiline(draw, (1455, 170, 1740, 220), "ORDINE DI ESPANSIONE", font(18, True), C["text"], max_lines=1)

    rounded(draw, (1460, 250, 1735, 520), 18, C["neutral_fill"], C["muted"], 2)
    draw_centered_multiline(draw, (1480, 265, 1715, 315), "UNIFORM-COST · 8", font(17, True), C["muted"], max_lines=1)
    draw_centered_multiline(
        draw,
        (1480, 330, 1715, 495),
        "message_received\norder_identified\npayment_inspected\nagent_asked\npayment_ok\ntracking_checked\ndelay_confirmed\nticket_opened",
        font(13, True),
        C["text"],
        spacing=4,
        max_lines=8,
    )

    rounded(draw, (1460, 565, 1735, 835), 18, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(draw, (1480, 580, 1715, 630), "A* · 5", font(17, True), C["blue"], max_lines=1)
    draw_centered_multiline(
        draw,
        (1480, 650, 1715, 805),
        "message_received\norder_identified\ntracking_checked\ndelay_confirmed\nticket_opened",
        font(14, True),
        C["text"],
        spacing=7,
        max_lines=5,
    )

    return save_png(image, ROOT / "assets/chapters/10_search_planning/SEARCH-01/candidate-v1.png")


def tree_node(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    label: str,
    color: str,
    fill: str,
) -> tuple[int, int, int, int]:
    x, y = center
    box = (x - 82, y - 38, x + 82, y + 38)
    rounded(draw, box, 18, fill, color, 3)
    draw_centered_multiline(draw, (box[0] + 10, box[1] + 8, box[2] - 10, box[3] - 8), label, font(17, True), color, max_lines=1)
    return box


def make_search02() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "SEARCH-02 · Minimax e potatura alpha-beta",
        "La potatura evita una foglia che non può cambiare il valore della radice MAX",
        width,
    )

    root = tree_node(draw, (900, 210), "MAX · 4", C["blue"], C["blue_fill"])
    children = {
        "A": tree_node(draw, (430, 470), "A · MIN · 3", C["purple"], C["purple_fill"]),
        "B": tree_node(draw, (900, 470), "B · MIN · 2", C["purple"], C["purple_fill"]),
        "C": tree_node(draw, (1370, 470), "C · MIN · 4", C["purple"], C["purple_fill"]),
    }

    for child in children.values():
        arrow(
            draw,
            (int((root[0] + root[2]) / 2), root[3] + 4),
            (int((child[0] + child[2]) / 2), child[1] - 6),
            fill=C["neutral"],
            width=4,
            head=12,
        )

    leaves = {
        "A1": (300, 735, "3", False),
        "A2": (560, 735, "5", False),
        "B1": (770, 735, "2", False),
        "B2": (1030, 735, "9", True),
        "C1": (1240, 735, "4", False),
        "C2": (1500, 735, "4", False),
    }
    parent_map = {"A1": "A", "A2": "A", "B1": "B", "B2": "B", "C1": "C", "C2": "C"}

    leaf_boxes = {}
    for name, (x, y, value, pruned) in leaves.items():
        color = C["red"] if pruned else C["green"]
        fill = C["red_fill"] if pruned else C["green_fill"]
        leaf_boxes[name] = tree_node(draw, (x, y), value, color, fill)
        parent = children[parent_map[name]]
        if pruned:
            draw.line(
                (int((parent[0] + parent[2]) / 2), parent[3] + 4, x, y - 44),
                fill=C["red"],
                width=3,
            )
            draw.line((x - 34, y - 34, x + 34, y + 34), fill=C["red"], width=6)
            draw.line((x + 34, y - 34, x - 34, y + 34), fill=C["red"], width=6)
        else:
            arrow(
                draw,
                (int((parent[0] + parent[2]) / 2), parent[3] + 4),
                (x, y - 44),
                fill=C["neutral"],
                width=3,
                head=10,
            )

    rounded(draw, (650, 835, 1150, 920), 18, C["red_fill"], C["red"], 2)
    draw_centered_multiline(
        draw,
        (680, 848, 1120, 907),
        "Dopo A, alpha = 3. In B, MIN trova 2: la foglia 9 non può migliorare la scelta di MAX.",
        font(16, True),
        C["text"],
        max_lines=3,
    )

    rounded(draw, (120, 850, 535, 915), 15, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(draw, (140, 858, 515, 907), "minimax: 6 foglie", font(16, True), C["blue"], max_lines=1)
    rounded(draw, (1265, 850, 1680, 915), 15, C["green_fill"], C["green"], 2)
    draw_centered_multiline(draw, (1285, 858, 1660, 907), "alpha-beta: 5 foglie", font(16, True), C["green"], max_lines=1)

    return save_png(image, ROOT / "assets/chapters/10_search_planning/SEARCH-02/candidate-v1.png")


def main() -> None:
    for path in [make_search01(), make_search02()]:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
