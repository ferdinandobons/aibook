# Registro dei claim. Capitolo 79

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `serving` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-79-01

- Affermazione esatta: Prompt e output hanno lunghezze differenti. Un batch statico spreca slot quando alcune sequenze terminano.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Efficient Memory Management for Large Language Model Serving with PagedAttention; 3. Memory Challenges in LLM Serving; 3.1. Memory Management in Existing Systems (claim collegato alla sezione «Richieste eterogenee» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-79-02

- Affermazione esatta: Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Large-scale Pretraining Improves Sample Efficiency of Active Learning based Molecule Virtual Screening; 1 Introduction; 2 Results and discussion (claim collegato alla sezione «Continuous batching» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-79-03

- Affermazione esatta: Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Efficiently Programming Large Language Models using SGLang; 1 Introduction; 2 Background (claim collegato alla sezione «Throughput e latency» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-79-04

- Affermazione esatta: Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving; 2.2 LLM Serving Optimization; 6.3 Latency Breakdown (claim collegato alla sezione «Admission control» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-79-05

- Affermazione esatta: TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Efficient Memory Management for Large Language Model Serving with PagedAttention; 3. Memory Challenges in LLM Serving; 3.1. Memory Management in Existing Systems (claim collegato alla sezione «Metriche di servizio» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-79-CODE

- Affermazione esatta: lo snippet snip_79_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_79_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
