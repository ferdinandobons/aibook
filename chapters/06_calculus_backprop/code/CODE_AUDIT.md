# Audit del codice. Capitolo 6

## Stato

- Snippet: `SNIP-CALC-001`
- File: `snip_calc_001_manual_autograd.py`
- Test: `test_calculus_backprop.py`
- Ambiente: `Python 3.13.5`, `PyTorch 2.10.0+cpu`, CPU, float64
- Esito: **superato**

## Contratto

Lo snippet deve:

1. eseguire il forward della rete scalare;
2. calcolare i gradienti manualmente;
3. calcolare gli stessi gradienti con autograd;
4. confrontarli con differenze finite centrate;
5. eseguire `torch.autograd.gradcheck`;
6. mostrare l'accumulo in `.grad` dopo due backward distinti.

## Controlli

- [x] seed non necessario, perché il calcolo non usa casualità;
- [x] tutti i tensori del controllo differenziale usano float64;
- [x] forward manuale e PyTorch coincidono;
- [x] gradienti manuali e autograd coincidono a 12 cifre decimali nei test;
- [x] differenze finite coincidono a 7 cifre decimali;
- [x] `gradcheck` restituisce `True`;
- [x] prima chiamata a backward su `u^2`, con `u=2`, produce `.grad=4`;
- [x] seconda chiamata indipendente accumula fino a `.grad=8`;
- [x] nessun optimizer viene eseguito;
- [x] nessun risultato viene presentato come misura di training reale.

## Test registrati

```text
test_forward_values
test_manual_matches_autograd
test_finite_differences_match_manual
test_gradcheck
test_backward_accumulates_gradients
```

Esito:

```text
Ran 5 tests
OK
```

## Versioni

Il codice è stato eseguito con PyTorch `2.10.0+cpu`. I contratti delle API sono stati ricontrollati separatamente sulla documentazione stable `2.13` il 31 luglio 2026. La documentazione consultata non viene presentata come ambiente di esecuzione.

## Limiti

- esempio scalare e deterministico;
- nessuna misura di velocità;
- nessuna GPU;
- nessun custom `autograd.Function`;
- nessuna derivata di ordine superiore;
- differenze finite usate soltanto come controllo.

## Verdetto

Codice e test sostengono i valori numerici, l'accumulo dei gradienti e il confronto tra derivazione manuale, autograd e differenze finite usati nel capitolo.
