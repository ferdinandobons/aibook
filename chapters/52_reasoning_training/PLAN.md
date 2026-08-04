# Piano editoriale. Capitolo 52

## Obiettivo didattico

Seguire **Addestrare e distillare il reasoning** da prompt, trace del teacher, answer e costo in token a traccia selezionata, risposta e misura di costo, osservando distillazione, self-consistency e rejection sampling senza oltrepassare questo limite: una traccia leggibile non prova faithfulness causale.

## Prerequisiti reali

- Capitolo 46: Supervised fine-tuning e instruction tuning
- Capitolo 50: Process supervision, outcome supervision e verifier
- Capitolo 51: Reinforcement learning con reward verificabili

## Percorso della lezione

1. **Tracce e risposte.** Una traccia di ragionamento è testo prodotto dal modello. Può aiutare il training senza costituire una prova fedele del processo interno. Prova: SRC-52-001.
2. **Distillazione.** Un teacher produce soluzioni o distribuzioni che diventano target per uno student. Filtraggio e copertura stabiliscono cosa viene trasferito. Prova: SRC-52-004.
3. **Self-consistency e rejection sampling.** Più candidate vengono generate e selezionate con voto o verifier. Il dataset risultante dipende dalla procedura di selezione. Prova: SRC-52-002.
4. **Faithfulness.** Una spiegazione corretta può essere post-hoc. Valutare risposta e fedeltà richiede esperimenti differenti. Prova: SRC-52-003.
5. **Costo e lunghezza.** Tracce più lunghe aumentano token e latenza. Il training deve distinguere utilità della risposta e budget del processo. Prova: SRC-52-001.

## Prove e artefatti

- riferimento minimo: `code/snip_52_contract.py`; test: `code/test_52_contract.py`; output: `code/outputs/SNIP-52-001.txt`.
- visuali candidate: TRAINING-01, TRAINING-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
