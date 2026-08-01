# Piano interno. Capitolo 5

## Identità

- `chapter_id`: `CH-P02-LINEAR-ALGEBRA`
- Parte: `P02`, Matematica, informazione e calcolo
- Titolo: Algebra lineare, vettori e tensori
- Profilo: fondamento matematico e contratti delle shape
- Oggetto continuo: tre richieste rappresentate da quattro numeri ciascuna e trasformate in tre punteggi di classe
- Domanda centrale: come descriviamo e trasformiamo molte quantità senza perdere significato, assi e compatibilità delle dimensioni?

## Prerequisiti

- aritmetica elementare;
- funzioni e somme;
- Python di base per lo snippet.

## Concetti differiti

- derivate e backpropagation;
- probabilità e covarianza;
- condizionamento e stabilità numerica;
- decomposizioni avanzate e algoritmi iterativi;
- algebra multilineare specializzata.

## Stato finale del lettore

Il lettore sa:

1. distinguere scalare, vettore, matrice e tensore;
2. leggere una shape e assegnare un significato a ogni asse;
3. distinguere operazioni elemento per elemento, prodotto scalare e prodotto matriciale;
4. ricostruire una trasformazione affine `XW^T+b`;
5. capire perché alcune dimensioni devono coincidere;
6. riconoscere broadcasting, batch e contrazione di assi;
7. spiegare span, indipendenza, rango e sottospazio;
8. leggere la SVD come somma di componenti ordinate;
9. collegare formule e operazioni PyTorch.

## Progressione didattica

1. Una richiesta diventa quattro numeri.
2. Più richieste formano una matrice; più matrici formano un tensore.
3. Gli assi hanno significato, non soltanto lunghezza.
4. Somma, scaling, norme e prodotto scalare.
5. Matrice-vettore e matrice-matrice come combinazioni organizzate.
6. Trasformazione affine e bias condiviso tramite broadcasting.
7. Batch e dimensioni di testa o tempo.
8. Span, indipendenza e rango.
9. SVD e approssimazione a rango ridotto.
10. Layout, view e contiguità come confine implementativo.

## Codice

### `SNIP-LA-001`

- `X`: tre esempi per quattro feature, shape `[3,4]`;
- `W`: tre righe di pesi per quattro feature, shape `[3,4]`;
- `b`: tre bias, shape `[3]`;
- output: `X @ W.T + b`, shape `[3,3]`;
- matrice di Gram: `X @ X.T`, shape `[3,3]`;
- matrice di rango due e SVD ridotta;
- ricostruzione con errore inferiore a `1e-12` in float64.

## Visuali previste

### `LA-01`. Dalle shape al layer lineare

Mostra `X[batch,feature]`, `W[classe,feature]`, trasposizione, contrazione dell'asse feature, bias in broadcasting e output `[batch,classe]`.

### `LA-02`. Rango e SVD come componenti ordinate

Mostra una matrice di rango due, le direzioni singolari, i valori singolari e la ricostruzione; chiarisce che il terzo valore è numericamente nullo nell'esempio.

## Gate specifici

- ogni asse riceve un nome prima della notazione compatta;
- `tensor` non viene presentato come oggetto diverso dalla generalizzazione degli array multidimensionali;
- prodotto elemento per elemento e prodotto matriciale restano distinti;
- la trasposizione non viene descritta come modifica dei valori;
- il bias viene collegato al broadcasting senza implicare copie fisiche obbligatorie;
- rango numerico e rango esatto non vengono confusi;
- la SVD non viene presentata come unica decomposizione possibile;
- `view`, `reshape` e contiguità restano un confine implementativo, non la definizione matematica del tensore.
