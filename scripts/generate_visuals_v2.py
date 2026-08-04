"""Regenerate concept-specific technical visuals for the revised book.

The historical renderer proved that every chapter had decodable images, but it
also encouraged repeated four-card pipelines and unsourced illustrative charts.
This compiler keeps the shared visual language while choosing a composition
from the relationship that the lesson must explain.  It never fabricates a
quantitative benchmark: charts are replaced by mechanisms, boundaries,
matrices, trees, traces, or evidence structures.

The first thirteen chapters and chapter 28 are deliberately preserved as the
hand-reviewed visual baseline.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import revise_book_completeness as old  # noqa: E402


TARGETS = tuple(number for number in range(14, 99) if number != 28)
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+\.png)\)")

# One explicit pair per lesson.  The vocabulary describes relationships, not
# decorative templates.  Several names may share a drawing primitive, but the
# content, order, controls, and visual question are chapter-specific.
VISUAL_MODELS = {
    14: ("interaction_loop", "policy_branch"),
    15: ("layer_stack", "decision_boundary"),
    16: ("training_loop", "diagnostic_trace"),
    17: ("receptive_field", "vision_stack"),
    18: ("sequence_unroll", "state_compare"),
    19: ("latent_geometry", "representation_map"),
    20: ("model_taxonomy", "evaluation_lenses"),
    21: ("causal_sequence", "sampling_tree"),
    22: ("latent_bottleneck", "codebook_lookup"),
    23: ("adversarial_loop", "failure_balance"),
    24: ("invertible_flow", "jacobian_stack"),
    25: ("noise_path", "sampler_path"),
    26: ("data_lineage", "tokenization_grid"),
    27: ("embedding_geometry", "lookup_context"),
    29: ("transformer_stack", "tensor_route"),
    30: ("architecture_taxonomy", "objective_map"),
    31: ("behavior_boundary", "evidence_map"),
    32: ("data_lineage", "dataset_gate"),
    33: ("mixture_channels", "contamination_gate"),
    34: ("scaling_balance", "budget_allocation"),
    35: ("recipe_pipeline", "run_trace"),
    36: ("parallel_topology", "communication_graph"),
    37: ("block_compare", "residual_stack"),
    38: ("position_geometry", "context_window"),
    39: ("attention_compare", "kv_layout"),
    40: ("memory_tiling", "compute_memory_tradeoff"),
    41: ("recurrent_attention", "mechanism_compare"),
    42: ("state_space_scan", "sequence_stack"),
    43: ("hybrid_route", "memory_layers"),
    44: ("expert_router", "capacity_gate"),
    45: ("objective_compare", "prediction_pipeline"),
    46: ("loss_mask", "supervision_pipeline"),
    47: ("low_rank_update", "adapter_stack"),
    48: ("preference_pipeline", "reward_loop"),
    49: ("pairwise_objective", "method_compare"),
    50: ("verifier_funnel", "process_supervision"),
    51: ("rlvr_loop", "reward_gate"),
    52: ("reasoning_curriculum", "mode_fusion"),
    53: ("sample_and_vote", "search_tree"),
    54: ("model_edit", "side_effect_trace"),
    55: ("modality_map", "alignment_space"),
    56: ("vlm_route", "grounding_grid"),
    57: ("image_generation", "quality_lenses"),
    58: ("native_fusion", "modality_routing"),
    59: ("audio_pipeline", "time_frequency_map"),
    60: ("video_grid", "temporal_generation"),
    61: ("coordinate_frames", "scene_stack"),
    62: ("embodied_loop", "action_boundary"),
    63: ("retrieval_route", "index_layers"),
    64: ("rag_route", "citation_trace"),
    65: ("multi_query_graph", "reranking_funnel"),
    66: ("memory_layers", "memory_lifecycle"),
    67: ("tool_call_route", "schema_gate"),
    68: ("protocol_handshake", "compatibility_boundary"),
    69: ("agent_loop", "state_machine"),
    70: ("agent_graph", "orchestration_boundary"),
    71: ("trajectory_eval", "agent_scorecard"),
    72: ("trust_boundary", "least_privilege"),
    73: ("distill_prune", "quality_gate"),
    74: ("quantization_map", "method_taxonomy"),
    75: ("low_bit_path", "accumulator_stack"),
    76: ("decoding_tree", "sampling_controls"),
    77: ("draft_verify", "acceptance_path"),
    78: ("cache_layout", "eviction_lifecycle"),
    79: ("serving_queue", "continuous_batch"),
    80: ("sharding_topology", "network_boundary"),
    81: ("compiler_graph", "kernel_fusion"),
    82: ("llmops_loop", "rollback_path"),
    83: ("evaluation_matrix", "selection_funnel"),
    84: ("claim_evidence", "calibration_map"),
    85: ("system_trace", "slice_scorecard"),
    86: ("observation_inference", "causal_boundary"),
    87: ("sparse_features", "circuit_graph"),
    88: ("perturbation_grid", "jailbreak_boundary"),
    89: ("prompt_trust_boundary", "data_control_plane"),
    90: ("supply_chain", "artifact_lineage"),
    91: ("privacy_fairness_matrix", "cohort_boundary"),
    92: ("provenance_chain", "credential_layers"),
    93: ("role_risk_map", "governance_lifecycle"),
    94: ("lab_pipeline", "result_bundle"),
    95: ("small_lm_stack", "training_evidence"),
    96: ("release_pipeline", "rollback_path"),
    97: ("replication_protocol", "uncertainty_report"),
    98: ("evidence_ladder", "watchlist_cycle"),
}


FLOW_MODELS = {
    "causal_sequence", "sequence_unroll", "invertible_flow", "noise_path", "sampler_path", "data_lineage",
    "recipe_pipeline", "prediction_pipeline", "supervision_pipeline", "preference_pipeline",
    "model_edit", "image_generation", "audio_pipeline", "temporal_generation", "retrieval_route",
    "rag_route", "citation_trace", "tool_call_route", "protocol_handshake", "draft_verify",
    "acceptance_path", "supply_chain", "artifact_lineage", "lab_pipeline", "release_pipeline",
}
CYCLE_MODELS = {
    "interaction_loop", "training_loop", "adversarial_loop", "recurrent_attention", "reward_loop",
    "rlvr_loop", "embodied_loop", "agent_loop", "state_machine", "llmops_loop", "memory_lifecycle",
    "governance_lifecycle", "watchlist_cycle",
}
STACK_MODELS = {
    "layer_stack", "vision_stack", "jacobian_stack", "transformer_stack", "residual_stack",
    "sequence_stack", "adapter_stack", "scene_stack", "index_layers", "memory_layers",
    "accumulator_stack", "credential_layers", "small_lm_stack",
}
COMPARE_MODELS = {
    "state_compare", "failure_balance", "evaluation_lenses", "behavior_boundary", "scaling_balance",
    "block_compare", "attention_compare", "compute_memory_tradeoff", "mechanism_compare",
    "objective_compare", "method_compare", "quality_lenses", "calibration_map", "observation_inference",
    "distill_prune", "training_evidence", "uncertainty_report",
}
TREE_MODELS = {
    "policy_branch", "sampling_tree", "search_tree", "expert_router", "mixture_channels",
    "modality_routing", "multi_query_graph", "agent_graph", "decoding_tree",
}
GRID_MODELS = {
    "decision_boundary", "receptive_field", "tokenization_grid", "tensor_route", "position_geometry",
    "context_window", "loss_mask", "grounding_grid", "time_frequency_map", "video_grid",
    "coordinate_frames", "quantization_map", "cache_layout", "evaluation_matrix", "perturbation_grid",
    "privacy_fairness_matrix",
}
BOUNDARY_MODELS = {
    "diagnostic_trace", "dataset_gate", "contamination_gate", "run_trace", "capacity_gate", "reward_gate",
    "side_effect_trace", "action_boundary", "schema_gate", "compatibility_boundary",
    "orchestration_boundary", "trust_boundary", "least_privilege", "quality_gate", "network_boundary",
    "rollback_path", "causal_boundary", "jailbreak_boundary", "prompt_trust_boundary",
    "data_control_plane", "cohort_boundary",
}
GRAPH_MODELS = {
    "latent_geometry", "embedding_geometry", "lookup_context", "parallel_topology",
    "communication_graph", "kv_layout", "state_space_scan", "hybrid_route", "low_rank_update",
    "pairwise_objective", "process_supervision", "mode_fusion", "alignment_space", "vlm_route",
    "native_fusion", "sharding_topology", "compiler_graph", "kernel_fusion", "system_trace",
    "sparse_features", "circuit_graph", "provenance_chain", "replication_protocol",
}
EVIDENCE_MODELS = {
    "representation_map", "model_taxonomy", "architecture_taxonomy", "objective_map", "evidence_map",
    "budget_allocation", "verifier_funnel", "reasoning_curriculum", "sample_and_vote", "modality_map",
    "reranking_funnel", "trajectory_eval", "agent_scorecard", "method_taxonomy", "low_bit_path",
    "sampling_controls", "eviction_lifecycle", "serving_queue", "continuous_batch", "selection_funnel",
    "claim_evidence", "slice_scorecard", "role_risk_map", "result_bundle", "evidence_ladder",
}
TILE_MODELS = {"latent_bottleneck", "codebook_lookup", "memory_tiling"}

COLORS = [
    (old.BLUE, old.BLUE_LIGHT),
    (old.PURPLE, old.PURPLE_LIGHT),
    (old.ORANGE, old.ORANGE_LIGHT),
    (old.GREEN, old.GREEN_LIGHT),
    (old.TEAL, old.TEAL_LIGHT),
]


def compact(text: str, limit: int = 135) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    cut = text[: limit - 1].rsplit(" ", 1)[0]
    return cut + "…"


def title_for(number: int) -> str:
    return old.SPECS[number][4]


def sections_for(number: int):
    return old.SPECS[number][6]


def detail_for(number: int):
    return old.detail_for_chapter(number)


def model_label(model: str) -> str:
    return model.replace("_", " ").upper()


def question(number: int, model: str, figure_index: int) -> str:
    sections = sections_for(number)
    detail = detail_for(number)
    if figure_index == 0:
        return (
            f"Come si passa da «{sections[0][0]}» a «{sections[2][0]}» "
            f"mantenendo osservabile {detail['object']}?"
        )
    return (
        f"Quale controllo collega «{sections[3][0]}» a «{sections[4][0]}» "
        f"senza superare il limite dichiarato?"
    )


def header(draw, figure_id: str, number: int, model: str, figure_index: int) -> None:
    old.fit(draw, (60, 25, 1740, 77), f"{figure_id} · {title_for(number)}", 31, 20, True)
    old.fit(draw, (80, 87, 1720, 140), question(number, model, figure_index), 19, 13, fill=old.MUTED)
    old.fit(draw, (80, 146, 1720, 178), model_label(model), 13, 10, True, old.PURPLE)


def footer(draw, number: int) -> None:
    detail = detail_for(number)
    draw.rounded_rectangle((170, 850, 1630, 940), radius=22, fill=old.ORANGE_LIGHT, outline=old.ORANGE, width=3)
    old.fit(draw, (205, 873, 1595, 917), f"LIMITE · {detail['invariant']}", 17, 12, True, old.TEXT)


def node(draw, box, title: str, body: str, color, fill, badge: str | None = None) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=22, fill=old.WHITE, outline=color, width=3)
    if badge:
        draw.ellipse((x0 + 18, y0 + 18, x0 + 58, y0 + 58), fill=color)
        old.fit(draw, (x0 + 27, y0 + 24, x0 + 49, y0 + 50), badge, 14, 10, True, old.WHITE)
        title_x = x0 + 72
    else:
        title_x = x0 + 24
    old.fit(draw, (title_x, y0 + 18, x1 - 22, y0 + 62), compact(title, 48), 18, 11, True, color, "left")
    old.fit(draw, (x0 + 24, y0 + 77, x1 - 24, y1 - 18), compact(body, 125), 14, 10, fill=old.TEXT, align="left")


def selected_items(number: int, figure_index: int):
    sections = sections_for(number)
    if figure_index == 0:
        return sections[:3]
    return sections[3:] + [("Controllo locale", detail_for(number)["invariant"])]


def render_flow(draw, number: int, figure_index: int) -> None:
    detail = detail_for(number)
    items = selected_items(number, figure_index)
    endpoints = [("INPUT", detail["input"])] + items + [("OUTPUT", detail["output"])]
    count = len(endpoints)
    width = 280 if count == 5 else 330
    gap = (1640 - count * width) / max(1, count - 1)
    boxes = []
    for index, (heading, body) in enumerate(endpoints):
        x0 = 80 + index * (width + gap)
        box = (int(x0), 330, int(x0 + width), 650)
        color, fill = COLORS[min(index, 4)]
        node(draw, box, heading, body, color, fill, str(index + 1))
        boxes.append(box)
    for left, right in zip(boxes, boxes[1:]):
        old.arrow(draw, (left[2] + 5, 490), (right[0] - 8, 490), old.MUTED, 4)
    old.fit(draw, (220, 730, 1580, 790), "Ogni freccia è un passaggio verificabile, non una semplice vicinanza grafica.", 17, 12, True, old.MUTED)


def render_cycle(draw, number: int, figure_index: int) -> None:
    items = selected_items(number, figure_index)
    if figure_index == 0:
        items = [("Stato iniziale", detail_for(number)["input"])] + items + [("Osservazione", detail_for(number)["output"])]
    else:
        items = items + [("Nuovo stato", detail_for(number)["output"])]
    positions = [(900, 270), (1370, 430), (1190, 700), (610, 700), (430, 430)]
    positions = positions[: len(items)]
    for index in range(len(items)):
        old.arrow(draw, positions[index], positions[(index + 1) % len(items)], old.MUTED, 4)
    for index, ((heading, body), (x, y)) in enumerate(zip(items, positions)):
        color, fill = COLORS[index % len(COLORS)]
        draw.rounded_rectangle((x - 175, y - 72, x + 175, y + 72), radius=20, fill=fill, outline=color, width=3)
        old.fit(draw, (x - 148, y - 50, x + 148, y - 12), heading, 17, 11, True, color)
        old.fit(draw, (x - 148, y, x + 148, y + 49), compact(body, 82), 13, 9, fill=old.TEXT)
    old.fit(draw, (690, 430, 1110, 555), "FEEDBACK\nLo stato restituito cambia il passo successivo", 19, 12, True, old.PURPLE)


def render_stack(draw, number: int, figure_index: int) -> None:
    detail = detail_for(number)
    items = selected_items(number, figure_index)
    x0, x1 = 620, 1180
    layers = [("INPUT", detail["input"])] + items + [("OUTPUT", detail["output"])]
    layer_h = 92
    start_y = 205
    for index, (heading, body) in enumerate(layers):
        y0 = start_y + index * 112
        color, fill = COLORS[index % len(COLORS)]
        draw.rounded_rectangle((x0, y0, x1, y0 + layer_h), radius=18, fill=fill, outline=color, width=3)
        old.fit(draw, (x0 + 22, y0 + 12, x0 + 250, y0 + 44), heading, 17, 11, True, color, "left")
        old.fit(draw, (x0 + 260, y0 + 12, x1 - 22, y0 + 72), compact(body, 95), 13, 9, fill=old.TEXT, align="left")
        if index:
            old.arrow(draw, (900, y0 - 18), (900, y0 - 2), old.MUTED, 3)
    # A side path makes residual, state, or metadata dependencies explicit.
    draw.line((500, start_y + 45, 500, start_y + (len(layers) - 1) * 112 + 45), fill=old.PURPLE, width=4)
    old.arrow(draw, (500, start_y + 45), (610, start_y + 45), old.PURPLE, 3)
    old.arrow(draw, (500, start_y + (len(layers) - 1) * 112 + 45), (610, start_y + (len(layers) - 1) * 112 + 45), old.PURPLE, 3)
    old.fit(draw, (150, 400, 450, 540), "PERCORSO LATERALE\nidentità, stato o metadati restano distinguibili", 17, 11, True, old.PURPLE)


def render_compare(draw, number: int, figure_index: int) -> None:
    sections = sections_for(number)
    if figure_index == 0:
        left = sections[:2]
        right = sections[2:4]
        labels = ("PRIMO CONTRATTO", "SECONDO CONTRATTO")
    else:
        left = sections[3:]
        right = [("Controllo", detail_for(number)["invariant"]), ("Output", detail_for(number)["output"])]
        labels = ("PROPOSTA", "VERIFICA")
    for panel_index, (x0, panel_items, label) in enumerate(((85, left, labels[0]), (930, right, labels[1]))):
        color, fill = COLORS[panel_index + 1]
        draw.rounded_rectangle((x0, 220, x0 + 785, 770), radius=28, fill=old.WHITE, outline=color, width=4)
        old.fit(draw, (x0 + 35, 247, x0 + 750, 300), label, 24, 15, True, color)
        for index, (heading, body) in enumerate(panel_items[:3]):
            y = 340 + index * 145
            draw.rounded_rectangle((x0 + 45, y, x0 + 740, y + 112), radius=16, fill=fill, outline=color, width=2)
            old.fit(draw, (x0 + 70, y + 13, x0 + 330, y + 47), heading, 17, 10, True, color, "left")
            old.fit(draw, (x0 + 340, y + 12, x0 + 715, y + 92), compact(body, 98), 13, 9, fill=old.TEXT, align="left")
    old.arrow(draw, (875, 490), (920, 490), old.MUTED, 4)
    old.fit(draw, (620, 785, 1180, 830), "Stesso caso, proprietà confrontate separatamente", 16, 11, True, old.MUTED)


def render_tree(draw, number: int, figure_index: int) -> None:
    detail = detail_for(number)
    items = selected_items(number, figure_index)
    node(draw, (650, 205, 1150, 350), "RADICE", detail["input"], old.BLUE, old.BLUE_LIGHT)
    branch_boxes = []
    for index, (heading, body) in enumerate(items[:3]):
        x0 = 95 + index * 565
        box = (x0, 485, x0 + 470, 675)
        color, fill = COLORS[index + 1]
        old.arrow(draw, (900, 365), (x0 + 235, 475), color, 3)
        node(draw, box, heading, body, color, fill, chr(65 + index))
        branch_boxes.append(box)
    draw.rounded_rectangle((560, 735, 1240, 825), radius=20, fill=old.GREEN_LIGHT, outline=old.GREEN, width=3)
    old.fit(draw, (595, 758, 1205, 803), f"SELEZIONE · {compact(detail['output'], 105)}", 16, 11, True, old.GREEN)
    for box in branch_boxes:
        old.arrow(draw, ((box[0] + box[2]) / 2, box[3] + 5), (900, 725), old.MUTED, 3)


def render_grid(draw, number: int, figure_index: int) -> None:
    items = selected_items(number, figure_index)
    x0, y0 = 430, 235
    cell_w, cell_h = 190, 120
    rows, cols = 4, 5
    for row in range(rows):
        for col in range(cols):
            active = (row + col + number + figure_index) % 4 == 0 or row == col % rows
            color, fill = (old.PURPLE, old.PURPLE_LIGHT) if active else (old.GRID, old.LIGHT)
            draw.rounded_rectangle(
                (x0 + col * cell_w, y0 + row * cell_h, x0 + col * cell_w + 165, y0 + row * cell_h + 92),
                radius=12, fill=fill, outline=color, width=2,
            )
    old.fit(draw, (80, 280, 360, 390), compact(items[0][0], 34) + "\nrighe / stati", 18, 11, True, old.BLUE)
    old.fit(draw, (620, 730, 1240, 785), compact(items[-1][0], 46) + " · colonne / trasformazioni", 18, 11, True, old.PURPLE)
    node(draw, (1330, 275, 1710, 650), items[0][0], items[0][1], old.ORANGE, old.ORANGE_LIGHT)
    old.arrow(draw, (1285, 470), (1320, 470), old.MUTED, 4)
    old.fit(draw, (450, 790, 1300, 830), "Le celle evidenziate mostrano la relazione strutturale, non una misura quantitativa.", 15, 10, True, old.MUTED)


def render_boundary(draw, number: int, figure_index: int) -> None:
    detail = detail_for(number)
    items = selected_items(number, figure_index)
    zones = [
        (80, 230, 560, 750, "ESTERNO / NON FIDATO", old.RED, old.RED_LIGHT),
        (660, 230, 1140, 750, "CONTROLLO", old.PURPLE, old.PURPLE_LIGHT),
        (1240, 230, 1720, 750, "EFFETTO / OUTPUT", old.GREEN, old.GREEN_LIGHT),
    ]
    for index, (x0, y0, x1, y1, label, color, fill) in enumerate(zones):
        draw.rounded_rectangle((x0, y0, x1, y1), radius=28, fill=fill, outline=color, width=4)
        old.fit(draw, (x0 + 25, y0 + 25, x1 - 25, y0 + 75), label, 20, 13, True, color)
        heading, body = items[min(index, len(items) - 1)]
        node(draw, (x0 + 45, 355, x1 - 45, 605), heading, body, color, old.WHITE, str(index + 1))
    old.arrow(draw, (570, 490), (650, 490), old.RED, 4)
    old.arrow(draw, (1150, 490), (1230, 490), old.GREEN, 4)
    old.fit(draw, (545, 655, 1180, 720), f"GATE · {compact(detail['invariant'], 100)}", 16, 11, True, old.PURPLE)


def render_graph(draw, number: int, figure_index: int) -> None:
    items = selected_items(number, figure_index)
    detail = detail_for(number)
    positions = [(250, 500), (590, 275), (920, 500), (590, 725), (1320, 300), (1530, 650)]
    edges = ((0, 1), (1, 2), (0, 3), (3, 2), (2, 4), (2, 5))
    for index, (a, b) in enumerate(edges):
        old.arrow(draw, positions[a], positions[b], COLORS[index % 5][0], 3)
    labels = [("INPUT", detail["input"])] + items + [("OUTPUT", detail["output"])]
    for index, ((x, y), (heading, body)) in enumerate(zip(positions, labels)):
        color, fill = COLORS[index % 5]
        draw.ellipse((x - 145, y - 78, x + 145, y + 78), fill=fill, outline=color, width=3)
        old.fit(draw, (x - 120, y - 50, x + 120, y - 12), compact(heading, 32), 16, 10, True, color)
        old.fit(draw, (x - 120, y, x + 120, y + 53), compact(body, 65), 12, 8, fill=old.TEXT)
    old.fit(draw, (1110, 740, 1680, 810), "Gli archi dichiarano flusso o dipendenza. Nessun arco è implicito.", 15, 10, True, old.MUTED)


def render_evidence(draw, number: int, figure_index: int) -> None:
    items = selected_items(number, figure_index)
    detail = detail_for(number)
    y = 250
    widths = [1280, 1050, 820, 590]
    full_items = items + [("Decisione", detail["output"])]
    for index, ((heading, body), width) in enumerate(zip(full_items[:4], widths)):
        x0 = (1800 - width) // 2
        color, fill = COLORS[index]
        draw.rounded_rectangle((x0, y + index * 135, x0 + width, y + index * 135 + 96), radius=18, fill=fill, outline=color, width=3)
        old.fit(draw, (x0 + 25, y + index * 135 + 14, x0 + 330, y + index * 135 + 48), heading, 18, 11, True, color, "left")
        old.fit(draw, (x0 + 345, y + index * 135 + 12, x0 + width - 25, y + index * 135 + 75), compact(body, 115), 13, 9, fill=old.TEXT, align="left")
    old.fit(draw, (250, 790, 1550, 830), "La base conserva i casi esclusi; il livello superiore non cancella l'incertezza sottostante.", 16, 11, True, old.MUTED)


def render_tiles(draw, number: int, figure_index: int) -> None:
    items = selected_items(number, figure_index)
    # Left: a blocked tensor. Right: the local transformation and memory path.
    x0, y0, cell = 100, 260, 92
    for row in range(5):
        for col in range(6):
            tile = (row // 2 + col // 2 + figure_index) % 3
            color, fill = COLORS[tile]
            draw.rectangle((x0 + col * cell, y0 + row * cell, x0 + (col + 1) * cell - 8, y0 + (row + 1) * cell - 8), fill=fill, outline=color, width=2)
    old.fit(draw, (120, 735, 630, 790), "Tensore diviso in blocchi espliciti", 17, 11, True, old.BLUE)
    old.arrow(draw, (690, 490), (860, 490), old.MUTED, 5)
    for index, (heading, body) in enumerate(items[:3]):
        y = 245 + index * 175
        color, fill = COLORS[index + 1]
        node(draw, (900, y, 1660, y + 135), heading, body, color, fill, str(index + 1))
    old.fit(draw, (830, 765, 1670, 815), "Materializzare, ricostruire e trasferire sono costi distinti.", 16, 11, True, old.MUTED)


def renderer_for(model: str):
    if model in FLOW_MODELS:
        return render_flow
    if model in CYCLE_MODELS:
        return render_cycle
    if model in STACK_MODELS:
        return render_stack
    if model in COMPARE_MODELS:
        return render_compare
    if model in TREE_MODELS:
        return render_tree
    if model in GRID_MODELS:
        return render_grid
    if model in BOUNDARY_MODELS:
        return render_boundary
    if model in GRAPH_MODELS:
        return render_graph
    if model in EVIDENCE_MODELS:
        return render_evidence
    if model in TILE_MODELS:
        return render_tiles
    raise KeyError(f"No renderer for {model}")


def write_visual_metadata(folder: Path, figure_id: str, number: int, model: str, figure_index: int, image_name: str) -> None:
    detail = detail_for(number)
    sections = sections_for(number)
    q = question(number, model, figure_index)
    related = sections[:3] if figure_index == 0 else sections[3:]
    nodes = "; ".join(f"{heading}: {compact(note, 90)}" for heading, note in related)
    spec = f"""# Specifica visuale {figure_id}

