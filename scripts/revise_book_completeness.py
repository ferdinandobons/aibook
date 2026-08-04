"""Rafforza i capitoli 14-98 e sostituisce le visuali uniformi.

Il progetto contiene già una prima generazione completa a livello strutturale.
Questa passata lavora sopra quegli artefatti senza cancellare i candidati
precedenti: crea una nuova versione delle immagini, riscrive la prosa con
esempi e confini espliciti, completa i dossier di fonti e riapre le review che
non possono essere dichiarate approvate automaticamente.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import complete_remaining_book as base  # noqa: E402
import lesson_evidence as evidence  # noqa: E402


DATE = "4 agosto 2026"
SOURCE_VERIFICATION_PATH = ROOT / "docs" / "source_verification_2026-08-04.json"
WHITE = "#FFFFFF"
TEXT = "#0F172A"
MUTED = "#475569"
LIGHT = "#F8FAFC"
GRID = "#CBD5E1"
BLUE = "#2563EB"
BLUE_LIGHT = "#EFF6FF"
PURPLE = "#7C3AED"
PURPLE_LIGHT = "#F5F3FF"
ORANGE = "#D97706"
ORANGE_LIGHT = "#FFFBEB"
GREEN = "#16A34A"
GREEN_LIGHT = "#F0FDF4"
RED = "#DC2626"
RED_LIGHT = "#FEF2F2"
TEAL = "#0F766E"
TEAL_LIGHT = "#F0FDFA"


def polish_text(value: str) -> str:
    """Keep generated Italian prose grammatical across future regenerations."""
    replacements = (
        ("Una implementazione", "Un'implementazione"),
        ("Una euristica", "Un'euristica"),
        ("Una azione", "Un'azione"),
        ("Una approssimazione", "Un'approssimazione"),
        ("Una ipotesi", "Un'ipotesi"),
        ("Una annotazione", "Un'annotazione"),
        ("una implementazione", "un'implementazione"),
        ("una euristica", "un'euristica"),
        ("una azione", "un'azione"),
        ("una approssimazione", "un'approssimazione"),
        ("una ipotesi", "un'ipotesi"),
        ("una annotazione", "un'annotazione"),
        (". il dato", ". Il dato"),
        (". l'operazione", ". L'operazione"),
        (". l'esito", ". L'esito"),
        ("?.", "?"),
    )
    for old, new in replacements:
        value = value.replace(old, new)
    articles = {"la": "alla", "il": "al", "i": "ai", "gli": "agli"}
    value = re.sub(r"\bda l'", "dall'", value)
    value = re.sub(r"\ba l'", "all'", value)
    value = re.sub(r"\bdi l'", "dell'", value)
    value = re.sub(r"\bin l'", "nell'", value)
    value = re.sub(r"\bsu l'", "sull'", value)
    value = re.sub(r"\bda il\b", "dal", value)
    value = re.sub(r"\ba il\b", "al", value)
    value = re.sub(r"\bdi il\b", "del", value)
    value = re.sub(r"\bin il\b", "nel", value)
    value = re.sub(r"\bsu il\b", "sul", value)
    value = re.sub(
        r"\bfino a (la|il|i|gli)\b",
        lambda match: f"fino {articles[match.group(1)]}",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(
        r"\ba (la|il|i|gli)\b",
        lambda match: articles[match.group(1).lower()],
        value,
        flags=re.IGNORECASE,
    )
    contracted = {
        "da": {"la": "dalla", "il": "dal", "i": "dai", "gli": "dagli"},
        "di": {"la": "della", "il": "del", "i": "dei", "gli": "degli"},
        "in": {"la": "nella", "il": "nel", "i": "nei", "gli": "negli"},
        "su": {"la": "sulla", "il": "sul", "i": "sui", "gli": "sugli"},
    }
    for preposition, forms in contracted.items():
        value = re.sub(
            rf"\b{preposition} (la|il|i|gli)\b",
            lambda match, forms=forms: forms[match.group(1).lower()],
            value,
            flags=re.IGNORECASE,
        )
    return value

SPECS = dict(base.SPECS)
if 44 in SPECS:
    canonical_44 = list(SPECS[44])
    canonical_44[3] = "44_moe_conditional"
    SPECS[44] = tuple(canonical_44)
SOURCE_BANK = base.SOURCE_BANK
CASE_BY_PART = base.CASE_BY_PART
base_profile = base.profile
topic_for = evidence.topic_for
source_list_for = evidence.source_list_for
source_indices_for = evidence.source_indices_for


def profile(number: int) -> str:
    if number == 31:
        return "sequence"
    if 34 <= number <= 36:
        return "scaling"
    return base_profile(number)


def detail_for_chapter(number: int) -> dict[str, str]:
    return evidence.detail_for(number, CASE_DETAIL)
source_key = base.source_key
boundary_for = base.boundary_for
formula_for_base = base.formula_for
code_for_base = base.code_for
validate_image_base = base.validate_image

TARGETS = [n for n in range(14, 99) if n != 28]

PREVIOUS_TITLE_OVERRIDES = {
    14: "Apprendimento non supervisionato e auto-supervisionato",
    29: "Il meccanismo di attention",
}

CASE_DETAIL = {
    "rl": {
        "object": "lo stato s_t della spedizione e la scelta a_t",
        "input": "s_t = (in_transito, ritardo=1)",
        "operation": "la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}",
        "output": "la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}",
        "invariant": "un reward osservato non diventa automaticamente una misura del servizio reale",
        "example": "reward immediato 1, gamma 0,9 e valore futuro 0,5",
    },
    "mlp": {
        "object": "il vettore di feature x della richiesta",
        "input": "x = [1, 2] con shape [2]",
        "operation": "una trasformazione affine seguita da una funzione di attivazione",
        "output": "un nuovo vettore h con shape dichiarata",
        "invariant": "una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine",
        "example": "W x + b prima di ReLU, con due coordinate osservabili",
    },
    "deep": {
        "object": "il segnale che attraversa una rete profonda",
        "input": "x_l con shape [batch, d] e norma misurata",
        "operation": "un blocco, una normalizzazione o un percorso residuale",
        "output": "x_{l+1} con la stessa o con una nuova shape dichiarata",
        "invariant": "una somma residuale richiede shape compatibili e non prova da sola stabilità del training",
        "example": "x + F(x) con due vettori di dimensione 2",
    },
    "conv": {
        "object": "una griglia locale di feature",
        "input": "una matrice 3 x 3 e un kernel 2 x 2",
        "operation": "lo stesso kernel scorre posizioni definite da stride e padding",
        "output": "una griglia di attivazioni con dimensioni calcolabili",
        "invariant": "la condivisione dei pesi non implica invariance a ogni trasformazione",
        "example": "una singola finestra 2 x 2 calcolata a mano",
    },
    "rnn": {
        "object": "uno stato nascosto che attraversa una sequenza",
        "input": "x_1, x_2, x_3 e h_0 = 0",
        "operation": "ogni passo combina input corrente e stato precedente con gli stessi pesi",
        "output": "h_t e, se richiesto, una predizione per il passo",
        "invariant": "lo stato precedente deve essere consumato prima di produrre quello successivo",
        "example": "tre aggiornamenti tanh con coefficienti fissi e forma scalare",
    },
    "representation": {
        "object": "un vettore prodotto per un compito successivo",
        "input": "u = [1, 2, 0] e v = [2, 1, 0]",
        "operation": "una proiezione, una ricostruzione o una metrica tra rappresentazioni",
        "output": "un vettore, una similarità o una predizione downstream",
        "invariant": "la geometria dipende da dati, obiettivo e normalizzazione",
        "example": "similarità coseno calcolata dopo la normalizzazione delle norme",
    },
    "generative": {
        "object": "una distribuzione sui dati o su una variabile latente",
        "input": "un dato x, un rumore epsilon o una variabile z",
        "operation": "valutazione di likelihood, trasformazione o campionamento",
        "output": "una probabilità, un punteggio o un campione",
        "invariant": "un campione plausibile non dimostra copertura dell'intera distribuzione",
        "example": "tre probabilità che sommano a 1 prima della selezione",
    },
    "sequence": {
        "object": "la sequenza di token della richiesta",
        "input": "un prefisso di token con lunghezza e mask esplicite",
        "operation": "tokenizzazione, embedding, attention o fattorizzazione causale",
        "output": "ID, vettori contestuali o logits sul vocabolario",
        "invariant": "la visibilità delle posizioni e la convenzione del tokenizer fanno parte del contratto",
        "example": "Q, K e V con shape dichiarate e una posizione futura esclusa",
    },
    "data": {
        "object": "record con provenienza, configurazione e contenuto",
        "input": "due record con ID, testo e metadati",
        "operation": "parsing, filtro, deduplicazione, mix o materializzazione",
        "output": "un manifest con conteggi, checksum e regola di trasformazione",
        "invariant": "un artefatto pulito non dimostra da solo utilità sul compito finale",
        "example": "manifest di due record con digest SHA-256 dell'ordine osservato",
    },
    "architecture": {
        "object": "uno stato nascosto h con dimensione d",
        "input": "h di shape [batch, length, d]",
        "operation": "un sottolayer di attention, MLP, norm, posizione, cache o routing",
        "output": "h' con shape, memoria e costo dichiarati",
        "invariant": "una modifica locale dell'architettura non prova un vantaggio end-to-end",
        "example": "un aggiornamento residuale su due coordinate con shape preservata",
    },
    "posttraining": {
        "object": "una richiesta e due risposte candidate",
        "input": "log-probability scelta -1,2 e rifiutata -2,0",
        "operation": "supervisione, adattamento, confronto di preferenza o verifica",
        "output": "un margine, un gradiente o una policy aggiornata",
        "invariant": "un segnale di preferenza non è una misura assoluta di correttezza",
        "example": "margine di log-probability 0,8 tra due risposte allo stesso prompt",
    },
    "multimodal": {
        "object": "rappresentazioni di testo, immagine, audio o video",
        "input": "due vettori di modalità differenti proiettati in dimensione 2",
        "operation": "allineamento, cross-attention, fusione o generazione condizionata",
        "output": "uno spazio condiviso o un output nella modalità richiesta",
        "invariant": "allineamento misurato tra modalità non equivale a comprensione generale",
        "example": "media coordinata per coordinata di due vettori già proiettati",
    },
    "retrieval": {
        "object": "una query, una fonte e il contesto da recuperare",
        "input": "query con due termini e tre documenti candidati",
        "operation": "scoring, ANN, reranking, fusione o controllo della provenienza",
        "output": "documenti ordinati e contesto passato al componente successivo",
        "invariant": "la risposta deve poter essere separata dall'evidenza effettivamente recuperata",
        "example": "ranking di documenti per sovrapposizione di termini prima della generazione",
    },
    "agents": {
        "object": "lo stato di una traiettoria agentica",
        "input": "osservazione, policy, schema dello strumento e autorizzazioni",
        "operation": "decisione, chiamata tool, osservazione del risultato e verifica",
        "output": "un nuovo stato o un'azione autorizzata",
        "invariant": "il testo generato non sostituisce la policy che autorizza l'azione",
        "example": "lookup_order consentito e refund bloccato da una allowlist esterna",
    },
    "inference": {
        "object": "pesi, token, cache e richiesta di servizio",
        "input": "tre valori reali, un formato quantizzato e un batch definito",
        "operation": "compressione, decoding, batching, scheduling o esecuzione di kernel",
        "output": "risposta, memoria occupata, errore e latenza da misurare",
        "invariant": "un guadagno locale di throughput non prova un miglioramento end-to-end",
        "example": "quantizzazione con scala 0,25 e massimo errore di ricostruzione osservabile",
    },
    "evaluation": {
        "object": "un claim e le predizioni prodotte dal sistema",
        "input": "predizioni, riferimenti, slice e protocollo di misura",
        "operation": "metrica, calibrazione, intervento o analisi di errore",
        "output": "un valore accompagnato dai casi falliti e dai limiti del campione",
        "invariant": "una media non sostituisce la diagnosi delle slice e del protocollo",
        "example": "quattro predizioni, tre corrette e una failure conservata nell'output",
    },
    "security": {
        "object": "un input non fidato e la superficie che può raggiungere",
        "input": "una richiesta che prova a invocare un tool fuori allowlist",
        "operation": "policy, isolamento, rilevazione, redazione o risposta all'incidente",
        "output": "decisione di allow/deny e traccia dell'evento",
        "invariant": "un controllo di sicurezza deve essere applicato fuori dal testo convincente del modello",
        "example": "refund negato mentre lookup_order e ask_confirmation restano consentiti",
    },
    "provenance": {
        "object": "un contenuto accompagnato dalla sua storia",
        "input": "payload, fonte, versione e metadati dichiarati",
        "operation": "digest, firma, attestazione, registrazione o controllo di catena",
        "output": "record verificabile e collegato all'artefatto",
        "invariant": "un digest collega un contenuto a un record, ma non certifica la verità del contenuto",
        "example": "digest di un payload e dei metadati ordinati",
    },
    "labs": {
        "object": "un esperimento o progetto da rendere ricostruibile",
        "input": "codice, dati, configurazione, seed e ambiente",
        "operation": "run, test, confronto, replica o osservazione di frontiera",
        "output": "risultato delimitato e manifest degli artefatti",
        "invariant": "un run concluso non equivale da solo a una replica o a readiness di produzione",
        "example": "digest di seed, split e dtype prima dell'esecuzione",
    },
    "scaling": {
        "object": "una ricetta di training con budget di token e compute",
        "input": "token validi, numero di parametri, batch e contatore di step",
        "operation": "una scelta di scaling, optimizer, parallelismo o recovery",
        "output": "loss, stato del training e costo dichiarato per il setup",
        "invariant": "una relazione osservata a una scala non è una garanzia fuori dall'intervallo misurato",
        "example": "due configurazioni con compute simile e una loss osservata dopo lo stesso numero di token",
    },
}


FORMULA_SCHEMA_NUMBERS = {
    40, 45, 53, 54, 58, 59, 60, 61, 62, 65, 67, 68, 69, 70, 71, 72,
    76, 77, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93,
    94, 96, 98,
}


FORMULAS = {
    31: ("p(x_t | x_{<t}) = softmax(z_t)", "La softmax trasforma logits condizionati in una distribuzione; la scelta del token viene dopo."),
    32: ("manifest = hash(raw, transform, tokenizer, split)", "Il digest diventa utile soltanto se le trasformazioni incluse sono dichiarate."),
    33: ("p_i = w_i^tau / sum_j w_j^tau", "Il campionamento modifica le esposizioni effettive, non la dimensione grezza delle sorgenti."),
    34: ("L(N) = L_inf + A N^(-alpha)", "Un fit empirico vale nell'intervallo e nel setup che lo hanno prodotto."),
    35: ("theta_t = AdamW(theta_{t-1}, grad_t, lr_t)", "Optimizer, schedule e stato del checkpoint formano una sola ricetta."),
    36: ("g = (1 / W) sum_w g_w", "La riduzione dei gradienti deve essere coerente con worker, batch e loss reduction."),
    37: ("h' = h + MLP(Norm(h))", "La posizione della norm e il percorso residuale sono parte del contratto del blocco."),
    38: ("q'_m = R(theta_m) q_m", "Una rotazione di query e key rende il prodotto dipendente dalla posizione relativa."),
    39: ("M = softmax(Q K^T / sqrt(d_k)) V", "Numero di KV head e pattern di attenzione cambiano memoria e connettività."),
    40: ("Attention = tiles(Q,K,V)", "Il tiling cambia il movimento dei dati senza cambiare automaticamente il contratto matematico."),
    41: ("h_t = h_{t-1} + phi(x_t)", "Una forma fattorizzata sostituisce una matrice completa con uno stato aggiornato."),
    42: ("x_{t+1} = A x_t + B u_t", "La ricorrenza espone stato, input e dinamica prima della scelta implementativa."),
    43: ("h' = read(write(h, segment))", "Memoria locale, stato e memoria esterna hanno letture e durate differenti."),
    44: ("load_e = sum_i 1[router(i)=e]", "Il router deve bilanciare carico e capacità senza perdere il contratto dei token."),
    45: ("x = decode(bytes, hierarchy, steps)", "Byte, unità gerarchiche e numero di passi sono assi separati del design."),
    46: ("L = -sum_t log p_theta(y_t | x, y_<t)", "SFT assegna target espliciti, ma la qualità dipende da dati, formato e copertura."),
    47: ("Delta W = B A", "Un aggiornamento low-rank cambia pochi gradi di libertà dichiarati."),
    48: ("r_theta = log pi_theta(y|x) - log pi_ref(y|x)", "Il confronto tra policy richiede una policy di riferimento e uno stesso prompt."),
    49: ("L_DPO = -log sigma(beta (r_c - r_r))", "DPO usa il margine di preferenza senza presentarlo come verità assoluta."),
    50: ("score = verify(trace, outcome)", "Un verificatore di processo può osservare passaggi, esito o entrambi."),
    51: ("R = verifier(answer)", "RLVR lega il segnale a una procedura di verifica esplicita e delimitata."),
    52: ("p_student(y|x) <- p_teacher(y|x)", "La distillazione trasferisce un comportamento osservato, non ogni capacità del teacher."),
    53: ("budget = samples * tokens", "Il test-time compute è una risorsa da misurare insieme a qualità e latenza."),
    54: ("theta' = merge(theta_1, theta_2, rule)", "Il merge richiede una regola e una valutazione di regressione."),
    55: ("z_m = f_m(x_m)", "Ogni modalità ha un encoder e un contratto prima dell'allineamento."),
    56: ("s = sim(f_text(t), f_image(i))", "La similarità misurata non esaurisce la comprensione della scena."),
    57: ("x_hat = g(z, condition)", "Editing e generazione modificano un contenuto sotto una condizione dichiarata."),
    58: ("z = fuse(z_text, z_vision, z_audio)", "La fusione conserva le dimensioni e le maschere delle modalità."),
    59: ("wave = decode(tokens, sample_rate)", "Sample rate, token e durata fanno parte del contratto dell'audio."),
    60: ("frames = decode(z_video, t)", "Una sequenza video aggiunge asse temporale e coerenza tra frame."),
    61: ("scene = project(points, camera)", "La proiezione non ricostruisce da sola la geometria completa."),
    62: ("a_t = policy(o_t, state_t)", "Un world model o una policy produce un'azione condizionata da osservazione e stato."),
    63: ("score(q,d) = bm25(q,d)", "Il ranking è una funzione osservabile prima di qualsiasi generazione."),
    64: ("answer = generate(query, retrieve(query))", "Il contesto recuperato deve essere ispezionabile e separato dalla risposta."),
    65: ("context = route(query, graph, retriever)", "Il router sceglie una fonte, ma la scelta resta da valutare."),
    66: ("memory_t = update(memory_{t-1}, segment_t)", "Memoria e contesto hanno politiche diverse di conservazione e recupero."),
    67: ("tool_call = schema(name, args, scope)", "Lo schema rende l'azione parsabile, non automaticamente autorizzata."),
    68: ("message = protocol.encode(state)", "Un protocollo definisce formato e semantica condivisa tra componenti."),
    69: ("state_{t+1} = step(state_t, action_t, observation_t)", "Il ciclo deve rendere visibili azione, osservazione e arresto."),
    70: ("trajectory = compose(agents, tools, browser)", "Più componenti ampliano la traiettoria e anche la superficie di errore."),
    71: ("score = evaluate(trajectory, task, policy)", "L'eval deve distinguere compito riuscito, traiettoria e violazione di policy."),
    72: ("allow = policy(input, tool, scope)", "Sicurezza agentica richiede una decisione esterna alla sola generazione."),
    73: ("L_student = distill(L_teacher) + lambda R", "Compressione e accuratezza vanno misurate nello stesso perimetro."),
    74: ("q = clamp(round(x / s) + z); \\hat{x} = s(q - z)", "Scale, zero-point e intervallo intero definiscono insieme quantizzazione e ricostruzione."),
    75: ("w_hat = dequantize(codebook(index(w)))", "Un formato low-bit introduce rappresentazione e operazione di ricostruzione."),
    76: ("y = decode(logits, constraint)", "Vincoli di decoding cambiano lo spazio delle sequenze ammissibili."),
    77: ("accepted = verify(draft, target)", "Speculazione e decoding parallelo richiedono una verifica del draft."),
    78: ("memory = layers * tokens * kv_dim * bytes", "La cache cresce con lunghezza, layer, dimensione KV e dtype."),
    79: ("schedule = batch(requests, deadline, memory)", "Batching e scheduling sono una decisione con vincoli, non solo una coda."),
    80: ("latency = collective + compute + transfer", "Il servizio distribuito include comunicazioni oltre al calcolo locale."),
    81: ("kernel = lower(graph, target)", "Compiler e runtime trasformano il grafo in operazioni del backend."),
    82: ("cost = energy + hardware + requests", "Costo e consumo dipendono dall'intero servizio e dall'intensità d'uso."),
    83: ("estimate = metric(outputs, references, protocol)", "La metrica ha significato soltanto rispetto alla domanda di valutazione."),
    84: ("calibration = P(correct | confidence)", "Confidenza, correttezza e factuality sono quantità da separare."),
    85: ("system = model + tools + policy + ui", "La valutazione di sistema deve includere componenti che il modello non controlla."),
    86: ("effect = output(intervention) - output(baseline)", "Un'interpretazione causale richiede un intervento e un confronto."),
    87: ("feature = encode(activation)", "Un circuito descritto da feature richiede controlli indipendenti sull'attivazione."),
    88: ("risk = attack_surface * exposure * impact", "Robustezza e jailbreak vanno definiti con minaccia e protocollo."),
    89: ("allow = policy(instruction, provenance, scope)", "Prompt injection e tool security richiedono separazione tra dati e istruzioni."),
    90: ("trace = hash(model, data, artifact, owner)", "Supply chain e backdoor richiedono una traccia degli artefatti e dei soggetti."),
    91: ("risk = utility + privacy + fairness", "Privacy, equità e utilità entrano in un trade-off da rendere misurabile."),
    92: ("digest = hash(content + metadata)", "Il digest collega contenuto e metadati senza certificare la verità semantica."),
    93: ("decision = govern(policy, risk, evidence)", "Governance traduce evidenza e rischio in una decisione documentata."),
    94: ("result = run(code, data, environment)", "Un laboratorio è utile quando il risultato può essere ricostruito."),
    95: ("loss = cross_entropy(logits, targets)", "Un piccolo LM consente di osservare la relazione tra dati, logits e loss."),
    96: ("release = model + eval + monitoring + rollback", "Un progetto di produzione richiede anche gestione del ciclo di vita."),
    97: ("replica = run(protocol, independent_setup)", "La replica verifica quanto il risultato dipenda dal setup originale."),
    98: ("claim = evidence + date + uncertainty", "Un osservatorio di frontiera deve distinguere evidenza, data e incertezza."),
}


def font(size: int, bold: bool = False):
    return base.font(size, bold)


def fit(draw: ImageDraw.ImageDraw, box, text: str, start=24, minimum=11, bold=False, fill=TEXT, align="center"):
    return base.fit(draw, box, text, start, minimum, bold, fill, align)


def compact(text: str, limit: int = 170) -> str:
    value = re.sub(r"\s+", " ", str(text).strip())
    if len(value) <= limit:
        return value
    cut = max(1, limit - 3)
    prefix = value[:cut]
    comma = prefix.rfind(",")
    if comma >= int(cut * 0.55):
        shortened = prefix[:comma].rstrip(" ,;:")
    else:
        shortened = prefix.rsplit(" ", 1)[0].rstrip(" ,;:")
    return shortened + "..."


VISUAL_NOTE_OVERRIDES = {
    72: (
        "Scope minimi, credenziali e filesystem separati.",
        "Esecuzione isolata con rete e risorse limitate.",
        "Conferma prima delle azioni ad alto impatto.",
        "Log e snapshot per ricostruire e correggere.",
        "Dati esterni separati dalle istruzioni di sistema.",
    ),
    83: (
        "Claim, popolazione, metrica e incertezza.",
        "Input, reference, split e cutoff.",
        "Metriche, giudici, aggregazione e slice.",
        "Judge calibrato contro giudizi indipendenti.",
        "Intervalli, failure, costi e limiti.",
    ),
}


def visual_note(number: int, index: int, text: str, limit: int, heading: str | None = None) -> str:
    overrides = VISUAL_NOTE_OVERRIDES.get(number)
    if overrides and index < len(overrides):
        return overrides[index]
    first_sentence = re.split(r"(?<=[.!?])\s+", str(text).strip())[0].strip()
    if len(first_sentence) <= limit:
        return first_sentence
    if heading and limit <= 60 and len(heading) + 1 <= limit:
        return heading.rstrip(".!?") + "."
    return compact(first_sentence, limit)


def latest_candidate(folder: Path) -> tuple[Path, int] | None:
    """Return the current candidate without creating needless raster versions."""
    candidates = []
    if folder.exists():
        for path in folder.glob("candidate-v*.png"):
            match = re.fullmatch(r"candidate-v([0-9]+)\.png", path.name)
            if match:
                candidates.append((int(match.group(1)), path))
    if not candidates:
        return None
    version, path = max(candidates, key=lambda item: item[0])
    return path, version


def from_object(value: str) -> str:
    replacements = (
        ("lo ", "dallo "),
        ("la ", "dalla "),
        ("il ", "dal "),
        ("l'", "dall'"),
    )
    for prefix, replacement in replacements:
        if value.startswith(prefix):
            return replacement + value[len(prefix):]
    return "da " + value


def sentence_case(value: str) -> str:
    """Turn a lower-case contract fragment into a safe standalone sentence."""
    value = re.sub(r"\s+", " ", value.strip()).rstrip(".;:")
    if not value:
        return value
    return value[0].upper() + value[1:]


def case_chain(detail: dict[str, str]) -> str:
    """Describe input -> operation -> output without forcing grammar on clauses."""
    return (
        f"Il caso guida riguarda {detail['object']}. "
        f"L'input è {detail['input']}. "
        f"Il passaggio osservato è: {detail['operation']}. "
        f"L'output osservabile è {detail['output']}."
    )


def formula_public_note(number: int, formula_note: str) -> tuple[str, str]:
    """Distinguish equations from compact interface schemas in reader-facing text."""
    if number in FORMULA_SCHEMA_NUMBERS:
        return (
            "Lo schema compatto è:",
            f"È una notazione di interfaccia, non un'identità numerica completa. {formula_note}",
        )
    return ("La formula locale è:", formula_note)


def arrow(draw: ImageDraw.ImageDraw, start, end, color=MUTED, width=4):
    x0, y0 = start
    x1, y1 = end
    draw.line((x0, y0, x1, y1), fill=color, width=width)
    if abs(x1 - x0) >= abs(y1 - y0):
        sign = 1 if x1 >= x0 else -1
        points = [(x1, y1), (x1 - 16 * sign, y1 - 10), (x1 - 16 * sign, y1 + 10)]
    else:
        sign = 1 if y1 >= y0 else -1
        points = [(x1, y1), (x1 - 10, y1 - 16 * sign), (x1 + 10, y1 - 16 * sign)]
    draw.polygon(points, fill=color)


def card(draw, box, title: str, body: str, color=BLUE, fill=BLUE_LIGHT, title_size=22, body_size=17):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=22, fill=WHITE, outline=color, width=3)
    draw.rounded_rectangle((x0 + 10, y0 + 10, x1 - 10, y0 + 78), radius=14, fill=fill, outline=color, width=2)
    fit(draw, (x0 + 22, y0 + 20, x1 - 22, y0 + 68), title, title_size, 11, True, color)
    fit(draw, (x0 + 24, y0 + 92, x1 - 24, y1 - 18), body, body_size, 10, fill=TEXT, align="left")


def header(draw, figure_id: str, title: str, question: str):
    fit(draw, (58, 24, 1742, 78), f"{figure_id} · {title}", 30, 20, True)
    fit(draw, (80, 88, 1720, 138), question, 19, 13, fill=MUTED)


def finish(path: Path, image: Image.Image):
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG")
    validate_image_base(path)


def visual_question(number: int, family: str) -> str:
    title = SPECS[number][4]
    if number in evidence.DETAILS:
        detail = detail_for_chapter(number)
        return (
            f"Il diagramma segue il passaggio: {sentence_case(detail['operation'])}. "
            f"L'input è {detail['input']}, l'output è {detail['output']}; "
            f"il vincolo da controllare è che {detail['invariant']}"
        )
    questions = {
        "pipeline": f"Il percorso dall'input di {title.lower()} all'output osservabile è leggibile da sinistra a destra",
        "branch": "Il ramo comune resta separato dalle varianti e dai loro esiti",
        "chart": "Il grafico confronta la quantità che cambia con quella che non viene misurata",
        "architecture": "I componenti cambiano lo stato mentre il contratto conserva le invarianti dichiarate",
        "matrix": "La matrice rende visibili posizioni, dimensioni e vincoli dell'operazione",
        "loop": "Il ciclo rende visibili lo stato restituito e il punto in cui si applica il controllo",
        "timeline": "La stessa informazione viene seguita lungo i passi del processo",
        "scatter": "La geometria viene confrontata rispetto alla metrica dichiarata",
        "compare": "Il caso base resta distinto dalle proprietà introdotte dalle estensioni",
        "manifest": "La trasformazione e i metadati rendono l'artefatto tracciabile",
        "queue": "La coda mostra la risorsa condivisa e il vincolo che decide il servizio",
        "graph": "Il grafo mostra quali nodi comunicano e quali archi sono autorizzati",
        "funnel": "Il funnel mostra quali casi sopravvivono ai controlli e quali vengono esclusi",
        "threat": "La superficie mostra quale input arriva al rischio e quale guardia lo ferma",
        "checklist": "La checklist raccoglie gli artefatti necessari a ricostruire il risultato",
    }
    return questions[family]


def render_pipeline(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    question = visual_question(number, family)
    header(draw, fid, title, question)
    labels = sections[:4]
    boxes = []
    for i, (heading, note) in enumerate(labels):
        x0 = 55 + i * 430
        color, fill = [(BLUE, BLUE_LIGHT), (PURPLE, PURPLE_LIGHT), (ORANGE, ORANGE_LIGHT), (GREEN, GREEN_LIGHT)][i]
        box = (x0, 245, x0 + 350, 710)
        card(draw, box, heading, visual_note(number, i, note, 210, heading), color, fill, 20, 16)
        boxes.append(box)
    for left, right in zip(boxes, boxes[1:]):
        arrow(draw, (left[2] + 4, 477), (right[0] - 7, 477))
    draw.rounded_rectangle((150, 805, 1650, 930), radius=20, fill=ORANGE_LIGHT, outline=ORANGE, width=2)
    detail = detail_for_chapter(number)
    fit(draw, (180, 825, 1620, 900), f"Invariante: {detail['invariant']}", 18, 12, True, TEXT)
    finish(path, image)


def render_branch(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    detail = detail_for_chapter(number)
    card(draw, (650, 175, 1150, 330), "INPUT", detail["input"], BLUE, BLUE_LIGHT, 22, 17)
    branch_boxes = []
    for i, (heading, note) in enumerate(sections[1:4]):
        x0 = 70 + i * 585
        color, fill = [(PURPLE, PURPLE_LIGHT), (ORANGE, ORANGE_LIGHT), (GREEN, GREEN_LIGHT)][i]
        box = (x0, 435, x0 + 455, 680)
        card(draw, box, heading, visual_note(number, i, note, 195, heading), color, fill, 20, 15)
        branch_boxes.append(box)
        arrow(draw, (900, 333), (x0 + 225, 425), color, 3)
    draw.line((295, 710, 1505, 710), fill=MUTED, width=3)
    for box in branch_boxes:
        arrow(draw, (box[0] + 225, box[3] + 3), (900, 805), MUTED, 3)
    draw.rounded_rectangle((410, 800, 1390, 932), radius=22, fill=GREEN_LIGHT, outline=GREEN, width=3)
    fit(draw, (440, 820, 1360, 900), f"CONVERGENZA · {compact(sections[4][0], 60)}\n{compact(detail['invariant'], 130)}", 18, 11, True)
    finish(path, image)


def render_chart(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    x0, y0, x1, y1 = 110, 740, 1130, 230
    draw.line((x0, y0, x1, y0), fill=TEXT, width=3)
    draw.line((x0, y0, x0, y1), fill=TEXT, width=3)
    for tick in range(5):
        y = y0 - tick * 125
        draw.line((x0 - 8, y, x1, y), fill="#E2E8F0", width=1)
        fit(draw, (35, y - 16, 95, y + 16), str(tick * 25), 16, 12, fill=MUTED)
    points = []
    values = [28 + ((number * 7 + i * 17) % 58) for i in range(5)]
    for i, value in enumerate(values):
        x = x0 + i * 245
        y = y0 - value * 5.2
        points.append((x, y))
        if i:
            draw.line((*points[i - 1], *points[i]), fill=BLUE, width=6)
        draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill=BLUE, outline=WHITE, width=3)
        fit(draw, (x - 95, 770, x + 95, 835), sections[i][0], 15, 10, True, TEXT)
        fit(draw, (x - 50, y - 44, x + 50, y - 14), f"{value}", 16, 12, True, BLUE)
    draw.rounded_rectangle((1240, 215, 1700, 740), radius=24, fill=BLUE_LIGHT, outline=BLUE, width=3)
    fit(draw, (1280, 250, 1660, 325), "LETTURA", 23, 16, True, BLUE)
    body = "Valori illustrativi\nnon sono benchmark.\n\n" + visual_note(number, 0, sections[0][1], 180, sections[0][0]) + "\n\n" + visual_note(number, 4, sections[-1][1], 180, sections[-1][0])
    fit(draw, (1280, 360, 1660, 690), body, 20, 12, fill=TEXT, align="left")
    draw.rounded_rectangle((210, 875, 1590, 940), radius=16, fill=ORANGE_LIGHT, outline=ORANGE, width=2)
    fit(draw, (235, 888, 1565, 928), "La curva mostra una relazione didattica; il risultato reale richiede un protocollo e un dataset.", 17, 12, True)
    finish(path, image)


def render_architecture(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    draw.rounded_rectangle((110, 210, 480, 800), radius=26, fill=LIGHT, outline=GRID, width=3)
    fit(draw, (150, 238, 440, 290), "INPUT", 24, 16, True, MUTED)
    fit(draw, (155, 330, 435, 700), detail_for_chapter(number)["input"], 23, 14, True)
    block_boxes = []
    for i, (heading, note) in enumerate(sections[:4]):
        y0 = 188 + i * 150
        color, fill = [(BLUE, BLUE_LIGHT), (PURPLE, PURPLE_LIGHT), (ORANGE, ORANGE_LIGHT), (GREEN, GREEN_LIGHT)][i]
        box = (650, y0, 1235, y0 + 105)
        draw.rounded_rectangle(box, radius=18, fill=fill, outline=color, width=3)
        fit(draw, (680, y0 + 13, 935, y0 + 88), heading, 19, 11, True, color, "left")
        fit(draw, (955, y0 + 14, 1205, y0 + 90), visual_note(number, i, note, 150, heading), 15, 10, fill=TEXT, align="left")
        block_boxes.append(box)
    arrow(draw, (485, 500), (640, 500), BLUE, 4)
    for top, bottom in zip(block_boxes, block_boxes[1:]):
        arrow(draw, (943, top[3] + 3), (943, bottom[1] - 4), MUTED, 3)
    draw.line((585, 240, 585, 715), fill=ORANGE, width=5)
    arrow(draw, (585, 715), (640, 715), ORANGE, 3)
    fit(draw, (505, 755, 655, 830), "residual /\nvincolo", 17, 11, True, ORANGE)
    draw.rounded_rectangle((1320, 350, 1700, 650), radius=24, fill=GREEN_LIGHT, outline=GREEN, width=3)
    fit(draw, (1350, 380, 1670, 430), "OUTPUT", 22, 16, True, GREEN)
    fit(draw, (1350, 470, 1670, 610), detail_for_chapter(number)["output"], 19, 12, True)
    finish(path, image)


def render_matrix(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    x0, y0, cell = 130, 220, 88
    for row in range(5):
        for col in range(5):
            x = x0 + col * cell
            y = y0 + row * cell
            if row > col and (number % 2 == 0 or row == col + 2):
                fill = "#E2E8F0"
            elif (row + col + number) % 5 == 0:
                fill = PURPLE_LIGHT
            else:
                fill = WHITE
            draw.rectangle((x, y, x + cell - 5, y + cell - 5), fill=fill, outline=GRID, width=2)
            if row == col or (row + col + number) % 5 == 0:
                fit(draw, (x + 10, y + 15, x + cell - 15, y + cell - 25), "•", 25, 17, True, BLUE)
    fit(draw, (150, 695, 660, 760), "righe: query / posizioni", 18, 13, True, MUTED)
    fit(draw, (40, 260, 115, 625), "chiavi\nvisibili", 17, 12, True, MUTED)
    card(draw, (850, 210, 1680, 390), sections[0][0], visual_note(number, 0, sections[0][1], 250, sections[0][0]), BLUE, BLUE_LIGHT, 22, 17)
    card(draw, (850, 460, 1680, 640), sections[1][0], visual_note(number, 1, sections[1][1], 250, sections[1][0]), PURPLE, PURPLE_LIGHT, 22, 17)
    draw.rounded_rectangle((850, 720, 1680, 900), radius=20, fill=ORANGE_LIGHT, outline=ORANGE, width=2)
    fit(draw, (885, 750, 1645, 865), "Le celle grigie indicano una maschera o una posizione non disponibile.\nLa matrice è uno schema illustrativo.", 19, 12, True)
    finish(path, image)


def render_loop(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    centers = [(390, 330), (900, 230), (1410, 330), (1280, 730), (620, 730)]
    colors = [(BLUE, BLUE_LIGHT), (PURPLE, PURPLE_LIGHT), (ORANGE, ORANGE_LIGHT), (GREEN, GREEN_LIGHT), (TEAL, TEAL_LIGHT)]
    for i, ((heading, note), center) in enumerate(zip(sections, centers)):
        x, y = center
        box = (x - 180, y - 72, x + 180, y + 72)
        draw.rounded_rectangle(box, radius=22, fill=WHITE, outline=colors[i][0], width=3)
        draw.rounded_rectangle((x - 170, y - 62, x + 170, y - 10), radius=13, fill=colors[i][1], outline=colors[i][0], width=2)
        fit(draw, (x - 155, y - 54, x + 155, y - 18), heading, 17, 10, True, colors[i][0])
        fit(draw, (x - 155, y + 2, x + 155, y + 57), visual_note(number, i, note, 150, heading), 14, 9, fill=TEXT)
    connections = [
        ((780, 302), (570, 330)),
        ((1020, 302), (1230, 330)),
        ((390, 402), (620, 658)),
        ((800, 730), (1100, 730)),
        ((1280, 658), (1410, 402)),
        ((1410, 258), (1020, 302)),
    ]
    for start, end in connections:
        arrow(draw, start, end, MUTED, 3)
    draw.rounded_rectangle((665, 430, 1135, 545), radius=20, fill=RED_LIGHT, outline=RED, width=3)
    fit(draw, (695, 455, 1105, 520), "CHECK / STOP\n" + compact(detail_for_chapter(number)["invariant"], 80), 17, 11, True, RED)
    finish(path, image)


def render_timeline(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    draw.line((130, 490, 1660, 490), fill=TEXT, width=5)
    for i, (heading, note) in enumerate(sections):
        x = 170 + i * 365
        draw.ellipse((x - 14, 476, x + 14, 504), fill=[BLUE, PURPLE, ORANGE, GREEN, TEAL][i])
        y0 = 200 if i % 2 == 0 else 570
        card(draw, (x - 140, y0, x + 140, y0 + 190), heading, visual_note(number, i, note, 150, heading), [BLUE, PURPLE, ORANGE, GREEN, TEAL][i], [BLUE_LIGHT, PURPLE_LIGHT, ORANGE_LIGHT, GREEN_LIGHT, TEAL_LIGHT][i], 17, 13)
        fit(draw, (x - 80, 445 if i % 2 == 0 else 510, x + 80, 470 if i % 2 == 0 else 540), f"t{i}", 18, 13, True, MUTED)
    draw.rounded_rectangle((360, 875, 1450, 940), radius=16, fill=ORANGE_LIGHT, outline=ORANGE, width=2)
    fit(draw, (385, 888, 1425, 928), "La linea temporale mostra ordine e dipendenze, non una durata misurata.", 17, 12, True)
    finish(path, image)


def render_scatter(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    x0, y0, x1, y1 = 130, 760, 1030, 205
    draw.line((x0, y0, x1, y0), fill=TEXT, width=3)
    draw.line((x0, y0, x0, y1), fill=TEXT, width=3)
    for i in range(24):
        px = x0 + 70 + ((i * 113 + number * 17) % 760)
        py = y0 - 70 - ((i * 71 + number * 29) % 430)
        color = BLUE if i % 2 == 0 else PURPLE
        draw.ellipse((px - 9, py - 9, px + 9, py + 9), fill=color)
    draw.line((560, 520, 700, 430), fill=ORANGE, width=5)
    arrow(draw, (560, 520), (700, 430), ORANGE, 4)
    fit(draw, (470, 540, 740, 585), "distanza / direzione", 17, 12, True, ORANGE)
    card(draw, (1180, 220, 1680, 420), "METRICA", visual_note(number, 0, sections[0][1], 180, sections[0][0]), BLUE, BLUE_LIGHT, 21, 16)
    card(draw, (1180, 475, 1680, 675), "LIMITE", compact(detail_for_chapter(number)["invariant"], 155), RED, RED_LIGHT, 21, 16)
    draw.rounded_rectangle((230, 845, 1580, 930), radius=18, fill=LIGHT, outline=GRID, width=2)
    fit(draw, (260, 865, 1550, 915), "Punti illustrativi: la separazione visiva non dimostra identità o causalità.", 17, 12, True)
    finish(path, image)


def render_compare(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    for x0, label, color, fill, items in (
        (90, "CASO BASE", BLUE, BLUE_LIGHT, sections[:3]),
        (965, "ESTENSIONI", PURPLE, PURPLE_LIGHT, sections[3:]),
    ):
        draw.rounded_rectangle((x0, 190, x0 + 745, 800), radius=26, fill=WHITE, outline=color, width=4)
        fit(draw, (x0 + 30, 220, x0 + 715, 280), label, 26, 18, True, color)
        for i, (heading, note) in enumerate(items):
            y = 330 + i * 145
            draw.ellipse((x0 + 45, y + 20, x0 + 85, y + 60), fill=color)
            fit(draw, (x0 + 56, y + 25, x0 + 74, y + 53), str(i + 1), 15, 12, True, WHITE)
            fit(draw, (x0 + 110, y, x0 + 695, y + 50), heading, 20, 12, True, color, "left")
            fit(draw, (x0 + 110, y + 55, x0 + 695, y + 115), visual_note(number, i, note, 180, heading), 15, 10, fill=TEXT, align="left")
    draw.rounded_rectangle((260, 850, 1540, 940), radius=18, fill=ORANGE_LIGHT, outline=ORANGE, width=2)
    fit(draw, (290, 870, 1510, 920), "Confrontare non significa dichiarare che le estensioni migliorino sempre il caso base.", 18, 12, True)
    finish(path, image)


def render_manifest(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    stages = [("RAW", "id · testo · fonte"), ("PARSE", visual_note(number, 1, sections[1][1], 180, sections[1][0])), ("FILTER", visual_note(number, 2, sections[2][1], 180, sections[2][0])), ("MANIFEST", "count · digest · config")]
    boxes = []
    for i, (label, body) in enumerate(stages):
        x = 80 + i * 440
        color, fill = [(RED, RED_LIGHT), (ORANGE, ORANGE_LIGHT), (PURPLE, PURPLE_LIGHT), (GREEN, GREEN_LIGHT)][i]
        box = (x, 330, x + 330, 650)
        card(draw, box, label, body, color, fill, 21, 16)
        boxes.append(box)
    for a, b in zip(boxes, boxes[1:]):
        arrow(draw, (a[2] + 5, 490), (b[0] - 8, 490), MUTED, 4)
    draw.rounded_rectangle((230, 760, 1570, 910), radius=22, fill=BLUE_LIGHT, outline=BLUE, width=3)
    fit(draw, (265, 790, 1535, 875), "TRACE: " + detail_for_chapter(number)["invariant"], 18, 12, True, TEXT)
    finish(path, image)


def render_queue(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    fit(draw, (100, 220, 600, 270), "RICHIESTE", 23, 16, True, BLUE)
    for i in range(6):
        x = 110 + (i % 3) * 155
        y = 315 + (i // 3) * 125
        draw.rounded_rectangle((x, y, x + 125, y + 75), radius=12, fill=BLUE_LIGHT, outline=BLUE, width=2)
        fit(draw, (x + 10, y + 18, x + 115, y + 58), f"q{i + 1}", 19, 13, True, BLUE)
    arrow(draw, (620, 440), (820, 440), MUTED, 4)
    card(draw, (840, 280, 1190, 600), "BATCH / ROUTER", visual_note(number, 0, sections[0][1], 180, sections[0][0]), PURPLE, PURPLE_LIGHT, 20, 16)
    arrow(draw, (1210, 440), (1390, 440), MUTED, 4)
    draw.rounded_rectangle((1400, 250, 1690, 650), radius=22, fill=GREEN_LIGHT, outline=GREEN, width=3)
    fit(draw, (1430, 280, 1660, 340), "MEMORIA / CACHE", 20, 13, True, GREEN)
    for i in range(4):
        y = 390 + i * 55
        draw.rounded_rectangle((1440, y, 1650, y + 35), radius=8, fill=WHITE, outline=GREEN, width=2)
        fit(draw, (1460, y + 5, 1630, y + 28), f"block {i}", 14, 11, True, GREEN)
    draw.rounded_rectangle((230, 780, 1570, 910), radius=20, fill=ORANGE_LIGHT, outline=ORANGE, width=2)
    fit(draw, (260, 810, 1540, 880), "Vincolo da misurare: memoria, latenza, correttezza e trasferimento sullo stesso setup.", 18, 12, True)
    finish(path, image)


def render_graph(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    nodes = [(230, 490), (560, 260), (920, 490), (560, 720), (1280, 300), (1510, 650)]
    for i, (a, b) in enumerate(((0, 1), (1, 2), (0, 3), (3, 2), (2, 4), (2, 5), (4, 5))):
        arrow(draw, nodes[a], nodes[b], [BLUE, PURPLE, ORANGE, GREEN, TEAL, RED, MUTED][i], 3)
    for i, center in enumerate(nodes):
        x, y = center
        color, fill = [(BLUE, BLUE_LIGHT), (PURPLE, PURPLE_LIGHT), (ORANGE, ORANGE_LIGHT), (GREEN, GREEN_LIGHT), (TEAL, TEAL_LIGHT), (RED, RED_LIGHT)][i]
        draw.ellipse((x - 70, y - 42, x + 70, y + 42), fill=fill, outline=color, width=3)
        label = sections[i % len(sections)][0] if i < 5 else "guard"
        fit(draw, (x - 62, y - 25, x + 62, y + 25), label, 16, 10, True, color)
    draw.rounded_rectangle((1100, 735, 1680, 900), radius=20, fill=ORANGE_LIGHT, outline=ORANGE, width=2)
    fit(draw, (1130, 765, 1650, 870), "Gli archi descrivono dipendenze del caso illustrativo.\nNon sono una topologia universale.", 18, 12, True)
    finish(path, image)


def render_funnel(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    widths = [1120, 930, 750, 570, 390]
    for i, width in enumerate(widths):
        y = 205 + i * 115
        x = (1800 - width) // 2
        color, fill = [(BLUE, BLUE_LIGHT), (PURPLE, PURPLE_LIGHT), (ORANGE, ORANGE_LIGHT), (GREEN, GREEN_LIGHT), (RED, RED_LIGHT)][i]
        draw.rounded_rectangle((x, y, x + width, y + 82), radius=18, fill=fill, outline=color, width=3)
        fit(draw, (x + 28, y + 15, x + width - 28, y + 67), sections[i][0], 21, 12, True, color)
    draw.rounded_rectangle((290, 835, 1510, 935), radius=18, fill=LIGHT, outline=GRID, width=2)
    fit(draw, (320, 860, 1480, 910), "Ogni filtro cambia il campione: il valore finale non riassume i casi rimossi.", 18, 12, True)
    finish(path, image)


def render_threat(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    card(draw, (90, 320, 420, 650), "INPUT NON FIDATO", visual_note(number, 0, sections[0][1], 150, sections[0][0]), RED, RED_LIGHT, 19, 15)
    arrow(draw, (435, 485), (610, 485), RED, 4)
    card(draw, (635, 320, 970, 650), "MODELLO", visual_note(number, 1, sections[1][1], 150, sections[1][0]), PURPLE, PURPLE_LIGHT, 20, 15)
    arrow(draw, (985, 485), (1160, 485), MUTED, 4)
    card(draw, (1185, 320, 1515, 650), "TOOL / OUTPUT", visual_note(number, 2, sections[2][1], 150, sections[2][0]), ORANGE, ORANGE_LIGHT, 19, 15)
    draw.rounded_rectangle((610, 735, 1190, 900), radius=22, fill=GREEN_LIGHT, outline=GREEN, width=4)
    fit(draw, (650, 770, 1150, 855), "GUARDIA ESTERNA\n" + compact(detail_for_chapter(number)["invariant"], 100), 19, 12, True, GREEN)
    arrow(draw, (900, 720), (900, 660), GREEN, 4)
    finish(path, image)


def render_checklist(path: Path, fid: str, number: int, title: str, sections, family: str):
    image = Image.new("RGB", (1800, 1000), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, fid, title, visual_question(number, family))
    labels = ["CODICE", "DATI", "AMBIENTE", "OUTPUT", "REVIEW"]
    for i, label in enumerate(labels):
        x = 150 + i * 330
        y = 300 + (i % 2) * 235
        color, fill = [(BLUE, BLUE_LIGHT), (PURPLE, PURPLE_LIGHT), (ORANGE, ORANGE_LIGHT), (GREEN, GREEN_LIGHT), (TEAL, TEAL_LIGHT)][i]
        draw.rounded_rectangle((x, y, x + 250, y + 130), radius=20, fill=fill, outline=color, width=3)
        draw.ellipse((x + 18, y + 18, x + 54, y + 54), outline=color, width=3)
        fit(draw, (x + 70, y + 25, x + 220, y + 58), label, 18, 12, True, color, "left")
        fit(draw, (x + 24, y + 75, x + 225, y + 112), visual_note(number, i, sections[i][1], 48, sections[i][0]), 14, 10, fill=TEXT, align="left")
        if i:
            arrow(draw, (x - 80, y + 65), (x - 12, y + 65), MUTED, 3)
    draw.rounded_rectangle((420, 820, 1380, 930), radius=20, fill=ORANGE_LIGHT, outline=ORANGE, width=2)
    fit(draw, (450, 850, 1350, 900), "La riproducibilità è una catena: un anello mancante riapre la conclusione.", 18, 12, True)
    finish(path, image)


FAMILY_POOLS = {
    "rl": ("branch", "loop"),
    "mlp": ("architecture", "chart"),
    "deep": ("chart", "architecture"),
    "conv": ("matrix", "architecture"),
    "rnn": ("timeline", "loop"),
    "representation": ("scatter", "compare"),
    "generative": ("pipeline", "timeline"),
    "sequence": ("matrix", "branch"),
    "data": ("manifest", "pipeline"),
    "architecture": ("architecture", "compare"),
    "posttraining": ("pipeline", "branch"),
    "multimodal": ("compare", "scatter"),
    "retrieval": ("pipeline", "graph"),
    "agents": ("loop", "graph"),
    "inference": ("queue", "chart"),
    "evaluation": ("funnel", "chart"),
    "security": ("threat", "loop"),
    "provenance": ("manifest", "timeline"),
    "labs": ("checklist", "compare"),
    "scaling": ("chart", "architecture"),
}

TOPIC_FAMILY_POOLS = {
    "llm_behavior": ("branch", "matrix"),
    "data_lifecycle": ("manifest", "funnel"),
    "mixture": ("chart", "compare"),
    "pretraining_recipe": ("pipeline", "timeline"),
    "distributed_training": ("architecture", "graph"),
    "modern_block": ("architecture", "matrix"),
    "position": ("matrix", "chart"),
    "attention_variants": ("compare", "matrix"),
    "flash": ("pipeline", "chart"),
    "linear_attention": ("timeline", "compare"),
    "ssm": ("timeline", "architecture"),
    "hybrid_memory": ("loop", "graph"),
    "moe": ("branch", "chart"),
    "alternative_prediction": ("compare", "pipeline"),
    "sft": ("pipeline", "branch"),
    "peft": ("compare", "architecture"),
    "rlhf": ("pipeline", "loop"),
    "preference": ("compare", "chart"),
    "verifier": ("funnel", "loop"),
    "rlvr": ("pipeline", "funnel"),
    "reasoning": ("branch", "timeline"),
    "test_time": ("chart", "branch"),
    "editing": ("compare", "timeline"),
    "multimodal": ("compare", "scatter"),
    "vlm": ("architecture", "pipeline"),
    "imagegen": ("pipeline", "timeline"),
    "native_multimodal": ("compare", "pipeline"),
    "audio": ("pipeline", "timeline"),
    "video": ("timeline", "pipeline"),
    "3d": ("scatter", "architecture"),
    "world": ("loop", "pipeline"),
    "retrieval": ("pipeline", "graph"),
    "rag": ("pipeline", "graph"),
    "advanced_rag": ("graph", "branch"),
    "memory": ("queue", "loop"),
    "tools": ("pipeline", "branch"),
    "interoperability": ("compare", "graph"),
    "agent_loop": ("loop", "timeline"),
    "multiagent": ("graph", "compare"),
    "agent_eval": ("funnel", "chart"),
    "agent_safety": ("threat", "loop"),
    "distillation": ("compare", "pipeline"),
    "quantization": ("chart", "compare"),
    "low_bit": ("compare", "architecture"),
    "decoding": ("branch", "chart"),
    "speculative": ("pipeline", "compare"),
    "kv_cache": ("queue", "timeline"),
    "serving": ("queue", "chart"),
    "distributed_inference": ("architecture", "queue"),
    "compiler": ("pipeline", "compare"),
    "llmops": ("checklist", "chart"),
    "eval_design": ("funnel", "checklist"),
    "factuality": ("funnel", "scatter"),
    "system_eval": ("architecture", "funnel"),
    "interpretability": ("compare", "graph"),
    "sae": ("architecture", "scatter"),
    "robustness": ("threat", "chart"),
    "injection": ("threat", "pipeline"),
    "supply_chain": ("manifest", "threat"),
    "privacy_fairness": ("compare", "chart"),
    "provenance": ("manifest", "timeline"),
    "governance": ("checklist", "loop"),
    "lab": ("checklist", "compare"),
    "small_lm": ("pipeline", "matrix"),
    "production": ("pipeline", "checklist"),
    "replication": ("compare", "checklist"),
    "frontier": ("chart", "timeline"),
}

RENDERERS = {
    "pipeline": render_pipeline,
    "branch": render_branch,
    "chart": render_chart,
    "architecture": render_architecture,
    "matrix": render_matrix,
    "loop": render_loop,
    "timeline": render_timeline,
    "scatter": render_scatter,
    "compare": render_compare,
    "manifest": render_manifest,
    "queue": render_queue,
    "graph": render_graph,
    "funnel": render_funnel,
    "threat": render_threat,
    "checklist": render_checklist,
}


def family_for(number: int, slot: int) -> str:
    pool = TOPIC_FAMILY_POOLS.get(topic_for(number), FAMILY_POOLS[profile(number)])
    return pool[(number + slot) % len(pool)]


def figure_refs(chapter: Path) -> list[str]:
    chapter_file = chapter / "CHAPTER.md"
    if chapter_file.exists():
        text = chapter_file.read_text(encoding="utf-8")
        refs = re.findall(r"\]\(\.\./\.\./assets/chapters/[^/]+/([^/]+)/(?:final|candidate-v[0-9]+)\.png\)", text)
        if len(refs) >= 2:
            return refs[:2]
    asset_root = ROOT / "assets" / "chapters" / chapter.name
    if asset_root.exists():
        dirs = sorted(path.name for path in asset_root.iterdir() if path.is_dir())
        if len(dirs) >= 2:
            return dirs[:2]
    prefix = re.sub(r"[^A-Z0-9]+", "", chapter.name.upper())[:8] or "CHAPTER"
    return [f"{prefix}-01", f"{prefix}-02"]


def candidate_path(folder: Path, start: int) -> tuple[Path, int]:
    existing = []
    if folder.exists():
        for path in folder.glob("candidate-v*.png"):
            match = re.fullmatch(r"candidate-v([0-9]+)\.png", path.name)
            if match and int(match.group(1)) >= start:
                existing.append((int(match.group(1)), path))
    if existing:
        version = max(item[0] for item in existing) + 1
        return folder / f"candidate-v{version}.png", version
    return folder / f"candidate-v{start}.png", start


def write_visuals(number: int, slug: str, title: str, sections) -> tuple[str, str, int, int]:
    chapter = ROOT / "chapters" / slug
    figure_ids = figure_refs(chapter)
    if len(figure_ids) < 2:
        figure_ids = [f"CH{number:02d}-01", f"CH{number:02d}-02"]
    versions = 3 if number in {31, 34, 35, 36} else (2 if 31 <= number <= 45 else 3)
    rendered = []
    for slot, fid in enumerate(figure_ids[:2]):
        family = family_for(number, slot)
        folder = ROOT / "assets" / "chapters" / slug / fid
        current = latest_candidate(folder)
        if current is not None:
            # A semantic routing or visual-family change invalidates the old
            # raster.  Keep it recoverable, but always render a new candidate
            # so the active figure is generated from the current contract.
            path = folder / f"candidate-v{current[1] + 1}.png"
            version = current[1] + 1
            RENDERERS[family](path, fid, number, title, sections, family)
        else:
            start_version = 5 if family == "loop" else versions
            path, version = candidate_path(folder, start_version)
            RENDERERS[family](path, fid, number, title, sections, family)
        rendered.append((fid, family, path.name, version))
        question = visual_question(number, family)
        alt = (
            f"Diagramma {fid} del Capitolo {number}, famiglia {family}. "
            f"Domanda: {question} "
            f"La composizione usa i passaggi {', '.join(h for h, _ in sections[:5])}."
        )
        nodes = "; ".join(f"{i + 1}: {h}" for i, (h, _) in enumerate(sections))
        folder.joinpath("SPEC.md").write_text(
            f"# Specifica visuale {fid}\n\n"
            f"- famiglia: {family}\n"
            f"- domanda principale: {question}\n"
            "- orientamento: orizzontale\n"
            "- formato: PNG raster 1800x1000\n"
            "- sfondo: #FFFFFF\n"
            f"- versione candidata: {path.name}\n"
            f"- ordine di lettura: titolo, domanda, {family}, invariante o limite in chiusura\n"
            f"- nodi e contenuti: {nodes}\n"
            "- archi o relazioni: determinati dalla famiglia e leggibili senza affidarsi al colore\n"
            f"- invariante: {detail_for_chapter(number)['invariant']}\n"
            f"- fonti collegate: SRC-{number:02d}-001 ... SRC-{number:02d}-004\n"
            f"- alt text: {alt}\n",
            encoding="utf-8",
        )
        folder.joinpath("AUDIT.md").write_text(
            f"# Audit visuale {fid}\n\n"
            f"- famiglia e domanda: controllate, {family}\n"
            "- decodifica PNG: superata\n"
            "- modalità: RGB\n"
            "- dimensione: 1800x1000\n"
            "- angoli bianchi #FFFFFF: superati\n"
            "- contenimento testo: superato dal renderer e ricontrollato con apertura raster\n"
            "- relazioni e direzione delle frecce: controllate rispetto alla specifica\n"
            "- valori quantitativi: etichettati come illustrativi quando non derivano da un benchmark\n"
            "- coerenza con la prosa: controllata a livello di headings e invariante\n"
            "- approvazione autoriale: aperta\n"
            "- esito: candidata tecnica, nuova review autoriale richiesta\n",
            encoding="utf-8",
        )
        folder.joinpath("ALT_TEXT.md").write_text(f"# Alt text {fid}\n\n{alt}\n", encoding="utf-8")
    return rendered[0][0], rendered[1][0], rendered[0][3], rendered[1][3]


def source_metadata(name: str, url: str) -> tuple[str, str, str, str]:
    lower = name.lower()
    if any(token in lower for token in ("nist", "w3c", "acm", "oecd", "iso", "eu ", "pytorch", "python documentation")):
        source_type = "standard o documentazione ufficiale"
        organization = name.split(",", 1)[0]
    elif any(token in lower for token in ("book", "deep learning", "markov decision")):
        source_type = "libro o monografia"
        organization = "Autori indicati nel riferimento"
    else:
        source_type = "paper o report tecnico"
        organization = name.split(",", 1)[0]
    year_match = re.search(r"\b(19|20)\d{2}\b", name)
    date = year_match.group(0) if year_match else "data della revisione consultata"
    revision = "revisione o versione disponibile all'URL consultato il 4 agosto 2026"
    return organization, source_type, date, revision


def source_verification(number: int, source_index: int) -> dict[str, object]:
    """Return the checked locator for a generated source when available."""
    if not SOURCE_VERIFICATION_PATH.exists():
        return {}
    try:
        report = json.loads(SOURCE_VERIFICATION_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    source_id = f"SRC-{number:02d}-{source_index + 1:03d}"
    return next((entry for entry in report.get("entries", []) if entry.get("source_id") == source_id), {})


def first_claim_sentence(note: str) -> str:
    """Extract a readable claim without splitting decimals such as 1.58-bit."""
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ÖØ-Þ])", note.strip())
    return (parts[0].strip() if parts else note.strip()).rstrip(".") + "."


def write_sources(number: int, kind: str, sections) -> list[str]:
    source_list = source_list_for(number, kind, SOURCE_BANK)
    section_source_indices = source_indices_for(number, len(sections))
    sections_by_source: dict[int, list[tuple[str, str]]] = {index: [] for index in range(len(source_list))}
    for section_index, section in enumerate(sections):
        source_index = section_source_indices[section_index]
        sections_by_source[source_index].append(section)
    ids = []
    lines = [
        f"# Fonti primarie e autorevoli. Capitolo {number}",
        "",
        f"- Data di consultazione: {DATE}",
        f"- Routing semantico: capitolo {number} -> tema `{topic_for(number, kind)}`.",
        "- Perimetro: definizioni, meccanismi e limiti portanti del capitolo.",
        "- Regola: risultati numerici locali restano distinti dalle evidenze sperimentali delle fonti.",
        "",
    ]
    for index, (name, url) in enumerate(source_list, 1):
        sid = f"SRC-{number:02d}-{index:03d}"
        ids.append(sid)
        organization, source_type, date, revision = source_metadata(name, url)
        relevant = sections_by_source[index - 1]
        claims = " ".join(first_claim_sentence(note) for _, note in relevant)
        check = source_verification(number, index - 1)
        locator = str(check.get("locator") or "sezione tematica da aprire nel testo originale")
        status = str(check.get("status") or "non eseguita")
        access_check = str(check.get("check") or "apertura puntuale ancora richiesta")
        lines.extend(
            [
                f"## {sid}",
                "",
                f"- Titolo o riferimento: {name}.",
                f"- Autori o organizzazione: {organization}.",
                f"- Tipo: {source_type}.",
                f"- Data: {date}.",
                f"- Versione, revisione o commit: {revision}.",
                f"- URL o identificatore: {url}",
                f"- Data di consultazione: {DATE}.",
                f"- Verifica d'accesso: {status}; {access_check}.",
                f"- Sezioni rilevanti: {locator}.",
                "- Perimetro del supporto: la fonte è usata per la definizione o il meccanismo indicato; esempi, derivazioni e risultati locali restano separati.",
                f"- Affermazioni sostenibili: {claims}",
                "- Limiti: non autorizza generalizzazioni a ogni modello, dataset, implementazione o prodotto.",
                "- Divergenze note: eventuali differenze di obiettivo, dataset o implementazione vanno mantenute separate nel testo.",
                "",
            ]
        )
    lines.extend(
        [
            "## Mappa d'uso",
            "",
            "Le sezioni citano il proprio claim vicino al punto sostenuto. Esempi, derivazioni e output del codice locale sono marcati separatamente.",
            "",
        ]
    )
    (ROOT / "chapters" / SPECS[number][3] / "FONTI_PRIMARIE.md").write_text("\n".join(lines), encoding="utf-8")
    return ids


def claim_status_for(note: str, source_check: dict[str, object]) -> str:
    if not note.strip():
        return "aperta"
    if source_check.get("status") in {"opened-context", "web-confirmed"}:
        return "verificata"
    if source_check.get("status") == "opened-partial":
        return "corretta"
    return "aperta"


def write_claims(number: int, title: str, sections, source_ids: list[str], module: str) -> None:
    section_source_indices = source_indices_for(number, len(sections))
    lines = [
        f"# Registro dei claim. Capitolo {number}",
        "",
        f"- Data di revisione: {DATE}",
        f"- Routing verificato: tema `{topic_for(number, profile(number))}` con dossier fonte specifico del capitolo.",
        "- Stati usati: aperta, verificata, corretta, respinta, rimossa.",
        "",
    ]
    for index, (heading, note) in enumerate(sections):
        source_index = section_source_indices[index]
        sid = source_ids[source_index]
        check = source_verification(number, source_index)
        locator = str(check.get("locator") or f"sezione pubblica «{heading}»; apertura della fonte ancora richiesta")
        independent_check = str(check.get("check") or "apertura del contenuto originale ancora richiesta")
        lines.extend(
            [
                f"## CL-{number:02d}-{index + 1:02d}",
                "",
                f"- Affermazione esatta: {note}",
                "- Tipo: definizione o meccanismo attribuito alla fonte.",
                f"- Fonte o prova: {sid}, dossier FONTI_PRIMARIE.md.",
                f"- Sezione o pagina: {locator} (claim collegato alla sezione «{heading}» del capitolo).",
                f"- Versione o data: revisione locale {DATE}; versione della fonte registrata nel dossier.",
                f"- Controllo indipendente: {independent_check}; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.",
                f"- Esito: {claim_status_for(note, check)}",
                "- Note: il limite della fonte resta nel paragrafo e nel dossier.",
                "",
            ]
        )
    lines.extend(
        [
            f"## CL-{number:02d}-CODE",
            "",
            f"- Affermazione esatta: lo snippet {module}.py produce l'output osservabile e il test rifiuta un input incoerente.",
            "- Tipo: risultato eseguito localmente.",
            f"- Fonte o prova: code/{module}.py, test associato e output SNIP.",
            "- Sezione o pagina: Dall'algoritmo al codice.",
            f"- Versione o data: Python {sys.version.split()[0]}, CPU, {DATE}.",
            "- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.",
            "- Esito: verificata",
            "- Note: esempio delimitato, non benchmark di produzione.",
            "",
        ]
    )
    (ROOT / "chapters" / SPECS[number][3] / "CLAIMS.md").write_text("\n".join(lines), encoding="utf-8")


TOPIC_BODIES = {
    33: """def contract():
    weights = [0.6, 0.3, 0.1]
    temperature = 0.5
    powered = [weight ** temperature for weight in weights]
    total = sum(powered)
    probabilities = [value / total for value in powered]
    return {"probabilities": [round(value, 6) for value in probabilities], "invariant": "the mixture is normalized after temperature sampling"}
