# Piano editoriale. Capitolo 20

## Obiettivo didattico

Seguire **Fondamenti della modellazione generativa** da un dato x, un rumore epsilon o una variabile z a una probabilità, un punteggio o un campione, osservando valutazione di likelihood, trasformazione o campionamento senza oltrepassare questo limite: un campione plausibile non dimostra copertura dell'intera distribuzione.

## Prerequisiti reali

- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 8: Teoria dell'informazione e funzioni obiettivo
- Capitolo 13: Apprendimento non supervisionato e auto-supervisionato
- Capitolo 19: Representation learning

## Percorso della lezione

1. **Imparare una distribuzione.** Un modello generativo descrive o campiona dati secondo una distribuzione. Densità, likelihood e sampling sono contratti distinti. Prova: SRC-20-001.
2. **Modelli espliciti e impliciti.** Un modello esplicito assegna una densità o probabilità valutabile. Un modello implicito definisce il campionamento senza una likelihood semplice. Prova: SRC-20-002.
3. **Variabili latenti.** Una variabile latente introduce struttura non osservata. L'inferenza deve collegare dati e latenti, esattamente o mediante approssimazione. Prova: SRC-20-003.
4. **Energy-based model.** Una energia non normalizzata assegna punteggi alle configurazioni. La costante di partizione rende difficile la likelihood in molti casi. Prova: SRC-20-004.
5. **Qualità, copertura e valutazione.** Campioni plausibili non garantiscono copertura. Likelihood e precision-recall generativa rispondono a domande diverse e richiedono protocolli dichiarati. Prova: SRC-20-005.

## Prove e artefatti

- eccezione motivata: Il capitolo confronta famiglie generative a livello concettuale; le implementazioni verificabili sono distribuite nei capitoli 21-25.
- visuali candidate: FOUNDATI-01, FOUNDATI-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
