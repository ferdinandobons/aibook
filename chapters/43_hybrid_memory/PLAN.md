# Piano editoriale. Capitolo 43

## Obiettivo didattico

Seguire **Architetture ibride e memoria interna** da segmento corrente, stato e memoria persistente a stato aggiornato e contenuto recuperato, osservando write, read, routing e fusione senza oltrepassare questo limite: durata e provenienza della memoria devono essere separate.

## Prerequisiti reali

- Capitolo 29: Il Transformer da zero
- Capitolo 39: Varianti dell'attention e gestione KV
- Capitolo 42: State-space model, recurrence e long convolution

## Percorso della lezione

1. **Ibridi tra layer.** Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati. Prova: SRC-43-001.
2. **Attention locale e stato.** Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre la finestra. Prova: SRC-43-002.
3. **Memoria segmentale.** Stati di segmenti precedenti possono essere riusati o compressi con stop-gradient e capacità limitata. Prova: SRC-43-003.
4. **Memoria associativa.** Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream. Prova: SRC-43-004.
5. **Memoria interna ed esterna.** Lo stato neurale non coincide con retrieval documentale. Reset, isolamento e provenienza hanno contratti differenti. Prova: SRC-43-001.

## Prove e artefatti

- riferimento minimo: `code/snip_43_contract.py`; test: `code/test_43_contract.py`; output: `code/outputs/SNIP-43-001.txt`.
- visuali candidate: HYBRID-01, HYBRID-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
