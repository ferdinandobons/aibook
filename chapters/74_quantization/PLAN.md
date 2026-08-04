# Piano editoriale. Capitolo 74

## Obiettivo didattico

Seguire **Quantizzazione** da valori, scale, zero-point, dtype e calibrazione a codici, tensore ricostruito, errore e memoria, osservando PTQ, QAT, weight-only o activation quantization senza oltrepassare questo limite: scala e dominio di calibrazione fanno parte del risultato.

## Prerequisiti reali

- Capitolo 9: Calcolo numerico, precisione e hardware
- Capitolo 73: Distillazione e pruning

## Percorso della lezione

1. **Scala e zero point.** Una mappa affine converte valori floating point in interi. La granularità per tensor o per channel cambia scale, errore e metadati. Prova: SRC-74-001.
2. **PTQ.** Post-training quantization usa calibration senza riaddestrare completamente. La rappresentatività dei dati di calibration è essenziale. Prova: SRC-74-002.
3. **QAT.** Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi. Prova: SRC-74-001.
4. **Weight-only e activation quantization.** Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo. Prova: SRC-74-003; SRC-74-002.
5. **Metodi per LLM.** GPTQ, AWQ e SmoothQuant ottimizzano oggetti differenti: ricostruzione, canali salienti e outlier delle attivazioni. I loro contratti non sono intercambiabili. Prova: SRC-74-004; SRC-74-003; SRC-74-002.

## Prove e artefatti

- riferimento minimo: `code/snip_74_contract.py`; test: `code/test_74_contract.py`; output: `code/outputs/SNIP-74-001.txt`.
- visuali candidate: QUANTIZATI-01, QUANTIZATI-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
