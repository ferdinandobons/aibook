# Piano editoriale. Capitolo 40

## Obiettivo didattico

Seguire **Attention hardware-aware** da tile di Q, K, V, dtype e device a stesso contratto matematico con memoria e latenza misurate, osservando tiling, softmax online e ricomputazione senza oltrepassare questo limite: una misura hardware dipende da shape, backend e precisione.

## Prerequisiti reali

- Capitolo 9: Calcolo numerico, precisione e hardware
- Capitolo 28: Il meccanismo di attention
- Capitolo 39: Varianti dell'attention e gestione KV

## Percorso della lezione

1. **FLOP e movimento dei dati.** Lo stesso operatore può avere traffico di memoria molto diverso. Prova: SRC-40-001.
2. **Tiling.** Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score. Prova: SRC-40-002.
3. **Softmax online.** Massimo, denominatore e numeratore vengono aggiornati blocco per blocco. Prova: SRC-40-003.
4. **Backward e ricomputazione.** Salvare meno intermedi scambia memoria con compute aggiuntivo. Prova: SRC-40-004.
5. **Backend.** FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse. Prova: SRC-40-001.

## Prove e artefatti

- riferimento minimo: `code/snip_40_contract.py`; test: `code/test_40_contract.py`; output: `code/outputs/SNIP-40-001.txt`.
- visuali candidate: FLASH-01, FLASH-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