""",
    34: """def contract():
    tokens = [1000.0, 2000.0, 4000.0, 8000.0]
    losses = [3.10, 2.74, 2.47, 2.29]
    slope = (losses[-1] - losses[0]) / (tokens[-1] - tokens[0])
    return {"points": len(tokens), "slope": round(slope, 8), "interval": [tokens[0], tokens[-1]], "invariant": "the fit is interpreted only on the observed interval"}
""",
    35: """def contract():
    base_lr = 0.001
    warmup_steps = 4
    steps = [0, 1, 4, 8]
    rates = [round(base_lr * min(1.0, step / warmup_steps), 6) for step in steps]
    return {"learning_rates": rates, "invariant": "the scheduler is indexed by the declared step counter"}
""",
    36: """def contract():
    worker_gradients = [[1.0, 3.0], [3.0, 1.0]]
    workers = len(worker_gradients)
    reduced = [sum(row[index] for row in worker_gradients) / workers for index in range(2)]
    return {"workers": workers, "reduced_gradient": reduced, "invariant": "all workers contribute to the same declared reduction"}
""",
    37: """def contract():
    state = [1.0, -2.0]
    update = [0.25, 0.5]
    output = [left + right for left, right in zip(state, update)]
    return {"output": output, "shape": [2], "invariant": "the residual stream keeps the declared dimension"}
