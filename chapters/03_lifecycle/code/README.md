# Codice del Capitolo 3

## `SNIP-LIFE-001`. Split, selezione e monitoraggio illustrativo

Lo snippet mostra quattro idee:

1. train, validation e test usano indici disgiunti;
2. due learning rate vengono confrontati sulla validation;
3. il test viene usato dopo la scelta;
4. un batch successivo viene confrontato con il training attraverso uno spostamento standardizzato della media.

File:

- `snip_life_001_split_train_monitor.py`;
- `test_lifecycle_snippet.py`;
- `outputs/SNIP-LIFE-001.txt`;
- `outputs/TESTS.txt`;
- `environments/python-pytorch.txt`.

## Esecuzione

```bash
python snip_life_001_split_train_monitor.py
python -m unittest -v
```

## Confini

- dataset sintetico;
- accuratezza non rappresentativa di un prodotto;
- shift della media non equivale a degradazione causale;
- nessun retraining automatico;
- nessuna stima di incertezza statistica.
