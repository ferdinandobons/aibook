# Piano editoriale. Capitolo 53

## Obiettivo didattico

Seguire **Test-time compute, ricerca e controllo del budget** da prompt, numero di campioni, token e deadline a risposta, costo, latenza e qualità, osservando best-of-n, tree search e adaptive compute senza oltrepassare questo limite: qualità e costo devono essere riportati insieme.

## Prerequisiti reali

- Capitolo 10: Ricerca, pianificazione e giochi
- Capitolo 31: Dalla rappresentazione linguistica agli LLM
- Capitolo 50: Process supervision, outcome supervision e verifier

## Percorso della lezione

1. **Più compute dopo il training.** Il sistema può generare più candidate, approfondire una traiettoria o usare ricerca prima di restituire la risposta. Prova: SRC-53-001.
2. **Best-of-n.** Un proposer genera n candidate e un verifier seleziona. Il beneficio dipende dalla diversità e dalla qualità del ranking. Prova: SRC-53-002.
3. **Tree search.** Stati parziali vengono espansi, valutati e potati. Branching factor, profondità e budget definiscono il costo. Prova: SRC-53-003.
4. **Adaptive compute.** Problemi differenti ricevono budget differenti secondo confidenza, difficoltà o policy. La stima di difficoltà può essere errata. Prova: SRC-53-004.
5. **Metriche costo-qualità.** Accuracy o reward devono essere riportati insieme a token, forward, latenza e fallimenti del verifier. Prova: SRC-53-001.

## Prove e artefatti

- riferimento minimo: `code/snip_53_contract.py`; test: `code/test_53_contract.py`; output: `code/outputs/SNIP-53-001.txt`.
- visuali candidate: COMPUTE-01, COMPUTE-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
