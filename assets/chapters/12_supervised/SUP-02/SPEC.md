# Specifica visuale `SUP-02`

## Identità

- Capitolo: `CH-P03-SUPERVISED`
- Famiglia: confronto controllato
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Come possono due soglie ottenere la stessa accuracy e produrre errori e costi differenti?

## Contenuto obbligatorio

### Soglia `0,30`

```text
TP=21
TN=24
FP=3
FN=2
accuracy=0,900
costo=13
```

### Soglia `0,50`

```text
TP=19
TN=26
FP=1
FN=4
accuracy=0,900
costo=21
```

### Slice con soglia `0,30`

```text
tracking disponibile: 34 casi, recall 1,000, costo 3
tracking mancante: 16 casi, recall 0,778, costo 10
```

Costo: falso negativo `5`, falso positivo `1`.

## Layout

- due confusion matrix parallele;
- box centrale `stessa media, errori diversi`;
- fascia inferiore per le slice;
- label target e predizione esplicite;
- numeri e colori coerenti.

## Regole

- `TP`, `TN`, `FP`, `FN` non devono essere invertiti;
- i conteggi devono sommare a 50 in entrambi i pannelli;
- il colore non sostituisce le label;
- il costo deve essere ricostruibile dai conteggi;
- il confronto non deve suggerire equivalenza dei due sistemi;
- nessun testo fuori dai box.

## Provenienza

Valori da `SNIP-SUP-001`. PNG raster generato da `scripts/generate_supervised_visuals.py`; nessun SVG.
