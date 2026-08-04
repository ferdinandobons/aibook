# Registro dei claim. Capitolo 53

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `test_time` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-53-01

- Affermazione esatta: Il sistema può generare più candidate, approfondire una traiettoria o usare ricerca prima di restituire la risposta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters; 2 A Unified Perspective on Test-Time Computation: Proposer and Verifier; 3 How to Scale Test-Time Computation Optimally (claim collegato alla sezione «Più compute dopo il training» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-53-02

- Affermazione esatta: Un proposer genera n candidate e un verifier seleziona. Il beneficio dipende dalla diversità e dalla qualità del ranking.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Self-Consistency Improves Chain of Thought Reasoning in Language Models; 2 Self-Consistency over Diverse Reasoning Paths; 3.3 Self-Consistency Helps When Chain-of-Thought Hurts Performance (claim collegato alla sezione «Best-of-n» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-53-03

- Affermazione esatta: Stati parziali vengono espansi, valutati e potati. Branching factor, profondità e budget definiscono il costo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Tree of Thoughts: Deliberate Problem Solving with Large Language Models; 1 Introduction; 2 Background (claim collegato alla sezione «Tree search» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-53-04

- Affermazione esatta: Problemi differenti ricevono budget differenti secondo confidenza, difficoltà o policy. La stima di difficoltà può essere errata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2.5 Outcome-supervised Reward Models (ORMs); 2.6 Process-supervised Reward Models (PRMs); 4.1 Process vs Outcome Supervision (claim collegato alla sezione «Adaptive compute» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-53-05

- Affermazione esatta: Accuracy o reward devono essere riportati insieme a token, forward, latenza e fallimenti del verifier.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters; 2 A Unified Perspective on Test-Time Computation: Proposer and Verifier; 3 How to Scale Test-Time Computation Optimally (claim collegato alla sezione «Metriche costo-qualità» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-53-CODE

- Affermazione esatta: lo snippet snip_53_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_53_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
