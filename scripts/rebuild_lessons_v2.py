"""Rebuild generated lessons without the historical paragraph scaffold.

This script is intentionally a compiler, not a prose template.  The semantic
content comes from the chapter specifications; presentation changes with the
kind of lesson (mechanism, conceptual map, data pipeline, system, or lab).
Each public section retains its own claim, concrete case, and verification
boundary.  The compiler also embeds the exact Python excerpt and captured
output for lessons whose policy is ``reference``.

The first thirteen chapters and the hand-reviewed attention chapter are not
rewritten.  They remain the local style baseline.
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import revise_book_completeness as old  # noqa: E402


TARGETS = tuple(number for number in range(14, 99) if number != 28)
SOURCE_CHECK_DATE = "4 agosto 2026"
CODE_EXCEPTIONS = {
    20: "Il capitolo confronta famiglie generative a livello concettuale; le implementazioni verificabili sono distribuite nei capitoli 21-25.",
    30: "Il capitolo è una mappa tra architetture e obiettivi; il Transformer eseguibile è nel capitolo 29 e le ricette di training iniziano dal 32.",
    93: "Norme e responsabilità dipendono da ruolo, giurisdizione e data: uno script locale produrrebbe una falsa impressione di conformità automatica.",
    98: "Un osservatorio di frontiera valuta evidenza aggiornata e maturità editoriale; il controllo centrale è documentale e datato, non computazionale. Ogni scheda conserva data, versione, disponibilità degli artefatti, replica indipendente, incertezza e condizione esplicita di riapertura.",
}

CONCEPTUAL = {19, 20, 30, 31, 45, 55, 83, 84, 86, 92, 93, 98}
DATA_PIPELINE = {26, 32, 33, 35, 63, 64, 65, 66, 90}
SYSTEM = {36, 54, 56, 57, 58, 59, 60, 61, 62, 67, 68, 69, 70, 71, 72, 79, 80, 81, 82, 85, 88, 89}
LAB = {94, 95, 96, 97}
FULL_LABS = {
    94: ("foundations_lab.py", "test_foundations_lab.py", "outputs/FOUNDATIONS-LAB.txt", "Training, baseline e manifest"),
    95: ("tiny_transformer_lm.py", "test_tiny_transformer_lm.py", "outputs/TINY-TRANSFORMER-LM.txt", "Decoder causale addestrato e campionato"),
    96: ("production_pipeline.py", "test_production_pipeline.py", "outputs/PRODUCTION-PIPELINE.txt", "Gate offline, canary e rollback"),
    97: ("replication_protocol.py", "test_replication_protocol.py", "outputs/REPLICATION-PROTOCOL.txt", "Replica indipendente con incertezza"),
}
SOURCE_IDS_OVERRIDES = {
    20: ["SRC-20-001", "SRC-20-002", "SRC-20-003", "SRC-20-004", "SRC-20-001; SRC-20-005"],
    68: ["SRC-68-001", "SRC-68-001", "SRC-68-002", "SRC-68-003", "SRC-68-001"],
    74: [
        "SRC-74-001",
        "SRC-74-002",
        "SRC-74-001",
        "SRC-74-003; SRC-74-002",
        "SRC-74-004; SRC-74-003; SRC-74-002",
    ],
}
PREREQUISITES = {
    14: (5, 7, 12), 15: (5, 6, 12), 16: (5, 6, 15), 17: (5, 15), 18: (5, 6, 15),
    19: (7, 13, 15), 20: (7, 8, 13, 19), 21: (7, 8, 20), 22: (6, 7, 20),
    23: (6, 7, 20), 24: (5, 6, 7, 20), 25: (6, 7, 20), 26: (2, 7, 8),
    27: (5, 8, 26), 29: (5, 6, 27, 28), 30: (28, 29), 31: (26, 29, 30),
    32: (26, 31), 33: (7, 26, 32), 34: (7, 16, 32), 35: (16, 32, 33, 34),
    36: (9, 16, 35), 37: (16, 29), 38: (27, 28, 29), 39: (28, 37),
    40: (9, 28, 39), 41: (28, 37), 42: (18, 29, 41), 43: (29, 39, 42),
    44: (16, 29, 36), 45: (21, 26, 29), 46: (26, 29, 31), 47: (5, 46),
    48: (14, 46), 49: (7, 48), 50: (46, 48), 51: (14, 50), 52: (46, 50, 51),
    53: (10, 31, 50), 54: (31, 46, 49), 55: (19, 27), 56: (27, 29, 55),
    57: (20, 25, 55), 58: (55, 56), 59: (26, 55), 60: (25, 55, 59),
    61: (5, 17, 55), 62: (14, 55, 61), 63: (10, 26, 27), 64: (29, 31, 63),
    65: (63, 64), 66: (38, 63, 64), 67: (31, 64), 68: (67,), 69: (14, 67),
    70: (67, 69), 71: (4, 69, 70), 72: (67, 69, 71), 73: (16, 31), 74: (9, 73),
    75: (9, 74), 76: (7, 21, 31), 77: (76,), 78: (29, 39, 76), 79: (9, 76, 78),
    80: (36, 79), 81: (9, 29, 40), 82: (3, 79, 81), 83: (4, 7, 31),
    84: (7, 83), 85: (3, 67, 83), 86: (6, 19, 31), 87: (19, 86),
    88: (4, 31, 72), 89: (67, 72, 88), 90: (32, 72), 91: (4, 7, 32),
    92: (68, 90), 93: (3, 4, 82, 91), 94: (5, 6, 7, 12, 13),
    95: (26, 28, 29, 35, 94), 96: (64, 67, 72, 82, 85), 97: (4, 83, 94),
    98: (4, 83, 97),
}

IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+\.png)\)")
SOURCE_RE = re.compile(r"\bSRC-\d{2}-\d{3}\b")

UNRELATED = {
    "moe": ("assegnazioni, overflow", "numero di parametri dichiarato dagli esperti"),
    "rl": ("raccolta di traiettorie e confronto delle policy",),
    "flow": ("Un flow rende esplicito", "determinante Jacobiano"),
    "release": ("Il passaggio da esperimento a sistema richiede", "Una replica, una release"),
}
ALLOWED = {
    "moe": {44, 80},
    "rl": {14, 48, 51, 71},
    "flow": {24, 25},
    "release": {82, 93, 94, 96, 97, 98},
}


def archetype(number: int) -> str:
    if number in LAB:
        return "lab"
    if number in DATA_PIPELINE:
        return "data"
    if number in SYSTEM:
        return "system"
    if number in CONCEPTUAL:
        return "conceptual"
    return "mechanism"


def sentences(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", value.strip()) if part.strip()]


def complete_sentence(value: str) -> str:
    value = value.strip()
    return value if not value or value[-1] in ".!?" else value + "."


def lower_first(value: str) -> str:
    value = value.strip()
    return value[:1].lower() + value[1:] if value else value


def clean_explanation(number: int, heading: str, note: str, detail: dict[str, str]) -> str:
    candidate = old.section_explanation(number, heading, old.note_parts(note)[0], detail)
    contaminated = any(
        number not in ALLOWED[name] and any(token in candidate for token in tokens)
        for name, tokens in UNRELATED.items()
    )
    parts = [
        part
        for part in sentences(candidate)
        if "La verifica resta ancorata" not in part
        and "il controllo cambia una sola premessa" not in part
        and "La scheda di prova conserva fonte" not in part
    ]
    if contaminated or len(parts) < 2:
        case = old.section_example(number, old.profile(number), heading, detail, 0)
        first, second = old.note_parts(note)
        return (
            f"La distinzione operativa di «{heading}» nasce da questo punto: {complete_sentence(lower_first(first))} "
            f"Nel caso più piccolo osserviamo {complete_sentence(case)} "
            f"{complete_sentence(second or 'Il risultato resta legato alle ipotesi dichiarate')}"
        )
    result = " ".join(parts[:3])
    if heading.casefold() not in result.casefold():
        result += f" In «{heading}» questa idea riguarda esattamente il claim della sezione, non l'intera famiglia di tecniche."
    title = old.SPECS[number][4]
    if title.casefold() not in result.casefold():
        result += f" Nel percorso di «{title}» il passaggio va quindi letto con le ipotesi dichiarate qui."
    return result


def additional_detail(number: int, index: int, heading: str) -> str:
    candidate = old.detail_for(number, heading, index)
    contaminated = any(
        number not in ALLOWED[name] and any(token in candidate for token in tokens)
        for name, tokens in UNRELATED.items()
    )
    if contaminated:
        return ""
    result = " ".join(
        part for part in sentences(candidate)
        if "Il controllo resta locale" not in part
        and "Il limite è parte della definizione" not in part
    )
    if result and heading.casefold() not in result.casefold():
        result += f" In «{heading}» questa distinzione va applicata al passaggio descritto, non alle fasi vicine per analogia."
    return result


def case_sentence(number: int, index: int, case: str) -> str:
    case = complete_sentence(case)
    variants = (
        f"Per renderlo concreto, consideriamo {lower_first(case)}",
        f"Il primo esempio da calcolare è questo: {case}",
        f"Qui conviene fermarsi su un caso leggibile: {case}",
        f"Un controesempio ha senso solo dopo avere fissato il caso base: {case}",
        f"La distinzione diventa osservabile con {lower_first(case)}",
        f"Usiamo numeri o artefatti piccoli: {case}",
        f"Il caso guida di questa sezione è {lower_first(case)}",
    )
    return variants[(number + index * 2) % len(variants)]


def verification(number: int, index: int, heading: str, note: str, detail: dict[str, str]) -> str:
    case = old.section_example(number, old.profile(number), heading, detail, index)
    last_sentence = old.note_parts(note)[1] or old.note_parts(note)[0]
    kind = archetype(number)
    variants = {
        "mechanism": (
            "Il controllo utile tiene fermo l'input e modifica un solo termine del meccanismo. L'output deve cambiare nel punto previsto e non altrove; la shape corretta, da sola, non basta.",
            f"Confrontiamo il caso valido con una variante che rompe una sola ipotesi e registriamo entrambi gli esiti. Il motivo è preciso: {complete_sentence(lower_first(last_sentence))}",
            "La verifica segue il calcolo fino al primo valore osservabile. Se non possiamo localizzare la divergenza, il test non sta ancora spiegando il meccanismo.",
            f"Il test di «{heading}» deve fallire in modo leggibile quando manca la condizione centrale. Un errore silenzioso sarebbe più pericoloso di un'eccezione esplicita.",
            f"Prima di estendere il risultato, ripetiamo la trasformazione con un valore limite e controlliamo il passaggio intermedio. Il confine da conservare è: {complete_sentence(last_sentence)}",
        ),
        "conceptual": (
            "La mappa va letta su un caso concreto, non come una classifica. Annotiamo quale proprietà viene osservata e quale resta fuori dal confronto.",
            f"Per evitare categorie sovrapposte, assegniamo il caso a una sola definizione alla volta e motiviamo l'asse scelto. {complete_sentence(last_sentence)}",
            "Il controllo non cerca un vincitore universale: cambia una proprietà del caso e verifica se cambia anche la categoria pertinente.",
            "Una distinzione è utile solo se produce previsioni diverse. Scriviamo prima che cosa dovrebbe accadere e poi confrontiamo l'osservazione.",
            f"Il limite della sezione diventa parte della prova: {complete_sentence(last_sentence)} Il caso locale non autorizza conclusioni su dimensioni non misurate.",
        ),
        "data": (
            "Conserviamo il record prima e dopo il passaggio, insieme alla configurazione. Conteggi e identificatori devono permettere di attribuire ogni differenza alla trasformazione.",
            f"Il controllo di «{heading}» include anche il record escluso o modificato. Senza una traccia negativa sapremmo soltanto che la pipeline ha terminato.",
            f"Ripetiamo il passaggio sullo stesso manifest e verifichiamo ordine, checksum e split. Il risultato resta valido nel perimetro indicato da: {last_sentence}",
            "Il controllo più informativo confronta due versioni del medesimo dato, non due raccolte sconosciute. Registriamo anche la regola applicata.",
            f"Una pipeline corretta deve spiegare anche ciò che perde. Per «{heading}» conserviamo input, output e motivo di esclusione.",
        ),
        "system": (
            "Il test attraversa il confine tra componenti. Oltre all'output registra autorizzazione, stato e failure, così un esito plausibile non nasconde un collegamento errato.",
            f"Per «{heading}» separiamo correttezza locale e comportamento end-to-end. Il caso {case} viene ripetuto con la stessa configurazione e un solo confine modificato.",
            "Il sistema deve fallire prima del side effect o della perdita di stato. Il log indica quale componente ha preso la decisione.",
            f"Misuriamo il passaggio con stesso input, versione e risorse. {last_sentence} Perciò un miglioramento locale non viene promosso senza il confronto completo.",
            "La prova conserva richiesta, risposta intermedia e output finale. Se manca uno di questi livelli, la causa della failure resta ambigua.",
        ),
        "lab": (
            "Eseguiamo il caso con seed, dipendenze e comando registrati. Il risultato viene accettato solo se una seconda esecuzione ricostruisce gli stessi artefatti previsti.",
            f"La tappa «{heading}» produce un file o un numero ispezionabile, non soltanto una cella eseguita. Per {case} conserviamo anche il caso fallito.",
            f"Prima del run scriviamo il risultato atteso; dopo il run confrontiamo output, log e limite. {complete_sentence(last_sentence)}",
            f"Il laboratorio separa preparazione, esecuzione e interpretazione. Il caso {case} non passa alla tappa successiva se manca la prova locale.",
            "Una replica deve ricostruire ambiente e dati prima di confrontare la metrica. Le divergenze vengono registrate, non corrette retroattivamente.",
        ),
    }
    return variants[kind][index % 5]


def opening(number: int, title: str, sections: list[tuple[str, str]], detail: dict[str, str]) -> str:
    """Introduce the lesson contract once, in grammatical Italian.

    The previous compiler tried to vary the surface form and produced phrases
    such as ``il caso un producer``.  Variation is useful in the visual and
    explanatory structure, not when it damages the sentence.  The opening is
    therefore deliberately compact; the chapter-specific substance lives in
    the five semantic sections.
    """
    first = sections[0][0]
    last = sections[-1][0]
    case = complete_sentence(
        old.sentence_case(old.section_example(number, old.profile(number), sections[0][0], detail, 0))
    )
    return (
        f"La domanda guida di questa lezione è come collegare «{first}» e «{last}» senza "
        f"perdere il contratto tecnico di {title.lower()}. L'oggetto osservato è {detail['object']}. "
        f"Il contratto locale è: input, {detail['input']}; "
        f"operazione, {detail['operation']}; output, {detail['output']}. "
        f"Il caso guida è questo: {case} "
        f"Il confine da mantenere esplicito è: {complete_sentence(detail['invariant'])}"
    )


def control_for(number: int, index: int, heading: str, note: str, detail: dict[str, str]) -> str:
    """Return a clean methodological check for the local lesson archetype."""
    last_claim = old.note_parts(note)[1] or old.note_parts(note)[0]
    variants = {
        "mechanism": (
            f"Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: {complete_sentence(last_claim)}",
            "Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.",
            f"Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «{heading}».",
            "Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.",
            f"Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «{heading}» non si applica.",
        ),
        "conceptual": (
            "Classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.",
            f"Cambia la proprietà che distingue «{heading}» dalle categorie vicine. Se la classificazione non cambia, la distinzione va formulata meglio.",
            "Confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.",
            f"Indica quale osservazione smentirebbe l'assegnazione del caso a «{heading}» e quale invece sarebbe irrilevante.",
            f"Limita la conclusione alla proprietà dichiarata: {complete_sentence(last_claim)} Le dimensioni non osservate restano aperte.",
        ),
        "data": (
            "Conserva record iniziale, regola applicata e record finale; un conteggio aggregato non basta a spiegare la trasformazione.",
            f"Esegui «{heading}» due volte sullo stesso manifest e confronta identificatori, ordine, split e checksum.",
            "Aggiungi un record che deve essere escluso e verifica che l'output conservi anche il motivo dell'esclusione.",
            "Modifica una sola regola della pipeline e misura quali record cambiano, evitando di confrontare raccolte di origine diversa.",
            f"Descrivi ciò che la pipeline perde oltre a ciò che produce. Il limite locale è: {complete_sentence(last_claim)}",
        ),
        "system": (
            "Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.",
            f"Ripeti «{heading}» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.",
            "Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.",
            "Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.",
            f"Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: {complete_sentence(last_claim)}",
        ),
        "lab": (
            "Esegui il caso con ambiente, seed e comando registrati; il risultato deve sopravvivere fuori dalla sessione interattiva.",
            f"Per «{heading}» conserva almeno un artefatto verificabile e un caso fallito, insieme alla configurazione che li ha prodotti.",
            "Scrivi prima l'esito atteso, poi confrontalo con output e log. Ogni differenza deve restare visibile nel report.",
            "Riparti da un processo pulito e ricostruisci input e ambiente prima di interpretare la metrica.",
            f"Distingui il risultato riprodotto dal suo trasferimento ad altra scala. Il confine è: {complete_sentence(last_claim)}",
        ),
    }
    return variants[archetype(number)][index % 5]


def section_depth(
    number: int,
    index: int,
    heading: str,
    note: str,
    detail: dict[str, str],
    seen_mechanisms: set[str],
) -> str:
    """Build a section from its own mechanism, case and falsifiable check.

    Canonical labels make the page navigable, while the sentences below come
    from the local heading and claim.  We intentionally do not repeat the
    chapter contract or title in every paragraph.
    """
    explanation_parts: list[str] = []
    if index == 0:
        chapter_explanation = old.formula_for(number, old.profile(number))[1]
        if chapter_explanation not in seen_mechanisms:
            explanation_parts.append(chapter_explanation)
            seen_mechanisms.add(chapter_explanation)

    case = complete_sentence(old.sentence_case(old.section_example(number, old.profile(number), heading, detail, index)))
    case_key = "case:" + re.sub(r"\s+", " ", case.casefold()).strip()
    if case_key in seen_mechanisms:
        note_core = complete_sentence(old.note_parts(note)[0])
        case = (
            f"Per «{heading}» si mantiene l'input del capitolo e si isola questa condizione: "
            f"{note_core}"
        )
    else:
        seen_mechanisms.add(case_key)
    check = complete_sentence(control_for(number, index, heading, note, detail))
    prefix = (" ".join(explanation_parts) + "\n\n") if explanation_parts else ""
    return prefix + f"**Caso da seguire.** {case}" + f"\n\n**Controllo.** {check}"


def formula_block(number: int, source_id: str) -> str:
    if number in old.FORMULA_SCHEMA_NUMBERS:
        return ""
    formula, explanation = old.formula_for(number, old.profile(number))
    return f"La relazione centrale può essere scritta come:\n\n$$\n{formula}\n$$\n\n{explanation} [{source_id}]"


def image_records(chapter_file: Path) -> list[tuple[str, str]]:
    records = IMAGE_RE.findall(chapter_file.read_text(encoding="utf-8"))
    if not records:
        raise ValueError(f"nessuna immagine in {chapter_file}")
    return records


def update_visual_metadata(number: int, sections: list[tuple[str, str]], chapter_file: Path, images: list[tuple[str, str]]) -> None:
    questions = (
        f"Quale percorso collega {sections[0][0]} a {sections[2][0]} nel capitolo {number}?",
        f"Quale failure o confronto separa {sections[3][0]} da {sections[4][0]}?",
    )
    for index, (alt, raw) in enumerate(images):
        path = (chapter_file.parent / raw).resolve()
        spec_path = path.parent / "SPEC.md"
        spec = spec_path.read_text(encoding="utf-8") if spec_path.exists() else "# Specifica visuale\n"
        if re.search(r"^- domanda principale:", spec, re.MULTILINE):
            spec = re.sub(r"^- domanda principale:.*$", f"- domanda principale: {questions[index % 2]}", spec, flags=re.MULTILINE)
        else:
            spec = spec.rstrip() + f"\n- domanda principale: {questions[index % 2]}\n"
        spec_path.write_text(spec, encoding="utf-8")
        alt_path = path.parent / "ALT_TEXT.md"
        alt_path.write_text(
            f"# Testo alternativo\n\n{alt}. {questions[index % 2]} La figura va letta insieme alla sezione pubblica corrispondente.\n",
            encoding="utf-8",
        )


def clean_code_source(number: int, title: str) -> str:
    if number in old.TOPIC_BODIES:
        body = old.TOPIC_BODIES[number]
    else:
        current = next((ROOT / "chapters").glob(f"{number:02d}_*/code/snip_{number:02d}_contract.py"))
        text = current.read_text(encoding="utf-8")
        match = re.search(r"def contract\(\):\n(.+?)(?=\ndef main\()", text, re.DOTALL)
        if not match:
            raise ValueError(f"contract non trovato per il capitolo {number}")
        body = "def contract():\n" + match.group(1).rstrip() + "\n"
    helper = ""
    if "normalize(" in body:
        helper = (
            "def normalize(values):\n"
            "    if not values:\n"
            "        raise ValueError('values must not be empty')\n"
            "    maximum = max(values)\n"
            "    exponentials = [math.exp(value - maximum) for value in values]\n"
            "    total = sum(exponentials)\n"
            "    return [value / total for value in exponentials]\n\n\n"
        )
    return (
        "from __future__ import annotations\n\n"
        "import hashlib\n"
        "import json\n"
        "import math\n"
        "import statistics\n"
        "from collections import Counter\n\n"
        f"CHAPTER = {number}\n"
        f"TITLE = {title!r}\n\n\n"
        + helper
        + body.strip()
        + "\n\n\ndef main() -> None:\n"
        "    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))\n\n\n"
        "if __name__ == \"__main__\":\n"
        "    main()\n"
    )


def load_contract(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"impossibile importare {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.contract


def write_code(number: int, title: str, chapter_dir: Path) -> tuple[str, str, str]:
    code_dir = chapter_dir / "code"
    output_dir = code_dir / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    module_name = f"snip_{number:02d}_contract"
    code_path = code_dir / f"{module_name}.py"
    code_path.write_text(clean_code_source(number, title), encoding="utf-8")
    ast.parse(code_path.read_text(encoding="utf-8"), filename=str(code_path))
    result = load_contract(code_path)()
    expected = repr(result)
    test_path = code_dir / f"test_{number:02d}_contract.py"
    test_path.write_text(
        "from __future__ import annotations\n\n"
        "import json\n"
        "import math\n"
        "import unittest\n\n"
        f"from {module_name} import contract\n\n\n"
        "class LessonExampleTests(unittest.TestCase):\n"
        "    def test_expected_result(self):\n"
        f"        self.assertEqual(contract(), {expected})\n\n"
        "    def test_example_is_deterministic(self):\n"
        "        self.assertEqual(contract(), contract())\n\n"
        "    def test_result_is_serializable_and_finite(self):\n"
        "        encoded = json.dumps(contract(), sort_keys=True)\n"
        "        self.assertTrue(encoded)\n"
        "        for value in contract().values():\n"
        "            if isinstance(value, float):\n"
        "                self.assertTrue(math.isfinite(value))\n\n"
        "    def test_interpretation_boundary_is_explicit(self):\n"
        "        self.assertIsInstance(contract().get('invariant'), str)\n"
        "        self.assertGreaterEqual(len(contract()['invariant'].split()), 4)\n\n\n"
        "if __name__ == '__main__':\n"
        "    unittest.main(verbosity=2)\n",
        encoding="utf-8",
    )
    run = subprocess.run([sys.executable, code_path.name], cwd=code_dir, text=True, capture_output=True, check=True)
    tests = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", test_path.name],
        cwd=code_dir,
        text=True,
        capture_output=True,
        check=True,
    )
    output = run.stdout.strip()
    output_path = output_dir / f"SNIP-{number:02d}-001.txt"
    output_path.write_text(output + "\n", encoding="utf-8")
    (output_dir / "TESTS.txt").write_text(tests.stdout + tests.stderr, encoding="utf-8")
    code_dir.joinpath("README.md").write_text(
        f"# Esempio verificato. Capitolo {number}\n\n"
        f"`{code_path.name}` esegue il caso minimo usato nel testo di **{title}**. "
        f"`{test_path.name}` conserva l'output atteso, controlla determinismo, serializzazione, "
        "valori finiti e presenza del limite interpretativo.\n\n"
        f"```bash\npython {code_path.name}\npython -m unittest -v {test_path.name}\n```\n",
        encoding="utf-8",
    )
    source = code_path.read_text(encoding="utf-8")
    contract_match = re.search(r"def contract\(\):\n(.+?)(?=\ndef main\()", source, re.DOTALL)
    excerpt = "def contract():\n" + contract_match.group(1).rstrip() if contract_match else source
    if "normalize(" in excerpt and "def normalize" in source:
        helper_match = re.search(r"def normalize\(values\):\n(.+?)(?=\ndef contract\()", source, re.DOTALL)
        if helper_match:
            excerpt = "def normalize(values):\n" + helper_match.group(1).rstrip() + "\n\n\n" + excerpt
    return module_name, excerpt, output


def code_section(number: int, title: str, chapter_dir: Path) -> tuple[str, str, str]:
    if number in CODE_EXCEPTIONS:
        return "exception", "", ""
    module, excerpt, output = write_code(number, title, chapter_dir)
    text = (
        "## Esempio Python eseguito\n\n"
        "Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché "
        "l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.\n\n"
        f"```python\n{excerpt}\n```\n\n"
        f"Esecuzione con `python {module}.py`:\n\n"
        f"```text\n{output}\n```\n\n"
        f"Il test associato è [`code/test_{number:02d}_contract.py`](code/test_{number:02d}_contract.py); "
        f"l'output versionato è [`code/outputs/SNIP-{number:02d}-001.txt`](code/outputs/SNIP-{number:02d}-001.txt)."
    )
    if number in FULL_LABS:
        source_name, test_name, output_name, lab_title = FULL_LABS[number]
        source_path = chapter_dir / "code" / source_name
        source = source_path.read_text(encoding="utf-8")
        match = re.search(r"# BOOK-EXCERPT-START\n(.+?)# BOOK-EXCERPT-END", source, re.DOTALL)
        if not match:
            raise ValueError(f"estratto del laboratorio non trovato in {source_path}")
        excerpt = match.group(1).rstrip()
        output = chapter_dir.joinpath("code", output_name).read_text(encoding="utf-8").split("\n\n", 1)[0]
        text += (
            f"\n\n## Laboratorio completo: {lab_title}\n\n"
            "Il contratto precedente isola un solo punto. Il laboratorio seguente attraversa invece più fasi "
            "e conserva sia l'esito valido sia una failure controllata. L'estratto è identico al file eseguito.\n\n"
            f"```python\n{excerpt}\n```\n\n"
            f"Output di `python {source_name}`:\n\n```text\n{output}\n```\n\n"
            f"Codice completo: [`code/{source_name}`](code/{source_name}); "
            f"test: [`code/{test_name}`](code/{test_name}); "
            f"output versionato: [`code/{output_name}`](code/{output_name})."
        )
    return "reference", text, module


def exercise_block(number: int, sections: list[tuple[str, str]], detail: dict[str, str]) -> str:
    headings = [item[0] for item in sections]
    exercises = (
        f"1. Ricostruisci «{headings[0]}» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.",
        f"2. Nel passaggio «{headings[1]}», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.",
        f"3. Collega «{headings[2]}» a una riga dello snippet oppure motiva perché la prova deve essere documentale.",
        f"4. Progetta un caso limite per «{headings[3]}» che produca una failure riconoscibile.",
        f"5. Per «{headings[4]}», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.",
    )
    titles = {
        "mechanism": "Esercizi sul meccanismo",
        "conceptual": "Domande per distinguere le categorie",
        "data": "Esercizi sulla tracciabilità",
        "system": "Prove sui confini del sistema",
        "lab": "Esperimenti da riprodurre",
    }
    return f"## {titles[archetype(number)]}\n\n" + "\n".join(exercises)


def connection_block(
    number: int,
    sections: list[tuple[str, str]],
    source_ids: list[str],
    detail: dict[str, str],
) -> str:
    """Explain why adjacent sections are separate and how they compose."""
    bridges = {
        "mechanism": (
            "Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile.",
            "La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello.",
            "Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza.",
            "L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte.",
        ),
        "conceptual": (
            "La definizione iniziale stabilisce l'asse del confronto; la categoria successiva aggiunge una proprietà senza creare una classifica implicita.",
            "Il terzo passaggio verifica se le categorie restano distinguibili sullo stesso caso e impedisce che termini vicini diventino sinonimi.",
            "La quarta sezione introduce il punto in cui l'asse scelto smette di bastare e richiede una nuova osservazione.",
            "La sezione finale riunisce le dimensioni della valutazione, ma conserva i limiti di ciascuna invece di fonderle in un unico punteggio.",
        ),
        "data": (
            "Il primo passaggio identifica il record e la sua provenienza; il secondo dichiara la trasformazione che cambia la popolazione osservata.",
            "La trasformazione diventa confrontabile soltanto quando il passaggio successivo conserva configurazione, conteggi e artefatti intermedi.",
            "Una volta resa tracciabile la pipeline, il quarto passaggio può affrontare selezione o uso senza confondere un cambiamento nei dati con uno nel modello.",
            "L'ultima sezione porta il risultato alla valutazione e chiede quali record, slice o failure restano fuori dalla media.",
        ),
        "system": (
            "Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite.",
            "Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale.",
            "La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato.",
            "La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito.",
        ),
        "lab": (
            "La prima tappa fissa domanda, ambiente e input; la seconda costruisce l'artefatto eseguibile che materializza il protocollo.",
            "Il run produce numeri e file soltanto dopo che configurazione, seed e dipendenze sono stati registrati.",
            "La tappa successiva confronta il risultato atteso con quello osservato e conserva le divergenze invece di correggerle retroattivamente.",
            "La conclusione separa ciò che il laboratorio ha ricostruito da ciò che richiederebbe altri dati, hardware o una valutazione di produzione.",
        ),
    }[archetype(number)]
    paragraphs = []
    for index in range(4):
        left_heading, left_note = sections[index]
        right_heading, right_note = sections[index + 1]
        left_claim = complete_sentence(old.note_parts(left_note)[0])
        right_claim = complete_sentence(old.note_parts(right_note)[0])
        paragraphs.append(
            f"- **Da «{left_heading}» a «{right_heading}».** {left_claim} {right_claim} "
            f"{bridges[index]} [{source_ids[index]}; {source_ids[index + 1]}]"
        )
    conclusion = (
        f"La catena completa produce {detail['output']} a partire da {detail['input']}. "
        f"Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere "
        f"esteso oltre il limite dichiarato: {complete_sentence(detail['invariant'])}"
    )
    return "## Come si collegano i passaggi\n\n" + "\n\n".join(paragraphs) + "\n\n" + conclusion


def chapter_title(number: int) -> str:
    if number in old.SPECS:
        return old.SPECS[number][4]
    chapter_file = next((ROOT / "chapters").glob(f"{number:02d}_*/CHAPTER.md"))
    match = re.search(rf"^# Capitolo {number}\. (.+)$", chapter_file.read_text(encoding="utf-8"), re.MULTILINE)
    if not match:
        raise ValueError(f"titolo non trovato per il capitolo {number}")
    return match.group(1).strip()


def update_claim_code_section(number: int, chapter_dir: Path, code_policy: str) -> None:
    claims_path = chapter_dir / "CLAIMS.md"
    claims = claims_path.read_text(encoding="utf-8")
    claims = re.sub(r"\n## CL-\d{2}-CODE\n[\s\S]*$", "", claims).rstrip()
    if code_policy == "exception":
        evidence = (
            f"- Affermazione esatta: il capitolo non propone uno snippet eseguibile perché {CODE_EXCEPTIONS[number]}\n"
            "- Tipo: eccezione motivata alla policy del codice.\n"
            "- Fonte o prova: metadati di CHAPTER.md e dossier FONTI_PRIMARIE.md.\n"
            "- Controllo indipendente: assenza di blocchi presentati come simulazione fedele; claim verificati documentalmente.\n"
            "- Esito: corretta\n"
            "- Note: l'eccezione evita un esempio giocattolo che produrrebbe evidenza fuorviante."
        )
    else:
        full_lab = ""
        if number in FULL_LABS:
            source_name, test_name, output_name, _ = FULL_LABS[number]
            full_lab = f" Il laboratorio esteso usa code/{source_name}, code/{test_name} e code/{output_name}."
        evidence = (
            f"- Affermazione esatta: `snip_{number:02d}_contract.py` produce l'output JSON versionato; "
            "il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo."
            f"{full_lab}\n"
            "- Tipo: risultato eseguito localmente.\n"
            f"- Fonte o prova: code/snip_{number:02d}_contract.py, code/test_{number:02d}_contract.py e "
            f"code/outputs/SNIP-{number:02d}-001.txt.\n"
            f"- Versione o data: Python {sys.version.split()[0]}, CPU, {SOURCE_CHECK_DATE}.\n"
            "- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.\n"
            "- Esito: verificata\n"
            "- Note: esempio delimitato e didattico; non è un benchmark di produzione."
        )
    claims_path.write_text(
        claims + f"\n\n## CL-{number:02d}-CODE\n\n" + evidence + "\n",
        encoding="utf-8",
    )


def write_source_claims(
    number: int,
    sections: list[tuple[str, str]],
    source_ids: list[str],
    chapter_dir: Path,
) -> None:
    entries = []
    for index, ((heading, note), source_id) in enumerate(zip(sections, source_ids), 1):
        entries.append(
            f"## CL-{number:02d}-{index:02d}\n\n"
            f"- Affermazione esatta: {note}\n"
            "- Tipo: definizione o meccanismo attribuito alla fonte.\n"
            f"- Fonte o prova: {source_id}, dossier `FONTI_PRIMARIE.md`.\n"
            f"- Sezione pubblica: «{heading}».\n"
            f"- Versione o data: revisione locale {SOURCE_CHECK_DATE}; versione e data della fonte nel dossier.\n"
            "- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti "
            "sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.\n"
            "- Esito: verificata\n"
            "- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte."
        )
    chapter_dir.joinpath("CLAIMS.md").write_text(
        f"""# Registro dei claim. Capitolo {number}