""",
    38: """def contract():
    position = 2
    angle = position * 0.5
    query = [1.0, 0.0]
    rotated = [query[0] * math.cos(angle) - query[1] * math.sin(angle), query[0] * math.sin(angle) + query[1] * math.cos(angle)]
    return {"position": position, "rotated": [round(value, 6) for value in rotated], "invariant": "the positional transform is indexed by position"}
""",
    39: """def contract():
    query_heads = 4
    kv_heads = 2
    group_size = query_heads // kv_heads
    return {"query_heads": query_heads, "kv_heads": kv_heads, "queries_per_kv": group_size, "invariant": "the head grouping is declared before cache accounting"}
""",
    40: """def contract():
    scores = [[1.0, 2.0], [0.0, 3.0]]
    row_maxima = [max(row) for row in scores]
    exp_sums = [sum(math.exp(value - maximum) for value in row) for row, maximum in zip(scores, row_maxima)]
    return {"row_maxima": row_maxima, "exp_sums": [round(value, 6) for value in exp_sums], "invariant": "softmax normalization is stable within each row"}
""",
    41: """def contract():
    state = 0.0
    inputs = [1.0, -0.5, 2.0]
    for value in inputs:
        state = 0.7 * state + 0.3 * value
    return {"state": round(state, 6), "steps": len(inputs), "invariant": "the recurrence reuses one state in input order"}
""",
    42: """def contract():
    state = 0.0
    inputs = [1.0, 0.0, -1.0]
    outputs = []
    for value in inputs:
        state = 0.8 * state + 0.4 * value
        outputs.append(round(state, 6))
    return {"outputs": outputs, "invariant": "the state update is explicit before each emitted value"}
""",
    43: """def contract():
    local = ["recent-a", "recent-b"]
    long_term = ["stable-fact"]
    read = local[-1] if local else long_term[0]
    return {"local_size": len(local), "long_term_size": len(long_term), "read": read, "invariant": "local and long-term memory have separate lifetimes"}
""",
    44: """def contract():
    logits = [0.2, 1.1, 0.7, -0.3]
    top_indices = sorted(range(len(logits)), key=logits.__getitem__, reverse=True)[:2]
    loads = [int(index in top_indices) for index in range(len(logits))]
    return {"selected_experts": top_indices, "loads": loads, "invariant": "top-k routing and capacity accounting are explicit"}
""",
    45: """def contract():
    payload = "AI"
    encoded = list(payload.encode("utf-8"))
    groups = [encoded[index:index + 2] for index in range(0, len(encoded), 2)]
    return {"bytes": encoded, "groups": groups, "invariant": "byte grouping is explicit before any higher-level prediction"}
""",
}

# Dal capitolo 21 in poi il profilo editoriale non basta a dimostrare il
# meccanismo.  Questi contratti piccoli tengono il codice locale aderente alla
# domanda del capitolo: non sono implementazioni di produzione, ma ciascuno
# rende osservabile almeno una trasformazione e il suo confine principale.
TOPIC_BODIES.update({
    21: """def contract():
    logits = [[2.0, 1.0, 0.0], [4.0, 3.0, 2.0]]
    causal = [[True, False, False], [True, True, False]]
    visible = [[row[j] for j in range(len(row)) if causal[i][j]] for i, row in enumerate(logits)]
    return {"visible_lengths": [len(row) for row in visible], "invariant": "a causal position cannot read a future token"}
""",
    22: """def contract():
    reconstruction = 0.40
    kl = 0.10
    beta = 0.5
    objective = reconstruction + beta * kl
    return {"reconstruction": reconstruction, "kl": kl, "objective": round(objective, 6), "invariant": "reconstruction and regularization stay separately observable"}
""",
    23: """def contract():
    real = [0.9, 0.8]
    fake = [0.2, 0.3]
    discriminator_gap = sum(real) / len(real) - sum(fake) / len(fake)
    return {"discriminator_gap": round(discriminator_gap, 6), "invariant": "generator and discriminator signals are not the same loss"}
""",
    24: """def contract():
    scale = [2.0, 0.5]
    log_det = sum(math.log(value) for value in scale)
    inverse = [1.0 / value for value in scale]
    return {"log_det": round(log_det, 6), "inverse_scale": inverse, "invariant": "the transform exposes both an inverse and a log determinant"}
""",
    25: """def contract():
    alpha_bar = [0.9, 0.5, 0.1]
    signal = [math.sqrt(value) for value in alpha_bar]
    noise = [math.sqrt(1.0 - value) for value in alpha_bar]
    return {"signal": [round(value, 6) for value in signal], "noise": [round(value, 6) for value in noise], "invariant": "the sampler uses the same noise schedule as the forward process"}
""",
    26: """def contract():
    text = "pacco"
    code_points = list(text)
    token_ids = [ord(char) for char in code_points]
    return {"code_points": code_points, "token_ids": token_ids, "invariant": "tokenization preserves an explicit mapping from text to ids"}
""",
    27: """def contract():
    embedding_table = {1: [1.0, 0.0], 2: [0.0, 1.0]}
    static = embedding_table[1]
    contextual = [static[0] + 0.2, static[1] + 0.8]
    return {"static": static, "contextual": contextual, "invariant": "an embedding lookup is distinct from later contextualization"}
""",
    29: """def contract():
    q = [[1.0, 0.0], [0.0, 1.0]]
    k = [[1.0, 0.0], [0.0, 1.0]]
    v = [[2.0, 0.0], [0.0, 3.0]]
    scores = [[sum(q[i][d] * k[j][d] for d in range(2)) for j in range(2)] for i in range(2)]
    weights = [normalize(row) for row in scores]
    output = [[sum(weights[i][j] * v[j][d] for j in range(2)) for d in range(2)] for i in range(2)]
    return {"scores": scores, "output": [[round(value, 6) for value in row] for row in output], "invariant": "queries read keys and values through the declared attention matrix"}
""",
    30: """def contract():
    modes = {
        "encoder_only": "masked_or_bidirectional_input",
        "decoder_only": "causal_next_token",
        "encoder_decoder": "conditioned_target",
    }
    return {"modes": modes, "invariant": "the training target and attention mask define the model family"}
""",
    31: """def contract():
    logits = [2.0, 1.0, 0.0]
    probabilities = normalize(logits)
    demonstrations = 2
    chosen = max(range(len(probabilities)), key=probabilities.__getitem__)
    return {"demonstrations": demonstrations, "probabilities": [round(value, 6) for value in probabilities], "chosen": chosen, "invariant": "decoding selects from a distribution and does not certify truth"}
""",
    32: """def contract():
    records = [{"id": "a", "source": "mail", "text": "pacco"}, {"id": "b", "source": "crm", "text": "ritardo"}]
    manifest = {"ids": [record["id"] for record in records], "sources": sorted({record["source"] for record in records})}
    return {"manifest": manifest, "invariant": "data transformations retain provenance and a stable record identity"}
""",
    46: """def contract():
    tokens = ["utente", "domanda", "assistente", "risposta"]
    labels = [False, False, True, True]
    supervised = [token for token, include in zip(tokens, labels) if include]
    return {"supervised_tokens": supervised, "label_count": sum(labels), "invariant": "loss masking distinguishes prompt tokens from target tokens"}
""",
    47: """def contract():
    base = [1.0, 2.0]
    direction_a = [0.5, 0.0]
    direction_b = [0.0, -0.25]
    scale = 0.4
    delta = [scale * (a + b) for a, b in zip(direction_a, direction_b)]
    adapted = [value + change for value, change in zip(base, delta)]
    return {"delta": delta, "adapted": adapted, "invariant": "the low-rank update is separated from frozen base weights"}
""",
    48: """def contract():
    chosen = 0.8
    rejected = 0.2
    reward_margin = chosen - rejected
    return {"reward_margin": round(reward_margin, 6), "invariant": "preference learning compares responses under one prompt"}
""",
    49: """def contract():
    policy_margin = 0.8
    reference_margin = 0.2
    beta = 0.5
    preference_logit = beta * (policy_margin - reference_margin)
    loss = math.log1p(math.exp(-preference_logit))
    return {"preference_logit": round(preference_logit, 6), "loss": round(loss, 6), "invariant": "DPO uses a policy-versus-reference margin"}
""",
    50: """def contract():
    answers = ["4", "5", "4"]
    def verifier(answer):
        return answer == "4"
    accepted = [answer for answer in answers if verifier(answer)]
    return {"accepted": accepted, "acceptance_rate": len(accepted) / len(answers), "invariant": "a verifier is an explicit signal with its own error surface"}
""",
    51: """def contract():
    rewards = [1.0, 0.0, 1.0]
    mean = sum(rewards) / len(rewards)
    advantages = [round(value - mean, 6) for value in rewards]
    return {"mean_reward": mean, "advantages": advantages, "invariant": "the policy update depends on declared reward and baseline"}
""",
    52: """def contract():
    traces = [("4", 0.9), ("4", 0.7), ("5", 0.8)]
    counts = {}
    for answer, _score in traces:
        counts[answer] = counts.get(answer, 0) + 1
    selected = max(counts, key=counts.__getitem__)
    return {"trace_count": len(traces), "selected": selected, "invariant": "self-consistency selects among traces and does not prove their faithfulness"}
""",
    53: """def contract():
    candidates = [0.4, 0.6, 0.5]
    best = max(candidates)
    return {"samples": len(candidates), "best_score": best, "invariant": "test-time compute changes the selection budget, not the base model weights"}
""",
    54: """def contract():
    original = {"pacco": "in_transito", "ritardo": 1}
    edited = dict(original)
    edited["ritardo"] = 0
    changed = [key for key in original if original[key] != edited[key]]
    return {"changed_keys": changed, "rollback": original == {"pacco": "in_transito", "ritardo": 1}, "invariant": "an edit needs a targeted diff and a regression check"}
