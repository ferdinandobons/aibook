# Audit del codice. Capitolo 11

## Stato

- Snippet: `SNIP-KNOW-001`
- Ambiente: Python 3.13.5, standard library, CPU
- Data del run: 31 luglio 2026
- Test: 7 superati
- Esito: **superato**

## Forward chaining

- [x] fatti rappresentati come tuple immutabili;
- [x] variabili riconoscibili dal prefisso `?`;
- [x] matching separato dalla istanziazione;
- [x] stessa sostituzione condivisa tra le premesse;
- [x] iterazione fino a assenza di nuovi fatti;
- [x] fixpoint idempotente;
- [x] nessuna negazione derivata dall'assenza;
- [x] output ordinato soltanto per riproducibilità della stampa.

## Rete bayesiana

- [x] prior e tabelle condizionali espliciti;
- [x] distribuzioni Bernoulli normalizzate;
- [x] congiunta fattorizzata come `P(H)P(M|H)P(T|H)`;
- [x] otto assegnamenti enumerabili;
- [x] somma della congiunta uguale a uno entro precisione floating point;
- [x] posterior normalizzato sui due valori di `H`;
- [x] posterior positivo `0,875` verificato;
- [x] caso con segnali assenti inferiore al prior.

## Coerenza con il testo

- [x] stessi predicati e stesso ordine `order_42`;
- [x] stesse tre regole;
- [x] stesse probabilità;
- [x] stesso posterior;
- [x] nessun claim di causalità derivato dal codice;
- [x] nessun output presentato come misura di produzione.

## Limiti

- il motore tratta soltanto fatti ground e regole positive;
- non implementa negazione, disgiunzione, quantificatori completi o termini funzionali;
- la ricerca delle sostituzioni è esaustiva e non ottimizzata;
- il modello probabilistico è binario e codificato a mano;
- l'indipendenza condizionata è una assunzione del codice;
- non vengono apprese probabilità o struttura;
- non viene misurata la complessità su grafi grandi.

## Verdetto

Il codice sostiene i claim eseguiti e rende visibili due contratti distinti. Una derivazione logica positiva e una inferenza probabilistica per enumerazione. Non viene usato come prova di proprietà più generali.
