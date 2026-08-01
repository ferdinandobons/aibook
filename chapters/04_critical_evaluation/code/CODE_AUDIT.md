# Audit del codice. Capitolo 4

## Stato

- Snippet: `SNIP-EVAL-001`
- Ambiente: Python 3.13.5, standard library
- Esito: **superato**
- Test: 4/4 superati

## Controlli

- [x] I due modelli vengono valutati sugli stessi esempi.
- [x] Le accuratezze complessive sono `19/24` e `20/24`.
- [x] Il gruppo urgente contiene otto esempi.
- [x] Nel gruppo urgente il modello A ottiene `7/8` e il modello B `5/8`.
- [x] La somma pesata degli errori è `8.0` per A e `13.0` per B.
- [x] Il bootstrap ricampiona gli indici una volta per coppia di predizioni, conservando il confronto appaiato.
- [x] Seed e numero di resample sono registrati.
- [x] Il risultato è deterministico nell'ambiente dichiarato.
- [x] L'intervallo percentile al 95% è `[-0.208, 0.292]` dopo arrotondamento a tre decimali.
- [x] Il testo non presenta l'intervallo come prova di equivalenza.

## Limiti

- dataset piccolo e costruito;
- pesi degli errori illustrativi;
- percentile bootstrap semplice;
- nessun confronto tra run di training;
- nessuna conclusione operativa o causale.

## Verdetto

Il codice è coerente con il perimetro didattico del capitolo e può essere incluso nella candidatura.
