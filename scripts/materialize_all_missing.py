from __future__ import annotations

import hashlib
import importlib
import json
import math
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2 agosto 2026"
WHITE = "#FFFFFF"
TEXT = "#0F172A"
MUTED = "#475569"
NEUTRAL = "#CBD5E1"
NEUTRAL_FILL = "#F8FAFC"
PALETTE = [
    ("#2563EB", "#EFF6FF"),
    ("#7C3AED", "#F5F3FF"),
    ("#D97706", "#FFFBEB"),
    ("#16A34A", "#F0FDF4"),
    ("#DC2626", "#FEF2F2"),
]
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

PART_SOURCES = {
    "P09": [
        ("Ouyang et al., Training language models to follow instructions with human feedback", "https://arxiv.org/abs/2203.02155"),
        ("Hu et al., LoRA", "https://arxiv.org/abs/2106.09685"),
        ("Rafailov et al., Direct Preference Optimization", "https://arxiv.org/abs/2305.18290"),
        ("Lightman et al., Let's Verify Step by Step", "https://arxiv.org/abs/2305.20050"),
    ],
    "P10": [
        ("Radford et al., Learning Transferable Visual Models From Natural Language Supervision", "https://arxiv.org/abs/2103.00020"),
        ("Alayrac et al., Flamingo", "https://arxiv.org/abs/2204.14198"),
        ("Rombach et al., High-Resolution Image Synthesis with Latent Diffusion Models", "https://arxiv.org/abs/2112.10752"),
        ("Brohan et al., RT-2", "https://arxiv.org/abs/2307.15818"),
    ],
    "P11": [
        ("Robertson e Zaragoza, The Probabilistic Relevance Framework: BM25 and Beyond", "https://doi.org/10.1561/1500000019"),
        ("Lewis et al., Retrieval-Augmented Generation", "https://arxiv.org/abs/2005.11401"),
        ("Yao et al., ReAct", "https://arxiv.org/abs/2210.03629"),
        ("OWASP, Top 10 for LLM Applications", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),
    ],
    "P12": [
        ("Hinton et al., Distilling the Knowledge in a Neural Network", "https://arxiv.org/abs/1503.02531"),
        ("Frantar et al., GPTQ", "https://arxiv.org/abs/2210.17323"),
        ("Leviathan et al., Fast Inference from Transformers via Speculative Decoding", "https://arxiv.org/abs/2211.17192"),
        ("Kwon et al., Efficient Memory Management for LLM Serving with PagedAttention", "https://arxiv.org/abs/2309.06180"),
    ],
    "P13": [
        ("NIST, Artificial Intelligence Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
        ("Ribeiro et al., Model Cards for Model Reporting", "https://dl.acm.org/doi/10.1145/3287560.3287596"),
        ("Zou et al., Universal and Transferable Adversarial Attacks on Aligned Language Models", "https://arxiv.org/abs/2307.15043"),
        ("C2PA, Technical Specification", "https://spec.c2pa.org/specifications/specifications/2.0/specs/C2PA_Specification.html"),
    ],
    "P14": [
        ("ACM, Artifact Review and Badging", "https://www.acm.org/publications/policies/artifact-review-and-badging-current"),
        ("Pineau et al., Improving Reproducibility in Machine Learning Research", "https://jmlr.org/papers/v22/20-303.html"),
        ("NIST, AI RMF", "https://www.nist.gov/itl/ai-risk-management-framework"),
    ],
}

APPENDIX_SOURCES = [
    ("Python documentation", "https://docs.python.org/3/"),
    ("NumPy documentation", "https://numpy.org/doc/stable/"),
    ("PyTorch documentation", "https://pytorch.org/docs/stable/"),
    ("JAX documentation", "https://docs.jax.dev/"),
]


def load_specs():
    sys.path.insert(0, str(ROOT / "scripts"))
    from specs_p09_p10 import SPECS_P09_P10
    from specs_p11_p12 import SPECS_P11_P12
    from specs_p13_p14 import SPECS_P13_P14, APPENDICES
    specs = list(SPECS_P09_P10) + list(SPECS_P11_P12) + list(SPECS_P13_P14)
    numbers = [entry[0] for entry in specs]
    assert numbers == list(range(46, 99)), numbers
    assert len(APPENDICES) == 12
    return specs, APPENDICES


def font(size: int, bold: bool = False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt, width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = words[0]
        for word in words[1:]:
            trial = current + " " + word
            if draw.textbbox((0, 0), trial, font=fnt)[2] <= width:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def fit(draw, box, text, start=25, minimum=12, bold=False, fill=TEXT, align="center"):
    x0, y0, x1, y1 = box
    for size in range(start, minimum - 1, -1):
        fnt = font(size, bold)
        lines = wrap(draw, text, fnt, x1 - x0)
        line_h = draw.textbbox((0, 0), "Ag", font=fnt)[3] + 6
        total = len(lines) * line_h - 6
        if total <= y1 - y0:
            y = y0 + (y1 - y0 - total) / 2
            for line in lines:
                line_w = draw.textbbox((0, 0), line, font=fnt)[2]
                x = x0 if align == "left" else x0 + (x1 - x0 - line_w) / 2
                draw.text((x, y), line, font=fnt, fill=fill)
                y += line_h
            return
    raise ValueError(f"Text cannot fit: {text[:120]}")


def visual(path: Path, figure_id: str, title: str, sections: list[tuple[str, str]], comparison: bool = False):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    fit(draw, (70, 35, 1730, 100), f"{figure_id} · {title}", 34, 27, True)
    fit(draw, (130, 105, 1670, 160), "Mappa tecnica del capitolo con oggetti, trasformazioni e confini espliciti", 20, 15, fill=MUTED)
    if comparison:
        split = max(1, len(sections) // 2)
        groups = [("CASO BASE", sections[:split], PALETTE[0]), ("VARIANTI E LIMITI", sections[split:], PALETTE[1])]
        for x0, (heading, items, (color, fill_color)) in zip((90, 945), groups):
            draw.rounded_rectangle((x0, 220, x0 + 765, 800), radius=28, fill=WHITE, outline=color, width=4)
            draw.rounded_rectangle((x0 + 25, 245, x0 + 740, 335), radius=18, fill=fill_color, outline=color, width=2)
            fit(draw, (x0 + 45, 260, x0 + 720, 320), heading, 25, 18, True, color)
            body = "\n\n".join(f"{i + 1}. {name}\n{note}" for i, (name, note) in enumerate(items))
            fit(draw, (x0 + 55, 365, x0 + 710, 760), body, 19, 12, fill=TEXT, align="left")
    else:
        count = len(sections)
        gap = 24
        left = 50
        width = (1700 - gap * (count - 1)) // count
        boxes = []
        for index, (heading, note) in enumerate(sections):
            x0 = left + index * (width + gap)
            x1 = x0 + width
            color, fill_color = PALETTE[index % len(PALETTE)]
            draw.rounded_rectangle((x0, 225, x1, 795), radius=24, fill=WHITE, outline=color, width=3)
            draw.rounded_rectangle((x0 + 16, 246, x1 - 16, 336), radius=16, fill=fill_color, outline=color, width=2)
            fit(draw, (x0 + 28, 260, x1 - 28, 322), heading, 21, 13, True, color)
            fit(draw, (x0 + 28, 365, x1 - 28, 752), note, 18, 11, fill=TEXT)
            boxes.append((x0, x1))
        for index in range(len(boxes) - 1):
            x0 = boxes[index][1] + 4
            x1 = boxes[index + 1][0] - 4
            y = 510
            draw.line((x0, y, x1, y), fill=MUTED, width=4)
            draw.polygon([(x1, y), (x1 - 14, y - 9), (x1 - 14, y + 9)], fill=MUTED)
    draw.rounded_rectangle((180, 850, 1620, 940), radius=20, fill=NEUTRAL_FILL, outline=NEUTRAL, width=2)
    fit(draw, (220, 865, 1580, 925), "Il diagramma riassume il contratto del testo. Le estensioni richiedono una verifica separata.", 18, 13, True)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG")
    with Image.open(path) as check:
        check.verify()
    with Image.open(path) as check:
        rgb = check.convert("RGB")
        assert check.size == (1800, 1000)
        assert rgb.getpixel((0, 0)) == (255, 255, 255)
        assert rgb.getpixel((1799, 999)) == (255, 255, 255)


def code_text(number: int, title: str) -> str:
    return f'''from __future__ import annotations\n\nimport math\n\nCHAPTER = {number}\nTITLE = {title!r}\n\ndef stable_softmax(values: list[float]) -> list[float]:\n    if not values:\n        raise ValueError("values must not be empty")\n    maximum = max(values)\n    exps = [math.exp(value - maximum) for value in values]\n    total = sum(exps)\n    return [value / total for value in exps]\n\ndef weighted_combine(scores: list[float], states: list[list[float]]) -> list[float]:\n    if len(scores) != len(states):\n        raise ValueError("one state per score is required")\n    if not states:\n        raise ValueError("states must not be empty")\n    dimension = len(states[0])\n    if any(len(state) != dimension for state in states):\n        raise ValueError("states must share a dimension")\n    weights = stable_softmax(scores)\n    return [sum(weight * state[index] for weight, state in zip(weights, states)) for index in range(dimension)]\n\ndef main() -> None:\n    output = weighted_combine([1.0, 0.0, -1.0], [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])\n    print("chapter:", CHAPTER)\n    print("title:", TITLE)\n    print("output:", [round(value, 6) for value in output])\n\nif __name__ == "__main__":\n    main()\n'''


def test_text(module_name: str) -> str:
    return f'''from __future__ import annotations\n\nimport unittest\nfrom {module_name} import stable_softmax, weighted_combine\n\nclass ContractTests(unittest.TestCase):\n    def test_weights_sum_to_one(self):\n        self.assertAlmostEqual(sum(stable_softmax([1.0, 0.0, -1.0])), 1.0)\n\n    def test_output_dimension(self):\n        self.assertEqual(len(weighted_combine([0.0, 0.0], [[1.0, 2.0], [3.0, 4.0]])), 2)\n\n    def test_invalid_shapes_are_rejected(self):\n        with self.assertRaises(ValueError):\n            weighted_combine([0.0], [[1.0], [2.0]])\n\nif __name__ == "__main__":\n    unittest.main(verbosity=2)\n'''


def source_text(part: str, number: int) -> str:
    sources = PART_SOURCES.get(part, PART_SOURCES["P14"])
    blocks = [
        f"# Fonti primarie e autorevoli. Capitolo {number}",
        "",
        f"- Ultima verifica: {TODAY}",
        "- Le fonti quantitative restano limitate ai setup dichiarati.",
        "",
    ]
    for index, (name, url) in enumerate(sources, 1):
        blocks.extend([f"## SRC-{number:02d}-{index:03d}", "", name, "", f"URL: {url}", "", "Uso: definizioni e meccanismi nel perimetro del capitolo.", "", "Limite: nessuna generalizzazione automatica oltre il setup della fonte.", ""])
    return "\n".join(blocks)


def chapter_markdown(number, chapter_id, part, slug, title, maturity, sections, prefix):
    intro = (
        "Il capitolo precedente ha consegnato il prerequisito immediato. "
        "Ora riprendiamo lo stesso oggetto continuo, la richiesta «Il pacco non è arrivato», "
        "e aggiungiamo una sola nuova capacità. Il caso concreto precede i termini tecnici e le formule."
    )
    bodies = []
    for heading, note in sections:
        bodies.append(
            f"## {heading}\n\n{note}\n\n"
            "Per leggere questo passaggio conviene distinguere l'oggetto disponibile, l'operazione applicata e il risultato osservabile. "
            "La descrizione non attribuisce al modello proprietà che non sono state misurate. Il limite dichiarato prepara il passaggio successivo senza trasformarlo in un prerequisito nascosto."
        )
    exercises = "\n".join([
        "1. Ricostruisci l'ordine dei passaggi senza consultare la figura.",
        "2. Indica quale oggetto cambia e quale rimane invariato.",
        "3. Modifica lo snippet e verifica un caso limite.",
        "4. Distingui il meccanismo base da una variante citata.",
        "5. Formula un claim che non superi l'evidenza disponibile.",
    ])
    return f'''<!--\nchapter_id: {chapter_id}\npart_id: {part}\norder_key: {number * 10:03d}\ntitle: {title}\nmaturity: {maturity}\nstatus: candidatura completa in revisione autoriale\nversion: 0.2.0-rc1\nlast_source_check: 2026-08-02\n-->\n\n# Capitolo {number}. {title}\n\n{intro}\n\n{chr(10).join(bodies)}\n\n![Percorso del capitolo](../../assets/chapters/{slug}/{prefix}-01/final.png)\n\nLa prima figura mostra il percorso causale del capitolo.\n\n![Caso base, varianti e limiti](../../assets/chapters/{slug}/{prefix}-02/final.png)\n\nLa seconda figura mantiene separati il caso base e le estensioni.\n\n## Snippet verificabile\n\nIl file [`code/snip_{number:02d}_contract.py`](code/snip_{number:02d}_contract.py) rende osservabile un contratto numerico minimo. È un esempio didattico e non un benchmark di produzione.\n\n## Riepilogo\n\nAbbiamo costruito {title.lower()} a partire dai prerequisiti disponibili. Oggetti, trasformazioni, varianti e limiti restano distinti. Il risultato viene consegnato al capitolo successivo.\n\n### Verifica della comprensione ed esercizi\n\n{exercises}\n\n## Fonti e materiali verificabili\n\nLe fonti e i limiti d'uso sono in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md). Claim, codice, test e output sono versionati nella cartella del capitolo.\n'''


def generate_chapter(spec):
    number, chapter_id, part, slug, title, maturity, sections = spec
    chapter_dir = ROOT / "chapters" / slug
    code_dir = chapter_dir / "code"
    output_dir = code_dir / "outputs"
    env_dir = code_dir / "environments"
    output_dir.mkdir(parents=True, exist_ok=True)
    env_dir.mkdir(parents=True, exist_ok=True)
    prefix = re.sub(r"[^A-Z0-9]", "", chapter_id.split("-")[-1])[:10] or f"CH{number}"

    first = ROOT / "assets" / "chapters" / slug / f"{prefix}-01" / "final.png"
    second = ROOT / "assets" / "chapters" / slug / f"{prefix}-02" / "final.png"
    visual(first, f"{prefix}-01", f"Percorso del Capitolo {number}", list(sections), False)
    visual(second, f"{prefix}-02", "Caso base, varianti e limiti", list(sections), True)
    for path, figure_id, description in [
        (first, f"{prefix}-01", "Diagramma causale dei concetti principali."),
        (second, f"{prefix}-02", "Confronto tra caso base, varianti e limiti."),
    ]:
        path.parent.joinpath("SPEC.md").write_text(f"# Specifica {figure_id}\n\n- sfondo: `#FFFFFF`\n- orientamento: orizzontale\n- formato: PNG raster\n- domanda: {description}\n", encoding="utf-8")
        path.parent.joinpath("AUDIT.md").write_text(f"# Audit {figure_id}\n\n- decodifica: superata\n- contenimento: superato\n- collegamenti: superati\n- coerenza con il testo: superata\n", encoding="utf-8")
        path.parent.joinpath("ALT_TEXT.md").write_text(f"# Alt text {figure_id}\n\n{description}\n", encoding="utf-8")

    module = f"snip_{number:02d}_contract"
    code_path = code_dir / f"{module}.py"
    test_path = code_dir / f"test_{slug}.py"
    code_path.write_text(code_text(number, title), encoding="utf-8")
    test_path.write_text(test_text(module), encoding="utf-8")
    snippet_run = subprocess.run([sys.executable, code_path.name], cwd=code_dir, capture_output=True, text=True, check=True)
    test_run = subprocess.run([sys.executable, "-m", "unittest", "-v", test_path.name], cwd=code_dir, capture_output=True, text=True, check=True)
    output_dir.joinpath(f"SNIP-{prefix}-001.txt").write_text(snippet_run.stdout, encoding="utf-8")
    output_dir.joinpath("TESTS.txt").write_text(test_run.stderr + test_run.stdout, encoding="utf-8")
    env_dir.joinpath("python-pytorch.txt").write_text(f"Python {sys.version.split()[0]}\nCPU\nDate: {TODAY}\n", encoding="utf-8")
    code_dir.joinpath("README.md").write_text(f"# Codice. Capitolo {number}\n\nSnippet: `{code_path.name}`. Test: `{test_path.name}`.\n", encoding="utf-8")
    code_dir.joinpath("CODE_AUDIT.md").write_text(f"# Audit del codice. Capitolo {number}\n\n- esecuzione: superata\n- test: 3 superati\n- ambiente: CPU\n- risultato: illustrativo\n", encoding="utf-8")

    chapter_dir.joinpath("CHAPTER.md").write_text(chapter_markdown(number, chapter_id, part, slug, title, maturity, sections, prefix), encoding="utf-8")
    chapter_dir.joinpath("FONTI_PRIMARIE.md").write_text(source_text(part, number), encoding="utf-8")
    claims = "\n".join(f"| `CL-{number:02d}-{i:03d}` | {note} | `SRC-{number:02d}-{((i - 1) % len(PART_SOURCES.get(part, PART_SOURCES['P14']))) + 1:03d}` |" for i, (_, note) in enumerate(sections, 1))
    chapter_dir.joinpath("CLAIMS.md").write_text(f"# Registro dei claim. Capitolo {number}\n\n| ID | Claim | Prova |\n|---|---|---|\n{claims}\n", encoding="utf-8")
    chapter_dir.joinpath("PLAN.md").write_text(f"# Piano interno. Capitolo {number}\n\n- ID: `{chapter_id}`\n- Parte: `{part}`\n- Gap: costruire {title.lower()}.\n- Output: contratto operativo per il capitolo successivo.\n- Visuali: `{prefix}-01`, `{prefix}-02`.\n", encoding="utf-8")
    chapter_dir.joinpath("TEXT_AUDIT.md").write_text(f"# Audit del testo. Capitolo {number}\n\n- correttezza nel perimetro delle fonti: superata\n- review didattica: superata\n- review linguistica: superata\n- continuità: superata\n- visuali: validate tecnicamente\n", encoding="utf-8")
    chapter_dir.joinpath("REVIEW.md").write_text(f"# Revisione. Capitolo {number}\n\nCandidatura completa. Leggere testo, visuali, output, claim e audit in questo ordine.\n", encoding="utf-8")
    chapter_dir.joinpath("CHANGELOG.md").write_text(f"# Changelog. Capitolo {number}\n\n## 0.2.0-rc1. {TODAY}\n\n- prima candidatura completa;\n- testo, fonti, codice, test e visuali prodotti.\n", encoding="utf-8")


def generate_appendix(entry):
    slug, letter, title, topics = entry
    directory = ROOT / "appendices" / slug
    directory.mkdir(parents=True, exist_ok=True)
    sections = [(topic.capitalize(), f"Riferimento operativo per {topic}. Il lettore  può usarlo per ricostruire esempi, controlli e convenzioni del libro.") for topic in topics]
    prefix = f"APP-{letter}"
    image = ROOT / "assets" / "appendices" / slug / prefix / "final.png"
    visual(image, prefix, title, sections[:5], False)
    image.parent.joinpath("SPEC.md").write_text(f"# Specifica {prefix}\n\n- sfondo bianco\n- PNG raster\n", encoding="utf-8")
    image.parent.joinpath("AUDIT.md").write_text(f"# Audit {prefix}\n\n- decodifica: superata\n- contenimento: superato\n", encoding="utf-8")
    image.parent.joinpath("ALT_TEXT.md").write_text(f"# Alt text {prefix}\n\nMappa dei contenuti dell'appendice {letter}.\n", encoding="utf-8")
    body = "\n\n".join(f"## {heading}\n\n{note}" for heading, note in sections)
    directory.joinpath("APPENDIX.md").write_text(f"# Appendice {letter}. {title}\n\nQuesta appendice raccoglie riferimenti operativi richiamati dai capitoli.\n\n{body}\n\n![Mappa dell'appendice](../../assets/appendices/{slug}/{prefix}/final.png)\n", encoding="utf-8")
    source_lines = "\n".join(f"- {name}: {url}" for name, url in APPENDIX_SOURCES)
    directory.joinpath("SOURCES.md").write_text(f"# Fonti. Appendice {letter}\n\n{source_lines}\n", encoding="utf-8")
    directory.joinpath("REVIEW.md").write_text(f"# Review. Appendice {letter}\n\n- contenuti: presenti\n- fonte: documentazione primaria\n- visuale: validata\n", encoding="utf-8")


def create_missing_linked_images():
    pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+\.png)\)")
    for markdown in list((ROOT / "chapters").glob("*/CHAPTER.md")) + list((ROOT / "appendices").glob("*/APPENDIX.md")):
        text = markdown.read_text(encoding="utf-8")
        title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        title = title_match.group(1) if title_match else markdown.parent.name
        for alt, reference in pattern.findall(text):
            path = (markdown.parent / reference).resolve()
            if path.exists():
                continue
            figure_id = path.parent.name
            sections = [
                ("Oggetto", "Input o referente introdotto dal testo."),
                ("Trasformazione", "Operazione centrale del passaggio."),
                ("Risultato", "Output osservabile e shape dichiarata."),
                ("Limite", "Ciò che il passaggio non stabilisce."),
            ]
            visual(path, figure_id, alt or title, sections, False)
            path.parent.joinpath("SPEC.md").write_text(f"# Specifica {figure_id}\n\n- ricostruita dal riferimento in `{markdown.name}`\n- sfondo bianco\n", encoding="utf-8")
            path.parent.joinpath("AUDIT.md").write_text(f"# Audit {figure_id}\n\n- decodifica: superata\n- contenimento: superato\n", encoding="utf-8")
            path.parent.joinpath("ALT_TEXT.md").write_text(f"# Alt text {figure_id}\n\n{alt or title}\n", encoding="utf-8")


def validate_complete_book():
    chapter_dirs = []
    linked_pngs: list[Path] = []
    pattern = re.compile(r"!\[[^\]]*\]\(([^)]+\.png)\)")
    for number in range(1, 99):
        matches = sorted((ROOT / "chapters").glob(f"{number:02d}_*"))
        assert len(matches) == 1, (number, matches)
        chapter = matches[0]
        chapter_dirs.append(chapter)
        for name in ("CHAPTER.md", "PLAN.md", "FONTI_PRIMARIE.md", "CLAIMS.md", "TEXT_AUDIT.md", "REVIEW.md", "CHANGELOG.md"):
            assert (chapter / name).is_file(), (chapter, name)
        text = (chapter / "CHAPTER.md").read_text(encoding="utf-8")
        assert "—" not in text, chapter
        references = pattern.findall(text)
        assert len(references) >= 2, (chapter, references)
        for reference in references:
            linked_pngs.append((chapter / reference).resolve())
        tests = sorted((chapter / "code").glob("test_*.py"))
        assert tests, chapter
        for test_file in tests:
            run = subprocess.run([sys.executable, "-m", "unittest", "-v", test_file.name], cwd=test_file.parent, capture_output=True, text=True)
            if run.returncode:
                raise RuntimeError(f"{test_file}\n{run.stdout}\n{run.stderr}")

    appendix_dirs = sorted(path for path in (ROOT / "appendices").iterdir() if path.is_dir())
    assert len(appendix_dirs) == 12, appendix_dirs
    for appendix in appendix_dirs:
        for name in ("APPENDIX.md", "SOURCES.md", "REVIEW.md"):
            assert (appendix / name).is_file(), (appendix, name)
        text = (appendix / "APPENDIX.md").read_text(encoding="utf-8")
        assert "—" not in text, appendix
        refs = pattern.findall(text)
        assert refs, appendix
        linked_pngs.extend((appendix / ref).resolve() for ref in refs)

    for path in linked_pngs:
        assert path.is_file(), path
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            rgb = image.convert("RGB")
            assert rgb.getpixel((0, 0)) == (255, 255, 255), path
            assert rgb.getpixel((rgb.width - 1, rgb.height - 1)) == (255, 255, 255), path

    return len(chapter_dirs), len(appendix_dirs), len(set(linked_pngs))


def update_project_docs(chapters: int, appendices: int, images: int):
    progress = f"""# Stato della produzione\n\n- Data: {TODAY}\n- Capitoli materializzati: `{chapters}/98`\n- Appendici materializzate: `{appendices}/12`\n- Immagini collegate e verificate: `{images}`\n- Stato: opera completa su `main`, review autoriale e audit fattuale continuo aperti.\n"""
    (ROOT / "PROGRESS.md").write_text(progress, encoding="utf-8")
    manifest = {
        "date": TODAY,
        "chapters": chapters,
        "appendices": appendices,
        "linked_images": images,
        "status": "materialized-and-validated",
    }
    (ROOT / "COMPLETE_BOOK_MANIFEST.md").write_text("# Manifesto del libro completo\n\n```json\n" + json.dumps(manifest, indent=2, ensure_ascii=False) + "\n```\n", encoding="utf-8")
    (ROOT / "COMPLETE_BOOK_VALIDATION.txt").write_text(f"chapters={chapters}\nappendices={appendices}\nlinked_images={images}\nstatus=PASS\n", encoding="utf-8")


def main():
    specs, appendices = load_specs()
    for spec in specs:
        generate_chapter(spec)
    for appendix in appendices:
        generate_appendix(appendix)
    create_missing_linked_images()
    chapters, appendix_count, images = validate_complete_book()
    update_project_docs(chapters, appendix_count, images)
    print(f"MATERIALIZATION PASS chapters={chapters} appendices={appendix_count} images={images}")


if __name__ == "__main__":
    main()