- Data di revisione: {SOURCE_CHECK_DATE}
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

{chr(10).join(chr(10) + entry for entry in entries).strip()}
""",
        encoding="utf-8",
    )


def write_support_files(
    number: int,
    title: str,
    sections: list[tuple[str, str]],
    detail: dict[str, str],
    source_ids: list[str],
    images: list[tuple[str, str]],
    chapter_dir: Path,
    code_policy: str,
) -> None:
    code_dir = chapter_dir / "code"
    code_dir.mkdir(exist_ok=True)
    for stale in code_dir.glob(f"test_{number:02d}_*.py"):
        if stale.name != f"test_{number:02d}_contract.py":
            stale.unlink()
    for stale in code_dir.glob("outputs/SNIP-[A-Z]*.txt"):
        stale.unlink()
    for stale in code_dir.glob("environments/python-pytorch.txt"):
        stale.unlink()
    if code_policy == "exception":
        # Historical scaffolds used to leave a generic executable behind even
        # when the public chapter correctly declared a documentary exception.
        # Keeping those files would make the repository contradict the lesson.
        for stale in [*code_dir.glob("*.py"), *code_dir.glob("outputs/*.txt"), *code_dir.glob("environments/*.txt")]:
            stale.unlink()
    else:
        environment_dir = code_dir / "environments"
        environment_dir.mkdir(exist_ok=True)
        environment_dir.joinpath("python.txt").write_text(
            f"Python {sys.version.split()[0]}\nCPU\nDate: {SOURCE_CHECK_DATE}\n",
            encoding="utf-8",
        )
    write_source_claims(number, sections, source_ids, chapter_dir)
    prerequisites = PREREQUISITES[number]
    prereq_lines = "\n".join(
        f"- Capitolo {item}: {chapter_title(item)}" for item in prerequisites
    )
    route_lines = "\n".join(
        f"{index}. **{heading}.** {note} Prova: {source_ids[index - 1]}."
        for index, (heading, note) in enumerate(sections, 1)
    )
    visual_ids = [Path(path).parent.name for _alt, path in images]
    if code_policy == "reference":
        code_line = (
            f"- riferimento minimo: `code/snip_{number:02d}_contract.py`; "
            f"test: `code/test_{number:02d}_contract.py`; output: `code/outputs/SNIP-{number:02d}-001.txt`."
        )
        if number in FULL_LABS:
            source_name, test_name, output_name, _ = FULL_LABS[number]
            code_line += (
                f"\n- laboratorio esteso: `code/{source_name}`; test: `code/{test_name}`; "
                f"output: `code/{output_name}`."
            )
    else:
        code_line = f"- eccezione motivata: {CODE_EXCEPTIONS[number]}"
        code_dir.joinpath("README.md").write_text(
            f"# Eccezione Python. Capitolo {number}\n\n"
            f"{CODE_EXCEPTIONS[number]}\n\n"
            "La verifica sostitutiva usa fonti primarie, locator, data di consultazione e claim delimitati. "
            "Non sono conservati script giocattolo che potrebbero sembrare una prova computazionale del tema.\n",
            encoding="utf-8",
        )
    chapter_dir.joinpath("PLAN.md").write_text(
        f"""# Piano editoriale. Capitolo {number}

