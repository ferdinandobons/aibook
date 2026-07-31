# Guida alla revisione. Capitolo 7

## Versione

- `chapter_id`: `CH-P02-PROBABILITY`
- Versione: `0.2.0-rc1`
- Stato: candidatura completa in revisione autoriale
- Codice: sei test registrati
- Visuali: validate tecnicamente

## Percorso consigliato

1. `CHAPTER.md`;
2. `PROB-01/candidate-v1.png`;
3. `PROB-02/candidate-v1.png`;
4. `code/snip_prob_001_bayes_sampling.py`;
5. output e test;
6. `CLAIMS.md`;
7. `FONTI_PRIMARIE.md`;
8. `TEXT_AUDIT.md`.

## Aspetti da valutare

- Il passaggio da incertezza concreta a spazio campionario è naturale?
- Congiunta, marginale e condizionata restano distinguibili?
- Bayes è comprensibile prima come normalizzazione della tabella?
- Il limite delle likelihood illustrative è abbastanza chiaro?
- Indipendenza e indipendenza condizionata non vengono confuse?
- La distinzione tra massa e densità è sufficiente?
- Parametro, statistica, stimatore e stima rimangono separati?
- La likelihood è chiaramente distinta da posterior e prior?
- LLN e CLT sono presentati senza promesse eccessive?
- Confidenza e credibilità hanno interpretazioni corrette?
- Il codice sostiene il testo senza sostituirlo?
- L'italiano rimane fluido nei passaggi probabilistici?

## Prova di comprensione semplificata

Il revisore dovrebbe poter spiegare che:

1. il sistema attribuisce una probabilità a stati che non osserva direttamente;
2. una nuova evidenza redistribuisce la massa tra le spiegazioni compatibili;
3. Bayes combina prior e likelihood;
4. un campione produce statistiche variabili anche con parametro fisso;
5. la likelihood confronta parametri sui dati osservati;
6. frequentista e bayesiano assegnano significati diversi all'incertezza sui parametri.

## Decisioni richieste

- [ ] Approvo il caso di Bayes.
- [ ] Approvo il livello su distribuzioni e momenti.
- [ ] Approvo la derivazione della MLE Bernoulli.
- [ ] Approvo la sezione su LLN e CLT.
- [ ] Approvo il confronto frequentista-bayesiano.
- [ ] Approvo `PROB-01`.
- [ ] Approvo `PROB-02`.
- [ ] Autorizzo il congelamento dopo le eventuali correzioni.
