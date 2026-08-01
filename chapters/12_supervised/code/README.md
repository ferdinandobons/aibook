# Codice. Capitolo 12

## Snippet

`SNIP-SUP-001`, file `snip_sup_001_logistic_threshold.py`.

Lo snippet costruisce un dataset sintetico binario, addestra una logistic regression PyTorch con penalità L2, seleziona una soglia sulla validation mediante un costo asimmetrico e valuta il test soltanto dopo la selezione.

## Oggetti osservabili

```text
train: 120 esempi
validation: 50 esempi
test: 50 esempi
feature del modello: 2
slice di audit: tracking disponibile / tracking mancante
```

Il target positivo indica un caso urgente nel generatore illustrativo. Il dataset non rappresenta utenti o richieste reali.

## Esecuzione

```bash
python snip_sup_001_logistic_threshold.py
python -m unittest -v test_supervised_learning.py
```

## Contratti verificati

- la loss riceve logits e target binari;
- la penalità L2 viene aggiunta alla loss sui dati;
- il training riduce l'obiettivo registrato;
- le probabilità restano finite e in `[0,1]`;
- la soglia viene selezionata soltanto da probabilità e target della validation;
- il test non entra nella selezione;
- baseline, soglia predefinita e soglia selezionata vengono confrontate sullo stesso test;
- le metriche delle slice ricostruiscono l'intero test set.

## Ambiente

La versione dell'ambiente eseguito è in `environments/python-pytorch.txt`. La documentazione stable consultata è registrata separatamente in `../FONTI_PRIMARIE.md`.
