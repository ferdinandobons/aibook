# Piano editoriale. Capitolo 38

## Obiettivo didattico

Seguire **Posizione e contesto lungo** da query, key e indice di posizione a score dipendente dalla posizione, osservando posizione assoluta, relativa, RoPE o bias senza oltrepassare questo limite: estendere il contesto richiede una misura fuori dalla lunghezza addestrata.

## Prerequisiti reali

- Capitolo 27: Embedding e spazio semantico
- Capitolo 28: Il meccanismo di attention
- Capitolo 29: Il Transformer da zero

## Percorso della lezione

1. **Posizione assoluta.** Embedding appresi o sinusoidali aggiungono un segnale legato all'indice. Prova: SRC-38-001.
2. **Posizione relativa.** Bias o rappresentazioni relative modificano i confronti in funzione della distanza. Prova: SRC-38-002.
3. **RoPE.** Rotazioni di query e key rendono il prodotto scalare dipendente dall'offset relativo. Prova: SRC-38-003.
4. **ALiBi.** Bias lineari penalizzano distanze maggiori con slope per head. Prova: SRC-38-004.
5. **Estensione e valutazione.** Positional interpolation e metodi affini estendono gli indici, ma l'uso effettivo del contesto deve essere misurato. Prova: SRC-38-001.

## Prove e artefatti

- riferimento minimo: `code/snip_38_contract.py`; test: `code/test_38_contract.py`; output: `code/outputs/SNIP-38-001.txt`.
- visuali candidate: POS-01, POS-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
