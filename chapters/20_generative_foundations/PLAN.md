# Piano interno. Capitolo 20

- Domanda centrale: quale contratto costruisce Fondamenti della modellazione generativa?
- Oggetto continuo: una distribuzione sui dati o su una variabile latente; input guida: un dato x, un rumore epsilon o una variabile z.
- Prerequisito stabile: Capitolo 19, Representation learning.
- Gap: valutazione di likelihood, trasformazione o campionamento.
- Output consegnato: una probabilità, un punteggio o un campione; consumer successivo: Capitolo 21, Modelli autoregressivi.
- Invariante principale: un campione plausibile non dimostra copertura dell'intera distribuzione.
- Visuali: FOUNDATI-01 e FOUNDATI-02, con famiglie compositive variabili.
- Snippet: code/snip_20_contract.py; output: code/outputs/SNIP-20-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Imparare una distribuzione

- Ultima affermazione stabile: una distribuzione sui dati o su una variabile latente.
- Concetto nuovo: Un modello generativo descrive o campiona dati secondo una distribuzione. Densità, likelihood e sampling sono contratti distinti.
- Input e shape: un dato x, un rumore epsilon o una variabile z.
- Operazione: valutazione di likelihood, trasformazione o campionamento.
- Output e shape: una probabilità, un punteggio o un campione.
- Che cosa cambia: il passaggio specifico di «Imparare una distribuzione».
- Invariante: un campione plausibile non dimostra copertura dell'intera distribuzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre probabilità che sommano a 1 prima della selezione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Modelli espliciti e impliciti.
- Prova: SRC-20-001 e sezione pubblica corrispondente.

## Transizione 2. Modelli espliciti e impliciti

- Ultima affermazione stabile: una distribuzione sui dati o su una variabile latente.
- Concetto nuovo: Un modello esplicito assegna una densità o probabilità valutabile. Un modello implicito definisce il campionamento senza una likelihood semplice.
- Input e shape: un dato x, un rumore epsilon o una variabile z.
- Operazione: valutazione di likelihood, trasformazione o campionamento.
- Output e shape: una probabilità, un punteggio o un campione.
- Che cosa cambia: il passaggio specifico di «Modelli espliciti e impliciti».
- Invariante: un campione plausibile non dimostra copertura dell'intera distribuzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre probabilità che sommano a 1 prima della selezione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Variabili latenti.
- Prova: SRC-20-002 e sezione pubblica corrispondente.

## Transizione 3. Variabili latenti

- Ultima affermazione stabile: una distribuzione sui dati o su una variabile latente.
- Concetto nuovo: Una variabile latente introduce struttura non osservata. L'inferenza deve collegare dati e latenti, esattamente o mediante approssimazione.
- Input e shape: un dato x, un rumore epsilon o una variabile z.
- Operazione: valutazione di likelihood, trasformazione o campionamento.
- Output e shape: una probabilità, un punteggio o un campione.
- Che cosa cambia: il passaggio specifico di «Variabili latenti».
- Invariante: un campione plausibile non dimostra copertura dell'intera distribuzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre probabilità che sommano a 1 prima della selezione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Energy-based model.
- Prova: SRC-20-003 e sezione pubblica corrispondente.

## Transizione 4. Energy-based model

- Ultima affermazione stabile: una distribuzione sui dati o su una variabile latente.
- Concetto nuovo: Una energia non normalizzata assegna punteggi alle configurazioni. La costante di partizione rende difficile la likelihood in molti casi.
- Input e shape: un dato x, un rumore epsilon o una variabile z.
- Operazione: valutazione di likelihood, trasformazione o campionamento.
- Output e shape: una probabilità, un punteggio o un campione.
- Che cosa cambia: il passaggio specifico di «Energy-based model».
- Invariante: un campione plausibile non dimostra copertura dell'intera distribuzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre probabilità che sommano a 1 prima della selezione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Qualità, copertura e valutazione.
- Prova: SRC-20-004 e sezione pubblica corrispondente.

## Transizione 5. Qualità, copertura e valutazione

- Ultima affermazione stabile: una distribuzione sui dati o su una variabile latente.
- Concetto nuovo: Campioni plausibili non garantiscono copertura. Likelihood, precision-recall generativa e valutazione umana rispondono a domande diverse.
- Input e shape: un dato x, un rumore epsilon o una variabile z.
- Operazione: valutazione di likelihood, trasformazione o campionamento.
- Output e shape: una probabilità, un punteggio o un campione.
- Che cosa cambia: il passaggio specifico di «Qualità, copertura e valutazione».
- Invariante: un campione plausibile non dimostra copertura dell'intera distribuzione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre probabilità che sommano a 1 prima della selezione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Modelli autoregressivi.
- Prova: SRC-20-001 e sezione pubblica corrispondente.
