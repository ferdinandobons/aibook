# Audit del testo. Capitolo 8

## Stato

- Versione: `0.2.0-rc1`
- Data: 31 luglio 2026
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato dopo seconda lettura**
- Gate anti-template: **superato**
- Esito editoriale e linguistico: **superato**
- Chiarezza per lettore non esperto: **superata**
- Codice: sette test registrati
- Visuali: validate tecnicamente
- Revisione autoriale: aperta

## Prima lettura critica

Difetti corretti:

1. self-information ed entropia rischiavano di essere interpretate come significato semantico;
2. entropia, cross-entropy e KL comparivano troppo vicine;
3. la KL poteva essere letta come distanza simmetrica;
4. il passaggio dalla likelihood alla NLL richiedeva il dataset esplicito;
5. logits e probabilità dovevano essere separati prima della softmax;
6. il confronto corretto/errato doveva mantenere la stessa entropia;
7. il gradiente `p-q` richiedeva una spiegazione operativa;
8. la stabilità numerica doveva precedere i dettagli API;
9. target soft e label smoothing richiedevano un confine sui target non validi;
10. MSE e L1 non potevano essere collegate a likelihood senza dichiarare varianza o scala fissata;
11. `KLDivLoss` richiedeva la distinzione tra `mean` e `batchmean`;
12. la prima visuale usava il punto decimale invece della virgola italiana.

Correzioni:

- aggiunti limiti semantici alla self-information;
- costruita la sequenza entropia, cross-entropy, KL;
- dichiarata asimmetria della KL;
- esplicitata la likelihood del dataset;
- introdotti logits prima della softmax;
- usate distribuzioni permutate nel confronto;
- collegato il gradiente alle direzioni dei logits;
- separata la stabilità dalle API;
- marcati i vincoli dei target probabilistici;
- aggiunte condizioni ai collegamenti con MSE e L1;
- verificato `batchmean` sulla documentazione;
- uniformati i decimali nelle visuali.

## Seconda lettura integrale

### Lettore non esperto

- [x] parte da un classificatore concreto;
- [x] self-information spiegata prima della formula di entropia;
- [x] bit e nat dichiarati;
- [x] target e predizione restano visibili;
- [x] NLL costruita dalla probabilità della classe osservata;
- [x] logits distinti dalle probabilità;
- [x] previsione errata confrontata con lo stesso target;
- [x] codice dopo il meccanismo.

### Lettore tecnico

- [x] entropia congiunta e condizionata coerenti;
- [x] mutua informazione espressa come KL;
- [x] decomposizione della cross-entropy corretta;
- [x] KL non trattata come metrica;
- [x] gradiente `p-q` corretto;
- [x] invarianza della softmax a una costante comune;
- [x] log-sum-exp e stabilità corretti;
- [x] riduzioni e contratti PyTorch controllati;
- [x] MSE e L1 collegate a modelli con condizioni esplicite.

## Audit numerico

- [x] probabilità `[0,785597; 0,175290; 0,039113]`;
- [x] NLL corretta `0,241311`;
- [x] entropia predittiva `0,621585`;
- [x] `H(q)=0,394398`;
- [x] `KL(q||p)=0,071914`;
- [x] `H(q,p)=0,466311`;
- [x] gradiente `[-0,214403; 0,175290; 0,039113]`;
- [x] loss errata `3,241311`;
- [x] log-softmax stabile `[-0,4076; -1,4076; -2,4076]`.

## Audit fattuale e temporale

- [x] Shannon e Cover e Thomas per le definizioni;
- [x] Goodfellow, Murphy e MacKay per i collegamenti al learning;
- [x] scoring rule ricontrollata su Gneiting e Raftery;
- [x] PyTorch stable 2.13 controllata il 31 luglio 2026;
- [x] ambiente eseguito distinto dalla documentazione.

## Audit linguistico

- [x] italiano scritto direttamente;
- [x] nessun em dash;
- [x] termini inglesi introdotti nel punto d'uso;
- [x] formule accompagnate da una lettura in prosa;
- [x] nessuna sequenza di microsezioni schematiche;
- [x] lettura ad alta voce superata internamente.

## Verdetto

Il testo `0.2.0-rc1` supera i gate fattuali, matematici, didattici, anti-template, editoriali, linguistici e di accessibilità. Può essere sottoposto alla revisione autoriale.
