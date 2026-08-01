# Specifica visuale `UNSUP-02`

## Identità

- Capitolo: `CH-P03-UNSUPERVISED-SELF`
- Famiglia: pipeline tensoriale
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Da dove proviene il target in un compito di masked reconstruction senza label umana?

## Pipeline

```text
x=[a,b,c,d]
-> mask=[0,1,0,1]
-> corrupted=[a,0,c,0] + mask
-> encoder z[2]
-> decoder x_hat[4]
-> MSE soltanto su b,d
```

Un percorso separato collega il dato originale alla loss e porta il testo:

```text
target auto-generato: valori originali nelle posizioni mascherate
```

## Regole

- la loss riceve ricostruzione e target originale;
- la maschera non appare come categoria semantica;
- l'encoder non riceve i valori nascosti;
- il decoder produce tutte le coordinate, ma la loss illustrata usa quelle mascherate;
- shape `[2]` e `[4]` visibili;
- nessuna freccia ambigua;
- nessun testo fuori dai box.

## Provenienza

Pipeline coerente con `SNIP-UNSUP-001`; PNG raster generato da `scripts/generate_unsupervised_visuals.py`; nessun SVG.