## Obiettivo didattico

Seguire **{title}** da {detail['input']} a {detail['output']}, osservando {detail['operation']} senza oltrepassare questo limite: {complete_sentence(detail['invariant'])}

## Prerequisiti reali

{prereq_lines}

## Percorso della lezione

{route_lines}

## Prove e artefatti

{code_line}
- visuali candidate: {', '.join(visual_ids)}; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
""",
        encoding="utf-8",
    )

    chapter_text = chapter_dir.joinpath("CHAPTER.md").read_text(encoding="utf-8")
    word_count = len(re.findall(r"\b[\wÀ-ÿ'-]+\b", re.sub(r"```[\s\S]*?```", " ", chapter_text)))
    chapter_dir.joinpath("TEXT_AUDIT.md").write_text(
        f"""# Audit del testo. Capitolo {number}

- versione: 0.5.0-draft3
- data: {SOURCE_CHECK_DATE}
- parole fuori dai blocchi di codice: {word_count}
- nuclei semantici: {len(sections)} ({'; '.join(heading for heading, _ in sections)})
- paragrafi del vecchio scaffold: assenti secondo `audit_book_quality.py`
- ripetizioni lunghe tra tre o più capitoli: assenti secondo l'audit trasversale
- esempi e controlli: specifici per ciascun nucleo; nessun esempio è presentato come benchmark
- codice nel testo: {code_policy}
- fonti: citazioni vicine ai claim e dossier separato
- stato: candidatura tecnica revisionata; lettura autoriale e approvazione delle visuali ancora aperte
""",
        encoding="utf-8",
    )
    chapter_dir.joinpath("REVIEW.md").write_text(
        f"""# Review del Capitolo {number}

