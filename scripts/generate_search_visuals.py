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


def state_node(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    label: str,
    *,
    color: str,
    fill: str,
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


def cost_label(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    text: str,
    color: str,
) -> None:
    x, y = center
    rounded(draw, (x - 24, y - 18, x + 24, y + 18), 9, C["white"], color, 2)
    draw_centered_multiline(
        draw,
        (x - 18, y - 13, x + 18, y + 13),
        text,
        font(13, True),
        C["text"],
        max_lines=1,
    )


def routed_edge(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[int, int]],
    cost: str,
    label_center: tuple[int, int],
    *,
    color: str,
    width: int = 3,
) -> None:
    for start, end in zip(points, points[1:-1]):
        draw.line((*start, *end), fill=color, width=width)
    arrow(draw, points[-2], points[-1], fill=color, width=width, head=11)
    cost_label(draw, label_center, cost, color)


def direct_edge(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    cost: str,
    *,
    color: str,
    width: int,
    label_offset: tuple[int, int] = (0, 0),
) -> None:
    arrow(draw, start, end, fill=color, width=width, head=11)
    x = int((start[0] + end[0]) / 2 + label_offset[0])
    y = int((start[1] + end[1]) / 2 + label_offset[1])
    cost_label(draw, (x, y), cost, color)


def make_search01() -> Path:
    width, height = 1800, 1000
    image = Image.new("RGB", (width, height), C["white"])
    draw = ImageDraw.Draw(image)
    title_block(
        draw,
        "SEARCH-01 · Uniform-cost e A* sullo stesso grafo",
        "Stesso piano ottimo di costo 6; l'euristica consistente evita tre espansioni nel caso illustrativo",
        width,
    )

    rounded(draw, (35, 145, 1400, 925), 28, C["white"], C["neutral"], 3)
    draw.text((65, 165), "SPAZIO DEGLI STATI", font=font(18, True), fill=C["muted"])

    positions = {
        "message_received": (155, 505),
        "order_identified": (430, 245),
        "payment_inspected": (430, 505),
        "agent_asked": (430, 765),
        "tracking_checked": (720, 245),
        "payment_ok": (720, 505),
        "delay_confirmed": (1010, 245),
        "ticket_opened": (1260, 505),
    }
    optimal = {
        "message_received",
        "order_identified",
        "tracking_checked",
        "delay_confirmed",
        "ticket_opened",
    }

    boxes: dict[str, tuple[int, int, int, int]] = {}
    for state, center in positions.items():
        if state == "ticket_opened":
            boxes[state] = state_node(
                draw,
                center,
                state,
                color=C["green"],
                fill=C["green_fill"],
                width=200,
            )
        elif state in optimal:
            boxes[state] = state_node(
                draw,
                center,
                state,
                color=C["blue"],
                fill=C["blue_fill"],
            )
        else:
            boxes[state] = state_node(
                draw,
                center,
                state,
                color=C["muted"],
                fill=C["neutral_fill"],
            )

    def right(state: str) -> tuple[int, int]:
        box = boxes[state]
        return box[2] + 4, int((box[1] + box[3]) / 2)

    def left(state: str) -> tuple[int, int]:
        box = boxes[state]
        return box[0] - 4, int((box[1] + box[3]) / 2)

    routed_edge(
        draw,
        [right("message_received"), (300, 620), (1120, 620), left("ticket_opened")],
        "7",
        (709, 621),
        color=C["amber"],
    )
    routed_edge(
        draw,
        [right("order_identified"), (570, 165), (1150, 165), (boxes["ticket_opened"][0] - 4, boxes["ticket_opened"][1] + 12)],
        "6",
        (864, 165),
        color=C["neutral"],
    )
    routed_edge(
        draw,
        [right("payment_inspected"), (820, 560), (1120, 560), (boxes["ticket_opened"][0] - 4, boxes["ticket_opened"][1] + 25)],
        "12",
        (959, 560),
        color=C["neutral"],
    )
    routed_edge(
        draw,
        [right("agent_asked"), (800, 780), (1110, 780), (boxes["ticket_opened"][0] - 4, boxes["ticket_opened"][3] - 14)],
        "8",
        (954, 780),
        color=C["neutral"],
    )

    direct_edge(
        draw,
        right("payment_ok"),
        left("ticket_opened"),
        "10",
        color=C["neutral"],
        width=3,
        label_offset=(0, -18),
    )

    main_edges = [
        ("message_received", "order_identified", "1", C["green"], (0, -14)),
        ("message_received", "payment_inspected", "1", C["neutral"], (0, -16)),
        ("message_received", "agent_asked", "2", C["neutral"], (0, 14)),
        ("order_identified", "tracking_checked", "2", C["green"], (0, -16)),
        ("tracking_checked", "delay_confirmed", "1", C["green"], (0, -16)),
        ("delay_confirmed", "ticket_opened", "2", C["green"], (0, -22)),
        ("payment_inspected", "payment_ok", "1", C["neutral"], (0, -16)),
    ]
    for source, destination, cost, color, offset in main_edges:
        direct_edge(
            draw,
            right(source),
            left(destination),
            cost,
            color=color,
            width=5 if color == C["green"] else 3,
            label_offset=offset,
        )

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
    draw_centered_multiline(
        draw,
        (1455, 170, 1740, 220),
        "ORDINE DI ESPANSIONE",
        font(18, True),
        C["text"],
        max_lines=1,
    )

    rounded(draw, (1460, 250, 1735, 520), 18, C["neutral_fill"], C["muted"], 2)
    draw_centered_multiline(
        draw,
        (1480, 265, 1715, 315),
        "UNIFORM-COST · 8",
        font(17, True),
        C["muted"],
        max_lines=1,
    )
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
    draw_centered_multiline(
        draw,
        (1480, 580, 1715, 630),
        "A* · 5",
        font(17, True),
        C["blue"],
        max_lines=1,
    )
    draw_centered_multiline(
        draw,
        (1480, 650, 1715, 805),
        "message_received\norder_identified\ntracking_checked\ndelay_confirmed\nticket_opened",
        font(14, True),
        C["text"],
        spacing=7,
        max_lines=5,
    )

    return save_png(
        image,
        ROOT / "assets/chapters/10_search_planning/SEARCH-01/candidate-v2.png",
    )


