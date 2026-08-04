# Specifica visuale `CALC-01`

## Identità

- Capitolo: `CH-P02-CALCULUS-BACKPROP`
- Sezione: Un forward e un backward completi
- Famiglia: grafo computazionale / esempio numerico
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`
- Standard: `docs/03_VISUALI.md`

## Domanda unica

Come convivono sullo stesso grafo i valori calcolati nel forward, le derivate locali e i gradienti propagati nel backward?

## Oggetto numerico

```text
x = 2,0
w1 = 1,5
b1 = -0,5
z = 2,5
h = 0,986614
w2 = -0,7
b2 = 0,2
y_hat = -0,490630
y = 0,4
loss = 0,396611
```

Gradienti:

```text
dL/dy_hat = -0,890630
dL/dh = 0,623441
dL/dz = 0,016579
dL/dw2 = -0,878708
dL/db2 = -0,890630
dL/dw1 = 0,033157
dL/db1 = 0,016579
```

## Layout obbligatorio

1. Titolo e sottotitolo.
2. Fascia superiore, forward da sinistra a destra:
   `Input -> Affine 1 -> tanh -> Affine 2 -> Loss`.
3. Fascia centrale, derivate locali allineate ai nodi corrispondenti.
4. Fascia inferiore, backward da destra a sinistra.
5. Footer che separa backpropagation e optimizer step.

## Regole semantiche

- il backward non modifica i valori del forward;
- i gradienti devono essere distinti graficamente dai valori;
- ogni derivata locale deve apparire sotto l'operazione a cui appartiene;
- le frecce del backward devono puntare da destra a sinistra;
- nessuna freccia deve attraversare un box o una label;
- l'optimizer non deve apparire come parte del grafo differenziale.

## Palette

- blu: forward e input;
- viola: trasformazioni;
- verde: loss e risultati;
- ambra: derivate locali e backward;
- grigio chiaro: box dei gradienti.

## Contenimento

- tutto il testo resta dentro i box;
- formule e pedici sono integralmente visibili;
- padding visibile su ogni lato;
- nessuna label tocca il bordo;
- il footer non sovrappone i nodi.

## Produzione

Tre tentativi con lo strumento immagini sono stati respinti perché rappresentavano dashboard sullo stato del libro anziché il grafo matematico. La candidata revisionabile è un PNG raster costruito dal renderer `scripts/generate_calculus_visuals.py` sulla base di questa specifica. Non viene usato SVG.
- domanda principale: Quale trasformazione centrale rende osservabile «La derivata descrive una sensibilità locale» nel capitolo 6?