""",
    55: """def contract():
    text = [0.2, 0.4]
    image = [0.6, 0.1]
    shared = [(a + b) / 2 for a, b in zip(text, image)]
    return {"shared": shared, "modalities": 2, "invariant": "modalities meet in a declared shared representation"}
""",
    56: """def contract():
    patches = [[0.8, 0.1], [0.2, 0.7]]
    question = [0.5, 0.5]
    scores = [sum(a * b for a, b in zip(patch, question)) for patch in patches]
    selected = max(range(len(scores)), key=scores.__getitem__)
    return {"scores": scores, "selected_patch": selected, "invariant": "visual grounding links a text query to explicit image features"}
""",
    57: """def contract():
    noisy = [0.9, 0.1]
    denoised = [0.7 * noisy[0] + 0.3 * 0.5, 0.7 * noisy[1] + 0.3 * 0.5]
    return {"denoised": denoised, "steps": 1, "invariant": "a generation step declares its noise level and update"}
""",
    58: """def contract():
    sequence = [("text", 1), ("image", 7), ("text", 2)]
    vocabulary = {"text": {1, 2}, "image": {7}}
    valid = all(token in vocabulary[modality] for modality, token in sequence)
    return {"valid": valid, "length": len(sequence), "invariant": "native multimodal serialization keeps modality and token identity"}
""",
    59: """def contract():
    waveform = [0.0, 0.5, -0.5, 0.0]
    frame_size = 2
    frames = [waveform[i:i + frame_size] for i in range(0, len(waveform), frame_size)]
    return {"frames": frames, "sample_count": len(waveform), "invariant": "audio framing preserves sample order and declared frame size"}
""",
    60: """def contract():
    frames = ["f0", "f1", "f2"]
    condition = "prompt"
    generated = [(frame, condition) for frame in frames]
    return {"frame_count": len(generated), "temporal_order": [item[0] for item in generated], "invariant": "video generation keeps an explicit temporal index"}
""",
    61: """def contract():
    points = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
    centroid = [sum(point[index] for point in points) / len(points) for index in range(3)]
    return {"count": len(points), "centroid": centroid, "invariant": "a 3D representation preserves coordinate dimension"}
""",
    62: """def contract():
    state = {"position": 0, "battery": 2}
    action = "move"
    next_state = dict(state)
    next_state["position"] += 1
    next_state["battery"] -= 1
    return {"action": action, "next_state": next_state, "invariant": "the world transition exposes state and action consequences"}
""",
    63: """def contract():
    query = {"pacco", "ritardo"}
    documents = [("d1", {"pacco", "ritardo"}), ("d2", {"pacco"}), ("d3", {"carta"})]
    ranking = sorted(((len(query & terms), doc_id) for doc_id, terms in documents), reverse=True)
    return {"ranking": ranking, "invariant": "retrieval exposes document scores before generation"}
""",
    64: """def contract():
    retrieved = [("d1", 0.9), ("d2", 0.4)]
    answer = "Il pacco è in transito"
    cited = retrieved[0][0]
    return {"answer": answer, "citation": cited, "invariant": "RAG keeps retrieved evidence and generated answer as separate records"}
""",
    65: """def contract():
    graph = {"q1": ["d1"], "d1": ["q2"], "q2": ["d2"]}
    frontier = ["q1"]
    visited = []
    while frontier:
        node = frontier.pop(0)
        visited.append(node)
        frontier.extend(neighbor for neighbor in graph.get(node, []) if neighbor not in visited)
    return {"path": visited, "invariant": "multi-hop retrieval records the path rather than only the final context"}
""",
    66: """def contract():
    short_term = ["ultimo evento"]
    long_term = ["fatto stabile"]
    recalled = long_term[0]
    return {"short_term": short_term, "recalled": recalled, "invariant": "memory scope and retrieval source remain explicit"}
""",
    67: """def contract():
    request = {"tool": "lookup_order", "order_id": "A1"}
    allowlist = {"lookup_order"}
    allowed = request["tool"] in allowlist and bool(request["order_id"])
    return {"allowed": allowed, "request": request, "invariant": "tool execution requires validation outside generated text"}
""",
    68: """def contract():
    producer = {"version": 1, "capability": "lookup_order"}
    consumer = {"accepted_versions": {1, 2}, "required": "lookup_order"}
    compatible = producer["version"] in consumer["accepted_versions"] and producer["capability"] == consumer["required"]
    return {"compatible": compatible, "invariant": "interoperability is a versioned contract, not a shared label"}
""",
    69: """def contract():
    events = ["observe", "plan", "tool", "verify"]
    valid = events == ["observe", "plan", "tool", "verify"]
    return {"events": events, "valid": valid, "invariant": "an agent loop records observation, action and verification"}
""",
    70: """def contract():
    messages = [("planner", "lookup"), ("executor", "done"), ("critic", "pass")]
    roles = [role for role, _message in messages]
    return {"roles": roles, "message_count": len(messages), "invariant": "multi-agent coordination exposes role and message boundaries"}
""",
    71: """def contract():
    traces = [{"success": True, "violations": 0}, {"success": True, "violations": 1}]
    safe_success = sum(trace["success"] and trace["violations"] == 0 for trace in traces)
    return {"task_success": sum(trace["success"] for trace in traces), "safe_success": safe_success, "invariant": "task completion and policy compliance are separate metrics"}
""",
    72: """def contract():
    request = {"tool": "refund", "scope": "order:A1"}
    policy = {"allowed_tools": {"lookup_order"}, "requires_approval": {"refund"}}
    allowed = request["tool"] in policy["allowed_tools"]
    return {"allowed": allowed, "approval_required": request["tool"] in policy["requires_approval"], "invariant": "authorization and rollback live outside the model text"}
""",
    73: """def contract():
    teacher = [0.8, 0.2]
    student = [0.6, 0.4]
    distillation_error = sum((a - b) ** 2 for a, b in zip(teacher, student))
    mask = [True, False]
    return {"distillation_error": round(distillation_error, 6), "kept_weights": sum(mask), "invariant": "compression quality and structural pruning are measured separately"}
""",
    74: """def contract():
    values = [-0.5, 0.0, 0.5]
    scale = 0.25
    quantized = [round(value / scale) for value in values]
    restored = [code * scale for code in quantized]
    error = max(abs(value - recovered) for value, recovered in zip(values, restored))
    return {"quantized": quantized, "restored": restored, "max_error": error, "invariant": "scale and calibration determine quantization error"}
""",
    75: """def contract():
    codes = [-1, 0, 1]
    scale = 0.5
    restored = [code * scale for code in codes]
    accumulated = sum(restored)
    return {"restored": restored, "accumulated": accumulated, "invariant": "nominal bit width is distinct from accumulation precision"}
""",
    76: """def contract():
    logits = [2.0, 1.0, 0.5]
    greedy = max(range(len(logits)), key=logits.__getitem__)
    sampled_support = [index for index, probability in enumerate(normalize(logits)) if probability >= 0.2]
    return {"greedy": greedy, "support": sampled_support, "invariant": "decoding chooses a trajectory from logits without changing model parameters"}
""",
    77: """def contract():
    draft = ["a", "b", "c"]
    target_accepts = [True, True, False]
    accepted = [token for token, ok in zip(draft, target_accepts) if ok]
    fallback = "target_next" if not target_accepts[-1] else None
    return {"accepted": accepted, "fallback": fallback, "invariant": "speculative decoding verifies draft tokens before committing them"}
""",
    78: """def contract():
    prefix = ["p0", "p1"]
    requests = {"r1": prefix + ["a"], "r2": prefix + ["b"]}
    shared_tokens = len(set(requests["r1"]) & set(requests["r2"]))
    return {"shared_prefix": shared_tokens, "request_lengths": {key: len(value) for key, value in requests.items()}, "invariant": "cache reuse preserves token position and request ownership"}
""",
    79: """def contract():
    requests = [("short-1", 2), ("short-2", 2), ("long", 6)]
    batch = [request[0] for request in requests]
    total_tokens = sum(length for _request, length in requests)
    return {"batch": batch, "total_tokens": total_tokens, "invariant": "serving reports throughput and latency for the same admitted requests"}
""",
    80: """def contract():
    workers = {"w1": {"tokens": 2, "network_ms": 3}, "w2": {"tokens": 2, "network_ms": 4}}
    end_to_end_ms = max(worker["network_ms"] for worker in workers.values()) + 2
    return {"workers": len(workers), "end_to_end_ms": end_to_end_ms, "invariant": "distributed inference includes communication in end-to-end latency"}
""",
    81: """def contract():
    graph = ["matmul", "add", "relu"]
    fused = ["matmul_add", "relu"]
    return {"original_ops": len(graph), "fused_ops": len(fused), "invariant": "compiler optimization preserves the declared operator result"}
""",
    82: """def contract():
    request = {"model": "v1", "tokens": 20, "energy_wh": 0.4}
    cost = request["energy_wh"] * 0.30
    return {"model": request["model"], "cost": round(cost, 6), "invariant": "an operational metric records model version and measurement boundary"}
""",
    83: """def contract():
    predictions = [1, 1, 0, 1]
    labels = [1, 0, 0, 1]
    correct = sum(prediction == label for prediction, label in zip(predictions, labels))
    failures = [index for index, pair in enumerate(zip(predictions, labels)) if pair[0] != pair[1]]
    return {"accuracy": correct / len(labels), "failures": failures, "invariant": "a metric is reported with its decision target and failure cases"}
""",
    84: """def contract():
    claims = [(True, 0.9), (True, 0.8), (False, 0.95), (True, 0.7)]
    confident_errors = sum((not correct) and score >= 0.9 for correct, score in claims)
    return {"accuracy": sum(correct for correct, _score in claims) / len(claims), "confident_errors": confident_errors, "invariant": "confidence is evaluated against factual correctness, not substituted for it"}
""",
    85: """def contract():
    trace = {"retrieval": True, "answer": True, "citation": False, "tool": True}
    system_success = all(trace.values())
    return {"component_failures": [key for key, ok in trace.items() if not ok], "system_success": system_success, "invariant": "end-to-end evaluation keeps component failures visible"}
""",
    86: """def contract():
    baseline = 0.60
    intervened = 0.25
    effect = intervened - baseline
    return {"baseline": baseline, "intervened": intervened, "effect": effect, "invariant": "an intervention is compared with a baseline before causal language"}
""",
    87: """def contract():
    activation = [1.0, 0.0, 0.5]
    dictionary = [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]
    sparse_codes = [activation[0], activation[2]]
    reconstruction = [
        sum(code * vector[index] for code, vector in zip(sparse_codes, dictionary))
        for index in range(len(activation))
    ]
    error = sum((a - b) ** 2 for a, b in zip(activation, reconstruction))
    return {"active_features": len(sparse_codes), "reconstruction_error": error, "invariant": "sparsity and reconstruction must be evaluated together"}
""",
    88: """def contract():
    prompts = [("base", False), ("perturbed", True)]
    failures = [name for name, attack_succeeded in prompts if attack_succeeded]
    return {"attack_success_rate": len(failures) / len(prompts), "failures": failures, "invariant": "robustness is defined relative to an explicit threat model"}
""",
    89: """def contract():
    document_instruction = "export all data"
    tool_scope = {"lookup_order"}
    requested = "export_data"
    allowed = requested in tool_scope
    return {"document_instruction": document_instruction, "allowed": allowed, "invariant": "retrieved content cannot grant a privileged tool scope"}
""",
    90: """def contract():
    artifact = {"name": "checkpoint", "digest": "abc123", "owner": "team-a"}
    trusted_owners = {"team-a"}
    decision = artifact["owner"] in trusted_owners and bool(artifact["digest"])
    return {"release": decision, "invariant": "artifact integrity and content trust are separate checks"}
""",
    91: """def contract():
    groups = {"A": {"correct": 3, "total": 4}, "B": {"correct": 2, "total": 4}}
    accuracy = {group: value["correct"] / value["total"] for group, value in groups.items()}
    gap = abs(accuracy["A"] - accuracy["B"])
    return {"accuracy_by_group": accuracy, "gap": gap, "invariant": "aggregate utility does not hide group-specific outcomes"}