def game_node(
    draw: ImageDraw.ImageDraw,
    center: tuple[int, int],
    label: str,
    color: str,
    fill: str,
) -> tuple[int, int, int, int]:
    x, y = center
    box = (x - 82, y - 38, x + 82, y + 38)
    rounded(draw, box, 18, fill, color, 3)
    draw_centered_multiline(
        draw,
        (box[0] + 10, box[1] + 8, box[2] - 10, box[3] - 8),
        label,
        font(17, True),
        color,
        max_lines=1,
    )
    return box


def dashed_line(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str,
    *,
    width: int = 3,
    segments: int = 12,
) -> None:
    x0, y0 = start
    x1, y1 = end
    for index in range(segments):
        if index % 2:
            continue
        t0 = index / segments
        t1 = (index + 1) / segments
        draw.line(
            (
                x0 + (x1 - x0) * t0,
                y0 + (y1 - y0) * t0,
                x0 + (x1 - x0) * t1,
                y0 + (y1 - y0) * t1,
            ),
            fill=color,
            width=width,
        )


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

    root = game_node(draw, (900, 210), "MAX · 4", C["blue"], C["blue_fill"])
    children = {
        "A": game_node(draw, (430, 470), "A · MIN · 3", C["purple"], C["purple_fill"]),
        "B": game_node(draw, (900, 470), "B · MIN · 2", C["purple"], C["purple_fill"]),
        "C": game_node(draw, (1370, 470), "C · MIN · 4", C["purple"], C["purple_fill"]),
    }

    for child in children.values():
        arrow(
            draw,
            (900, root[3] + 4),
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
    parent_map = {
        "A1": "A",
        "A2": "A",
        "B1": "B",
        "B2": "B",
        "C1": "C",
        "C2": "C",
    }

    for name, (x, y, value, pruned) in leaves.items():
        parent = children[parent_map[name]]
        parent_bottom = (int((parent[0] + parent[2]) / 2), parent[3] + 4)
        if not pruned:
            arrow(
                draw,
                parent_bottom,
                (x, y - 44),
                fill=C["neutral"],
                width=3,
                head=10,
            )
            game_node(draw, (x, y), value, C["green"], C["green_fill"])
            continue

        dashed_line(draw, parent_bottom, (x, y - 44), C["red"])
        rounded(draw, (905, 545, 1075, 588), 10, C["white"], C["red"], 2)
        draw_centered_multiline(
            draw,
            (915, 551, 1065, 582),
            "ramo potato",
            font(13, True),
            C["red"],
            max_lines=1,
        )
        rounded(draw, (948, 697, 1112, 773), 18, C["red_fill"], C["red"], 3)
        draw.line((958, 707, 990, 739), fill=C["red"], width=5)
        draw.line((990, 707, 958, 739), fill=C["red"], width=5)
        draw.line((1070, 731, 1102, 763), fill=C["red"], width=5)
        draw.line((1102, 731, 1070, 763), fill=C["red"], width=5)
        rounded(draw, (1000, 714, 1060, 756), 10, C["white"], C["red"], 2)
        draw_centered_multiline(
            draw,
            (1006, 719, 1054, 751),
            value,
            font(19, True),
            C["red"],
            max_lines=1,
        )

    rounded(draw, (650, 835, 1150, 920), 18, C["red_fill"], C["red"], 2)
    draw_centered_multiline(
        draw,
        (680, 848, 1120, 907),
        "Dopo A, α = 3. In B, MIN trova 2: la foglia 9 non può migliorare la scelta di MAX.",
        font(16, True),
        C["text"],
        max_lines=3,
    )

    rounded(draw, (120, 850, 535, 915), 15, C["blue_fill"], C["blue"], 2)
    draw_centered_multiline(
        draw,
        (140, 858, 515, 907),
        "minimax: 6 foglie",
        font(16, True),
        C["blue"],
        max_lines=1,
    )
    rounded(draw, (1265, 850, 1680, 915), 15, C["green_fill"], C["green"], 2)
    draw_centered_multiline(
        draw,
        (1285, 858, 1660, 907),
        "alpha-beta: 5 foglie",
        font(16, True),
        C["green"],
        max_lines=1,
    )

    return save_png(
        image,
        ROOT / "assets/chapters/10_search_planning/SEARCH-02/candidate-v2.png",
    )


def main() -> None:
    for path in [make_search01(), make_search02()]:
        with Image.open(path) as image:
            print(
                f"{path.relative_to(ROOT)}: "
                f"{image.size[0]}x{image.size[1]}, {path.stat().st_size} bytes"
            )


if __name__ == "__main__":
    main()
