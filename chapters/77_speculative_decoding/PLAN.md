# Piano editoriale. Capitolo 77

## Obiettivo didattico

Seguire **Speculative e parallel decoding** da token proposti, logits draft e logits target a token accettati, velocità e distribuzione preservata, osservando proposta, verifica, accettazione e fallback senza oltrepassare questo limite: lo speedup richiede verifica senza cambiare il contratto di output.

## Prerequisiti reali

- Capitolo 76: Decoding e generazione vincolata

## Percorso della lezione

1. **Draft e target.** Un modello economico propone più token; il modello target li verifica in parallelo. Prova: SRC-77-001.
2. **Acceptance.** La regola di accettazione conserva esattamente la distribuzione target nel metodo speculativo standard. Prova: SRC-77-002.
3. **Speedup.** Il guadagno dipende da acceptance rate, costo del draft, lunghezza proposta e hardware. Prova: SRC-77-003.
4. **Medusa, EAGLE e ReDrafter.** Head multiple, feature prediction e recurrent drafter producono candidate con strutture differenti. Prova: SRC-77-004.
5. **Parallel decoding.** Metodi lookahead o Jacobi aggiornano più posizioni ma devono dichiarare se preservano esattamente la distribuzione originale. Prova: SRC-77-001.

## Prove e artefatti

- riferimento minimo: `code/snip_77_contract.py`; test: `code/test_77_contract.py`; output: `code/outputs/SNIP-77-001.txt`.
- visuali candidate: DECODING-01, DECODING-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
