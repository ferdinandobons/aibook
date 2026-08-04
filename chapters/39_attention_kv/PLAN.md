# Piano editoriale. Capitolo 39

## Obiettivo didattico

Seguire **Varianti dell'attention e gestione KV** da Q con h_q teste e KV con h_kv teste a score, cache e pattern di comunicazione, osservando MHA, MQA, GQA, località o sparsità senza oltrepassare questo limite: raggruppamento delle teste e costo della KV cache restano espliciti.

## Prerequisiti reali

- Capitolo 28: Il meccanismo di attention
- Capitolo 37: Anatomia del blocco moderno

## Percorso della lezione

1. **MHA.** Ogni query head possiede key e value dedicate. Prova: SRC-39-001.
2. **MQA.** Tutte le query head condividono una singola coppia key-value, riducendo la cache. Prova: SRC-39-002.
3. **GQA.** Gruppi di query head condividono un numero intermedio di KV head. Prova: SRC-39-003.
4. **Local e sparse attention.** Finestre e pattern selezionati riducono le coppie ma cambiano la connettività. Prova: SRC-39-004.
5. **MLA e cache.** Compressione latente e numero di KV head sono strategie differenti. La memoria dipende anche da layer, dtype, batch e lunghezza. Prova: SRC-39-001.

## Prove e artefatti

- riferimento minimo: `code/snip_39_contract.py`; test: `code/test_39_contract.py`; output: `code/outputs/SNIP-39-001.txt`.
- visuali candidate: KV-01, KV-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
