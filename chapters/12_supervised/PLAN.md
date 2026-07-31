# Piano interno. Capitolo 12

## Identità

- `chapter_id`: `CH-P03-SUPERVISED`
- Parte: `P03`, Apprendimento, ottimizzazione e decisione
- Titolo: **Apprendimento supervisionato**
- Stato: `research`
- Oggetto continuo: un dataset di richieste etichettate per distinguere casi di consegna urgenti e non urgenti
- Domanda centrale: come si apprende una funzione da coppie input-target e come si valuta se il comportamento generalizza oltre gli esempi di training?

## Progressione prevista

1. Coppie `(x,y)` e funzione obiettivo.
2. Classificazione e regressione.
3. Predittore, loss e rischio empirico.
4. Baseline e split.
5. Modello lineare e logistic regression.
6. Decision boundary e soglia.
7. Generalizzazione e overfitting.
8. Bias, varianza e rumore.
9. Regolarizzazione ed early stopping.
10. Alberi, margini ed ensemble come famiglie alternative.
11. Dati sbilanciati, pesi e metriche.
12. Shift tra training e uso reale.
13. PyTorch, codice e test.

## Visuali previste

- `SUP-01`: dal dataset alla funzione appresa, con confine tra training, validation e test;
- `SUP-02`: stessa accuracy media, errori diversi tra slice e costi differenti.

## Codice previsto

- classificatore logistico PyTorch su dataset sintetico;
- baseline maggioritaria;
- scelta della soglia sulla validation;
- test usato dopo la selezione;
- regolarizzazione L2;
- metriche complessive e per slice;
- test automatici.

## Gate specifici

- target osservato distinto dal concetto reale;
- training error distinto da generalization error;
- test set non usato per selezionare il modello;
- accuracy non trattata come metrica universale;
- overfitting non spiegato soltanto attraverso il numero di parametri;
- bias-varianza presentata nel perimetro statistico corretto;
- class weight, resampling e soglia distinti;
- nessun benchmark sintetico presentato come risultato reale.