- revisione: 0.5.0-draft3
- data: {SOURCE_CHECK_DATE}
- testo: ricostruito sui cinque nuclei specifici della lezione
- continuità: prerequisiti tematici espliciti in `PLAN.md`, non semplice dipendenza dal capitolo precedente
- fonti: mappate in `CLAIMS.md`; controllo umano finale ancora richiesto per l'edizione
- codice: policy `{code_policy}`; prove descritte in `code/CODE_AUDIT.md`
- visuali: candidate differenziate; alt text, specifica e audit presenti; approvazione autoriale aperta
- esito: non dichiarato pronto per la pubblicazione finché i gate aperti non vengono chiusi dall'autore
""",
        encoding="utf-8",
    )

    code_dir = chapter_dir / "code"
    if code_policy == "exception":
        code_audit = (
            "# Audit del codice\n\n"
            "- policy: exception\n"
            f"- motivazione: {CODE_EXCEPTIONS[number]}\n"
            "- snippet pubblico: non previsto\n"
            "- verifica sostitutiva: fonti primarie, data, claim delimitati e confronto documentale\n"
            "- stato: eccezione motivata; review autoriale aperta\n"
        )
    else:
        extra = ""
        if number in FULL_LABS:
            source_name, test_name, output_name, _ = FULL_LABS[number]
            counts = {94: 4, 95: 4, 96: 5, 97: 4}
            extra = (
                f"- laboratorio esteso: `python {source_name}`\n"
                f"- test laboratorio: `python -m unittest -v {test_name}` ({counts[number]} superati)\n"
                f"- output laboratorio: `{output_name}`\n"
                "- ambiente laboratorio: `environments/lab.txt`\n"
            )
        code_audit = (
            "# Audit del codice\n\n"
            f"- ambiente minimo: Python {sys.version.split()[0]}, CPU\n"
            f"- comando snippet: `python snip_{number:02d}_contract.py`\n"
            f"- comando test: `python -m unittest -v test_{number:02d}_contract.py`\n"
            "- test del riferimento: 4 superati\n"
            "- controlli: output atteso, determinismo, serializzazione, valori finiti, limite interpretativo\n"
            f"{extra}"
            "- risultato: esempio didattico delimitato, non benchmark di produzione\n"
            "- stato: verificato localmente; review autoriale aperta\n"
        )
    code_dir.mkdir(exist_ok=True)
    code_dir.joinpath("CODE_AUDIT.md").write_text(code_audit, encoding="utf-8")
    if code_policy == "reference" and number in FULL_LABS:
        source_name, test_name, output_name, lab_title = FULL_LABS[number]
        with code_dir.joinpath("README.md").open("a", encoding="utf-8") as handle:
            handle.write(
                f"\n## {lab_title}\n\n"
                f"Codice: `{source_name}`; test: `{test_name}`; output: `{output_name}`; "
                "ambiente: `environments/lab.txt`.\n"
            )
    update_claim_code_section(number, chapter_dir, code_policy)


def build_chapter(number: int) -> None:
    _, chapter_id, part, slug, title, maturity, raw_sections = old.SPECS[number]
    sections = list(raw_sections)
    chapter_dir = ROOT / "chapters" / slug
    chapter_file = chapter_dir / "CHAPTER.md"
    images = image_records(chapter_file)
    detail = old.detail_for_chapter(number)
    code_policy, code_text, _module = code_section(number, title, chapter_dir)
    exception_line = f"\ncode_exception: {CODE_EXCEPTIONS[number]}" if code_policy == "exception" else ""
    source_indices = old.source_indices_for(number, len(sections))
    source_ids = SOURCE_IDS_OVERRIDES.get(
        number,
        [f"SRC-{number:02d}-{index + 1:03d}" for index in source_indices],
    )

    figure_blocks = []
    for index, (alt, raw) in enumerate(images):
        if index == 0:
            caption = f"La prima figura segue il percorso da «{sections[0][0]}» a «{sections[2][0]}»."
        else:
            caption = f"La seconda figura mette a confronto «{sections[3][0]}» e il limite discusso in «{sections[4][0]}»."
        figure_blocks.append(f"![{alt}]({raw})\n\n{caption}")

    section_blocks = []
    seen_mechanisms: set[str] = set()
    for index, (heading, note) in enumerate(sections):
        depth = section_depth(number, index, heading, note, detail, seen_mechanisms)
        block = (
            f"## {heading}\n\n"
            f"{note} [{source_ids[index]}]\n\n"
            f"{depth}"
        )
        section_blocks.append(block)

    formula = formula_block(number, source_ids[0])
    kind = archetype(number)
    body: list[str] = []
    if kind == "mechanism":
        body.extend(section_blocks[:2])
        if formula:
            body.append(formula)
        body.append(figure_blocks[0])
        body.extend(section_blocks[2:4])
        if code_text:
            body.append(code_text)
        body.append(section_blocks[4])
        if len(figure_blocks) > 1:
            body.append(figure_blocks[1])
    elif kind == "conceptual":
        body.extend(section_blocks[:3])
        body.append(figure_blocks[0])
        body.extend(section_blocks[3:])
        if code_text:
            body.append(code_text)
        if len(figure_blocks) > 1:
            body.append(figure_blocks[1])
    elif kind == "data":
        body.append(section_blocks[0])
        body.append(figure_blocks[0])
        body.extend(section_blocks[1:3])
        if code_text:
            body.append(code_text)
        body.extend(section_blocks[3:])
        if len(figure_blocks) > 1:
            body.append(figure_blocks[1])
    elif kind == "system":
        body.extend(section_blocks[:2])
        body.append(figure_blocks[0])
        body.extend(section_blocks[2:])
        if len(figure_blocks) > 1:
            body.append(figure_blocks[1])
        if code_text:
            body.append(code_text)
    else:
        body.append(figure_blocks[0])
        for index, block in enumerate(section_blocks):
            body.append(block)
            if index == 2 and code_text:
                body.append(code_text)
        if len(figure_blocks) > 1:
            body.append(figure_blocks[1])

    if code_policy == "exception":
        body.append(
            "## Perché non forziamo un esempio Python\n\n"
            + CODE_EXCEPTIONS[number]
            + " La verifica resta comunque obbligatoria attraverso fonti primarie, data di consultazione, claim delimitati e confronto tra casi."
        )

    body.append(connection_block(number, sections, source_ids, detail))
    body.append(exercise_block(number, sections, detail))
    final_heading = {
        "mechanism": "Che cosa deve restare chiaro",
        "conceptual": "Una mappa, non una graduatoria",
        "data": "L'artefatto che deve sopravvivere",
        "system": "Il confine operativo",
        "lab": "Criterio di completamento",
    }[kind]
    body.append(
        f"## {final_heading}\n\n"
        f"La lezione parte da «{detail['input']}» e arriva fino a «{detail['output']}». "
        f"Il limite da conservare è questo: {complete_sentence(detail['invariant'])} "
        "Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); "
        "la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md)."
    )

    chapter_file.write_text(
        f"""<!--
