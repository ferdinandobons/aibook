# Piano editoriale. Capitolo 79

## Obiettivo didattico

Seguire **Serving, batching e scheduling** da prompt, deadline, lunghezza, memoria e priorità a throughput, latency p50/p99 e richieste ammesse, osservando batching continuo, admission e scheduling senza oltrepassare questo limite: throughput e latenza devono essere misurati insieme.

## Prerequisiti reali

- Capitolo 9: Calcolo numerico, precisione e hardware
- Capitolo 76: Decoding e generazione vincolata
- Capitolo 78: KV cache e riuso del contesto

## Percorso della lezione

1. **Richieste eterogenee.** Prompt e output hanno lunghezze differenti. Un batch statico spreca slot quando alcune sequenze terminano. Prova: SRC-79-001.
2. **Continuous batching.** Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse. Prova: SRC-79-002.
3. **Throughput e latency.** Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency. Prova: SRC-79-003.
4. **Admission control.** Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema. Prova: SRC-79-004.
5. **Metriche di servizio.** TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta. Prova: SRC-79-001.

## Prove e artefatti

- riferimento minimo: `code/snip_79_contract.py`; test: `code/test_79_contract.py`; output: `code/outputs/SNIP-79-001.txt`.
- visuali candidate: SERVING-01, SERVING-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
