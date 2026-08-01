# Audit del codice. Capitolo 8

## Stato

- Snippet: `SNIP-INFO-001`
- Ambiente: Python 3.13.5, PyTorch 2.10.0+cpu, CPU, float64
- Esito: **superato**

## Contratto

Il codice deve:

1. trasformare logits in probabilità;
2. confrontare NLL manuale e `F.cross_entropy`;
3. calcolare entropia, cross-entropy e KL;
4. verificare la decomposizione `H(q,p)=H(q)+KL(q||p)`;
5. verificare il gradiente `p-q`;
6. confrontare previsione corretta e confidentemente errata;
7. mostrare la stabilità di `log_softmax` su logits grandi.

## Test

- [x] probabilità sommano a uno;
- [x] NLL manuale uguale a CrossEntropyLoss;
- [x] decomposizione cross-entropy verificata a `1e-12`;
- [x] target one-hot: cross-entropy uguale a KL;
- [x] gradiente dei logits uguale a `p-one_hot`;
- [x] loss errata maggiore di quella corretta;
- [x] differenza tra le due loss pari a `3,0` nel caso simmetrico;
- [x] formula ingenua sui logits grandi produce `nan`;
- [x] `log_softmax` resta finita.

Esito:

```text
Ran 7 tests
OK
```

## API

- `F.cross_entropy` riceve logits non normalizzati;
- `torch.log_softmax` è usata lungo `dim=0` nel caso non batch;
- target come indice usa dtype intero;
- l'implementazione manuale delle distribuzioni verifica non negatività e somma a uno;
- documentazione stable `2.13` controllata separatamente dall'ambiente `2.10.0+cpu`.

## Limiti

- un solo esempio a tre classi;
- nessuna label smoothing API;
- nessun peso di classe;
- nessun `ignore_index`;
- nessun batch multidimensionale;
- nessun test di calibrazione;
- nessuna misura di velocità.

## Verdetto

Il codice sostiene le formule, i valori, il gradiente e il caso di stabilità numerica usati nel capitolo.
