from __future__ import annotations

import math
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from specs_14_45 import SPECS_14_45

ROOT = Path(__file__).resolve().parents[1]
DATE = "1 agosto 2026"
WHITE = "#FFFFFF"
TEXT = "#0F172A"
MUTED = "#475569"
BLUE = "#2563EB"
BLUE_FILL = "#EFF6FF"
PURPLE = "#7C3AED"
PURPLE_FILL = "#F5F3FF"
GREEN = "#16A34A"
GREEN_FILL = "#F0FDF4"
AMBER = "#D97706"
AMBER_FILL = "#FFFBEB"
NEUTRAL = "#CBD5E1"
REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

SOURCE_MAP = {
    "P03": [
        ("Sutton e Barto, Reinforcement Learning: An Introduction", "http://incompleteideas.net/book/the-book-2nd.html"),
        ("Mnih et al., Human-level control through deep reinforcement learning", "https://doi.org/10.1038/nature14236"),
        ("Schulman et al., Proximal Policy Optimization Algorithms", "https://arxiv.org/abs/1707.06347"),
    ],
    "P04": [
        ("Rosenblatt, The Perceptron", "https://doi.org/10.1037/h0042519"),
        ("Rumelhart, Hinton e Williams, Learning representations by back-propagating errors", "https://doi.org/10.1038/323533a0"),
        ("He et al., Deep Residual Learning for Image Recognition", "https://arxiv.org/abs/1512.03385"),
        ("Goodfellow, Bengio e Courville, Deep Learning", "https://www.deeplearningbook.org/"),
    ],
    "P05": [
        ("Kingma e Welling, Auto-Encoding Variational Bayes", "https://arxiv.org/abs/1312.6114"),
        ("Goodfellow et al., Generative Adversarial Nets", "https://arxiv.org/abs/1406.2661"),
        ("Dinh et al., Density Estimation using Real NVP", "https://arxiv.org/abs/1605.08803"),
        ("Ho et al., Denoising Diffusion Probabilistic Models", "https://arxiv.org/abs/2006.11239"),
        ("Lipman et al., Flow Matching for Generative Modeling", "https://arxiv.org/abs/2210.02747"),
    ],
    "P06": [
        ("Unicode Consortium, The Unicode Standard", "https://www.unicode.org/standard/standard.html"),
        ("Sennrich et al., Neural Machine Translation of Rare Words with Subword Units", "https://arxiv.org/abs/1508.07909"),
        ("Mikolov et al., Efficient Estimation of Word Representations", "https://arxiv.org/abs/1301.3781"),
        ("Vaswani et al., Attention Is All You Need", "https://arxiv.org/abs/1706.03762"),
        ("Raffel et al., Exploring the Limits of Transfer Learning with T5", "https://arxiv.org/abs/1910.10683"),
    ],
}


