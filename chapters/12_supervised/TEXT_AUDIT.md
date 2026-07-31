# Audit del testo. Capitolo 12

## Stato

- Versione: `0.2.0-rc1`
- Data: 31 luglio 2026
- Esito fattuale: **superato**
- Esito matematico: **superato**
- Esito algoritmico: **superato**
- Esito didattico: **superato dopo seconda lettura**
- Gate anti-template: **superato**
- Esito editoriale e linguistico: **superato**
- Chiarezza per lettore non esperto: **superata**
- Codice: otto test registrati
- Visuali: validate tecnicamente dopo due iterazioni
- Revisione autoriale: aperta

## Audit di continuità

### Prerequisiti realmente usati

- Capitolo 3: ruoli di train, validation e test;
- Capitolo 4: baseline, slice, costo e test separato;
- Capitolo 5: vettori, layer lineare e shape;
- Capitolo 6: gradienti e optimizer step;
- Capitolo 7: campione, distribuzione e stima;
- Capitolo 8: logits e cross-entropy;
- Capitolo 9: stabilità numerica e dtype;
- Capitolo 11: differenza tra regole specificate e quantità stimate.

Ogni prerequisito viene richiamato in prosa prima dell'uso. Il capitolo non presume che il lettore ricordi formule non ripetute.

### Ponte in ingresso

Il capitolo parte dal limite del Capitolo 11: fatti, regole e probabilità erano specificati direttamente. Introduce quindi l'apprendimento da coppie input-target come capacità mancante.

### Ponte in uscita

Il riepilogo prepara il Capitolo 13 rimuovendo la label esterna e anticipando, senza spiegarli ancora, apprendimento non supervisionato e auto-supervisionato.

## Prima lettura critica

Difetti trovati e corretti:

1. il target rischiava di essere presentato come verità invece che come osservazione prodotta da una procedura;
2. rischio empirico e generalizzazione erano troppo vicini e potevano sembrare equivalenti;
3. la soglia `0,50` poteva essere letta come proprietà obbligatoria della logistic regression;
4. la frontiera decisionale con soglia generica non era esplicitata;
5. train, validation e test rischiavano di diventare una checklist invece di un protocollo causale;
6. la penalità L2 poteva essere confusa con una modifica delle label;
7. bias-varianza rischiava di essere generalizzata oltre la loss quadratica;
8. class weight, resampling e soglia dovevano essere separati;
9. le famiglie alternative rischiavano di trasformare la sezione in una rassegna enciclopedica;
10. la slice con 16 casi richiedeva un limite sulla precisione della stima;
11. il confronto tra soglie richiedeva i pesi del costo direttamente nella visuale;
12. `SUP-01` doveva mostrare che il modello appreso viene usato anche su validation e test.

## Correzioni applicate

- target distinto dal concetto reale;
- rischio atteso separato dal rischio empirico;
- formula della frontiera per soglia generica;
- baseline introdotta prima del risultato del modello;
- split spiegati attraverso il flusso delle decisioni;
- L2 descritta come parte dell'obiettivo;
- condizioni della decomposizione bias-varianza dichiarate;
- interventi sull'imbalance separati per punto di applicazione;
- SVM, random forest e boosting ridotti a famiglie con contratto essenziale;
- denominatori delle slice mantenuti visibili;
- costi `FN=5`, `FP=1` aggiunti a `SUP-02`;
- collegamenti verticali aggiunti a `SUP-01`.

## Seconda lettura integrale

### Lettore non esperto

- [x] parte da un dataset concreto;
- [x] input e target introdotti prima delle formule;
- [x] classificazione e regressione distinte con esempi;
- [x] rischio empirico tradotto in media della loss;
- [x] generalizzazione spiegata come comportamento su casi non usati;
- [x] baseline comprensibile;
- [x] logistic regression costruita da logit e sigmoide;
- [x] soglia separata dal training;
- [x] confusion matrix attraversata nel testo;
- [x] codice dopo il meccanismo.

### Lettore tecnico

- [x] formule e simboli coerenti;
- [x] frontiera per soglia generica corretta;
- [x] BCE applicata ai logits;
- [x] regolarizzazione L2 esplicita;
- [x] selezione della soglia esclusivamente sulla validation;
- [x] metriche ricostruibili dai conteggi;
- [x] costi ricostruibili;
- [x] claim su bias-varianza limitati;
- [x] fonti delle famiglie alternative pertinenti;
- [x] API stable distinta dall'ambiente eseguito.

### Lettore che riprende il capitolo

- [x] sezioni organizzate per problema;
- [x] formule principali localizzabili;
- [x] visuali riassuntive senza sostituire la prosa;
- [x] riepilogo ricostruisce dataset, training, selezione e test;
- [x] ponte al capitolo successivo esplicito.

## Audit numerico

- [x] objective `0,778276 -> 0,313711`;
- [x] soglia validation `0,30`;
- [x] validation `TP=16`, `TN=27`, `FP=6`, `FN=1`, costo `11`;
- [x] test soglia `0,30`: `TP=21`, `TN=24`, `FP=3`, `FN=2`, costo `13`;
- [x] test soglia `0,50`: `TP=19`, `TN=26`, `FP=1`, `FN=4`, costo `21`;
- [x] entrambe le accuracy `0,900`;
- [x] baseline accuracy `0,540`, recall `0`, costo `115`;
- [x] slice `34+16=50`;
- [x] otto test superati.

## Audit linguistico

- [x] italiano scritto direttamente;
- [x] nessun em dash;
- [x] paragrafi causali, non moduli ripetuti;
- [x] termini inglesi introdotti nel punto d'uso;
- [x] nessuna metafora portante;
- [x] cautele non duplicate senza funzione;
- [x] lettura ad alta voce superata internamente.

## Verdetto

Il capitolo supera i gate fattuali, matematici, algoritmici, didattici, anti-template, editoriali, linguistici, visuali e di continuità. Può essere sottoposto alla revisione autoriale.
