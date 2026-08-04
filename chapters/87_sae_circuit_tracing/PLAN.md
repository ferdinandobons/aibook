# Piano editoriale. Capitolo 87

## Obiettivo didattico

Seguire **Sparse autoencoder e interpretabilità scalabile** da attivazione, dizionario, sparsità e ricostruzione a feature, errore di ricostruzione e circuito candidato, osservando training SAE, splitting, dead features e tracing senza oltrepassare questo limite: interpretabilità di una feature richiede valutazione e controlli indipendenti.

## Prerequisiti reali

- Capitolo 19: Representation learning
- Capitolo 86: Interpretabilità delle rappresentazioni e dei circuiti

## Percorso della lezione

1. **Superposition.** Più feature possono condividere le stesse dimensioni di attivazione. La sparsità offre una ipotesi per separarle. Prova: SRC-87-001.
2. **Sparse autoencoder.** Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream. Loss e sparsity coefficient determinano il dizionario. Prova: SRC-87-002.
3. **Dead e splitting features.** Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità. Prova: SRC-87-003.
4. **Circuit tracing.** Feature e attribution graph possono collegare input, computazione e output. Il grafo resta una approssimazione del calcolo completo. Prova: SRC-87-004.
5. **Valutazione.** Interpretabilità automatica, causal intervention e coverage devono essere misurate. Una etichetta leggibile non prova monosemanticità universale. Prova: SRC-87-001.

## Prove e artefatti

- riferimento minimo: `code/snip_87_contract.py`; test: `code/test_87_contract.py`; output: `code/outputs/SNIP-87-001.txt`.
- visuali candidate: TRACING-01, TRACING-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