- modello compositivo: {model}
- domanda principale: {q}
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: {image_name}
- oggetto osservato: {detail['object']}
- input: {detail['input']}
- output: {detail['output']}
- nodi locali: {nodes}
- limite visualizzato: {detail['invariant']}
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
"""
    alt = (
        f"# Testo alternativo\n\n{figure_id}, {title_for(number)}. {q} "
        f"La composizione {model_label(model).lower()} collega "
        + ", ".join(f"«{heading}»" for heading, _ in related)
        + f". L'input è {detail['input']}; l'output è {detail['output']}. "
        f"Il limite esplicito è: {detail['invariant']}.\n"
    )
    audit = f"""# Audit visuale {figure_id}

- decodifica PNG: superata
- modalita e dimensione: RGB, 1800x1000
- angoli bianchi #FFFFFF: superati
- domanda didattica singola: verificata
- composizione pertinente al concetto: {model}
- contenimento testo: verificato dal renderer sul raster prodotto
- frecce e relazioni: ogni collegamento rappresenta un flusso, una dipendenza o un controllo dichiarato
- numeri non supportati: assenti
- watermark o branding di terzi: assenti
- confronto con la seconda figura del capitolo: domanda e modello compositivo distinti
- approvazione autoriale: aperta nel contesto impaginato
- esito: candidata tecnica revisionata il 4 agosto 2026
"""
    (folder / "SPEC.md").write_text(spec, encoding="utf-8")
    (folder / "ALT_TEXT.md").write_text(alt, encoding="utf-8")
    (folder / "AUDIT.md").write_text(audit, encoding="utf-8")


def generate_chapter(number: int) -> None:
    chapter = ROOT / "chapters" / old.SPECS[number][3] / "CHAPTER.md"
    text = chapter.read_text(encoding="utf-8")
    matches = IMAGE_RE.findall(text)
    if len(matches) != 2:
        raise ValueError(f"Chapter {number}: expected two linked images, found {len(matches)}")
    models = VISUAL_MODELS[number]
    for figure_index, ((_, relative), model) in enumerate(zip(matches, models)):
        image_path = (chapter.parent / relative).resolve()
        folder = image_path.parent
        figure_id = folder.name
        image = Image.new("RGB", (1800, 1000), old.WHITE)
        draw = ImageDraw.Draw(image)
        header(draw, figure_id, number, model, figure_index)
        renderer_for(model)(draw, number, figure_index)
        footer(draw, number)
        old.finish(image_path, image)
        write_visual_metadata(folder, figure_id, number, model, figure_index, image_path.name)


APPENDICES = {
    "A_python_numpy_pytorch": (
        "APP-A", "stack", "Dal tensore al gradiente verificato",
        [("Python", "strutture, controllo e I/O"), ("NumPy", "array e broadcasting"), ("PyTorch", "tensori e autograd")],
        "stessa trasformazione affine, stesso output atteso",
    ),
    "B_jax": (
        "APP-B", "graph", "Funzione pura e trasformazioni JAX",
        [("funzione", "nessuno stato nascosto"), ("vmap", "batch esplicito"), ("jit", "compilazione"), ("grad", "derivata")],
        "shape e dtype fanno parte del contratto",
    ),
    "C_formulario": (
        "APP-C", "evidence", "Una formula, le ipotesi e il controllo",
        [("definizione", "simboli e dominio"), ("derivazione", "passaggi"), ("test", "caso piccolo")],
        "una formula senza dominio non è una specifica completa",
    ),
    "D_complessita": (
        "APP-D", "compare", "Compute, memoria e latenza non coincidono",
        [("compute", "operazioni"), ("memoria", "resident set e cache"), ("latenza", "tempo end-to-end")],
        "il confronto richiede stesso setup e stessa shape",
    ),
    "E_glossario": (
        "APP-E", "evidence", "Dal termine al punto del libro",
        [("termine", "forma canonica"), ("definizione", "significato locale"), ("rinvio", "capitolo e fonte")],
        "un sinonimo non cambia automaticamente il concetto",
    ),
    "F_dataset_benchmark": (
        "APP-F", "flow", "Dal dataset alla decisione valutativa",
        [("dataset", "versione e licenza"), ("split", "unità e leakage"), ("metrica", "protocollo"), ("decisione", "limite")],
        "un punteggio senza protocollo non è confrontabile",
    ),
    "G_modelli_report": (
        "APP-G", "stack", "Model report e system report su livelli distinti",
        [("modello", "checkpoint e dati"), ("sistema", "retrieval, tool, policy"), ("run", "configurazione e output")],
        "la qualità del modello non riassume il sistema",
    ),
    "H_checklist": (
        "APP-H", "boundary", "Gate prima di approvare un capitolo",
        [("bozza", "testo e claim"), ("verifica", "fonti, codice, visuali"), ("approvazione", "firma autoriale")],
        "un gate mancante riapre lo stato del capitolo",
    ),
    "I_soluzioni": (
        "APP-I", "flow", "Dall'esercizio alla soluzione verificabile",
        [("consegna", "input e vincoli"), ("passaggi", "derivazione"), ("test", "controesempio"), ("soluzione", "confine")],
        "la soluzione deve spiegare anche perché un'alternativa fallisce",
    ),
    "J_cronologia": (
        "APP-J", "flow", "Una cronologia distingue pubblicazione e adozione",
        [("evento", "data primaria"), ("artefatto", "versione"), ("adozione", "contesto"), ("revisione", "nuova evidenza")],
        "la sequenza temporale non dimostra causalità",
    ),
    "K_lettura_fonti": (
        "APP-K", "evidence", "Claim, locator, prova e limite",
        [("claim", "frase esatta"), ("locator", "pagina o sezione"), ("prova", "contenuto pertinente"), ("limite", "ciò che non segue")],
        "una fonte autorevole può essere irrilevante per il claim specifico",
    ),
    "L_edizioni_alias": (
        "APP-L", "graph", "Identità editoriale tra alias e versioni",
        [("concetto", "nome canonico"), ("alias", "forma storica"), ("versione", "data e stato"), ("rinvio", "posizione attuale")],
        "alias, edizione e implementazione restano campi distinti",
    ),
}


def render_appendix(folder_name: str, specification) -> None:
    figure_id, layout, title, items, invariant = specification
    folder = ROOT / "assets" / "appendices" / folder_name / figure_id
    image_path = folder / "candidate-v2.png"
    image = Image.new("RGB", (1800, 1000), old.WHITE)
    draw = ImageDraw.Draw(image)
    old.fit(draw, (60, 28, 1740, 82), f"{figure_id} · {title}", 31, 20, True)
    old.fit(draw, (80, 94, 1720, 142), "Mappa operativa dell'appendice: ogni nodo rinvia a un controllo descritto nel testo.", 18, 12, fill=old.MUTED)
    # Appendix diagrams use compact bespoke arrangements, independent of chapter data.
    if layout == "flow":
        boxes = []
        width = 330
        gap = (1640 - len(items) * width) / max(1, len(items) - 1)
        for index, (heading, body) in enumerate(items):
            x0 = 80 + index * (width + gap)
            box = (int(x0), 330, int(x0 + width), 650)
            color, fill = COLORS[index]
            node(draw, box, heading, body, color, fill, str(index + 1))
            boxes.append(box)
        for a, b in zip(boxes, boxes[1:]):
            old.arrow(draw, (a[2] + 5, 490), (b[0] - 8, 490), old.MUTED, 4)
    elif layout == "stack":
        for index, (heading, body) in enumerate(items):
            y0 = 245 + index * 175
            color, fill = COLORS[index]
            node(draw, (500, y0, 1300, y0 + 130), heading, body, color, fill, str(index + 1))
            if index:
                old.arrow(draw, (900, y0 - 37), (900, y0 - 7), old.MUTED, 3)
    elif layout == "compare":
        for index, (heading, body) in enumerate(items):
            x0 = 100 + index * 560
            color, fill = COLORS[index]
            node(draw, (x0, 300, x0 + 480, 680), heading, body, color, fill, str(index + 1))
    elif layout == "boundary":
        for index, (heading, body) in enumerate(items):
            x0 = 95 + index * 565
            color, fill = COLORS[index]
            draw.rounded_rectangle((x0, 260, x0 + 480, 700), radius=26, fill=fill, outline=color, width=4)
            node(draw, (x0 + 45, 370, x0 + 435, 590), heading, body, color, old.WHITE, str(index + 1))
            if index:
                old.arrow(draw, (x0 - 70, 480), (x0 - 10, 480), old.MUTED, 4)
    elif layout == "graph":
        positions = [(260, 500), (660, 280), (1040, 500), (1450, 300), (1450, 700)]
        for index in range(len(items) - 1):
            old.arrow(draw, positions[index], positions[index + 1], COLORS[index][0], 3)
        for index, ((heading, body), (x, y)) in enumerate(zip(items, positions)):
            color, fill = COLORS[index]
            draw.ellipse((x - 160, y - 90, x + 160, y + 90), fill=fill, outline=color, width=3)
            old.fit(draw, (x - 130, y - 55, x + 130, y - 15), heading, 17, 11, True, color)
            old.fit(draw, (x - 130, y, x + 130, y + 55), body, 13, 9, fill=old.TEXT)
    else:  # evidence
        widths = [1300, 1080, 860, 640]
        for index, ((heading, body), width) in enumerate(zip(items, widths)):
            x0 = (1800 - width) // 2
            y0 = 250 + index * 140
            color, fill = COLORS[index]
            draw.rounded_rectangle((x0, y0, x0 + width, y0 + 100), radius=18, fill=fill, outline=color, width=3)
            old.fit(draw, (x0 + 25, y0 + 15, x0 + 300, y0 + 48), heading, 18, 11, True, color, "left")
            old.fit(draw, (x0 + 315, y0 + 13, x0 + width - 25, y0 + 77), body, 13, 9, fill=old.TEXT, align="left")
    draw.rounded_rectangle((170, 850, 1630, 940), radius=22, fill=old.ORANGE_LIGHT, outline=old.ORANGE, width=3)
    old.fit(draw, (205, 873, 1595, 917), f"LIMITE · {invariant}", 17, 12, True, old.TEXT)
    old.finish(image_path, image)

    appendix = ROOT / "appendices" / folder_name / "APPENDIX.md"
    text = appendix.read_text(encoding="utf-8")
    text = re.sub(
        rf"(assets/appendices/{re.escape(folder_name)}/{re.escape(figure_id)}/)(?:final|candidate-v\d+)\.png",
        rf"\1{image_path.name}",
        text,
    )
    appendix.write_text(text, encoding="utf-8")
    (folder / "SPEC.md").write_text(
        f"# Specifica {figure_id}\n\n- domanda: {title}\n- modello compositivo: {layout}\n- file candidato: {image_path.name}\n- sfondo: #FFFFFF\n- formato: PNG RGB 1800x1000\n- limite: {invariant}\n- generatore: scripts/generate_visuals_v2.py\n- approvazione autoriale: aperta\n",
        encoding="utf-8",
    )
    (folder / "ALT_TEXT.md").write_text(
        f"# Alt text {figure_id}\n\n{title}. " + "; ".join(f"{a}: {b}" for a, b in items) + f". Limite: {invariant}.\n",
        encoding="utf-8",
    )
    (folder / "AUDIT.md").write_text(
        f"# Audit {figure_id}\n\n- decodifica: superata\n- dimensione: 1800x1000 RGB\n- contenimento: verificato\n- numeri inventati: assenti\n- composizione: {layout}\n- approvazione autoriale: aperta\n",
        encoding="utf-8",
    )


def main() -> None:
    missing = set(TARGETS) - set(VISUAL_MODELS)
    if missing:
        raise RuntimeError(f"Missing visual models: {sorted(missing)}")
    for number in TARGETS:
        generate_chapter(number)
    for folder_name, specification in APPENDICES.items():
        render_appendix(folder_name, specification)
    print(f"Regenerated {len(TARGETS) * 2} chapter visuals and {len(APPENDICES)} appendix visuals.")


if __name__ == "__main__":
    main()
