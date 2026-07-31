# Audit del codice. Capitolo 7

## Stato

- Snippet: `SNIP-PROB-001`
- Ambiente: Python 3.13.5, PyTorch 2.10.0+cpu, CPU, float64
- Seed: `2026`
- Esito: **superato**

## Contratto

Il codice deve:

1. normalizzare correttamente un aggiornamento di Bayes binario;
2. produrre posterior `2/3` dopo la prima evidenza e `0,875` dopo la seconda;
3. calcolare la MLE Bernoulli come media campionaria;
4. verificare la log-likelihood su candidati locali;
5. ottenere media e varianza teoriche da `torch.distributions.Bernoulli`;
6. mostrare la variabilità di medie campionarie con dimensioni diverse;
7. distinguere numeri illustrativi, risultati eseguiti e proprietà generali.

## Test

- [x] probabilità dell'evidenza `0,24`;
- [x] posterior prima evidenza `0,666666...`;
- [x] posterior seconda evidenza `0,875`;
- [x] MLE Bernoulli uguale alla media;
- [x] log-likelihood massima sul punto `0,375` nella griglia locale del test;
- [x] media teorica Bernoulli `0,30`;
- [x] varianza teorica Bernoulli `0,21`;
- [x] grande campione entro `0,02` dai momenti teorici;
- [x] grande campione non artificialmente forzato a essere uguale al parametro.

Esito registrato:

```text
Ran 6 tests
OK
```

## Riproducibilità

Il campionamento usa `torch.manual_seed(2026)`. Le frequenze ottenute sono risultati del run registrato e possono dipendere da ambiente e generatore. I claim matematici non dipendono dai valori specifici del campione.

## API

`torch.distributions.Bernoulli` è stato eseguito con PyTorch `2.10.0+cpu`. Parametri, momenti, `sample` e `log_prob` sono stati ricontrollati sulla documentazione stable `2.13`.

## Limiti

- stato e evidenze binari;
- likelihood illustrative;
- indipendenza condizionata assunta nel secondo aggiornamento;
- nessuna stima causale;
- nessun intervallo numerico prodotto dal codice;
- nessun metodo Monte Carlo avanzato.

## Verdetto

Il codice sostiene i valori numerici, i momenti Bernoulli, la MLE e la dimostrazione campionaria usati nel capitolo.
