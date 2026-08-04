# Piano editoriale. Capitolo 45

## Obiettivo didattico

Seguire **Byte, predizione multi-token e language diffusion** da byte, gerarchia, target e numero di passi a unità predette, loss e durata di decoding, osservando raggruppamento, multi-token prediction o diffusione discreta senza oltrepassare questo limite: granularità della rappresentazione e parallelismo sono assi distinti.

## Prerequisiti reali

- Capitolo 21: Modelli autoregressivi
- Capitolo 26: Il testo come dato
- Capitolo 29: Il Transformer da zero

## Percorso della lezione

1. **Byte e caratteri.** Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe. Prova: SRC-45-001.
2. **Gerarchie di byte.** Patch fisse o dinamiche riducono la lunghezza vista dal modello globale. Prova: SRC-45-002.
3. **Predizione multi-token.** Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato. Prova: SRC-45-003.
4. **Diffusione linguistica.** Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi. Prova: SRC-45-004.
5. **Assi separati.** Unità del testo, architettura e obiettivo di predizione sono scelte distinte che interagiscono. Prova: SRC-45-001.

## Prove e artefatti

- riferimento minimo: `code/snip_45_contract.py`; test: `code/test_45_contract.py`; output: `code/outputs/SNIP-45-001.txt`.
- visuali candidate: ALT-01, ALT-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
