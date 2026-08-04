# Specifica visuale `CALC-02`

## Identità

- Capitolo: `CH-P02-CALCULUS-BACKPROP`
- Sezione: Dal grafo scalare al reverse mode
- Famiglia: processo / confronto tra nodi locali
- Orientamento: orizzontale
- File candidato: `candidate-v2.png`
- Sfondo: bianco puro `#FFFFFF`
- Standard: `docs/03_VISUALI.md`

## Domanda unica

Che cosa fa ciascun nodo durante il reverse mode quando riceve un gradiente dal resto del grafo?

## Contenuto obbligatorio

Tre pannelli, nell'ordine:

1. nodo loss;
2. nodo affine;
3. nodo `tanh`.

Ogni pannello contiene:

```text
1. gradiente in arrivo
2. derivata o derivate locali
3. gradiente o gradienti in uscita
```

Valori:

```text
Nodo loss
in arrivo: 1
locale: dL/dy_hat = y_hat - y
in uscita: -0,890630

Nodo affine
in arrivo: -0,890630
locali: dy_hat/dh = w2; dy_hat/dw2 = h; dy_hat/db2 = 1
in uscita: dL/dh = 0,623441; dL/dw2 = -0,878708; dL/db2 = -0,890630

Nodo tanh
in arrivo: 0,623441
locale: dh/dz = 1-h^2 = 0,026592
in uscita: dL/dz = 0,016579
```

## Footer

Il footer deve separare:

- differenziazione: calcola `dL/dtheta` sul grafo eseguito;
- optimizer step: usa i gradienti per proporre un aggiornamento.

## Collegamenti

- le frecce tra pannelli sono etichettate `VJP`;
- nessuna freccia attraversa i pannelli;
- il footer non copre i box `in uscita`;
- il flusso non deve far pensare che l'optimizer faccia parte del reverse mode.

## Palette

- blu: gradiente in arrivo;
- ambra: derivata locale e VJP;
- verde: gradiente in uscita;
- viola: differenziazione;
- rosso tenue: optimizer step.

## Contenimento

- massimo quattro righe per contenitore interno;
- formule e segni completamente visibili;
- padding uniforme;
- nessuna sovrapposizione tra footer e pannelli.

## Produzione

La prima versione raster è stata respinta perché il footer copriva parzialmente i box inferiori. `candidate-v2.png` aumenta lo spazio verticale e mantiene tutti i contenuti separati. Il file è un PNG raster, non un SVG.
- domanda principale: Quale confronto o limite chiarisce «Più input richiedono derivate parziali e gradienti»?
