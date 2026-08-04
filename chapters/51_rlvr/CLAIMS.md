# Registro dei claim. Capitolo 51

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `rlvr` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-51-01

- Affermazione esatta: Problemi con risposta controllabile, come codice o matematica, consentono reward da test, parser o esecutori.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models; 2 Math Pre-Training; 2.2 Validating the Quality of the DeepSeekMath Corpus (claim collegato alla sezione «Reward verificabile» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-51-02

- Affermazione esatta: La policy genera più soluzioni per la stessa richiesta. Il reward confronta traiettorie e costruisce advantage o ranking.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models; 2 Math Pre-Training; 2.2 Validating the Quality of the DeepSeekMath Corpus (claim collegato alla sezione «Rollout e gruppi» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-51-03

- Affermazione esatta: Algoritmi group-relative normalizzano reward all'interno di gruppi e aggiornano log-probability con vincoli di stabilità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning; 2.2 DeepSeek-R1-Zero: Reinforcement Learning on the Base Model; 2.2.1 Reinforcement Learning Algorithm (claim collegato alla sezione «GRPO e policy update» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-51-04

- Affermazione esatta: Un risultato finale corretto non identifica quali passaggi siano utili. Exploration, curriculum e shaping cambiano la densità del segnale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2.5 Outcome-supervised Reward Models (ORMs); 2.6 Process-supervised Reward Models (PRMs); 4.1 Process vs Outcome Supervision (claim collegato alla sezione «Sparse reward» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-51-05

- Affermazione esatta: Un test incompleto può premiare exploit. Il reward verificabile è affidabile soltanto nel perimetro del verificatore.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Solving math word problems with process- and outcome-based feedback; 4.1 When to use process- vs. outcome-based feedback?; 4.1.2 Process-based approaches both require and facilitate human understanding (claim collegato alla sezione «Verificabilità limitata» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-51-CODE

- Affermazione esatta: lo snippet snip_51_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_51_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