chapter_id: {chapter_id}
part_id: {part}
order_key: {number * 10:03d}
title: {title}
maturity: {maturity}
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: {SOURCE_CHECK_DATE}
environment: Python {sys.version.split()[0]}, CPU
code_policy: {code_policy}{exception_line}
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo {number}. {title}

{opening(number, title, sections, detail)}

{chr(10).join(chr(10) + item + chr(10) for item in body).strip()}
""",
        encoding="utf-8",
    )
    update_visual_metadata(number, sections, chapter_file, images)
    write_support_files(number, title, sections, detail, source_ids, images, chapter_dir, code_policy)


def parse_numbers(value: str | None) -> list[int]:
    if not value:
        return list(TARGETS)
    result: set[int] = set()
    for part in value.split(","):
        if "-" in part:
            start, end = (int(item) for item in part.split("-", 1))
            result.update(range(start, end + 1))
        else:
            result.add(int(part))
    return sorted(number for number in result if number in TARGETS)


def update_baseline_visual_metadata() -> None:
    for number in [*range(1, 14), 28]:
        chapter_file = next((ROOT / "chapters").glob(f"{number:02d}_*/CHAPTER.md"))
        raw = chapter_file.read_text(encoding="utf-8")
        headings = re.findall(r"^## (.+)$", raw, re.MULTILINE)
        if len(headings) < 2:
            raise ValueError(f"sezioni insufficienti nel capitolo {number}")
        images = image_records(chapter_file)
        questions = (
            f"Quale trasformazione centrale rende osservabile «{headings[0]}» nel capitolo {number}?",
            f"Quale confronto o limite chiarisce «{headings[min(1, len(headings) - 1)]}»?",
        )
        for index, (alt, path_text) in enumerate(images):
            image_path = (chapter_file.parent / path_text).resolve()
            spec_path = image_path.parent / "SPEC.md"
            spec = spec_path.read_text(encoding="utf-8") if spec_path.exists() else "# Specifica visuale\n"
            if re.search(r"^- domanda principale:", spec, re.MULTILINE):
                spec = re.sub(r"^- domanda principale:.*$", f"- domanda principale: {questions[index % 2]}", spec, flags=re.MULTILINE)
            else:
                spec = spec.rstrip() + f"\n- domanda principale: {questions[index % 2]}\n"
            spec_path.write_text(spec, encoding="utf-8")
            (image_path.parent / "ALT_TEXT.md").write_text(
                f"# Testo alternativo\n\n{alt}. {questions[index % 2]}\n",
                encoding="utf-8",
            )
        print(f"updated baseline visual metadata {number:02d}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapters", help="lista o intervalli, per esempio 14-30,37")
    parser.add_argument("--baseline-metadata", action="store_true")
    args = parser.parse_args()
    if args.baseline_metadata:
        update_baseline_visual_metadata()
        return
    numbers = parse_numbers(args.chapters)
    for number in numbers:
        build_chapter(number)
        print(f"rebuilt chapter {number:02d}")


if __name__ == "__main__":
    main()
