# Piano interno. Capitolo 12

## Identità

- `chapter_id`: `CH-P03-SUPERVISED`
- Parte: `P03`, Apprendimento, ottimizzazione e decisione
- Titolo: **Apprendimento supervisionato**
- Stato: candidatura completa in revisione autoriale
- Versione prevista: `0.2.0-rc1`
- Oggetto continuo: un dataset di richieste etichettate per distinguere casi di consegna urgenti e non urgenti
- Domanda centrale: come si apprende una funzione da coppie input-target e come si valuta se il comportamento generalizza oltre gli esempi di training?

## Contratto di continuità

### Prerequisiti stabili

- distinzione tra modello e sistema, Capitolo 1;
- training, validation, test, baseline e monitoraggio, Capitoli 3 e 4;
- vettori, matrici, layer lineare e shape, Capitolo 5;
- gradienti e optimizer step, Capitolo 6;
- campione, popolazione, probabilità e likelihood, Capitolo 7;
- logits, cross-entropy e rischio empirico, Capitolo 8;
- dtype, stabilità e riproducibilità numerica, Capitolo 9;
- regole e probabilità specificate direttamente, Capitolo 11.

### Concetti richiamati ma rispiegati localmente

- logistic regression;
- binary cross-entropy;
- precision, recall e confusion matrix;
- regolarizzazione L2;
- early stopping;
- bias e varianza nel perimetro introduttivo.

### Forward reference non necessarie alla comprensione

- calibration avanzata e conformal prediction;
- apprendimento auto-supervisionato;
- causal inference;
- online learning e distributed training.

### Gap che apre il capitolo

Nel Capitolo 11 fatti, regole e probabilità erano dichiarati direttamente. Qui manca un metodo per apprendere una funzione da esempi etichettati e per stimarne il comportamento su casi non usati nell'update.

### Output consegnato al capitolo successivo

Un protocollo supervisionato completo, con input, target, loss, modello, split, soglia, metriche e controllo delle slice. Il Capitolo 13 rimuoverà la disponibilità di una label esterna per ogni esempio e studierà obiettivi non supervisionati e auto-supervisionati.

## Progressione

1. Coppie `(x,y)` e processo che produce le label.
2. Classificazione e regressione.
3. Predittore, loss, rischio empirico e rischio atteso.
4. Baseline prima del modello complesso.
5. Logistic regression come caso base.
6. Train, validation e test come protocollo.
7. Soglia di decisione, costi e metriche.
8. Generalizzazione e overfitting.
9. Bias, varianza, rumore, regolarizzazione ed early stopping.
10. Alberi, margini ed ensemble come famiglie alternative.
11. Dati sbilanciati, pesi, resampling e soglia.
12. Metriche per slice e shift tra training e uso reale.
13. PyTorch, codice e test.
14. Ponte verso apprendimento non supervisionato e auto-supervisionato.

## Oggetto numerico

```text
feature 1: segnale di ritardo osservabile
feature 2: segnale linguistico di urgenza
target: caso urgente, 0 o 1
slice di audit: tracking disponibile oppure tracking mancante

train: 120 esempi
validation: 50 esempi
test: 50 esempi

costo illustrativo:
falso negativo = 5
falso positivo = 1
```

Il dataset è sintetico e non descrive un servizio reale.

## Codice

### `SNIP-SUP-001`

- dataset sintetico con split già fissati;
- baseline della classe maggioritaria;
- logistic regression `nn.Linear(2,1)` in float64;
- binary cross-entropy con logits e penalità L2;
- training soltanto sul train set;
- scelta della soglia soltanto sulla validation;
- test usato dopo la selezione;
- metriche complessive e per slice;
- confronto con soglia predefinita `0,50`;
- otto test automatici.

## Visuali

### `SUP-01`. Dal dataset al risultato di test

Mostra due flussi separati:

```text
train -> loss e optimizer -> parametri
validation + parametri -> soglia
parametri + soglia -> test finale
```

Il test non deve apparire come sorgente di parametri, soglia o regolarizzazione.

### `SUP-02`. Stessa accuracy, errori diversi

Confronta le confusion matrix delle soglie `0,30` e `0,50`, entrambe con accuracy `0,900`, ma con costo illustrativo `13` e `21`. La fascia inferiore separa le slice con tracking disponibile e mancante.

## Gate specifici

- target osservato distinto dal concetto reale;
- training error distinto da generalization error;
- test set non usato per selezionare modello o soglia;
- accuracy non trattata come metrica universale;
- overfitting non spiegato soltanto attraverso il numero di parametri;
- bias-varianza presentata nel perimetro statistico corretto;
- class weight, resampling e soglia distinti;
- soglia descritta come parte della decisione, non del training dei parametri;
- baseline confrontata sullo stesso test;
- metriche aggregate accompagnate da slice pertinenti;
- nessun benchmark sintetico presentato come risultato reale;
- ponte a Capitolo 13 esplicito, senza anticiparne il meccanismo.
