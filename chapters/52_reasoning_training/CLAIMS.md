# Registro dei claim. Capitolo 52

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `reasoning` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-52-01

- Affermazione esatta: Una traccia di ragionamento è testo prodotto dal modello. Può aiutare il training senza costituire una prova fedele del processo interno.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-52-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Chain-of-Thought Prompting Elicits Reasoning in Large Language Models; 3 Arithmetic Reasoning; 3.4 Robustness of Chain of Thought (claim collegato alla sezione «Tracce e risposte» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-52-02

- Affermazione esatta: Un teacher produce soluzioni o distribuzioni che diventano target per uno student. Filtraggio e copertura stabiliscono cosa viene trasferito.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-52-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Distilling the Knowledge in a Neural Network; 2 Distillation; 2.1 Matching logits is a special case of distillation (claim collegato alla sezione «Distillazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-52-03

- Affermazione esatta: Più candidate vengono generate e selezionate con voto o verifier. Il dataset risultante dipende dalla procedura di selezione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-52-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Self-Consistency Improves Chain of Thought Reasoning in Language Models; 2 Self-Consistency over Diverse Reasoning Paths; 3.3 Self-Consistency Helps When Chain-of-Thought Hurts Performance (claim collegato alla sezione «Self-consistency e rejection sampling» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-52-04

- Affermazione esatta: Una spiegazione corretta può essere post-hoc. Valutare risposta e fedeltà richiede esperimenti differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-52-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning; 2.2 DeepSeek-R1-Zero: Reinforcement Learning on the Base Model; 2.2.1 Reinforcement Learning Algorithm (claim collegato alla sezione «Faithfulness» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-52-05

- Affermazione esatta: Tracce più lunghe aumentano token e latenza. Il training deve distinguere utilità della risposta e budget del processo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-52-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Chain-of-Thought Prompting Elicits Reasoning in Large Language Models; 3 Arithmetic Reasoning; 3.4 Robustness of Chain of Thought (claim collegato alla sezione «Costo e lunghezza» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-52-CODE

- Affermazione esatta: lo snippet snip_52_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_52_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