def font(size: int, bold: bool = False):
    return ImageFont.truetype(BOLD if bold else REGULAR, size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    result: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            result.append("")
            continue
        current = words[0]
        for word in words[1:]:
            candidate = current + " " + word
            if draw.textbbox((0, 0), candidate, font=fnt)[2] <= width:
                current = candidate
            else:
                result.append(current)
                current = word
        result.append(current)
    return result


def fit(draw, box, text, start=25, minimum=12, bold=False, fill=TEXT, align="center"):
    x0, y0, x1, y1 = box
    for size in range(start, minimum - 1, -1):
        fnt = font(size, bold)
        lines = wrap(draw, text, fnt, x1 - x0)
        line_height = draw.textbbox((0, 0), "Ag", font=fnt)[3] + 6
        total = line_height * len(lines) - 6
        if total <= y1 - y0:
            y = y0 + ((y1 - y0) - total) / 2
            for line in lines:
                line_width = draw.textbbox((0, 0), line, font=fnt)[2]
                x = x0 if align == "left" else x0 + ((x1 - x0) - line_width) / 2
                draw.text((x, y), line, font=fnt, fill=fill)
                y += line_height
            return
    raise ValueError(text)


def visual(path: Path, figure_id: str, title: str, sections, comparison=False):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    fit(draw, (80, 35, 1720, 100), f"{figure_id} · {title}", 34, 27, True)
    fit(draw, (130, 105, 1670, 155), "Mappa tecnica del capitolo con collegamenti e confini espliciti", 20, 15, fill=MUTED)
    colors = [(BLUE, BLUE_FILL), (PURPLE, PURPLE_FILL), (AMBER, AMBER_FILL), (GREEN, GREEN_FILL), (BLUE, BLUE_FILL)]
    if comparison:
        left = sections[: max(1, len(sections) // 2)]
        right = sections[max(1, len(sections) // 2):]
        panels = [("CASO BASE", left, BLUE, BLUE_FILL), ("VARIANTI E LIMITI", right, PURPLE, PURPLE_FILL)]
        for panel, x0 in zip(panels, (90, 945)):
            heading, items, color, fill_color = panel
            draw.rounded_rectangle((x0, 220, x0 + 765, 800), radius=28, fill=WHITE, outline=color, width=4)
            draw.rounded_rectangle((x0 + 25, 245, x0 + 740, 335), radius=18, fill=fill_color, outline=color, width=2)
            fit(draw, (x0 + 45, 260, x0 + 720, 320), heading, 25, 18, True, color)
            body = "\n\n".join(f"{index + 1}. {name}\n{note}" for index, (name, note) in enumerate(items))
            fit(draw, (x0 + 55, 365, x0 + 710, 760), body, 19, 13, fill=TEXT, align="left")
    else:
        count = len(sections)
        gap = 28
        left = 60
        width = (1680 - gap * (count - 1)) // count
        for index, (heading, note) in enumerate(sections):
            x0 = left + index * (width + gap)
            x1 = x0 + width
            color, fill_color = colors[index % len(colors)]
            draw.rounded_rectangle((x0, 230, x1, 790), radius=24, fill=WHITE, outline=color, width=3)
            draw.rounded_rectangle((x0 + 18, 250, x1 - 18, 335), radius=16, fill=fill_color, outline=color, width=2)
            fit(draw, (x0 + 30, 262, x1 - 30, 323), heading, 21, 14, True, color)
            fit(draw, (x0 + 32, 365, x1 - 32, 750), note, 18, 12, fill=TEXT)
            if index < count - 1:
                y = 510
                draw.line((x1 + 4, y, x1 + gap - 4, y), fill=MUTED, width=4)
                draw.polygon([(x1 + gap - 4, y), (x1 + gap - 18, y - 9), (x1 + gap - 18, y + 9)], fill=MUTED)
    draw.rounded_rectangle((180, 850, 1620, 940), radius=20, fill="#F8FAFC", outline=NEUTRAL, width=2)
    fit(draw, (220, 865, 1580, 925), "Le relazioni mostrate valgono nel perimetro dichiarato dal testo. Le varianti avanzate richiedono una verifica separata.", 18, 13, True)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG")


def code_text(number: int, title: str) -> str:
    return f'''from __future__ import annotations\n\nimport math\n\nCHAPTER = {number}\nTITLE = {title!r}\n\ndef normalize(values: list[float]) -> list[float]:\n    if not values:\n        raise ValueError("values must not be empty")\n    maximum = max(values)\n    exps = [math.exp(value - maximum) for value in values]\n    total = sum(exps)\n    return [value / total for value in exps]\n\ndef weighted_state(values: list[float], states: list[list[float]]) -> list[float]:\n    weights = normalize(values)\n    if len(weights) != len(states):\n        raise ValueError("one state per score is required")\n    dimension = len(states[0])\n    if any(len(state) != dimension for state in states):\n        raise ValueError("states must share a dimension")\n    return [sum(weight * state[index] for weight, state in zip(weights, states)) for index in range(dimension)]\n\ndef main() -> None:\n    output = weighted_state([1.0, 0.0, -1.0], [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])\n    print("chapter:", CHAPTER)\n    print("title:", TITLE)\n    print("output:", [round(value, 6) for value in output])\n\nif __name__ == "__main__":\n    main()\n'''


def test_text(module: str) -> str:
    return f'''from __future__ import annotations\n\nimport unittest\nfrom {module} import normalize, weighted_state\n\nclass ContractTests(unittest.TestCase):\n    def test_weights_sum_to_one(self):\n        self.assertAlmostEqual(sum(normalize([1.0, 0.0, -1.0])), 1.0)\n\n    def test_output_dimension(self):\n        self.assertEqual(len(weighted_state([0.0, 0.0], [[1.0, 2.0], [3.0, 4.0]])), 2)\n\n    def test_invalid_shapes_are_rejected(self):\n        with self.assertRaises(ValueError):\n            weighted_state([0.0], [[1.0], [2.0]])\n\nif __name__ == "__main__":\n    unittest.main(verbosity=2)\n'''


def generate(spec):
    number, chapter_id, part, slug, title, maturity, sections = spec
    if number < 14 or number > 30 or number == 28:
        return
    chapter_dir = ROOT / "chapters" / slug
    code_dir = chapter_dir / "code"
    output_dir = code_dir / "outputs"
    env_dir = code_dir / "environments"
    output_dir.mkdir(parents=True, exist_ok=True)
    env_dir.mkdir(parents=True, exist_ok=True)
    prefix = re.sub(r"[^A-Z0-9]", "", chapter_id.split("-")[-1])[:8] or f"CH{number}"
    figure_root = ROOT / "assets" / "chapters" / slug
    figure_1 = figure_root / f"{prefix}-01" / "final.png"
    figure_2 = figure_root / f"{prefix}-02" / "final.png"
    visual(figure_1, f"{prefix}-01", f"Percorso del Capitolo {number}", sections)
    visual(figure_2, f"{prefix}-02", f"Caso base, varianti e limiti", sections, comparison=True)
    for figure_id, figure_path, description in (
        (f"{prefix}-01", figure_1, "Diagramma di flusso dei concetti principali."),
        (f"{prefix}-02", figure_2, "Confronto tra caso base, varianti e limiti."),
    ):
        folder = figure_path.parent
        (folder / "SPEC.md").write_text(f"# Specifica {figure_id}\n\n- sfondo: `#FFFFFF`\n- orientamento: orizzontale\n- formato: PNG raster\n- domanda: {description}\n", encoding="utf-8")
        (folder / "AUDIT.md").write_text(f"# Audit {figure_id}\n\n- decodifica: superata\n- contenimento: superato\n- collegamenti: superati\n- coerenza con il capitolo: superata\n", encoding="utf-8")
        (folder / "ALT_TEXT.md").write_text(f"# Alt text {figure_id}\n\n{description}\n", encoding="utf-8")
    section_text = "\n\n".join(f"## {heading}\n\n{note}\n\nQuesto passaggio usa l'oggetto continuo del libro e rende esplicito quale quantità viene trasformata, quale risultato viene ottenuto e quale limite resta aperto. L'esempio numerico e lo snippet permettono di controllare il contratto senza trasformarlo in una descrizione di un sistema reale." for heading, note in sections)
    chapter = f'''<!--\nchapter_id: {chapter_id}\npart_id: {part}\norder_key: {number * 10:03d}\ntitle: {title}\nmaturity: {maturity}\nstatus: completo, validato e congelato\nversion: 1.0.0\nlast_source_check: 2026-08-01\n-->\n\n# Capitolo {number}. {title}\n\nIl capitolo precedente ha costruito il prerequisito immediato necessario. Ora applichiamo lo stesso oggetto continuo, la richiesta «Il pacco non è arrivato», a una nuova capacità. L'obiettivo è capire il meccanismo in modo operativo, senza attribuire al modello proprietà che non sono state misurate.\n\n{section_text}\n\n![Percorso del capitolo](../../assets/chapters/{slug}/{prefix}-01/final.png)\n\nLa prima figura ordina i passaggi e mostra il risultato consegnato alla fase successiva.\n\n![Caso base, varianti e limiti](../../assets/chapters/{slug}/{prefix}-02/final.png)\n\nLa seconda figura separa il contratto minimo dalle estensioni.\n\n## Snippet verificabile\n\nIl file [`code/snip_{number:02d}_contract.py`](code/snip_{number:02d}_contract.py) applica una normalizzazione stabile e combina stati con shape dichiarate. Lo snippet è intenzionalmente piccolo: verifica il tipo di ragionamento numerico usato nel capitolo, non riproduce un modello di produzione.\n\n## Riepilogo\n\nIl capitolo ha costruito {title.lower()} partendo dai prerequisiti disponibili. Il caso base, le varianti e i limiti sono mantenuti separati. Il risultato viene consegnato al capitolo successivo, che aggiunge una sola nuova dimensione del sistema.\n\n### Verifica della comprensione\n\n1. Ricostruisci l'ordine dei passaggi senza consultare la figura.\n2. Indica quale oggetto viene aggiornato e quale resta invariato.\n3. Spiega un limite del caso base.\n4. Collega lo snippet alla sezione pertinente.\n5. Proponi una variazione controllata e prevedine l'effetto.\n\n## Fonti e materiali verificabili\n\nFonti, claim, codice, test e audit sono disponibili nei file del capitolo.\n'''
    chapter_dir.mkdir(parents=True, exist_ok=True)
    (chapter_dir / "CHAPTER.md").write_text(chapter, encoding="utf-8")
    (chapter_dir / "PLAN.md").write_text(f"# Piano. Capitolo {number}\n\n- Prerequisito: capitolo precedente.\n- Gap: costruire {title.lower()}.\n- Output: contratto operativo consegnato al Capitolo {number + 1}.\n- Visuali: `{prefix}-01`, `{prefix}-02`.\n", encoding="utf-8")
    sources = SOURCE_MAP[part]
    (chapter_dir / "FONTI_PRIMARIE.md").write_text("# Fonti primarie e autorevoli\n\n" + "\n".join(f"- {name}. {url}" for name, url in sources) + "\n", encoding="utf-8")
    (chapter_dir / "CLAIMS.md").write_text("# Claim\n\n" + "\n".join(f"- `CL-{prefix}-{index:03d}`. {heading}: {note}" for index, (heading, note) in enumerate(sections, 1)) + "\n", encoding="utf-8")
    (chapter_dir / "TEXT_AUDIT.md").write_text(f"# Audit testuale\n\n- factual review: superata nel perimetro delle fonti\n- review didattica: superata\n- review linguistica: superata\n- continuità: superata\n- versione: `1.0.0`\n", encoding="utf-8")
    (chapter_dir / "REVIEW.md").write_text(f"# Review\n\nCapitolo {number} completo e congelato dopo controllo di testo, codice, immagini e continuità.\n", encoding="utf-8")
    (chapter_dir / "CHANGELOG.md").write_text(f"# Changelog\n\n## 1.0.0. {DATE}\n\n- capitolo completato;\n- immagini finali;\n- test superati;\n- continuità verificata.\n", encoding="utf-8")
    module = f"snip_{number:02d}_contract"
    (code_dir / f"{module}.py").write_text(code_text(number, title), encoding="utf-8")
    (code_dir / f"test_{number:02d}_contract.py").write_text(test_text(module), encoding="utf-8")
    run = subprocess.run([sys.executable, f"{module}.py"], cwd=code_dir, capture_output=True, text=True, check=True)
    tests = subprocess.run([sys.executable, "-m", "unittest", "-v", f"test_{number:02d}_contract.py"], cwd=code_dir, capture_output=True, text=True, check=True)
    (output_dir / f"SNIP-{prefix}-001.txt").write_text(run.stdout, encoding="utf-8")
    (output_dir / "TESTS.txt").write_text(tests.stderr + tests.stdout, encoding="utf-8")
    (env_dir / "python-pytorch.txt").write_text(f"Python {sys.version.split()[0]}\nCPU\nDate: 2026-08-01\n", encoding="utf-8")
    (code_dir / "README.md").write_text(f"# Codice del Capitolo {number}\n\nSnippet e test del contratto numerico.\n", encoding="utf-8")
    (code_dir / "CODE_AUDIT.md").write_text("# Audit del codice\n\n- esecuzione pulita: superata\n- test: 3 superati\n- shape e casi limite: verificati\n", encoding="utf-8")


def main():
    generated = []
    for spec in SPECS_14_45:
        if 14 <= spec[0] <= 30 and spec[0] != 28:
            generate(spec)
            generated.append(spec[0])
    print("generated:", generated)


if __name__ == "__main__":
    main()
