# Codice del Capitolo 8

## `SNIP-INFO-001`

File:

```text
snip_info_001_cross_entropy.py
```

Mostra:

- softmax e log-softmax;
- NLL manuale e `F.cross_entropy`;
- entropia della distribuzione prevista;
- cross-entropy con target probabilistico;
- decomposizione `H(q,p)=H(q)+KL(q||p)`;
- gradiente rispetto ai logits;
- previsione confidentemente errata;
- instabilità della softmax ingenua con logits grandi.

## Esecuzione

```bash
python snip_info_001_cross_entropy.py
python -m unittest -v
```

Output e test sono nella cartella `outputs/`. L'ambiente è registrato in `environments/python-pytorch.txt`.

## Confini

- esempio a tre classi;
- logaritmi naturali e unità in nat;
- nessuna misura di calibrazione;
- target morbido illustrativo;
- la dimostrazione di overflow dipende dall'aritmetica float64 del run;
- nessun benchmark di prestazioni.
