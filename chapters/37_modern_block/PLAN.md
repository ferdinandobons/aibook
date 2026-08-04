# Piano editoriale. Capitolo 37

## Obiettivo didattico

Seguire **Anatomia del blocco moderno** da h di shape [batch, length, d] e norma misurata a h' con shape preservata e statistiche confrontabili, osservando norm, attention, MLP e gating nell'ordine scelto senza oltrepassare questo limite: ordine dei sottolayer e shape sono parte del blocco.

## Prerequisiti reali

- Capitolo 16: Addestrare reti profonde
- Capitolo 29: Il Transformer da zero

## Percorso della lezione

1. **Residual stream.** Ogni sottolayer produce un aggiornamento sommato a un percorso identità. Prova: SRC-37-001.
2. **Pre-norm e post-norm.** La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco. Prova: SRC-37-002.
3. **RMSNorm.** RMSNorm scala usando la media quadratica e non sottrae la media. Prova: SRC-37-003.
4. **SwiGLU.** Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down. Prova: SRC-37-004.
5. **Ordine e parallelismo.** Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine. Prova: SRC-37-001.

## Prove e artefatti

- riferimento minimo: `code/snip_37_contract.py`; test: `code/test_37_contract.py`; output: `code/outputs/SNIP-37-001.txt`.
- visuali candidate: BLOCK-01, BLOCK-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