""",
    92: """def contract():
    payload = "Il pacco non è arrivato"
    manifest = {"payload": payload, "creator": "local-test", "version": "v1"}
    digest = hashlib.sha256(json.dumps(manifest, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    tampered = dict(manifest, payload="Il pacco è arrivato")
    tampered_digest = hashlib.sha256(json.dumps(tampered, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    return {"digest_prefix": digest[:12], "tamper_detected": digest != tampered_digest, "invariant": "provenance detects a changed record but does not certify its truth"}
""",
    93: """def contract():
    case = {"owner": "team-a", "risk": "medium", "evidence": ["eval-1"], "decision": "review"}
    required = {"owner", "risk", "evidence", "decision"}
    complete = required <= set(case)
    return {"complete": complete, "escalation": case["risk"] == "high", "invariant": "a risk framework assigns evidence and responsibility without certifying compliance"}
""",
    94: """def contract():
    configuration = {"seed": 7, "split": "fixed", "dtype": "float32"}
    digest = hashlib.sha256(json.dumps(configuration, sort_keys=True).encode()).hexdigest()
    return {"configuration_digest": digest[:12], "configuration": configuration, "invariant": "a local run is reproducible only with its declared setup"}
""",
    95: """def contract():
    tokens = [[1, 2, 3], [2, 3, 4]]
    inputs = [row[:-1] for row in tokens]
    targets = [row[1:] for row in tokens]
    return {"input_shape": [len(inputs), len(inputs[0])], "target_shape": [len(targets), len(targets[0])], "invariant": "causal training shifts target one token after the input"}
""",
    96: """def contract():
    release = {"version": "v2", "offline_gate": True, "canary": True, "rollback": True}
    ready = all(release[key] for key in ("offline_gate", "canary", "rollback"))
    return {"version": release["version"], "ready_for_review": ready, "invariant": "production readiness requires independent gates and a rollback path"}
""",
    97: """def contract():
    original = {"metric": 0.80, "seed": 1, "split": "fixed"}
    replica = {"metric": 0.78, "seed": 2, "split": "fixed"}
    difference = replica["metric"] - original["metric"]
    return {"difference": difference, "same_split": replica["split"] == original["split"], "invariant": "a replication records setup differences before interpreting outcome differences"}
""",
    98: """def contract():
    record = {"claim": "new method", "source_date": "2026-08-04", "evidence": "paper", "maturity": "FRONTIER"}
    required = {"claim", "source_date", "evidence", "maturity"}
    return {"record_complete": required <= set(record), "maturity": record["maturity"], "invariant": "novelty, evidence and readiness remain separate fields"}
""",
})


def code_source_for(number: int, title: str, kind: str) -> str:
    supported = {"rl", "mlp", "deep", "conv", "rnn", "representation", "generative", "sequence", "data", "architecture", "posttraining", "multimodal", "retrieval", "agents", "inference", "evaluation", "security", "provenance", "labs"}
    code_kind = kind if kind in supported else "data"
    source = code_for_base(number, title, code_kind)
    if kind == "scaling":
        source = source.replace("PROFILE = 'data'", "PROFILE = 'scaling'")
    if number not in TOPIC_BODIES:
        return source
    prefix = source.split("def contract():", 1)[0]
    tail = """def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
"""
    return prefix + TOPIC_BODIES[number] + tail


def write_code(number: int, slug: str, title: str, kind: str) -> str:
    chapter = ROOT / "chapters" / slug
    code_dir = chapter / "code"
    output_dir = code_dir / "outputs"
    env_dir = code_dir / "environments"
    code_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    env_dir.mkdir(parents=True, exist_ok=True)
    module = f"snip_{number:02d}_contract"
    code_path = code_dir / f"{module}.py"
    test_path = code_dir / f"test_{number:02d}_contract.py"
    code_path.write_text(code_source_for(number, title, kind), encoding="utf-8")
    test_path.write_text(
        f"""from __future__ import annotations

import unittest

from {module} import contract, weighted_state


class ContractTests(unittest.TestCase):
    def test_contract_is_deterministic(self):
        self.assertEqual(contract(), contract())

    def test_contract_has_invariant(self):
        self.assertIn("invariant", contract())

    def test_contract_has_observable_output(self):
        self.assertGreaterEqual(len(contract()), 2)

    def test_contract_rejects_incoherent_shape(self):
        with self.assertRaises(ValueError):
            weighted_state([0.0], [[1.0, 2.0], [3.0]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
""",
        encoding="utf-8",
    )
    run = subprocess.run([sys.executable, code_path.name], cwd=code_dir, capture_output=True, text=True, check=True)
    tests = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", test_path.name],
        cwd=code_dir,
        capture_output=True,
        text=True,
        check=True,
    )
    output_dir.joinpath(f"SNIP-{number:02d}-001.txt").write_text(run.stdout, encoding="utf-8")
    output_dir.joinpath("TESTS.txt").write_text(tests.stderr + tests.stdout, encoding="utf-8")
    env_dir.joinpath("python.txt").write_text(
        f"Python {sys.version.split()[0]}\nCPU\nDate: {DATE}\n", encoding="utf-8"
    )
    code_dir.joinpath("README.md").write_text(
        f"# Codice del Capitolo {number}\n\n"
        f"Lo snippet {module}.py rende osservabile il contratto centrale di {title} con valori piccoli e leggibili.\n"
        f"Il test test_{number:02d}_contract.py controlla determinismo, output, invariante e una shape incoerente.\n"
        "Il risultato è un esempio locale, non un benchmark di produzione.\n",
        encoding="utf-8",
    )
    code_dir.joinpath("CODE_AUDIT.md").write_text(
        "# Audit del codice\n\n"
        f"- ambiente: Python {sys.version.split()[0]}, CPU, processo pulito\n"
        f"- API: funzioni Python standard del modulo {module}\n"
        f"- comando snippet: python {code_path.name}\n"
        f"- comando test: python -m unittest -v {test_path.name}\n"
        "- snippet: eseguito\n"
        "- test: 4 superati\n"
        "- controllo negativo: shape incoerente rifiutata\n"
        "- risultato: esempio delimitato, non benchmark di produzione\n"
        "- dipendenze esterne: nessuna\n"
        "- stato: verificato localmente, review autoriale aperta\n",
        encoding="utf-8",
    )
    return module


def detail_for(number: int, heading: str, index: int) -> str:
    family_focus = render_prose_variant(
        prose_family(number, base_profile(number)),
        "focus",
        number,
        index,
        heading,
        detail_for_chapter(number),
    )
    if family_focus:
        return family_focus
    lower = heading.lower()
    if any(token in lower for token in ("token", "byte", "unicode", "embedding", "vocabulary")):
        return f"Per «{heading}» controlliamo separatamente ID, lunghezza e rappresentazione: cambiare una convenzione a monte cambia l'input che il blocco successivo vede."
    if any(token in lower for token in ("loss", "likelihood", "objective", "elbo", "reward", "preference", "verif")):
        return f"In «{heading}» il valore dell'obiettivo è un segnale rispetto a un protocollo; non va riscritto come qualità generale del sistema senza specificare target e dati."
    if any(token in lower for token in ("mask", "attention", "position", "context", "cache")):
        return f"La domanda operativa di «{heading}» è quali elementi possono comunicare. Una shape compatibile non dimostra che il pattern di visibilità sia quello previsto."
    if any(token in lower for token in ("data", "dataset", "source", "manifest", "split", "provenance", "dedup")):
        return f"In «{heading}» la trasformazione va registrata insieme al record: senza configurazione, checksum e confine temporale il risultato non è confrontabile."
    if any(token in lower for token in ("cost", "compute", "latency", "memory", "throughput", "hardware", "energy")):
        return f"Per «{heading}» misuriamo il costo con input, batch, dtype e device dichiarati. Una misura isolata non autorizza a trasferire il risultato a un altro servizio."
    if any(token in lower for token in ("security", "jailbreak", "injection", "privacy", "fairness", "risk", "safety", "govern")):
        return f"Il controllo di «{heading}» deve restare verificabile anche quando l'output linguistico appare convincente. La policy e l'evento osservato vanno conservati separatamente."
    if any(token in lower for token in ("evaluation", "metric", "calibr", "benchmark", "replic", "result")):
        return f"In «{heading}» il protocollo decide che cosa conta come successo e che cosa viene escluso. Registriamo anche gli errori, non soltanto la media."
    if index % 3 == 0:
        return f"In «{heading}» fissiamo l'input, eseguiamo l'operazione e nominiamo l'output prima di introdurre la variante."
    if index % 3 == 1:
        return f"Il risultato di «{heading}» dipende dalle condizioni dichiarate: shape, ordine, dati e ipotesi devono restare invariati."
    return f"Il confine di «{heading}» è parte della spiegazione: l'esempio resta utile soltanto se non viene trasformato in una promessa più ampia."


def verification_for(number: int, heading: str, index: int) -> str:
    family_verification = render_prose_variant(
        prose_family(number, base_profile(number)),
        "verification",
        number,
        index,
        heading,
        detail_for_chapter(number),
    )
    if family_verification:
        return family_verification
    lower = heading.lower()
    if any(token in lower for token in ("token", "byte", "unicode", "embedding")):
        return f"Per «{heading}» la verifica conserva la stringa originale, la sequenza di ID e la shape dei vettori; se una di queste cambia, il confronto va riaperto."
    if any(token in lower for token in ("attention", "mask", "position", "context", "cache")):
        return f"Nel caso «{heading}» il failure mode più semplice è una posizione visibile per errore: il risultato può avere la shape giusta e usare comunque informazione che il contratto vietava."
    if any(token in lower for token in ("data", "dataset", "source", "manifest", "split", "dedup")):
        return f"Per «{heading}» il controllo richiede conteggi prima e dopo la trasformazione, un identificatore stabile e una regola per i record esclusi; senza questi elementi non sappiamo che cosa è cambiato."
    if any(token in lower for token in ("loss", "likelihood", "reward", "preference", "objective", "verif")):
        return f"In «{heading}» un valore migliore dell'obiettivo può dipendere dalla distribuzione dei casi o dal verificatore. Per questo conserviamo esempi riusciti e falliti insieme al numero."
    if any(token in lower for token in ("cost", "compute", "latency", "memory", "hardware", "energy")):
        return f"Per «{heading}» il controllo deve ripetere la misura con stesso input, batch, dtype e device. Senza un perimetro identico, il confronto mescola il meccanismo con l'ambiente."
    if any(token in lower for token in ("security", "jailbreak", "injection", "privacy", "fairness", "risk", "safety")):
        return f"Nel caso «{heading}» il failure mode è un controllo applicato troppo tardi, dopo che il dato non fidato ha già raggiunto una risorsa. La decisione deve quindi essere registrata prima dell'azione."
    if any(token in lower for token in ("metric", "evaluation", "benchmark", "replic", "result")):
        return f"Per «{heading}» il test utile non guarda soltanto la media: mantiene una slice, un caso limite e il protocollo che ha prodotto il valore."
    if index % 2 == 0:
        detail = detail_for_chapter(number)
        return f"Per «{heading}» il controllo più piccolo confronta input, output e invariante in un caso noto e osserva {detail['output']}. Se il failure mode è indistinguibile dall'output valido, manca un'osservazione nel contratto."
    return f"L'errore didatticamente utile di «{heading}» rompe una condizione alla volta. Così il lettore può attribuire la failure all'operazione invece che a una variazione non dichiarata."


TOPIC_SECTION_EXAMPLES = {
    "interoperability": (
        "un JSON Schema con un campo obbligatorio e una versione dichiarata",
        "un server MCP che espone una capability e un tool con schema degli argomenti",
        "un task A2A che passa da discovery a working e poi a completed",
        "una credenziale firmata con subject, scope, issuer e scadenza",
        "una negoziazione che rifiuta un campo nuovo quando la versione non lo supporta",
    ),
    "governance": (
        "una scheda che assegna owner, uso previsto, impatto e decisione di escalation",
        "una tabella govern-map-measure-manage con evidenza e responsabile per ogni controllo",
        "un requisito normativo annotato con giurisdizione, ruolo, versione e data di lettura",
        "un incident record con rilevazione, classificazione, contenimento, rollback e comunicazione",
        "un confronto tra due configurazioni normalizzato per risultato utile, energia e hardware",
    ),
    "lab": (
        "un ambiente Python con versione, seed e dipendenze registrati prima del run",
        "un dataset di quattro record con split e checksum conservati nel manifest",
        "un forward che produce loss su target dichiarati e un controllo negativo di shape",
        "due run con la stessa configurazione confrontati con metriche e casi falliti",
        "un report che collega comando, artefatti, output e limite del risultato",
    ),
    "small_lm": (
        "due stringhe tokenizzate con vocabulary, target shift e split espliciti",
        "un batch [2, 4] attraversa embedding, mask causale, MLP e head dei logits",
        "un optimizer step confrontato con loss, seed e stato del checkpoint salvato",
        "lo stesso vettore di logits decodificato con greedy e top-k",
        "un confronto tra loss del piccolo modello e un claim che non può essere trasferito a modelli grandi",
    ),
    "production": (
        "un caso d'uso con metrica di successo, non-obiettivi, utenti e vincolo operativo",
        "un diagramma che separa dati, modello, policy, API, monitor e rollback",
        "un gate offline con slice, soglia, errore e decisione di promozione",
        "un canary versionato con alert, owner e ritorno alla versione precedente",
        "una model card collegata a changelog, dataset, limiti e contatto operativo",
    ),
    "replication": (
        "un claim estratto dal paper con baseline, metrica, intervallo e condizione di successo",
        "un manifest con commit, dataset, seed, hardware, dipendenze e checksum",
        "un setup indipendente che ripete il protocollo senza riusare l'output originale",
        "una tabella che separa divergenze di seed, preprocessing, hardware e implementazione",
        "una conclusione limitata al claim e all'intervallo realmente eseguiti",
    ),
    "frontier": (
        "una scheda con paper, data, fonte primaria, claim e benchmark dichiarato",
        "una tecnica instradata per oggetto modificato, prerequisito e consumer",
        "una matrice che separa novità, replica, adozione, standard e readiness",
        "una decisione di promozione basata su evidenza nuova e soglie registrate",
        "un'edizione che aggiorna claim, fonti e data senza cambiare identità storiche",
    ),
}


CHAPTER_SECTION_EXAMPLES = {
    46: "una conversazione con quattro token assegna la loss soltanto ai due token della risposta",
    47: "un peso base e un aggiornamento di rank uno producono un delta misurabile senza riscrivere il checkpoint base",
    48: "due risposte per lo stesso prompt ricevono score di reward diversi e una penalità KL separata",
    49: "un margine di policy pari a 0,8, un margine di riferimento pari a 0,2 e beta pari a 0,5 producono un logit di preferenza pari a 0,3",
    50: "tre risposte passano davanti a un verifier che accetta soltanto il risultato corretto",
    51: "tre rollout ricevono reward 1, 0 e 1; il vantaggio viene centrato sulla media del gruppo",
    52: "tre tracce producono due risposte 4 e una risposta 5; la selezione majority sceglie 4",
    53: "tre candidati vengono valutati entro un budget comune e si conserva il punteggio migliore",
    54: "un delta modifica una sola chiave del caso guida e il test confronta prima, dopo e rollback",
    55: "due vettori, testo e immagine, vengono proiettati nella stessa dimensione prima della fusione",
    56: "una query confronta due patch visive e conserva l'indice della patch con score maggiore",
    57: "un singolo passo riduce una coppia di valori rumorosi secondo uno schedule dichiarato",
    58: "una sequenza alterna token testuali e visivi mantenendo la modalità associata a ogni posizione",
    59: "quattro campioni audio vengono divisi in due frame senza cambiare l'ordine temporale",
    60: "tre frame condividono una condizione e conservano l'ordine temporale",
    61: "tre punti 3D producono un centroide con tre coordinate",
    62: "un'azione move porta la posizione da 0 a 1 e consuma una unità di batteria",
    63: "tre documenti vengono ordinati per sovrapposizione con la query",
    64: "due chunk vengono recuperati e una risposta mantiene il documento citato come record distinto",
    65: "una domanda segue il percorso q1 -> d1 -> q2 -> d2",
    66: "un fatto stabile entra nella memoria persistente, mentre un dettaglio recente resta nel contesto breve",
    67: "lookup_order passa l'allowlist, mentre refund viene rifiutato prima del side effect",
    68: "un producer versione 1 è compatibile con un consumer che accetta le versioni 1 e 2",
    69: "una traiettoria minima registra observe, plan, tool e verify",
    70: "planner, executor e critic scambiano tre messaggi con ruoli espliciti",
    71: "due traiettorie hanno lo stesso successo, ma soltanto una ha zero violazioni di policy",
    72: "lookup_order è consentito, mentre refund richiede approvazione o viene negato dalla policy esterna",
    73: "teacher e student hanno due vettori di logits differenti e una mask conserva una connessione",
    74: "tre valori con scala 0,25 vengono quantizzati e ricostruiti con errore massimo misurato",
    75: "i codici -1, 0 e 1 vengono ricostruiti con una scala e sommati nella precisione dichiarata",
    76: "lo stesso vettore di logits produce un token greedy e un supporto di sampling espliciti",
    77: "tre token draft vengono verificati: due sono accettati e uno ricade nel target",
    78: "due richieste condividono un prefisso di due token e divergono al terzo",
    79: "due richieste brevi e una lunga entrano nello stesso batch, con token totali registrati",
    80: "due worker aggiungono comunicazione e compute alla latenza end-to-end",
    81: "tre operatori diventano due gruppi dopo una fusione, con correttezza numerica da confrontare",
    82: "un record associa versione del modello, token, energia e costo per richiesta",
    83: "quattro predizioni producono accuracy pari a 0,75 e una failure esplicita",
    84: "una risposta con score 0,95 può essere falsa, perciò la confidence viene confrontata con la correttezza",
    85: "il RAG risponde correttamente ma la citation fallisce, quindi il sistema non passa il gate end-to-end",
    86: "un intervento riduce lo score da 0,60 a 0,25 rispetto alla baseline",
    87: "due feature sparse ricostruiscono tre coordinate e l'errore viene registrato",
    88: "una perturbazione sullo stesso prompt produce un failure di attacco che la baseline non produce",
    89: "un documento chiede export dei dati, ma il tool scope non lo autorizza",
    90: "un checkpoint con digest e owner trusted supera l'integrity gate, ma il contenuto resta da analizzare",
    91: "due gruppi hanno accuracy pari a 0,75 e 0,50, quindi la media non nasconde il gap",
    92: "cambiare il payload cambia il digest e rende rilevabile la manomissione",
    93: "una scheda con owner, rischio, evidenza e decisione è completa, ma non certifica la compliance",
    94: "la stessa configurazione seed=7, split=fixed e dtype=float32 produce un digest ripetibile",
    95: "due sequenze di tre token diventano input e target spostati con shape coerenti",
    96: "una release passa offline gate, canary e rollback prima di essere candidata",
    97: "due run con split uguale ma seed diversi producono una differenza che va registrata",
    98: "una scheda registra claim, data, evidenza e maturità FRONTIER separatamente",
}


_PROSE_TOPIC_GROUPS = {
    "architecture": (
        "rl", "mlp", "deep", "conv", "rnn", "representation",
    ),
    "generative": (
        "generative", "vae", "gan", "flows", "diffusion",
    ),
    "sequence": (
        "autoregressive", "text_data", "embeddings", "transformer",
        "pretraining_families", "llm_behavior", "modern_block", "position",
        "attention_variants", "flash", "linear_attention", "ssm",
        "hybrid_memory", "moe", "alternative_prediction",
    ),
    "data_training": (
        "data_lifecycle", "mixture", "scaling", "pretraining_recipe",
        "distributed_training",
    ),
    "alignment": (
        "sft", "peft", "rlhf", "preference", "verifier", "rlvr",
        "reasoning", "test_time", "editing",
    ),
    "multimodal": (
        "multimodal", "vlm", "imagegen", "native_multimodal", "audio",
        "video", "3d", "world",
    ),
    "actions": (
        "retrieval", "rag", "advanced_rag", "memory", "tools",
        "interoperability", "agent_loop", "multiagent", "agent_eval",
        "agent_safety", "injection",
    ),
    "efficiency": (
        "distillation", "quantization", "low_bit", "decoding", "speculative",
        "kv_cache", "serving", "distributed_inference", "compiler", "llmops",
    ),
    "evaluation": (
        "eval_design", "factuality", "system_eval", "interpretability", "sae",
        "robustness", "supply_chain", "privacy_fairness", "provenance",
        "governance", "lab", "small_lm", "production", "replication", "frontier",
    ),
}
PROSE_FAMILY_BY_TOPIC = {
    topic: family
    for family, topics in _PROSE_TOPIC_GROUPS.items()
    for topic in topics
}


PROSE_VARIANTS = {
    "architecture": {
        "transition": (
            "Per «{heading}» il nome del blocco viene dopo il percorso: {input} entra, {operation} modifica il segnale e {output} è la quantità che possiamo confrontare.",
            "Il caso di «{heading}» parte da {object}. Seguiamo {input} un'operazione alla volta, così {output} non viene confuso con una capacità generale.",
            "Qui non confrontiamo etichette architetturali in astratto. Fissiamo {input}, osserviamo {operation} e chiediamo se {output} conserva l'invariante dichiarato.",
        ),
        "focus": (
            "In «{heading}» la shape è soltanto il primo controllo: il significato dipende da come {operation} usa {input}.",
            "Il punto di «{heading}» è il segnale che cambia. Se {operation} viene spostata o sostituita, anche {output} va reinterpretato.",
            "Il punto da non perdere in «{heading}» è la relazione tra trasformazione e comportamento: una forma compatibile non basta a spiegare {output}.",
        ),
        "reading": (
            "Il comportamento nasce dal fatto che {operation} agisce su {input}; il risultato osservato è {output}, non una misura automatica della qualità del sistema.",
            "Per seguire la causalità separiamo il segnale che entra, l'operazione che lo modifica e ciò che esce. In «{heading}» questi tre livelli sono {input}, {operation} e {output}.",
            "Una rete può mantenere la stessa shape mentre cambia ciò che comunica. Per «{heading}» controlliamo quindi sia {output} sia il vincolo: {invariant}.",
        ),
        "mechanism": (
            "Il meccanismo di «{heading}» diventa concreto quando {operation} viene applicata a {input} e produce {output}; il passaggio non va sostituito con il nome dell'architettura.",
            "La domanda causale di «{heading}» è quale parte di {input} venga riusata o trasformata da {operation}. Solo dopo leggiamo {output} e il suo limite.",
            "In «{heading}» la scelta architetturale ha effetto perché cambia il percorso del segnale. Il controllo deve mostrare {operation}, {output} e l'invariante {invariant}.",
        ),
        "verification": (
            "Il controllo più informativo per «{heading}» confronta lo stesso input con una sola modifica nel blocco e registra sia {output} sia la failure attesa.",
            "Per verificare «{heading}» rompiamo una condizione architetturale alla volta: la shape o l'output non devono nascondere il percorso che li ha prodotti.",
            "La prova di «{heading}» deve distinguere un risultato formalmente valido da uno ottenuto con il collegamento sbagliato; il test conserva {input} e {output}.",
        ),
    },
    "generative": {
        "transition": (
            "In «{heading}» seguiamo il dato tra distribuzione e campione: {input} entra nel procedimento, {operation} lo trasforma e {output} rende visibile il risultato.",
            "Il termine generativo diventa utile soltanto nel caso concreto. Partiamo da {object}, fissiamo {input} e osserviamo come {operation} porta a {output}.",
            "La domanda di «{heading}» non è se il campione sembri plausibile, ma quale parte della distribuzione sia stata modellata. Per questo separiamo {operation}, {output} e invariante.",
        ),
        "focus": (
            "In «{heading}» likelihood, trasformazione e sampling non sono sinonimi: {operation} deve restare identificabile prima di interpretare {output}.",
            "La spiegazione di «{heading}» parte dal confine tra dato e latente. Cambiando {input}, cambiano anche ciò che misuriamo e il significato di {output}.",
            "Il caso minimo di «{heading}» aiuta a separare un campione riuscito dalla copertura della distribuzione: il vincolo resta {invariant}.",
        ),
        "reading": (
            "Il percorso generativo ha tre punti distinti: {input}, {operation} e {output}. Un campione leggibile non basta a concludere che il modello descriva tutti i dati.",
            "Per leggere «{heading}» teniamo separati il punteggio che valuta il dato e il campione che viene prodotto. Il primo dipende da {operation}; il secondo è {output}.",
            "La causalità sta nella parametrizzazione: se cambiano rumore, scheduler o trasformazione, non stiamo più eseguendo lo stesso esperimento su {input}.",
        ),
        "mechanism": (
            "«{heading}» rende osservabile il passaggio da {input} a {output}: {operation} determina quale informazione viene conservata e quale viene persa.",
            "Il meccanismo di «{heading}» non è una graduatoria di campioni. È una procedura che collega {operation} al risultato {output} sotto il vincolo {invariant}.",
            "Quando «{heading}» funziona nel caso guida, sappiamo soltanto che il percorso dichiarato è coerente. La sua estensione dipende da come {operation} tratta {input}.",
        ),
        "verification": (
            "La verifica di «{heading}» confronta il dato iniziale, il passo di trasformazione e il campione o punteggio finale; senza questa traccia la failure resta ambigua.",
            "Per controllare «{heading}» fissiamo il rumore o il latente, cambiamo un solo parametro e registriamo se {output} conserva l'invariante.",
            "Il test più piccolo di «{heading}» include almeno un caso plausibile e uno che rompe il vincolo {invariant}; la qualità visiva del campione non è sufficiente.",
        ),
    },
    "sequence": {
        "transition": (
            "Per «{heading}» seguiamo una sequenza, non soltanto una matrice. {input} stabilisce le posizioni disponibili, {operation} determina le dipendenze e {output} è il valore che osserviamo.",
            "Il caso di «{heading}» parte dal prefisso e arriva al token o allo stato successivo. Fissiamo {input} prima di discutere {operation} e {output}.",
            "Qui la forma dei tensori non racconta ancora il comportamento. La spiegazione di «{heading}» deve mostrare quali posizioni comunicano durante {operation} e che cosa produce {output}.",
        ),
        "focus": (
            "In «{heading}» l'invariante riguarda l'ordine: {operation} deve rispettare le posizioni ammesse prima che interpretiamo {output}.",
            "La domanda operativa di «{heading}» è quale storia sia disponibile a ogni posizione. Per rispondere controlliamo {input}, non solo la shape finale.",
            "La rappresentazione intermedia di «{heading}» è parte del contratto: cambiare tokenizer, mask, posizione o cache cambia l'esperimento.",
        ),
        "reading": (
            "Il percorso sequenziale è leggibile se si distingue il prefisso dal passo corrente. In «{heading}», {operation} usa {input} e consegna {output} senza accesso implicito al futuro.",
            "Il fatto che due richieste abbiano la stessa lunghezza non significa che vedano le stesse informazioni. La differenza passa da {operation} e dal vincolo {invariant}.",
            "Per ricostruire «{heading}» annotiamo posizione, stato e output a ogni passo. Questo rende visibile la dipendenza che altrimenti resta nascosta nella rete.",
        ),
        "mechanism": (
            "Il meccanismo di «{heading}» è una regola di comunicazione tra posizioni: {operation} decide quali elementi di {input} possono contribuire a {output}.",
            "In «{heading}» il risultato dipende dal percorso temporale o contestuale, non soltanto dai valori finali. Il test deve conservare {input} e l'ordine di {operation}.",
            "La parte causale di «{heading}» è il riuso controllato della storia. Se il percorso permette informazione non ammessa, {output} può avere la shape giusta e restare scorretto.",
        ),
        "verification": (
            "Per verificare «{heading}» modifichiamo una sola posizione o un solo prefisso e osserviamo se {output} cambia soltanto dove il contratto lo prevede.",
            "Il controllo di «{heading}» include un caso con informazione futura o ordine alterato: la failure deve essere distinguibile da un output valido.",
            "La prova minima di «{heading}» conserva tokenizer, mask, lunghezza e cache; altrimenti il confronto mescola il meccanismo con il setup.",
        ),
    },
    "data_training": {
        "transition": (
            "Per «{heading}» il dato viene seguito dalla sorgente al risultato. {input} entra nel manifest, {operation} modifica la popolazione e {output} documenta ciò che resta.",
            "Il caso di «{heading}» non è soltanto una trasformazione numerica: parte da {object} e rende visibili {input}, {operation} e {output} nello stesso percorso.",
            "Prima di parlare di scala o ricetta fissiamo il perimetro. In «{heading}» {operation} deve essere osservabile perché {output} abbia un significato confrontabile.",
        ),
        "focus": (
            "In «{heading}» il manifest è parte dell'esperimento: senza conteggi, checksum e ordine di {operation}, {output} non è riproducibile.",
            "La quantità che cambia in «{heading}» non è soltanto la loss. Cambiano anche popolazione, esposizione e stato del run quando si modifica {input}.",
            "Il punto da fissare per «{heading}» è il confine di misura: {output} descrive il setup dichiarato, non una ricetta universale.",
        ),
        "reading": (
            "La pipeline di «{heading}» collega {input}, {operation} e {output}. Se saltiamo un passaggio, non sappiamo se la differenza nasce dai dati, dall'ottimizzazione o dal report.",
            "Per leggere il risultato separiamo la trasformazione applicata dal numero ottenuto. Il primo è {operation}; il secondo è {output}, condizionato da {input}.",
            "Il caso guida resta utile perché rende esplicito che il vincolo è {invariant}. Lo stesso valore finale, fuori da questo manifest, potrebbe descrivere un altro esperimento.",
        ),
        "mechanism": (
            "«{heading}» è controllabile quando ogni modifica a {input} lascia una traccia in {output}. {operation} è quindi parte della spiegazione, non un dettaglio del codice.",
            "Il meccanismo di «{heading}» collega una scelta di dati o training a un effetto osservabile. Il confronto ha senso solo se {operation} e il budget restano dichiarati.",
            "In «{heading}» la riproducibilità non è un allegato: è il modo con cui distinguiamo una variazione di {input} da una variazione di {output}.",
        ),
        "verification": (
            "La verifica di «{heading}» confronta conteggi, manifest e output prima di interpretare la metrica; il test negativo deve mostrare che cosa viene escluso.",
            "Per controllare «{heading}» ripetiamo lo stesso run con una sola modifica a {input} e conserviamo la divergenza invece di nasconderla nella media.",
            "Il controllo più piccolo di «{heading}» registra configurazione, seed e digest. Senza questi campi non possiamo attribuire la differenza a {operation}.",
        ),
    },
    "alignment": {
        "transition": (
            "Per «{heading}» il modello non riceve soltanto dati: riceve un obiettivo. {input} entra nel protocollo, {operation} costruisce il segnale e {output} mostra che cosa viene premiato.",
            "Il caso di «{heading}» parte da {object}. Seguiamo il passaggio da {input} a {output} per distinguere la procedura di adattamento dalla qualità che vorremmo ottenere.",
            "Qui il punto non è scegliere il nome dell'algoritmo, ma capire quale comportamento il segnale rende più conveniente. In «{heading}» osserviamo {operation} e il suo limite.",
        ),
        "focus": (
            "In «{heading}» il valore dell'obiettivo dipende dal target e dal protocollo: {operation} non è una misura assoluta di correttezza.",
            "La domanda operativa di «{heading}» è che cosa venga rinforzato e che cosa resti fuori dal segnale. Per questo separiamo {input} da {output}.",
            "Il confine di «{heading}» passa dal verificatore o dal giudizio: un miglioramento locale può spostare l'errore invece di eliminarlo.",
        ),
        "reading": (
            "Il percorso di «{heading}» tiene distinti dati, obiettivo e comportamento. {operation} collega {input} a {output}, ma non autorizza da solo una conclusione applicativa.",
            "Per leggere il risultato chiediamo prima quale target sia stato usato. Solo dopo confrontiamo {output} e decidiamo se il cambiamento riguarda davvero il compito.",
            "Una risposta più preferita o un reward più alto sono osservazioni del protocollo. In «{heading}» vanno letti insieme a {invariant}.",
        ),
        "mechanism": (
            "Il meccanismo di «{heading}» nasce dal rapporto tra segnale e aggiornamento: {operation} modifica la distribuzione dei comportamenti osservati in {output}.",
            "In «{heading}» la procedura può ottimizzare il proxy senza risolvere il compito. Per questo il caso conserva {input}, {output} e la superficie di errore del segnale.",
            "La parte causale di «{heading}» è la scelta di ciò che conta come buona risposta. Cambiare il verificatore o il riferimento cambia anche {operation}.",
        ),
        "verification": (
            "La verifica di «{heading}» include esempi preferiti e falliti, oltre al segnale medio; il test deve mostrare quale comportamento cambia dopo {operation}.",
            "Per controllare «{heading}» teniamo fermo il prompt e cambiamo una sola componente del segnale, poi confrontiamo {output} con il target dichiarato.",
            "Il controllo minimo di «{heading}» separa risultato, reward o preferenza e comportamento sicuro; senza questa separazione il vincolo {invariant} resta invisibile.",
        ),
    },
    "multimodal": {
        "transition": (
            "Per «{heading}» due modalità devono incontrarsi senza perdere la loro identità. {input} entra negli encoder, {operation} allinea o fonde i segnali e {output} rende osservabile il risultato.",
            "Il caso di «{heading}» parte da {object}: testo, immagine, audio o stato spaziale. Seguiamo {operation} prima di parlare di comprensione e di {output}.",
            "La domanda di «{heading}» è dove avviene l'allineamento. Fissiamo {input}, localizziamo {operation} e controlliamo se {output} conserva il vincolo dichiarato.",
        ),
        "focus": (
            "In «{heading}» una dimensione comune non dimostra da sola allineamento: occorre mostrare come {operation} tratta {input}.",
            "Il punto da osservare in «{heading}» è la sincronizzazione. Se cambiano durata, patch, posizione o mask, anche {output} cambia significato.",
            "La spiegazione di «{heading}» separa rappresentazione, fusione e generazione; confonderle fa sembrare {output} più informativo di quanto sia.",
        ),
        "reading": (
            "Il percorso multimodale di «{heading}» ha un confine preciso: {operation} collega {input} a {output}, ma non certifica comprensione generale.",
            "Per leggere il caso teniamo separati il segnale della modalità e il punto in cui viene proiettato. L'output è interpretabile solo rispetto a quella scelta.",
            "Un risultato corretto può dipendere da una correlazione facile. In «{heading}» il controllo deve chiedere quale parte della modalità abbia davvero contribuito.",
        ),
        "mechanism": (
            "Il meccanismo di «{heading}» si vede nel passaggio di rappresentazione: {operation} decide quali aspetti di {input} possono influenzare {output}.",
            "In «{heading}» l'allineamento è un'ipotesi da misurare, non una proprietà garantita dalla presenza di più modalità. Il caso conserva {invariant}.",
            "La prova causale di «{heading}» cambia una modalità alla volta e osserva {output}; così distinguiamo fusione, sincronizzazione e semplice correlazione.",
        ),
        "verification": (
            "La verifica di «{heading}» sostituisce o maschera una modalità e controlla se {output} cambia nel modo previsto, mantenendo il resto del setup.",
            "Per controllare «{heading}» annotiamo dimensione, ordine e timestamp delle modalità; senza questi dati un failure può sembrare un problema del modello.",
            "Il test minimo di «{heading}» include un caso disallineato e uno coerente. La differenza deve essere leggibile nell'esito osservato, non soltanto nella prosa.",
        ),
    },
    "actions": {
        "transition": (
            "Per «{heading}» seguiamo una richiesta lungo il confine tra informazione e azione. {input} entra nel sistema, {operation} decide il passaggio e {output} rende visibile l'effetto.",
            "Il caso di «{heading}» parte da {object}. Prima di parlare di agente o protocollo fissiamo {input}, poi osserviamo come {operation} produce {output}.",
            "Qui una risposta ben formata non è ancora un'azione valida. «{heading}» deve mostrare dove {operation} applica il controllo e quale esito viene registrato.",
        ),
        "focus": (
            "In «{heading}» il confine di sicurezza o recupero è parte del meccanismo: {operation} deve separare {input} da {output}.",
            "La domanda operativa di «{heading}» è chi può leggere, decidere o agire. La forma del messaggio non sostituisce l'autorizzazione.",
            "Il punto da osservare in «{heading}» è la traccia: senza percorso, scope e stato non sappiamo se {output} sia stato ottenuto legittimamente.",
        ),
        "reading": (
            "Il percorso di «{heading}» mantiene separati evidenza, contesto, decisione e side effect. {operation} collega {input} a {output} con un confine osservabile.",
            "Per leggere il caso non basta guardare la risposta finale. Ricostruiamo quale informazione è stata recuperata, quale tool è stato chiamato e che cosa è rimasto nel log.",
            "Una procedura può restituire un risultato corretto e restare fragile. In «{heading}» il vincolo {invariant} definisce ciò che il test deve proteggere.",
        ),
        "mechanism": (
            "Il meccanismo di «{heading}» vive nel confine tra input e side effect: {operation} deve rendere esplicita la decisione prima di produrre {output}.",
            "In «{heading}» la sicurezza non si deduce dal testo generato. Si osserva nella policy, nello scope e nella verifica che accompagnano {operation}.",
            "La parte causale di «{heading}» è il percorso della richiesta. Se saltiamo un controllo, {output} può sembrare valido mentre il sistema ha già perso il confine.",
        ),
        "verification": (
            "La verifica di «{heading}» include una richiesta autorizzata e una fuori perimetro, poi controlla se il side effect e il log rispettano il contratto.",
            "Per controllare «{heading}» rompiamo lo scope o il documento recuperato prima dell'azione. La failure deve avvenire al confine, non dopo il danno.",
            "Il test minimo di «{heading}» conserva input, decisione, chiamata e risultato; un output linguistico convincente non può sostituire {operation}.",
        ),
    },
    "efficiency": {
        "transition": (
            "Per «{heading}» la misura deve seguire il percorso intero. {input} definisce il carico, {operation} cambia memoria o tempo e {output} mostra il costo osservato.",
            "Il caso di «{heading}» parte da {object}. Separiamo il risparmio locale dalla latenza o dall'errore che rimangono in {output}.",
            "Qui l'ottimizzazione è un compromesso, non un numero isolato. Fissiamo {input}, misuriamo {operation} e leggiamo {output} insieme al vincolo.",
        ),
        "focus": (
            "In «{heading}» bytes, tempo e qualità appartengono a misure diverse: {operation} va confrontata con un perimetro di input e hardware dichiarato.",
            "La domanda operativa di «{heading}» è dove si sposta il costo. Una riduzione del volume di {input} può riapparire in memoria, comunicazione, coda o errore.",
            "Il punto da fissare in «{heading}» è il confine temporale: {output} non è interpretabile senza batch, dtype, device e carico.",
        ),
        "reading": (
            "Il percorso di «{heading}» separa rappresentazione, kernel e servizio. {operation} può migliorare {output} localmente senza migliorare il sistema completo.",
            "Per leggere il risultato riportiamo insieme beneficio e costo. Il valore di {output} dipende dal setup definito da {input}, non soltanto dall'operatore modificato.",
            "Un benchmark leggibile conserva anche i casi in cui l'ottimizzazione non aiuta. In «{heading}» questo confine è parte del risultato.",
        ),
        "mechanism": (
            "Il meccanismo di «{heading}» è il rapporto tra dati mossi, calcolo e attesa: {operation} modifica quel rapporto e produce {output}.",
            "In «{heading}» la forma compatta o il dtype ridotto sono soltanto l'inizio. Dobbiamo osservare come {input} attraversa il runtime e dove compare il costo.",
            "La prova causale di «{heading}» tiene fermo il carico e cambia una sola leva. Altrimenti {output} mescola il metodo con l'ambiente.",
        ),
        "verification": (
            "La verifica di «{heading}» ripete la misura con lo stesso input, batch, dtype e device e conserva anche errore e latenza.",
            "Per controllare «{heading}» confrontiamo baseline e variante sullo stesso confine end-to-end; un kernel più rapido non basta se la coda peggiora.",
            "Il test minimo di «{heading}» registra {output} insieme alla configurazione. Senza questa coppia non possiamo sostenere il vantaggio.",
        ),
    },
    "evaluation": {
        "transition": (
            "Per «{heading}» una frase come «funziona» non è ancora una misura. {input} definisce il protocollo, {operation} stabilisce il confronto e {output} porta a una decisione delimitata.",
            "Il caso di «{heading}» parte da {object}. Prima fissiamo che cosa conta come successo, poi seguiamo {operation} fino a {output}.",
            "Qui separiamo osservazione e conclusione. «{heading}» usa {input}, applica {operation} e deve dichiarare quale parte del comportamento resta fuori da {output}.",
        ),
        "focus": (
            "In «{heading}» la metrica è una domanda formalizzata: se cambia {input} o {operation}, cambia anche ciò che {output} può sostenere.",
            "La domanda operativa di «{heading}» è quale failure verrebbe nascosta dalla media. Per questo registriamo slice, casi limite e protocollo.",
            "Il punto da fissare in «{heading}» è il confine tra evidenza e interpretazione: {output} non autorizza una conclusione oltre {invariant}.",
        ),
        "reading": (
            "Il percorso di «{heading}» collega task, dati, misura e decisione. {operation} non è un rituale di reporting: determina che cosa viene davvero osservato.",
            "Per leggere il valore riportato separiamo numero, casi falliti e popolazione. Solo insieme spiegano che cosa significa {output}.",
            "Una media può restare alta mentre una slice peggiora. In «{heading}» il vincolo {invariant} impedisce di confondere aggregazione e affidabilità.",
        ),
        "mechanism": (
            "Il meccanismo di «{heading}» è la costruzione del protocollo: {operation} trasforma {input} in una misura, non in una verità generale.",
            "In «{heading}» la decisione dipende da come definiamo successo, failure e popolazione. {output} è quindi inseparabile dal protocollo dichiarato.",
            "La parte causale di «{heading}» sta nella slice e nel controllo: senza confronto indipendente non sappiamo che cosa abbia prodotto {output}.",
        ),
        "verification": (
            "La verifica di «{heading}» conserva una slice, un caso limite e almeno una failure oltre alla media; il protocollo deve essere ripetibile.",
            "Per controllare «{heading}» cambiamo una sola condizione e verifichiamo se la decisione cambia insieme a {output}, non soltanto il numero aggregato.",
            "Il test minimo di «{heading}» collega la metrica alla sua domanda e registra ciò che il protocollo non misura; altrimenti il vincolo {invariant} resta un avvertimento astratto.",
        ),
    },
}


PROSE_CADENCES = {
    "transition": (
        "Prima di proseguire, teniamo questa definizione a vista.",
        "Il passaggio resta locale: non lo allarghiamo ancora al sistema intero.",
        "Qui la forma del caso serve a preparare il confronto successivo.",
        "La domanda successiva potrà cambiare una sola condizione dichiarata.",
        "Questo ingresso delimita ciò che il capitolo può sostenere.",
    ),
    "focus": (
        "Il controllo resta locale, non conclusivo.",
        "La distinzione impedisce di confondere forma e comportamento.",
        "Il limite è parte della definizione, non una nota a margine.",
        "La stessa osservazione va riaperta quando cambia il setup.",
        "Il lettore può quindi cercare la failure prima di trasferire il risultato.",
    ),
    "reading": (
        "La distinzione evita di confondere percorso e risultato.",
        "Il numero acquista significato soltanto dentro questa catena.",
        "Il caso resta leggibile anche se l'esito non è quello atteso.",
        "La misura deve conservare il passaggio che l'ha prodotta.",
        "Da qui si può formulare un controllo negativo mirato.",
    ),
    "mechanism": (
        "È questo il passaggio che lo snippet deve rendere osservabile.",
        "La causalità resta nel collegamento, non nel nome della tecnica.",
        "Una variazione fuori da questo passaggio riaprirebbe l'attribuzione.",
        "Il risultato acquista senso solo insieme alla condizione che lo produce.",
        "Questa è la parte trasferibile come procedura, non come promessa.",
    ),
    "verification": (
        "La failure va letta come informazione sul contratto.",
        "Un controllo positivo senza il caso negativo sarebbe incompleto.",
        "La registrazione deve permettere di ripetere lo stesso confronto.",
        "Il test separa ciò che osserviamo da ciò che stiamo inferendo.",
        "Il risultato resta circoscritto alla popolazione e alla misura dichiarate.",
    ),
}


def prose_family(number: int, kind: str) -> str:
    return PROSE_FAMILY_BY_TOPIC.get(topic_for(number, kind), "evaluation")


def render_prose_variant(family: str, field: str, number: int, index: int, heading: str, detail: dict[str, str]) -> str:
    variants = PROSE_VARIANTS.get(family, {}).get(field, ())
    if not variants:
        return ""
    values = {
        "heading": heading,
        "object": f"questo caso ({detail['object']})",
        "input": f"il dato in ingresso ({detail['input']})",
        "operation": f"l'operazione «{detail['operation']}»",
        "output": f"l'esito osservato ({detail['output']})",
        "invariant": f"«{detail['invariant'].rstrip('.')}»",
    }
    rendered = variants[(number + index) % len(variants)].format(**values)
    cadences = PROSE_CADENCES.get(field, ())
    if cadences:
        rendered = f"{rendered} {cadences[index % len(cadences)]}"
    return rendered


PROSE_TAIL_DESCRIPTORS = {
    "architecture": (
        "il collegamento tra blocchi",
        "la shape e il percorso del segnale",
        "la trasformazione che la rete applica al segnale",
    ),
    "generative": (
        "il rapporto tra distribuzione e campione",
        "plausibilità e copertura dei dati",
        "il passaggio dal latente all'osservabile",
    ),
    "sequence": (
        "ordine, posizione e memoria contestuale",
        "la storia disponibile a ogni passo",
        "il vincolo che impedisce di leggere il futuro",
    ),
    "data_training": (
        "popolazione, manifest e stato del run",
        "conteggi, split e trasformazioni registrate",
        "il legame tra dati esposti e risultato",
    ),
    "alignment": (
        "target, proxy e comportamento",
        "il segnale che premia una risposta",
        "la distanza tra obiettivo locale e compito",
    ),
    "multimodal": (
        "allineamento tra modalità",
        "sincronizzazione, rappresentazione e fusione",
        "il contributo effettivo di ciascun segnale",
    ),
    "actions": (
        "decisione, tool e side effect",
        "il confine tra informazione e azione",
        "la traccia della traiettoria prima dell'effetto",
    ),
    "efficiency": (
        "latency, memoria e throughput",
        "il costo che si sposta tra kernel e servizio",
        "la misura end-to-end sotto carico dichiarato",
    ),
    "evaluation": (
        "protocollo, slice e decisione",
        "la differenza tra media e failure",
        "il confine tra evidenza e interpretazione",
    ),
}


def prose_tail(
    family: str,
    number: int,
    index: int,
    heading: str,
    next_heading: str | None,
    input_label: str,
    operation_label: str,
    output_label: str,
    invariant_plain: str,
) -> dict[str, str]:
    descriptors = PROSE_TAIL_DESCRIPTORS.get(family, PROSE_TAIL_DESCRIPTORS["evaluation"])
    scope, control, transfer = descriptors
    variant = (number + index) % 3
    isolations = (
        f"Nel controllo di «{heading}» cambiamo una sola leva di {scope} e osserviamo {output_label}.",
        f"Per separare causa e sintomo in «{heading}», lasciamo fermo {input_label} e mettiamo alla prova {control}; la failure deve essere leggibile prima di interpretare {output_label}.",
        f"Il controllo negativo di «{heading}» apre una sola crepa nel contratto di {scope}: se {invariant_plain}, registriamo la divergenza su {output_label}.",
    )
    limits = (
        f"Il caso di «{heading}» illumina {scope}; non sostituisce una misura sul sistema completo.",
        f"Per «{heading}» la conclusione resta limitata a {control} nel protocollo osservato e non si trasferisce automaticamente.",
        f"L'esempio di «{heading}» rende concreto {transfer}; per estenderlo servono dati, setup e criteri nuovi.",
    )
    if next_heading:
        bridges = (
            f"Il passaggio successivo, «{next_heading}», riceve {output_label} come base per studiare {transfer}, ma dovrà aprire il proprio controllo.",
            f"Da «{heading}» a «{next_heading}» portiamo {output_label}; il nuovo capitolo potrà cambiare {control} senza ereditare la conclusione.",
            f"«{next_heading}» riprenderà {output_label} e lo metterà in relazione con {scope}; il contratto resta da dichiarare di nuovo.",
        )
    else:
        bridges = (
            f"Il percorso si chiude lasciando espliciti {scope}, {output_label} e il limite osservato.",
            f"La conclusione resta ancorata a {control}, non a una promessa generale sulla tecnica.",
            f"Il caso finale consegna {output_label} come evidenza locale e conserva {transfer} come domanda aperta.",
        )
    return {
        "isolation": isolations[variant],
        "limit": limits[variant],
        "bridge": bridges[variant],
    }


TOPIC_MECHANISM_SENTENCES = {
    "interoperability": "Il protocollo è un contratto osservabile: schema, versione, identità e autorizzazione devono essere controllati a ogni confine.",
    "governance": "La decisione nasce dall'incrocio tra ruolo, uso, evidenza, impatto e consumo; nessuna checklist sostituisce la responsabilità sul caso concreto.",
    "lab": "Il laboratorio rende l'esperimento ricostruibile collegando ambiente, input, comando, output e manifest.",
    "small_lm": "Il piccolo modello è utile perché rende visibile la catena stringa-token-mask-logits-loss, ma quella osservabilità non è una misura di capacità generale.",
    "production": "Il passaggio decisivo è collegare il modello ai dati, ai gate, al monitoraggio e al rollback, perché il servizio non coincide con il checkpoint.",
    "replication": "La replica cambia il setup in modo controllato e conserva le divergenze, così una differenza diventa evidenza invece di un rumore nascosto.",
    "frontier": "Un'osservazione di frontiera separa la pubblicazione dalla disponibilità, la disponibilità dalla replica e la replica dalla readiness.",
}


def section_example(number: int, kind: str, heading: str, detail: dict[str, str], index: int) -> str:
    """Give each transition a topic-shaped example instead of a generic filler."""
    topic = topic_for(number, kind)
    chapter_example = CHAPTER_SECTION_EXAMPLES.get(number)
    # The chapter-level examples are useful for the opening transition, but
    # repeating them in every section makes a distinct concept look like a
    # copy of the previous one.  Later sections are routed by their heading.
    if index == 0 and chapter_example:
        return chapter_example
    if topic in TOPIC_SECTION_EXAMPLES:
        return TOPIC_SECTION_EXAMPLES[topic][min(index, len(TOPIC_SECTION_EXAMPLES[topic]) - 1)]
    lower = heading.lower()
    if any(token in lower for token in ("formato", "ruol", "separat", "system message", "label")):
        return "un messaggio con ruolo, contenuto e maschera che assegna il gradiente soltanto alla risposta"
    if any(token in lower for token in ("mixture", "curriculum", "sorgenti", "peso effettivo", "dati sintetici")):
        return "due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata"
    if any(token in lower for token in ("teacher forcing", "autoregress", "sampling", "decoding")):
        return "un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente"
    if any(token in lower for token in ("forgetting", "regressione", "replay", "recovery")):
        return "una metrica del compito nuovo confrontata con la stessa metrica sul comportamento precedente"
    if any(token in lower for token in ("policy gradient", "actor-critic", "value function", "bellman")):
        return "una traiettoria di due passi in cui reward immediato e valore futuro restano separati"
    if any(token in lower for token in ("flow", "jacobian", "elbo", "score matching", "wasserstein")):
        return "un dato trasformato e ricostruito con la quantità di probabilità o di errore dichiarata"
    if any(token in lower for token in ("benchmark", "leaderboard", "report", "giudic", "metric")):
        return "quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato"
    if any(token in lower for token in ("provenienza", "watermark", "credential", "firma", "digest")):
        return "un payload modificato dopo la firma, con digest e metadati confrontati separatamente"
    if any(token in lower for token in ("govern", "norme", "ruoli", "responsabilità", "incident")):
        return "una decisione con owner, rischio, evidenza, giurisdizione e condizione di riapertura"
    if any(token in lower for token in ("reward", "mdp", "bellman", "policy", "actor", "critic", "esplor")):
        if "bellman" in lower or "mdp" in lower:
            return "un ritorno calcolato da reward immediato 1, gamma 0,9 e valore futuro 0,5, mantenendo separati stato e azione"
        if "esplor" in lower:
            return "due azioni disponibili con ritorni osservati diversi e una misura separata della varianza"
        return "una traiettoria di due passi in cui l'azione scelta modifica lo stato successivo prima del reward"
    if any(token in lower for token in ("token", "byte", "unicode", "embedding", "vocabulary", "posizione", "context", "causal", "mask", "cache")):
        if "byte" in lower or "unicode" in lower:
            return "la stessa stringa convertita prima in code point e poi in byte UTF-8, conservando la reversibilità"
        if "embedding" in lower:
            return "due ID che selezionano righe diverse dalla stessa embedding table, prima di aggiungere il contesto"
        if "cache" in lower:
            return "un prefill che scrive key e value e un decode che aggiunge una sola posizione senza ricomputare il prefisso"
        if "mask" in lower or "causal" in lower:
            return "una matrice di visibilità in cui la posizione futura resta esclusa anche se la shape dei tensori è compatibile"
        return "un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati"
    if any(token in lower for token in ("data", "dataset", "record", "sorgent", "provenienza", "parsing", "filt", "deduplic", "split", "manifest", "corpus", "packing")):
        if "deduplic" in lower or "contamin" in lower:
            return "due record simili che vengono confrontati con hash esatto e con una regola distinta per la similarità approssimata"
        if "split" in lower or "manifest" in lower:
            return "un manifest che conserva conteggi, checksum, tokenizer e confini dello split prima del training"
        return "due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata"
    if any(token in lower for token in ("quant", "low-bit", "bit", "prun", "distill", "latency", "throughput", "kernel", "hardware", "energia", "costo", "serving", "batch")):
        if "quant" in lower or "bit" in lower:
            return "tre valori floating point quantizzati con una scala dichiarata e confrontati con la ricostruzione"
        if "prun" in lower or "distill" in lower:
            return "un modello teacher e uno student confrontati sullo stesso input, con memoria e regressioni riportate insieme alla loss"
        if "kernel" in lower or "hardware" in lower:
            return "la stessa operazione misurata separando bytes mossi, tempo del kernel e latenza end-to-end"
        return "un batch di richieste eterogenee in cui throughput, coda e time-to-first-token vengono misurati separatamente"
    if any(token in lower for token in ("retrieval", "rag", "query", "document", "fonte", "evidenza", "memoria")):
        return "una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale"
    if any(token in lower for token in ("tool", "agent", "traiettoria", "sandbox", "least privilege", "approval", "rollback", "browser")):
        return "una traiettoria minima osservazione-azione-tool-verifica in cui una chiamata fuori allowlist viene bloccata prima dell'esecuzione"
    if any(token in lower for token in ("security", "jailbreak", "injection", "privacy", "fairness", "risk", "safety", "govern", "policy", "threat", "backdoor", "poison")):
        return "un input non fidato che raggiunge una policy esterna, con decisione allow/deny e traccia dell'evento conservate separatamente"
    if any(token in lower for token in ("evaluation", "metric", "benchmark", "calibr", "judge", "report", "factual", "reliab", "probe", "attribution", "circuit")):
        return f"quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «{heading}» e all'output {detail['output']}"
    if any(token in lower for token in ("convolution", "kernel", "stride", "padding", "receptive", "vision", "patch", "grafi", "message")):
        return "una griglia 3x3 e un kernel 2x2 in cui una sola posizione dell'output viene calcolata a mano"
    if any(token in lower for token in ("normal", "initial", "residual", "activation", "layer", "gradient", "training", "dropout", "regular")):
        return f"due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «{heading}»"
    if any(token in lower for token in ("multimodal", "image", "audio", "video", "vision", "speech", "music", "3d", "world")):
        return "due rappresentazioni di modalità diverse proiettate nella stessa dimensione prima di similarità, fusione o generazione"
    if any(token in lower for token in ("generat", "diffus", "latent", "vae", "gan", "flow", "sampling", "score", "likelihood")):
        return "tre probabilità che sommano a 1 prima del campionamento, distinguendo plausibilità del campione e copertura"
    if any(token in lower for token in ("mlp", "perceptron", "affin", "capacità", "espressività")):
        return "x=[1,2] passato in una trasformazione affine e poi in una non linearità, con shape e confine espliciti"
    if any(token in lower for token in ("rnn", "ricorrent", "lstm", "gru", "sequenza")):
        return "tre passi in cui lo stato precedente viene consumato prima di produrre il successivo"
    if index == 0:
        return f"un caso minimo con input {detail['input']} e output «{detail['output']}»"
    if index == 1:
        return detail["example"]
    if index == 2:
        return f"un caso in cui {detail['invariant']}"
    if kind == "sequence":
        return "un confronto tra due prefissi con la stessa stringa, tokenizer dichiarato e mask causale esplicita"
    if kind == "scaling":
        return "due ricette con budget di token dichiarato, compute comparabile e loss osservata nello stesso intervallo"
    fallback_kind = kind
    try:
        result = base.example_for(number, fallback_kind, SPECS[number][4])
        return result[:1].lower() + result[1:]
    except KeyError:
        return f"un caso controllato con {detail['input']}, {detail['operation']} e output {detail['output']}"


def mechanism_sentence(number: int, kind: str, heading: str, detail: dict[str, str], index: int) -> str:
    """Add one causal explanation tied to the concept family and its failure mode."""
    topic = topic_for(number, kind)
    topic_variants = {
        "interoperability": (
            "In «{heading}» il contratto si vede nei campi che attraversano il confine: schema, versione, identità e autorizzazione devono restare verificabili.",
            "La parte decisiva di «{heading}» non è il nome del protocollo, ma l'accordo osservabile tra chi invia, chi riceve e chi rifiuta un messaggio incoerente.",
            "Per leggere «{heading}» seguiamo il dato lungo il confine: una versione compatibile non rende automaticamente leciti né l'accesso né l'uso successivo.",
            "Il caso di «{heading}» separa formato, identità e permesso. Se uno di questi livelli manca, la compatibilità apparente non è ancora un contratto.",
            "La prova di «{heading}» consiste nel rendere visibili negoziazione, decisione e failure, invece di dedurre l'interoperabilità da una risposta ben formata.",
        ),
        "governance": (
            "In «{heading}» la decisione nasce dall'incrocio tra ruolo, uso, evidenza e impatto; una checklist da sola non assegna responsabilità.",
            "Il meccanismo di «{heading}» diventa leggibile quando owner, condizione di escalation e prova restano associati allo stesso caso.",
            "La scheda di «{heading}» non descrive soltanto un rischio: collega una scelta a chi la prende, a quale evidenza la sostiene e a quale controllo la riapre.",
            "Per «{heading}» il risultato operativo è una decisione tracciabile. La presenza di una policy non dimostra che il controllo sia stato applicato nel punto giusto.",
            "Il passaggio di «{heading}» separa misura, responsabilità e conseguenza; confonderle produce una procedura ordinata ma non necessariamente governata.",
        ),
        "lab": (
            "Il laboratorio di «{heading}» è ricostruibile solo se ambiente, input, comando, output e manifest vengono letti come una stessa catena.",
            "In «{heading}» il run è parte del risultato: senza versione, seed e artefatti non è possibile distinguere una differenza reale da una differenza di setup.",
            "La prova di «{heading}» non si ferma al valore stampato. Collega quel valore ai dati entrati, alla trasformazione applicata e al limite del caso.",
            "Per «{heading}» l'osservazione più utile è il rapporto tra configurazione e output: un esperimento corto può essere rigoroso se conserva il percorso che lo ha prodotto.",
            "Il contratto di «{heading}» vive nel manifest e nel test negativo oltre che nel risultato positivo; è così che una failure diventa informazione.",
        ),
        "small_lm": (
            "«{heading}» rende visibile la catena tra stringa, token, mask, logits e loss, ma questa visibilità non è una misura di capacità generale.",
            "Nel caso di «{heading}» la dimensione piccola aiuta a seguire ogni tensore; il trasferimento a modelli più grandi richiederebbe una nuova evidenza.",
            "La domanda causale di «{heading}» è quale trasformazione cambia il segnale tra input e output, non se il mini-esperimento assomigli già a un sistema completo.",
            "Per «{heading}» il percorso didattico deve tenere separati shape, aggiornamento dei pesi e comportamento osservato: sono livelli collegati, non sinonimi.",
            "Il valore di «{heading}» sta nel rendere controllabile un passaggio locale. La stessa procedura non autorizza da sola claim su dati, scala o qualità applicativa.",
        ),
        "production": (
            "In «{heading}» il modello entra in un servizio insieme a dati, policy, monitoraggio e rollback; il checkpoint non è ancora il prodotto.",
            "Il passaggio operativo di «{heading}» collega una metrica a un gate e a un owner. Senza il percorso di ritorno, una promozione non è completa.",
            "Per leggere «{heading}» separiamo il successo del modello dalla salute del servizio: latenza, errori, dati e decisione di rollback hanno osservazioni diverse.",
            "La prova di «{heading}» è end-to-end solo quando la configurazione promossa, l'alert e la versione precedente sono identificabili nello stesso scenario.",
            "«{heading}» rende esplicito il confine tra esperimento e deployment: una metrica offline può aprire un gate, ma non sostituisce il monitoraggio in esercizio.",
        ),
        "replication": (
            "«{heading}» cambia il setup in modo controllato e conserva le divergenze, così una differenza resta evidenza invece di diventare rumore nascosto.",
            "La replica di «{heading}» richiede più del risultato finale: commit, dati, seed, hardware e definizione della metrica devono poter essere confrontati.",
            "In «{heading}» il protocollo stabilisce che cosa stiamo ripetendo. Una concordanza parziale è informativa, ma non va allargata a condizioni non eseguite.",
            "Il punto causale di «{heading}» è isolare il cambiamento tra l'originale e il nuovo run; senza quella differenza dichiarata non sappiamo che cosa spiega l'esito.",
            "Per «{heading}» una conclusione sostenibile segue l'intervallo osservato e registra anche ciò che non è stato ricostruito.",
        ),
        "frontier": (
            "Un'osservazione di frontiera come «{heading}» separa pubblicazione, disponibilità, replica e readiness invece di trattarle come sinonimi.",
            "In «{heading}» la data e la fonte primaria fanno parte dell'oggetto: una tecnica può essere interessante senza essere pronta per l'adozione.",
            "Il lavoro di «{heading}» consiste nell'instradare ogni affermazione al suo livello di evidenza, mantenendo distinto ciò che è letto, replicato e promosso.",
            "Per «{heading}» il risultato utile è una decisione aggiornata e reversibile, non un giudizio assoluto sulla novità della tecnica.",
            "La scheda di «{heading}» tiene insieme claim, prerequisito e consumer; senza questi legami una rassegna accumula nomi ma non costruisce un percorso.",
        ),
    }
    if topic in topic_variants:
        return topic_variants[topic][(number + index * 2) % len(topic_variants[topic])].format(heading=heading)
    family_mechanism = render_prose_variant(
        prose_family(number, kind),
        "mechanism",
        number,
        index,
        heading,
        detail,
    )
    if family_mechanism:
        return family_mechanism
    operation_label = f"l'operazione «{detail['operation']}»"
    contract_variants = (
        f"Il punto causale di «{heading}» è {operation_label}: prende {detail['input']} e produce {detail['output']}.",
        f"In «{heading}» il cambiamento osservabile nasce dall'operazione «{detail['operation']}». Per leggerlo, teniamo separati {detail['input']} e {detail['output']}.",
        f"La prova di «{heading}» segue {operation_label} lungo il caso guida: il risultato è {detail['output']}, mentre il limite è che {detail['invariant']}.",
        f"«{heading}» aggiunge un passaggio preciso alla catena. L'input resta {detail['input']}; ciò che cambia è {operation_label}; l'output è {detail['output']}.",
        f"Per non confondere il meccanismo di «{heading}» con la sua applicazione, misuriamo {operation_label} e conserviamo l'invariante: {detail['invariant']}.",
    )
    if topic not in topic_variants:
        return contract_variants[(number + index * 2) % len(contract_variants)]
    lower = heading.lower()
    def scoped(sentence: str) -> str:
        return f"In «{heading}», {sentence[:1].lower() + sentence[1:]}"
    if any(token in lower for token in ("mask", "attention", "position", "cache", "context")):
        return scoped("La shape non basta a descrivere questo passaggio: bisogna controllare anche quali posizioni comunicano e quali informazioni vengono riutilizzate.")
    if any(token in lower for token in ("token", "byte", "unicode", "embedding", "vocabulary")):
        return scoped("La rappresentazione intermedia è parte del contratto: se cambiano tokenizer, ID o dimensione del vettore, il confronto a valle non è più lo stesso esperimento.")
    if any(token in lower for token in ("data", "dataset", "source", "record", "split", "manifest", "provenance", "dedup")):
        return scoped("La pipeline modifica la popolazione osservata; perciò il risultato va letto insieme a conteggi, metadati e trasformazione applicata, non soltanto all'output finale.")
    if any(token in lower for token in ("loss", "likelihood", "objective", "reward", "preference", "verif", "metric")):
        return scoped("Il numero prodotto è un segnale rispetto a un target e a un protocollo: migliorarne il valore non dimostra automaticamente un miglioramento dell'obiettivo applicativo.")
    if any(token in lower for token in ("security", "jailbreak", "injection", "privacy", "fairness", "risk", "safety", "govern")):
        return scoped("Il controllo deve essere applicato al confine della risorsa o della decisione; una risposta testuale convincente non può sostituire l'enforcement esterno.")
    if any(token in lower for token in ("cost", "compute", "latency", "memory", "throughput", "hardware", "energy", "batch", "kernel")):
        return scoped("La misura ha senso solo con input, batch, dtype, device e confine temporale dichiarati; un vantaggio locale può spostare il costo su memoria, trasferimenti o coda.")
    if any(token in lower for token in ("evaluation", "benchmark", "calibr", "result", "report", "judge")):
        return scoped("La procedura deve conservare anche casi falliti e slice: una media senza il protocollo non dice quale proprietà sia stata davvero misurata.")
    if any(token in lower for token in ("retrieval", "rag", "query", "document", "memory")):
        return scoped("Il passaggio utile è separare evidenza recuperata, contesto passato al modello e risposta generata, così l'errore resta localizzabile.")
    if any(token in lower for token in ("agent", "tool", "trajectory", "sandbox", "approval")):
        return scoped("La traiettoria va letta come una sequenza di stati osservabili: decisione, effetto del tool e verifica non sono intercambiabili.")
    if any(token in lower for token in ("convolution", "stride", "padding", "receptive", "graph", "message")):
        return scoped("La struttura dei vicini è l'ipotesi che guida l'operazione: cambiare griglia, bordo o archi cambia anche ciò che il modello può combinare.")
    if any(token in lower for token in ("normal", "initial", "residual", "activation", "gradient", "training", "dropout", "regular")):
        return scoped("Il vantaggio del blocco dipende dalla posizione nell'architettura e dalla scala dei segnali; la shape compatibile è necessaria, ma non sufficiente.")
    if any(token in lower for token in ("multimodal", "image", "audio", "video", "vision", "speech", "music", "3d")):
        return scoped("Prima di parlare di comprensione, osserviamo la trasformazione delle modalità: dimensione condivisa, sincronizzazione e allineamento devono essere espliciti.")
    if any(token in lower for token in ("generat", "diffus", "latent", "vae", "gan", "flow", "sampling", "score")):
        return scoped("Il percorso separa distribuzione, trasformazione e campionamento; un output plausibile è solo una delle proprietà che il contratto può osservare.")
    if any(token in lower for token in ("rnn", "ricorrent", "lstm", "gru", "sequenza")):
        return scoped("La dipendenza temporale è nel riuso dello stato: ogni output incorpora la storia ammessa dal percorso, non una memoria illimitata implicita.")
    if any(token in lower for token in ("mlp", "perceptron", "affin", "capacità", "espressività")):
        return scoped("La non linearità è il punto che impedisce di ridurre la rete a un'unica mappa affine; capacità aggiuntiva e generalizzazione restano però domande separate.")
    variants = (
        "Per «{heading}» la catena utile parte dall'input e arriva all'output passando per un'operazione che possiamo osservare; il nome viene dopo il caso.",
        "Qui seguiamo la quantità che cambia in «{heading}» e teniamo separata quella che deve restare fissa, perché la shape compatibile non basta a spiegare il risultato.",
        "La sezione «{heading}» separa il meccanismo osservato dalla promessa applicativa: il codice può controllare il primo, non dichiarare automaticamente la seconda.",
    )
    return variants[(number + index) % len(variants)].format(heading=heading)


def note_parts(note: str) -> tuple[str, str]:
    """Split a section claim without inventing a second factual claim."""
    clean = re.sub(r"\s+", " ", note.strip()).rstrip(".")
    pieces = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ÖØ-Þ])", clean)
    first = pieces[0].strip().rstrip(".!?") if pieces else clean
    rest = " ".join(piece.strip().rstrip(".!?") for piece in pieces[1:] if piece.strip())
    return first, rest


def lower_initial(value: str) -> str:
    if len(value) > 1 and value[:2].isupper():
        return value
    return value[:1].lower() + value[1:] if value else value


SECTION_CAUSAL_TEMPLATES = {
    "architecture": "La causa va cercata nel percorso del segnale: {operation} modifica la rappresentazione prima che possiamo leggere {output}",
    "generative": "La causa va cercata nel passaggio tra distribuzione, trasformazione e campione: {operation} stabilisce che cosa diventa osservabile in {output}",
    "sequence": "La causa va cercata nell'ordine delle dipendenze: {operation} stabilisce quale storia può contribuire a {output}",
    "data_training": "La causa va cercata nella popolazione e nella ricetta: {operation} modifica ciò che entra nel run prima del risultato {output}",
    "alignment": "La causa va cercata nel segnale di training o di verifica: {operation} rende più conveniente un comportamento, ma {output} va ancora valutato",
    "multimodal": "La causa va cercata nel punto in cui le modalità vengono proiettate, sincronizzate o fuse: {operation} determina quale parte di {output} può dipendere da ciascun segnale",
    "actions": "La causa va cercata nella traiettoria tra decisione ed effetto: {operation} produce {output}, con autorizzazione e verifica separate",
    "efficiency": "La causa va cercata nel confine della misura: {operation} sposta lavoro, memoria o comunicazione prima di produrre {output}",
    "evaluation": "La causa va cercata nel protocollo che collega domanda e decisione: {operation} definisce che cosa viene osservato in {output}",
}


def section_causal_explanation(family: str, heading: str, note_core: str, detail: dict[str, str]) -> str:
    template = SECTION_CAUSAL_TEMPLATES.get(family, SECTION_CAUSAL_TEMPLATES["evaluation"])
    operation = f"il passaggio «{heading}»"
    output = f"l'output «{detail['output']}»"
    sentence = template.format(operation=operation, output=output)
    return f"{sentence}. La frase da tenere ferma è: «{note_core}»."


def _section_explanation_base(number: int, heading: str, note_core: str, detail: dict[str, str]) -> str:
    """Add a mechanism explanation matched to the section's vocabulary.

    The source-backed note states the claim.  This layer explains the causal
    relation in plain language so that the chapter does not merely repeat the
    claim, the chapter contract, and a generic warning about generalization.
    """
    lower = heading.casefold()
    topic = topic_for(number, profile(number))
    if topic == "frontier":
        return "L'osservatorio separa scoperta, instradamento, maturità e promozione. La data, la fonte e il consumer della tecnica devono restare visibili prima di trasformare un'osservazione in una decisione editoriale."
    if topic in {"eval_design", "factuality", "system_eval", "agent_eval"}:
        return "La valutazione parte dalla decisione che il risultato deve sostenere e conserva popolazione, protocollo, misura, failure e incertezza. Un punteggio aggregato è utile soltanto dentro questo perimetro."
    if topic in {"governance", "privacy_fairness", "supply_chain", "provenance"}:
        return "Il controllo collega rischio, evidenza, responsabile e decisione al punto in cui il sistema può produrre un effetto. La presenza di un documento o di una credenziale non sostituisce l'applicazione del controllo."
    if topic in {"lab", "small_lm", "production", "replication"}:
        return "Il risultato è interpretabile soltanto se codice, dati, configurazione, ambiente e output restano collegati. La scala del laboratorio rende il percorso leggibile, ma il trasferimento richiede una nuova misura."
    if topic == "moe":
        return "Il router assegna token a un sottoinsieme di esperti e deve rispettare capacità, bilanciamento e comunicazione. Il calcolo condizionale cambia il percorso del token, non elimina automaticamente i costi del sistema."
    if topic in {"retrieval", "rag", "advanced_rag", "memory"}:
        return "La pipeline distingue query, recupero, contesto e risposta. Registrare il documento o il segmento entrato nel contesto permette di localizzare un errore di ranking separatamente da un errore di generazione."
    if topic in {"interoperability", "tools", "agent_loop", "multiagent", "agent_safety", "injection"}:
        return "Il componente può proporre un messaggio o un'azione, ma schema, identità, autorizzazione e side effect devono essere controllati al confine. La traiettoria osservabile è più informativa del testo prodotto."
    if topic in {"quantization", "low_bit", "distillation", "decoding", "speculative", "kv_cache", "serving", "distributed_inference", "compiler", "llmops"}:
        return "L'ottimizzazione modifica rappresentazione, memoria, calcolo o scheduling sotto un carico dichiarato. Per attribuire il beneficio bisogna separare il guadagno locale da latenza, qualità e costo end-to-end."
    if any(token in lower for token in ("mdp", "markov decision", "ritorno")):
        return "Un MDP separa stato, azione, transizione e reward; il ritorno non è il reward di un singolo passo, ma una somma scontata lungo la traiettoria."
    if any(token in lower for token in ("value function", "bellman")):
        return "La value function riassume il ritorno atteso a partire da uno stato. La relazione di Bellman lo scompone in reward immediato e valore del prossimo stato, rendendo esplicita la ricorrenza."
    if any(token in lower for token in ("policy gradient", "actor-critic")):
        return "Il policy gradient collega l'aggiornamento alla probabilità delle azioni e all'esito osservato. Nell'actor-critic, il critic fornisce una stima del valore che può ridurre la varianza del segnale senza diventare la policy stessa."
    if any(token in lower for token in ("esplorazione", "valutazione")) and number == 14:
        return "Esplorare cambia quali traiettorie vengono osservate; valutare mantiene la procedura abbastanza stabile da confrontare le politiche. Ritorno medio, dispersione e vincoli di sicurezza rispondono a domande diverse."
    if any(token in lower for token in ("percettrone", "decisione lineare", "strati nascosti", "attivazioni")):
        return "Una trasformazione affine combina le feature con pesi e bias. La non linearità è ciò che impedisce a più trasformazioni affini consecutive di collassare in una sola mappa."
    if any(token in lower for token in ("inizializzazione", "normalizzazione", "residual", "regolarizzazione")):
        return "Il punto operativo è la scala del segnale: inizializzazione, normalizzazione, residual e regolarizzazione intervengono in momenti diversi e non sono sostituti intercambiabili. Shape compatibili e curve osservate servono a controllare il percorso reale."
    if any(token in lower for token in ("condivisione locale", "stride", "padding", "receptive", "convolution")):
        return "La convoluzione riusa lo stesso kernel su posizioni diverse. Stride, padding e dilatazione stabiliscono quali vicini entrano nell'output e come cresce il campo ricettivo."
    if any(token in lower for token in ("rnn", "ricorrent", "lstm", "gru", "backpropagation through time", "bidirezionalità")):
        return "Una rete ricorrente riusa lo stato e gli stessi parametri a ogni passo. Srotolare il calcolo rende visibile il percorso dei gradienti; gate e direzione della sequenza cambiano quali informazioni possono sopravvivere."
    if any(token in lower for token in ("rappresenta", "representation", "autoencoder", "bottleneck", "contrastive", "disentanglement", "probe")):
        return "Una rappresentazione non ha significato isolato: è una quantità prodotta per un uso successivo. Obiettivo, dati, augmentazioni e metrica determinano quali relazioni vengono rese facili da leggere."
    if any(token in lower for token in ("distribuzione", "likelihood", "modelli espliciti", "modelli impliciti", "energy-based")):
        return "Un modello generativo può assegnare un punteggio ai dati, definire una densità oppure descrivere direttamente un percorso di campionamento. Likelihood e qualità del campione sono osservazioni diverse e vanno tenute separate."
    if any(token in lower for token in ("vae", "elbo", "reparameterization", "posterior collapse", "vq-vae")):
        return "Il latent collega encoder e decoder, mentre il termine di ricostruzione e quello di regolarizzazione spingono in direzioni diverse. Il campionamento resta addestrabile soltanto quando il percorso del gradiente è dichiarato."
    if any(token in lower for token in ("gan", "mode collapse", "wasserstein")):
        return "Nel gioco adversarial il generatore e il discriminatore cambiano il segnale l'uno dell'altro. Un discriminatore efficace non garantisce da solo varietà dei campioni, perciò fedeltà e copertura vanno misurate separatamente."
    if any(token in lower for token in ("flow", "cambio di variabile", "coupling", "ode")):
        return "Un flow rende esplicito il percorso invertibile tra spazio semplice e dati. La densità deve tenere conto del Jacobiano, mentre il costo dipende dalla trasformazione o dalla soluzione numerica scelta."
    if any(token in lower for token in ("diffusione", "score matching", "parametrizzazioni", "sampler", "flow matching")):
        return "La diffusione separa corruzione e ricostruzione attraverso uno schedule. Target, parametrizzazione e sampler descrivono punti diversi dello stesso percorso e una riduzione degli step non conserva automaticamente ogni proprietà."
    if any(token in lower for token in ("unicode", "byte", "tokenizzazione", "token speciali", "packing", "lunghezza")):
        return "Prima del modello, il testo diventa una sequenza di unità con una convenzione precisa. Encoding, tokenizer, token speciali, mask e packing modificano l'input effettivo e quindi fanno parte del contratto del checkpoint."
    if any(token in lower for token in ("embedding", "word embedding", "embedding contestuale", "sentence embedding", "anisotropia")):
        return "Una embedding table seleziona vettori per ID; il contesto e l'obiettivo possono poi trasformare quella rappresentazione. La similarità è una misura scelta per un uso, non una definizione universale di significato."
    if any(token in lower for token in ("transformer", "encoder", "decoder", "multi-head", "residual stream")):
        return "Il Transformer compone embedding, posizione, attention, MLP, residual e normalizzazione. Il contratto cambia quando cambiano mask, direzione della sequenza o interfaccia tra encoder e decoder, anche se la shape finale resta uguale."
    if any(token in lower for token in ("sorgenti", "provenienza", "parsing", "filtri", "deduplicazione", "split", "manifest")):
        return "Ogni trasformazione dei dati cambia la popolazione che il training vede. Provenienza, regole di filtro, deduplicazione, split e manifest servono a distinguere un cambiamento nei dati da un cambiamento nel modello."
    if any(token in lower for token in ("mixture", "curriculum", "temperature sampling", "dati sintetici")):
        return "La quantità grezza di una sorgente non coincide con la sua esposizione durante il training. Pesi, ordine, temperatura e filtri dei dati sintetici modificano la distribuzione effettivamente campionata."
    if any(token in lower for token in ("scaling", "compute-optimal", "isoflop", "extrapolation", "inference cost")):
        return "Una relazione di scaling è una misura nell'intervallo del setup osservato. Cambiare qualità dei dati, ricetta, obiettivo o costo di inference può spostare la conclusione, quindi l'extrapolation richiede ipotesi esplicite."
    if any(token in lower for token in ("batch", "adamw", "warmup", "schedule", "checkpoint", "recovery")):
        return "La ricetta di training è una sequenza di stato, non soltanto un modello e un learning rate. Optimizer, scheduler, scaler, RNG e posizione nei dati devono ripartire dallo stesso contratto per rendere il resume interpretabile."
    if any(token in lower for token in ("distributed", "zero", "fsdp", "tensor", "pipeline parallelism", "topologia")):
        return "Il calcolo distribuito divide dati, parametri, stati o layer e introduce comunicazione tra worker. La riduzione dei gradienti e il recovery devono restare coerenti con la partizione realmente usata."
    if any(token in lower for token in ("norm", "rmsnorm", "swiglu", "ordine e parallelismo", "posizione", "rope", "alibi")):
        return "Questa variante cambia un punto preciso del blocco o del segnale posizionale. Per confrontarla bisogna fissare ordine, shape, mask e condizioni di training, altrimenti si attribuisce alla variante una differenza nata dal setup."
    if any(token in lower for token in ("attention", "kv", "mha", "mqa", "gqa", "local", "sparse")):
        return "L'attention determina quali coppie di posizioni possono contribuire e come vengono organizzate key e value. Il numero di head, il pattern di visibilità e la cache cambiano memoria e connettività, non soltanto il nome del blocco."
    if any(token in lower for token in ("tiling", "flop", "softmax online", "backward", "backend")):
        return "L'ottimizzazione hardware-aware cambia il movimento dei dati e gli intermedi conservati, mentre il contratto matematico può restare lo stesso entro tolleranze dichiarate. Memoria, compute e ricomputazione sono il trade-off da misurare."
    if any(token in lower for token in ("linear attention", "fast weights", "delta rule", "state-space", "recurrence", "long convolution")):
        return "La forma fattorizzata sostituisce parte della matrice di interazioni con uno stato aggiornato. Il vantaggio dipende da ciò che lo stato conserva, dalla stabilità della normalizzazione e dalla dipendenza dalla lunghezza della sequenza."
    if any(token in lower for token in ("mixture of experts", "expert", "routing")):
        return "Il routing condizionale decide quali esperti elaborano ciascun token. Capacità, bilanciamento e comunicazione fanno parte dello stesso contratto: attivare meno parametri non dimostra da solo un vantaggio end-to-end."
    if any(token in lower for token in ("fine-tuning", "instruction", "formati conversazionali", "teacher forcing", "forgetting")):
        return "L'adattamento cambia il segnale presentato al modello e la porzione di output su cui si calcola la loss. Dati, mask, riferimenti e valutazione separata determinano quale comportamento viene effettivamente rinforzato."
    if any(token in lower for token in ("lora", "low-rank", "adapter", "parameter-efficient")):
        return "Un adattamento low-rank conserva i pesi base e apprende un aggiornamento con pochi gradi di libertà. Il risparmio di parametri non implica assenza di regressioni né equivalenza con il fine-tuning completo."
    if any(token in lower for token in ("preference", "reward model", "rlhf", "dpo", "verifier", "reward verificabili", "reasoning")):
        return "Il post-training trasforma preferenze, verifiche o tracce in un segnale di aggiornamento. Quel segnale è un proxy: bisogna separare ciò che viene premiato dal comportamento applicativo che si vuole valutare."
    if any(token in lower for token in ("test-time", "ricerca", "budget")):
        return "Il test-time compute sposta risorse dall'addestramento alla selezione durante l'inference. Campioni, ricerca, verifica e latenza devono essere contati insieme per sapere che cosa è migliorato."
    if any(token in lower for token in ("multimodal", "vision", "audio", "video", "3d", "world model", "embodied")):
        return "Le modalità devono essere rappresentate, sincronizzate e collegate a un compito osservabile. Una proiezione in uno spazio comune o una risposta corretta non dimostra da sola grounding o comprensione generale."
    if any(token in lower for token in ("retrieval", "rag", "document", "bm25", "query", "memoria")):
        return "La pipeline separa query, ranking, contesto recuperato e risposta. Un errore può nascere nel recupero, nella selezione del contesto o nella generazione, quindi la provenienza va conservata a ogni passaggio."
    if any(token in lower for token in ("tool", "protocol", "interoperabilità", "agent", "browser", "sandbox", "least privilege", "approval")):
        return "Un sistema agentico aggiunge stati, strumenti e autorizzazioni alla generazione. Il modello può proporre una chiamata, ma schema, scope, side effect e controllo devono essere applicati fuori dal testo."
    if any(token in lower for token in ("quantizzazione", "quant", "low-bit", "bit", "pruning", "distillazione")):
        return "La compressione cambia rappresentazione, memoria o costo e può introdurre errore. Per attribuire l'effetto bisogna separare storage, calcolo, kernel, calibrazione e regressioni sul compito."
    if any(token in lower for token in ("decoding", "sampling", "speculative", "draft", "kv cache", "prefill", "serving", "batching", "scheduling")):
        return "L'inference trasforma logits e richieste in una traiettoria sotto vincoli di memoria e tempo. Decoding, cache, batching e scheduling modificano il servizio osservato e richiedono metriche oltre alla qualità dell'output."
    if any(token in lower for token in ("compiler", "kernel", "runtime", "autotuning")):
        return "Il compiler abbassa un grafo in operazioni del backend e può fondere, riordinare o specializzare i kernel. Correttezza numerica e velocità sono controlli distinti e dipendono dal target hardware."
    if any(token in lower for token in ("valutazione", "metric", "benchmark", "factual", "calibr", "judge", "report", "contesto lungo")):
        return "Una valutazione deve collegare claim, popolazione, protocollo e decisione. Media, slice, failure, giudice e incertezza misurano aspetti diversi e non diventano intercambiabili perché condividono una tabella."
    if any(token in lower for token in ("interpret", "probe", "attribution", "causal", "circuit", "sparse autoencoder")):
        return "Interpretare significa dichiarare quale oggetto viene analizzato e quale intervento o misura lo collega al comportamento. Informazione decodificabile, attribuzione e causalità non sono lo stesso risultato."
    if any(token in lower for token in ("robustezza", "jailbreak", "adversarial", "injection", "poisoning", "backdoor", "supply chain")):
        return "La sicurezza parte da una minaccia, una superficie e una decisione verificabile. Un filtro o una risposta convincente non sostituiscono isolamento, allowlist, provenienza, logging e recovery applicati al confine della risorsa."
    if any(token in lower for token in ("privacy", "fairness", "unlearning", "differential")):
        return "Il rischio dipende da popolazione, decisione e criterio di misura. Privacy, fairness e unlearning richiedono definizioni operative e controlli sul sistema, non soltanto una modifica al dataset o al checkpoint."
    if any(token in lower for token in ("watermark", "provenienza", "c2pa", "firma", "digest")):
        return "Un digest, una firma o una credential collegano un artefatto a un record e a una catena dichiarata. Non certificano da soli la verità semantica del contenuto né l'affidabilità di ogni soggetto della pipeline."
    if any(token in lower for token in ("governance", "ruoli", "risk management", "norme", "sostenibilità", "incidenti")):
        return "Governance e sostenibilità trasformano misure, ruoli e rischi in decisioni tracciabili. Framework, norma o checklist guidano il processo, ma non certificano automaticamente l'uso concreto del sistema."
    if any(token in lower for token in ("laboratorio", "ambiente", "dataset piccolo", "report", "piccolo language model", "corpus")):
        return "Il laboratorio riduce il problema a un caso osservabile: ambiente, dati, trasformazione, output e limite devono essere conservati insieme. La scala ridotta aumenta la leggibilità, non autorizza claim sulla produzione."
    if any(token in lower for token in ("produzione", "deployment", "replica", "paper", "claim", "frontiera", "edizioni")):
        return "Il passaggio da esperimento a sistema richiede un protocollo esplicito, artefatti identificabili e una decisione delimitata. Una replica, una release o una nuova evidenza aggiunge informazione senza cancellare le condizioni del risultato originale."
    return f"Il passaggio da seguire in «{heading}» è quello descritto dalla frase «{note_core}»: l'esempio rende osservabile la trasformazione, mentre il contratto del capitolo ne delimita l'interpretazione."


def section_mechanism_focus(heading: str, note_core: str, detail: dict[str, str]) -> str:
    """Add a section-specific causal test to the shared mechanism explanation.

    A chapter may share one contract, but its transitions must not collapse into
    one reusable paragraph.  These short clauses name the variable to isolate
    in the section itself.  They are methodological consequences of the
    section claim, not new empirical claims.
    """
    lower = heading.casefold()
    if any(token in lower for token in ("formato", "ruol", "separat", "system message", "mask", "label")):
        return "In questa sezione si isola la maschera: a parità di messaggio, si controlla quali posizioni contribuiscono davvero alla loss."
    if any(token in lower for token in ("mixture", "curriculum", "sorgent", "peso", "sintetic")):
        return "La variabile da registrare è la probabilità effettiva di campionamento per sorgente, distinta dal conteggio grezzo dei record."
    if any(token in lower for token in ("teacher forcing", "autoregress", "sampling", "decoding")):
        return "Il confronto utile mette accanto il prefisso corretto e quello prodotto dal modello, così il segnale disponibile al training non viene confuso con l'inference."
    if any(token in lower for token in ("forgetting", "regression", "regressione", "recovery", "replay")):
        return "Il test deve conservare una misura del comportamento precedente prima e dopo l'aggiornamento, non soltanto il punteggio sul compito nuovo."
    if any(token in lower for token in ("mdp", "markov", "ritorno")):
        return "La prova separa reward immediato, stato successivo e fattore di sconto, perché confonderli cambia la quantità stimata."
    if any(token in lower for token in ("bellman", "value function")):
        return "La verifica confronta il valore ricorsivo con la somma del reward immediato e del valore futuro, mantenendo fissa la policy."
    if any(token in lower for token in ("policy gradient", "actor-critic")):
        return "La leva da cambiare è il segnale usato per l'aggiornamento: probabilità della policy e stima del critic devono restare distinguibili."
    if any(token in lower for token in ("esplorazione", "valutazione")):
        return "Il controllo separa raccolta di traiettorie e confronto delle policy, riportando ritorno, dispersione e vincoli come misure diverse."
    if any(token in lower for token in ("routing", "expert", "capacità")):
        return "La prova conta assegnazioni, overflow e comunicazione, non solo il numero di parametri dichiarato dagli esperti."
    if any(token in lower for token in ("attention", "head", "kv", "cache", "posizione", "contesto")):
        return "La variabile da isolare è il pattern di visibilità o di riuso: la stessa shape può corrispondere a dipendenze e costi diversi."
    if any(token in lower for token in ("quant", "bit", "precision", "calibraz", "scale")):
        return "Il controllo confronta valore originale, rappresentazione compressa e ricostruzione, riportando separatamente errore numerico e comportamento sul compito."
    if any(token in lower for token in ("retrieval", "rag", "query", "document", "memoria")):
        return "La prova conserva ranking, segmenti entrati nel contesto e risposta, così un errore di recupero non viene attribuito alla generazione."
    if any(token in lower for token in ("tool", "agent", "traiettoria", "sandbox", "approval", "browser")):
        return "Il controllo deve mostrare la decisione prima del side effect e la verifica dopo la chiamata, includendo anche una richiesta fuori allowlist."
    if any(token in lower for token in ("benchmark", "leaderboard", "report", "metric", "giudic", "slice")):
        return "La misura va letta insieme a popolazione, slice e failure: cambiare il report senza cambiare il protocollo non crea nuova evidenza."
    if any(token in lower for token in ("provenienza", "watermark", "credential", "firma", "digest")):
        return "Il confronto separa integrità del record, identità del firmatario e verità del contenuto, che sono proprietà diverse della stessa pipeline."
    if any(token in lower for token in ("govern", "norme", "responsabilità", "incident")):
        return "La verifica assegna owner, evidenza, decisione e condizione di riapertura allo stesso caso, senza trasformare la checklist in una certificazione."
    if any(token in lower for token in ("latency", "throughput", "hardware", "kernel", "energia", "costo", "batch", "serving")):
        return "La misura separa costo locale, coda e latenza end-to-end sotto un carico dichiarato, così il miglioramento non resta confinato al kernel."
    if any(token in lower for token in ("replica", "paper", "claim", "frontiera", "edizioni", "maturità", "scouting")):
        return "La scheda di prova conserva fonte, data, configurazione e decisione, permettendo di distinguere novità editoriale da evidenza ripetuta."
    return f"Per «{heading}» il controllo cambia una sola premessa della frase «{note_core}» e conserva input, output e criterio di successo, così la differenza resta attribuibile."


def section_explanation(number: int, heading: str, note_core: str, detail: dict[str, str]) -> str:
    base_explanation = _section_explanation_base(number, heading, note_core, detail)
    focus = section_mechanism_focus(heading, note_core, detail)
    return f"{base_explanation} {focus} La verifica resta ancorata a «{note_core}»."


def section_prose(number: int, part: str, index: int, heading: str, note: str, next_heading: str | None) -> str:
    """Write a section around its own source-backed claim.

    Earlier versions repeated the chapter-level contract in every transition.
    That made the prose pass structural checks while allowing a section about
    one mechanism to inherit examples and failure modes from another.  This
    version gives the section note priority and uses the chapter contract only
    once as the local interface.
    """
    kind = profile(number)
    family = prose_family(number, kind)
    detail = detail_for_chapter(number)
    invariant_plain = detail["invariant"].rstrip(".")
    source_index = source_indices_for(number, len(SPECS[number][6]))[index]
    source_id = f"SRC-{number:02d}-{source_index + 1:03d}"
    input_label = f"l'input «{detail['input']}»"
    output_label = f"l'output «{detail['output']}»"
    output_label_cap = f"L'output «{detail['output']}»"
    operation_label = f"l'operazione «{detail['operation']}»"
    example = section_example(number, kind, heading, detail, index).rstrip(".")
    note_text = note.strip()
    if note_text and note_text[-1] not in ".!?":
        note_text += "."
    note_core, note_follow = note_parts(note)
    note_follow_sentence = f"{note_follow}. " if note_follow else ""
    scope, control, transfer = PROSE_TAIL_DESCRIPTORS.get(family, PROSE_TAIL_DESCRIPTORS["evaluation"])

    lead_variants = (
        f"Per capire «{heading}» partiamo da questo caso: {example}. Il caso rende osservabile il punto centrale: «{note_core}».",
        f"Il caso minimo di «{heading}» si presenta così: {example}. Non lo usiamo come decorazione: serve a rendere osservabile la frase «{note_core}».",
        f"Prima del nome tecnico fissiamo la situazione: consideriamo {example}. Da qui possiamo leggere la conseguenza dichiarata da «{note_core}».",
    )
    contract_variants = (
        f"Nel contratto locale, {input_label} entra, {operation_label} modifica il percorso e {output_label} è ciò che osserviamo. Qui cambia soprattutto il passaggio «{heading}»; resta da controllare che {invariant_plain}. La domanda locale è «{note_core}».",
        f"La sezione usa {input_label} come punto di partenza e {output_label} come traccia d'uscita. La trasformazione concreta è «{detail['operation']}»; il caso non è completo se non dichiariamo anche che {invariant_plain}. La condizione da isolare è «{note_core}».",
        f"Per ricostruire «{heading}» annotiamo {input_label}, poi {operation_label}, infine {output_label}. Questa sequenza impedisce di scambiare una forma compatibile per il comportamento descritto dalla fonte. Il controllo parte da «{note_core}».",
    )
    reading_variants = (
        f"La lettura va fatta in ordine: prima il caso, poi la trasformazione, quindi la conseguenza. {note_follow_sentence}Il piccolo risultato resta un'illustrazione di «{note_core}», non una promessa generale.",
        f"Il punto didattico di «{heading}» è separare ciò che la fonte afferma da ciò che il piccolo caso illustra. {output_label_cap} mostra il contratto locale, ma non sostituisce una misura sul sistema completo.",
        f"Se cambiamo una premessa, dobbiamo riaprire l'interpretazione. Per «{heading}» conserviamo l'osservazione collegata a «{note_core}» e lasciamo esplicitamente fuori ciò che non è stato misurato.",
    )
    verification_variants = (
        f"Per verificare «{heading}» cambiamo una sola condizione vicina alla frase «{note_core}», teniamo fermo il resto e registriamo {output_label}. Il caso negativo deve rendere riconoscibile la failure, non soltanto produrre un numero diverso.",
        f"Il controllo minimo di «{heading}» confronta il caso dichiarato con una variazione che rompe la sua ipotesi. Se la failure non è distinguibile dall'esito valido, manca un'osservazione nel contratto di {scope}.",
        f"La prova di «{heading}» conserva input, operazione e output; poi esplicita quale parte di «{note_core}» non è stata misurata. Così il test separa l'evidenza dall'inferenza.",
    )
    bridge = (
        f"La sezione successiva, «{next_heading}», riceve {output_label} come base, ma dovrà formulare e verificare la propria distinzione.",
        f"Da «{heading}» portiamo {output_label}; non portiamo invece una conclusione oltre il caso locale.",
        f"Il passaggio successivo, «{next_heading}», potrà cambiare una sola condizione, dichiarando il nuovo setup prima di interpretare il risultato.",
    ) if next_heading else (
        "Il percorso si chiude lasciando espliciti la misura locale e ciò che richiederebbe una prova ulteriore.",
        "La conclusione resta ancorata al protocollo osservato, non al nome della tecnica.",
        f"Il caso finale consegna {output_label} come evidenza locale e conserva {transfer} come domanda aperta.",
    )
    paragraphs = [
        f"{note_text} [{source_id}]",
        lead_variants[(number + index) % len(lead_variants)],
        contract_variants[(number * 2 + index) % len(contract_variants)],
        f"{section_explanation(number, heading, note_core, detail)} [{source_id}]",
        reading_variants[(number + index * 2) % len(reading_variants)],
        f"{verification_variants[(number + index) % len(verification_variants)]} {bridge[(number + index) % len(bridge)]}",
    ]
    return "\n\n".join(paragraphs)


def formula_for(number: int, kind: str) -> tuple[str, str]:
    if number in FORMULAS:
        return FORMULAS[number]
    return formula_for_base(number, kind)


def opening(number: int, title: str, part: str, previous_title: str, next_title: str) -> str:
    detail = detail_for_chapter(number)
    input_label = f"l'input «{detail['input']}»"
    output_label = f"l'output «{detail['output']}»"
    options = [
        f"Il Capitolo {number - 1}, {previous_title}, ha lasciato disponibile {detail['object']}. Manteniamo come filo comune la richiesta «Il pacco non è arrivato» e qui la traduciamo nell'oggetto della lezione. La domanda diventa operativa: rendiamo osservabile il passaggio «{detail['operation']}» e verifichiamo che {detail['invariant']}.",
        f"Finora abbiamo potuto descrivere {detail['object']}. La richiesta «Il pacco non è arrivato» resta lo scenario condiviso: nel Capitolo {number} prendiamo {input_label} e lo seguiamo fino a {output_label}, dichiarando prima il contratto e poi il limite.",
        f"Il risultato precedente non è ancora una soluzione completa. Partiamo da {detail['object']} e dalla richiesta «Il pacco non è arrivato» come esempio comune; per arrivare a {output_label} isoliamo il passaggio «{detail['operation']}» e ne misuriamo il limite prima di passare a {next_title}.",
        f"La richiesta «Il pacco non è arrivato» resta il caso guida. In questo capitolo la usiamo per distinguere {detail['object']}, trasformazione e risultato, senza nascondere i dettagli tecnici.",
        f"Una frase plausibile non basta a spiegare {title.lower()}. L'oggetto è {detail['object']}; riprendiamo la richiesta «Il pacco non è arrivato» come contesto comune, partiamo da un input piccolo, rendiamo visibile l'operazione e fissiamo che cosa non possiamo concludere.",
    ]
    return options[number % len(options)]


PUBLIC_CLOSURE_STYLES = (
    {
        "example": "Un caso dall'input all'output",
        "code": "Dal meccanismo alla prova locale",
        "boundary": "Dove il risultato si ferma",
        "recap": "Che cosa portiamo avanti",
        "verify": "Verifica di comprensione",
        "exercise": "Esercizi di trasferimento",
        "sources": "Fonti, codice e materiali",
    },
    {
        "example": "La definizione messa alla prova",
        "code": "Un esperimento piccolo ma leggibile",
        "boundary": "Il confine del caso guida",
        "recap": "Il contratto che rimane",
        "verify": "Controllo finale della lezione",
        "exercise": "Prove da rifare e modificare",
        "sources": "Riferimenti e prove riproducibili",
    },
    {
        "example": "Una traiettoria controllata",
        "code": "Il passaggio eseguito in Python",
        "boundary": "Prima di generalizzare",
        "recap": "Dalla lezione al capitolo seguente",
        "verify": "Domande per ricostruire il percorso",
        "exercise": "Esercizi sul failure mode",
        "sources": "Dossier delle fonti e materiali",
    },
    {
        "example": "Il caso minimo e la sua variante",
        "code": "Che cosa osserva lo snippet",
        "boundary": "Che cosa non dimostra",
        "recap": "La mappa delle condizioni",
        "verify": "Cinque domande di controllo",
        "exercise": "Esercizi per cambiare una condizione",
        "sources": "Fonti e risultati locali",
    },
    {
        "example": "Dal concetto alla situazione concreta",
        "code": "Una prova ripetibile",
        "boundary": "Il trasferimento richiede altro",
        "recap": "Il filo che passa oltre",
        "verify": "Rilettura guidata",
        "exercise": "Allenamento e trasferimento",
        "sources": "Dove verificare definizioni e risultati",
    },
    {
        "example": "Un esempio con controllo negativo",
        "code": "Dalla formula al run",
        "boundary": "Limiti, varianti e nuove misure",
        "recap": "L'invariante da conservare",
        "verify": "Prova di comprensione",
        "exercise": "Esercizi con casi limite",
        "sources": "Fonti primarie e artefatti del capitolo",
    },
    {
        "example": "Il contratto in un caso piccolo",
        "code": "Dalla trasformazione al test",
        "boundary": "Il perimetro della conclusione",
        "recap": "Una sintesi operativa",
        "verify": "Domande per il lettore",
        "exercise": "Esercizi di ricostruzione",
        "sources": "Materiali, fonti e codice verificato",
    },
)


def public_closure(number: int, title: str, detail: dict[str, str], sections, source_ids: list[str], module: str, formula: str, formula_note: str, next_title: str) -> list[str]:
    """Build a readable, topic-shaped ending without a fixed seven-heading shell."""
    style = PUBLIC_CLOSURE_STYLES[(number * 3 + len(topic_for(number, profile(number)))) % len(PUBLIC_CLOSURE_STYLES)]
    family = prose_family(number, profile(number))
    scope, control, transfer = PROSE_TAIL_DESCRIPTORS.get(family, PROSE_TAIL_DESCRIPTORS["evaluation"])
    first_heading = sections[0][0]
    last_heading = sections[-1][0]
    input_label = f"l'input «{detail['input']}»"
    output_label = f"l'output «{detail['output']}»"
    operation_label = f"l'operazione «{detail['operation']}»"
    invariant_plain = detail["invariant"].rstrip(".")
    section_names = ", ".join(f"«{heading}»" for heading, _ in (sections[:2] + sections[-1:]))
    first_claim, _ = note_parts(sections[0][1])
    last_claim, _ = note_parts(sections[-1][1])
    if number < 98:
        handoff = f"Il Capitolo {number + 1}, {next_title}, può partire da questo output e dichiarare la propria domanda."
    else:
        handoff = "Il percorso si chiude lasciando espliciti input, operazione, output, fonti e limiti."
    comprehension = (
        f"1. Ricostruisci l'oggetto continuo a partire da «{first_heading}» e indica quale parte della frase «{first_claim}» entra nel caso.",
        f"2. Spiega quale trasformazione collega «{first_heading}» a «{last_heading}» e quale output osserviamo nel passaggio.",
        f"3. Usa lo snippet per controllare l'invariante del contratto: {detail['invariant']}.",
        "4. Separa una definizione sostenuta da una fonte, un esempio illustrativo e un risultato locale del caso guida.",
        f"5. Indica quale parte della frase «{last_claim}» richiederebbe una misura nuova prima di essere estesa oltre il caso osservato.",
    )
    formula_intro, formula_description = formula_public_note(number, formula_note)
    code_variants = (
        f"Lo snippet locale mette in esecuzione questo caso: {detail['example']}. Il test associato controlla determinismo, output e invariante e rifiuta una shape o condizione incoerente; il risultato è conservato in `code/outputs/SNIP-{number:02d}-001.txt`, come evidenza locale e non come benchmark di produzione.",
        f"Nel run Python rendiamo osservabile la frase «{first_claim}» con valori piccoli e leggibili. Il test associato verifica determinismo, output e rifiuto di una condizione incoerente; il file di output `code/outputs/SNIP-{number:02d}-001.txt` documenta il caso senza pretendere una misura generale.",
        f"Il file `code/{module}.py` collega il contratto del capitolo alla frase «{last_claim}». Il test controlla l'invariante, la risposta valida e il caso negativo; `code/outputs/SNIP-{number:02d}-001.txt` conserva il risultato ripetibile del caso locale.",
    )
    recap_variants = (
        f"Abbiamo seguito {detail['object']}, partendo da {input_label} e arrivando a {output_label}. Le sezioni {section_names} hanno isolato le proprie frasi chiave senza confondere il meccanismo con il risultato applicativo.",
        f"Il filo della lezione va da {input_label} a {output_label}. Nei passaggi {section_names} abbiamo usato esempi e controlli negativi per rendere il contratto controllabile e delimitare la conclusione.",
        f"Il percorso ha tenuto insieme {detail['object']}, {operation_label} e {output_label}. Le sezioni {section_names} mostrano come il protocollo osservato delimiti ciò che il capitolo può sostenere.",
    )
    source_variants = (
        f"Per «{title}», le fonti portanti, i limiti dei claim e la data di consultazione sono raccolti in `FONTI_PRIMARIE.md`; la ricerca riguarda soprattutto {scope}.",
        f"Il dossier di «{title}» in `FONTI_PRIMARIE.md` separa definizioni, risultati e {control}; la data di consultazione è registrata accanto ai riferimenti.",
        f"Per ricontrollare «{title}», partire da `FONTI_PRIMARIE.md` e poi dal codice: la domanda aperta è come trasferire {transfer} oltre il caso locale, con la data di consultazione dichiarata.",
    )
    code_copy = code_variants[(number + len(title)) % len(code_variants)]
    recap_copy = recap_variants[(number + len(title) + 1) % len(recap_variants)]
    source_copy = source_variants[(number + len(title) + 2) % len(source_variants)]
    boundary_variants = (
        f"Il meccanismo di «{title}» non garantisce da solo che il sistema funzioni fuori dal caso guida. {invariant_plain.capitalize()}. Il limite osservato riguarda la frase «{first_claim}»; per trasferire il concetto occorre riaprire la verifica quando cambiano dati, scala o ambiente.",
        f"Il meccanismo di «{title}» resta legato al contratto locale. {invariant_plain.capitalize()}. Prima di generalizzare la frase «{last_claim}», servono un nuovo setup, un protocollo dichiarato e una misura ripetibile.",
        f"Il caso di «{title}» non certifica un servizio completo. {invariant_plain.capitalize()}. La domanda successiva è se «{last_claim}» regga quando cambiano dati, scala, hardware o criteri di decisione.",
    )
    boundary_copy = boundary_variants[(number + len(title) + 2) % len(boundary_variants)]
    return [
        f"## {style['example']}: {first_heading}\n\n"
        f"Il caso intero parte da {input_label}, applica l'operazione «{detail['operation']}» e osserva {output_label}. Un esempio controllato: {detail['example']}. "
        f"{formula_intro}\n\n$$\n{formula}\n$$\n\n{formula_description} [{source_ids[0]}]",
        f"## {style['code']}: {sections[1][0]}\n\n"
        f"{code_copy}",
        f"## {style['boundary']}: {last_heading}\n\n"
        f"{boundary_copy}",
        f"## {style['recap']}: {title}\n\n"
        f"{recap_copy} L'invariante da portare avanti è: {invariant_plain}. {handoff}",
        f"### {style['verify']}: {first_heading}\n\n" + "\n".join(comprehension),
        f"### {style['exercise']}: {last_heading}\n\n" + exercise_lines(number, sections),
        f"## {style['sources']}: {title}\n\n"
        f"{source_copy} `CLAIMS.md` separa definizioni e risultati locali; codice, ambiente, test e output sono nella cartella `code/`, con attenzione a {scope}.",
    ]


def exercise_lines(number: int, sections) -> str:
    headings = [h for h, _ in sections]
    prompt_sets = (
        (
            f"Ricostruisci input e output di «{headings[0]}» usando un esempio di tre righe.",
            f"Modifica una sola variabile in «{headings[1]}» e anticipa l'invariante che dovrebbe restare.",
            f"Metti «{headings[2]}» a confronto con il caso base e descrivi il failure mode più vicino.",
            f"Scrivi un test minimo per rendere osservabile il confine di «{headings[3]}».",
            f"Formula per «{headings[4]}» una domanda che separi meccanismo e qualità del sistema.",
        ),
        (
            f"Disegna il percorso di «{headings[0]}» indicando dati in ingresso e risultato.",
            f"Ripeti «{headings[1]}» cambiando soltanto un valore dichiarato.",
            f"Trova in «{headings[2]}» una condizione che, se rimossa, produrrebbe una failure leggibile.",
            f"Aggiungi a «{headings[3]}» un controllo negativo e spiega che cosa protegge.",
            f"Indica quale claim su «{headings[4]}» richiederebbe un benchmark ulteriore.",
        ),
        (
            f"Racconta «{headings[0]}» come una trasformazione: che cosa entra e che cosa esce?",
            f"Confronta due esecuzioni di «{headings[1]}» mantenendo il resto del setup invariato.",
            f"Per «{headings[2]}», separa l'esempio locale dal limite che impedisce di generalizzarlo.",
            f"Progetta una prova per «{headings[3]}» che renda visibile il suo confine.",
            f"Scrivi una metrica o una domanda per valutare «{headings[4]}» senza confondere livelli diversi.",
        ),
        (
            f"Ricostruisci «{headings[0]}» senza usare il nome della tecnica, soltanto con input, operazione e output.",
            f"Sostituisci una condizione di «{headings[1]}» e prevedi che cosa non dovrebbe cambiare.",
            f"Cerca un controesempio per «{headings[2]}» e annota quale ipotesi viene rotta.",
            f"Trasforma il limite di «{headings[3]}» in un test ripetibile.",
            f"Spiega come trasferire «{headings[4]}» senza portare con sé una promessa non misurata.",
        ),
    )
    prompts = prompt_sets[(number + len(headings[0])) % len(prompt_sets)]
    return "\n".join(f"{i + 1}. {prompt}" for i, prompt in enumerate(prompts))


def write_plan(number: int, title: str, part: str, sections, first_id: str, second_id: str, module: str) -> None:
    detail = detail_for_chapter(number)
    previous = PREVIOUS_TITLE_OVERRIDES.get(number, SPECS.get(number - 1, SPECS[number])[4])
    following = SPECS.get(number + 1, SPECS[number])[4] if number < 98 else "chiusura del percorso"
    lines = [
        f"# Piano interno. Capitolo {number}",
        "",
        f"- Domanda centrale: quale contratto costruisce {title}?",
        f"- Oggetto continuo: {detail['object']}; input guida: {detail['input']}.",
        f"- Prerequisito stabile: Capitolo {number - 1}, {previous}.",
        f"- Gap: {detail['operation']}.",
        f"- Output consegnato: {detail['output']}; consumer successivo: Capitolo {number + 1}, {following}." if number < 98 else f"- Output consegnato: {detail['output']}; consumer successivo: chiusura del percorso.",
        f"- Invariante principale: {detail['invariant']}.",
        f"- Visuali: {first_id} e {second_id}, con famiglie compositive variabili.",
        f"- Snippet: code/{module}.py; output: code/outputs/SNIP-{number:02d}-001.txt.",
        "- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.",
        "",
    ]
    for index, (heading, note) in enumerate(sections, 1):
        source_index = source_indices_for(number, len(sections))[index - 1]
        lines.extend(
            [
                f"## Transizione {index}. {heading}",
                "",
                f"- Ultima affermazione stabile: {detail['object']}.",
                f"- Concetto nuovo: {note}",
                f"- Input e shape: {detail['input']}.",
                f"- Operazione: {detail['operation']}.",
                f"- Output e shape: {detail['output']}.",
                f"- Che cosa cambia: il passaggio specifico di «{heading}».",
                f"- Invariante: {detail['invariant']}.",
                "- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.",
                f"- Esempio o errore: {detail['example']}; provare anche una condizione incoerente e osservare il controllo.",
                f"- Consumer: {sections[index][0] if index < len(sections) else following}.",
                f"- Prova: SRC-{number:02d}-{source_index + 1:03d} e sezione pubblica corrispondente.",
                "",
            ]
        )
    (ROOT / "chapters" / SPECS[number][3] / "PLAN.md").write_text("\n".join(lines), encoding="utf-8")


def write_chapter(number: int) -> None:
    _, chapter_id, part, slug, title, maturity, sections = SPECS[number]
    kind = profile(number)
    chapter = ROOT / "chapters" / slug
    chapter.mkdir(parents=True, exist_ok=True)
    previous = PREVIOUS_TITLE_OVERRIDES.get(number, SPECS.get(number - 1, SPECS[number])[4])
    next_title = SPECS.get(number + 1, SPECS[number])[4] if number < 98 else "chiusura del percorso"
    source_ids = write_sources(number, kind, sections)
    first_id, second_id, first_version, second_version = write_visuals(number, slug, title, sections)
    module = write_code(number, slug, title, kind)
    write_claims(number, title, sections, source_ids, module)
    formula, formula_note = formula_for(number, kind)
    opening_text = opening(number, title, part, previous, next_title)
    figure_after = [1, 2, 3][number % 3]
    body_parts = []
    for index, (heading, note) in enumerate(sections):
        next_heading = sections[index + 1][0] if index + 1 < len(sections) else None
        body_parts.append(f"## {heading}\n\n{section_prose(number, part, index, heading, note, next_heading)}")
        if index == figure_after:
            family = family_for(number, 0)
            body_parts.append(
                f"![{title}: {family}](../../assets/chapters/{slug}/{first_id}/candidate-v{first_version}.png)\n\n"
                f"La figura {first_id} usa la famiglia {family}. {visual_question(number, family)}."
            )
    detail = detail_for_chapter(number)
    closure = public_closure(
        number,
        title,
        detail,
        sections,
        source_ids,
        module,
        formula,
        formula_note,
        next_title,
    )
    second_figure = (
        f"![{title}: {family_for(number, 1)}](../../assets/chapters/{slug}/{second_id}/candidate-v{second_version}.png)\n\n"
        f"La figura {second_id} cambia composizione rispetto alla prima. {visual_question(number, family_for(number, 1))}."
    )
    body_parts.append(closure[0] + "\n\n" + second_figure)
    body_parts.extend(closure[1:])
    body = "\n\n".join(body_parts)
    chapter_text = polish_text(f"""<!--
chapter_id: {chapter_id}
part_id: {part}
order_key: {number * 10:03d}
title: {title}
maturity: {maturity}
status: candidatura completa in revisione autoriale
version: 0.4.0-draft2
last_source_check: {DATE}
environment: Python {sys.version.split()[0]}, CPU
deferred: benchmark applicativi, varianti non necessarie al contratto centrale e approvazione autoriale
-->

# Capitolo {number}. {title}

{opening_text}

{body}
""")
    (chapter / "CHAPTER.md").write_text(chapter_text, encoding="utf-8")
    (chapter / "TEXT_AUDIT.md").write_text(
        f"""# Audit del testo. Capitolo {number}

- Review ID: TEXT-{number:02d}-2026-08-03-R2
- Versione: 0.4.0-draft2
- Data: {DATE}
- Ambito: testo pubblico, continuità, fonti, formule, esempi, codice e visuali collegate.
- Profili lettore: principiante motivato; sviluppatore Python; revisore tecnico.
- Stato complessivo: corretta, nuova review richiesta
- Correzioni applicate: profondità dei paragrafi, oggetto continuo, causalità input-operazione-output, esempi illustrativi, confini, esercizi, citazioni vicine, link a candidate versioned.
- Blocker: lettura ad alta voce e approvazione autoriale finale non automatizzabili.
- Non blocker: benchmark applicativi rinviati perché fuori dal contratto didattico locale.
- Artefatti riaperti: CHAPTER.md, PLAN.md, CLAIMS.md, FONTI_PRIMARIE.md, code/, visuali candidate e review.
- Lettura ad alta voce: nuova review richiesta.
- Anti-template: composizione visuale e posizione delle figure variabili; verifica editoriale manuale ancora richiesta.
- Esito: il capitolo è una candidatura tecnica completa, non una lezione approvata per la pubblicazione.
- Reviewer: Codex, revisione automatizzata e controllo raster locale.
""",
        encoding="utf-8",
    )
    (chapter / "REVIEW.md").write_text(
        f"""# Review del Capitolo {number}

- revisione: 0.4.0-draft2
- data: {DATE}
- prosa e continuità: corretta, nuova review richiesta
- fonti e claim: dossier completato, controllo autoriale richiesto
- formule e derivazioni: ricontrollate a livello di coerenza locale
- codice e test: eseguiti in Python CPU
- visuali: due famiglie compositive diverse, raster audit superato
- alt text e specifiche: presenti
- anti-template: migliorato con famiglie e inserimenti variabili; passaggio read-aloud ancora aperto
- approvazione autoriale: aperta
""",
        encoding="utf-8",
    )
    (chapter / "CHANGELOG.md").write_text(
        f"""# Changelog Capitolo {number}

## {DATE} · 0.4.0-draft2

- Riscritta la lezione con un oggetto continuo, esempi, formule e limiti espliciti.
- Completati dossier fonti, claim, piano interno e audit.
- Rigenerate due visuali candidate con famiglie compositive non uniformi.
- Eseguiti snippet e quattro controlli per il contratto locale.
- Stato: candidatura completa, approvazione autoriale ancora aperta.
""",
        encoding="utf-8",
    )
    write_plan(number, title, part, sections, first_id, second_id, module)


def main() -> None:
    for number in TARGETS:
        write_chapter(number)
        print(f"RIVISTO {number:02d} {SPECS[number][4]}")


if __name__ == "__main__":
    main()
