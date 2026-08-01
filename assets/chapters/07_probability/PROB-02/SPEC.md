# Specifica visuale `PROB-02`

## Identità

- Capitolo: `CH-P02-PROBABILITY`
- Sezione: Campionamento e incertezza della stima
- Famiglia: confronto distribuzione / campioni
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Perché il parametro di una distribuzione può restare fisso mentre la media osservata cambia da un campione all'altro?

## Contenuto

Pannello distribuzione:

```text
Bernoulli
p = 0,30
E[X] = 0,30
Var(X) = 0,21
```

Tre campioni del run registrato:

```text
n = 10; successi = 6; media = 0,6000
n = 100; successi = 32; media = 0,3200
n = 10 000; successi = 3 042; media = 0,3042
```

Deviazione standard teorica della media, usando

```text
sqrt(p(1-p)/n)
```

con valori arrotondati:

```text
0,1449
0,0458
0,0046
```

## Layout

- distribuzione a sinistra;
- freccia verso tre campioni paralleli;
- barra proporzionale ai successi in ogni campione;
- media campionaria in evidenza;
- deviazione teorica della media in un box separato;
- footer sulla legge dei grandi numeri.

## Regole semantiche

- `p=0,30` è il parametro fisso;
- le medie sono risultati eseguiti;
- la barra rappresenta una proporzione, non una probabilità posteriore;
- campioni più grandi non vengono presentati come monotonicamente più vicini in ogni realizzazione;
- il footer dichiara condizioni e limite della LLN.

## Contenimento

- nessun testo sotto il bordo delle card;
- formula e valori visibili;
- padding inferiore sufficiente;
- footer separato dai pannelli;
- colore accompagnato da label e numeri.

## Provenienza

Le medie derivano da `SNIP-PROB-001`. I momenti e la deviazione teorica derivano dalla Bernoulli. La candidata è un PNG raster generato da `scripts/generate_probability_visuals.py`; non viene usato SVG.
