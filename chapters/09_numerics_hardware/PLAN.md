# Piano interno. Capitolo 9

## Identità

- `chapter_id`: `CH-P02-NUMERICS-HARDWARE`
- Parte: `P02`, Matematica, informazione e calcolo
- Titolo: `Calcolo numerico, precisione e hardware`
- Maturità: `CORE`
- Stato: testo, codice e visuali materializzati; revisione autoriale aperta
- Domanda centrale: come cambiano risultati, memoria e prestazioni quando numeri e operazioni vengono eseguiti con precisioni e hardware differenti?
- Oggetto continuo: un piccolo classificatore che calcola prodotti matriciali e softmax, osservato in `float16`, `bfloat16`, `float32` e `float64`
- Output finale: il lettore sa distinguere range, precisione, dtype di storage, dtype di calcolo e dtype di accumulo; riconosce overflow, underflow, non associatività, formule instabili, mixed precision e limiti di riproducibilità

## Prerequisiti

- vettori, matrici e prodotto matriciale, Capitolo 5;
- derivate e gradienti, Capitolo 6;
- probabilità e loss, Capitoli 7 e 8;
- Python e PyTorch soltanto per eseguire lo snippet.

## Concetti differiti

- quantizzazione intera e low-bit, Capitoli 74 e 75;
- kernel e compiler, Capitolo 81;
- training distribuito, Capitolo 36;
- serving e benchmark di produzione, Capitoli 79-82;
- stabilità di algoritmi spettrali avanzati, approfondimenti successivi.

## Sequenza didattica interna

1. i numeri reali del modello vengono approssimati da un insieme finito di valori;
2. un formato floating point separa segno, esponente e significando;
3. l'esponente governa soprattutto il range, il significando la precisione relativa;
4. `eps`, `tiny` e `max` descrivono proprietà diverse;
5. arrotondamento e cancellazione rendono l'aritmetica non associativa;
6. overflow, underflow, `inf` e `nan` sono risultati osservabili, non eccezioni sempre bloccanti;
7. formule equivalenti sulla carta possono avere stabilità diversa, come `logsumexp`;
8. `float16`, `bfloat16`, `float32` e `float64` offrono compromessi diversi;
9. mixed precision separa storage, calcolo e accumulo;
10. autocast e loss scaling risolvono problemi distinti;
11. hardware e librerie scelgono kernel, ordine delle riduzioni e precisione interna;
12. Tensor Core e TF32 possono aumentare throughput con condizioni e perdita di precisione controllata;
13. memoria, bandwidth e intensità aritmetica limitano le prestazioni insieme al picco di calcolo;
14. riproducibilità richiede ambiente, device, dtype, backend, seed e tolleranze;
15. il lettore ricostruisce un contratto numerico per ogni esperimento.

## Visuali previste

### `NUM-01`. Range e precisione dei dtype

- Domanda: perché due formati con lo stesso numero di bit possono comportarsi in modo molto diverso?
- Famiglia: confronto strutturale.
- Orientamento: orizzontale.
- Contenuto: `float16`, `bfloat16`, `float32`, `float64`; bit di segno, esponente e significando; `eps`, `max`, byte per elemento.
- Confine: i valori mostrati descrivono i formati, non il throughput di un dispositivo specifico.

### `NUM-02`. Contratto della mixed precision

- Domanda: quali quantità possono usare precisione ridotta e quali richiedono range o accumulo più ampio?
- Famiglia: processo / sistema.
- Orientamento: orizzontale.
- Contenuto: input e pesi, autocast, matmul/convolution, riduzioni e loss, gradienti, scaler opzionale per fp16, optimizer e master weights.
- Confine: la selezione effettiva degli operatori dipende da device, backend e versione.

## Codice

### `SNIP-NUM-001`

Mostra:

- proprietà `torch.finfo` dei quattro dtype;
- incremento minimo osservabile vicino a `1`;
- non associatività in `float32`;
- overflow della formula ingenua e stabilità di `torch.logsumexp`;
- differenza di range tra fp16 e bfloat16;
- autocast CPU in bfloat16 per una moltiplicazione matriciale;
- memoria teorica di un tensore per dtype.

## Gate specifici

- non presentare la precisione come una graduatoria assoluta;
- distinguere range, precisione, accumulo e memoria;
- non trasformare un risultato CPU in promessa GPU;
- non attribuire un'accelerazione senza benchmark sul dispositivo e sul kernel pertinenti;
- distinguere determinismo, riproducibilità statistica e identità bitwise;
- dichiarare che `float64` riduce alcuni errori ma non rende stabile ogni algoritmo;
- separare risultati eseguiti, documentazione e comportamento generale;
- mantenere formule stabili prima dei dettagli hardware;
- usare tolleranze motivate nei test, non confronti esatti indiscriminati.
