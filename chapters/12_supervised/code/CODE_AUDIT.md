# Audit del codice. Capitolo 12

## Stato

- Snippet: `SNIP-SUP-001`
- Ambiente: Python 3.13.5, PyTorch 2.10.0+cpu, CPU
- Test: 8 superati
- Data: 31 luglio 2026
- Esito: **superato**

## Dataset sintetico

- [x] generatori e seed espliciti;
- [x] train, validation e test creati separatamente;
- [x] shape `[N,2]` controllate;
- [x] target binari;
- [x] slice separata dalle feature del modello;
- [x] natura illustrativa dichiarata.

## Training

- [x] `nn.Linear(2,1)` in float64 per il toy example;
- [x] `binary_cross_entropy_with_logits` applicata ai logits;
- [x] penalità L2 esplicita;
- [x] Adam usato senza claim comparativo;
- [x] obiettivo iniziale e finale registrati;
- [x] probabilità ottenute in `inference_mode`.

## Selezione e valutazione

- [x] 17 soglie candidate da `0,10` a `0,90`;
- [x] criterio principale: costo pesato sulla validation;
- [x] tie-break dichiarato su F1 e soglia;
- [x] test escluso dalla selezione;
- [x] soglia selezionata e soglia `0,50` valutate sullo stesso test;
- [x] baseline maggioritaria ricavata soltanto dal training;
- [x] metriche per slice con denominatori espliciti.

## Test automatici

- [x] shape degli split;
- [x] riduzione dell'obiettivo;
- [x] probabilità valide;
- [x] selezione indipendente dal test;
- [x] riduzione del costo sulla validation;
- [x] confronto del costo sul test nel caso fissato;
- [x] ricostruzione del test dalle slice;
- [x] comportamento della baseline maggioritaria.

## Limiti

- dataset piccolo e sintetico;
- un solo seed di training;
- nessuna stima di calibrazione;
- nessun confronto con alberi, SVM o ensemble;
- nessun benchmark di velocità;
- la soglia ottima dipende dai costi e dalla validation fissata;
- il test del toy example non sostiene generalizzazioni su sistemi reali.

## Verdetto

Il codice rende osservabili i contratti discussi nel testo e sostiene soltanto i claim numerici registrati. Le condizioni sperimentali sono separate dalla documentazione PyTorch stable consultata.
