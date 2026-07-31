# Piano interno. Capitolo 6

## Identità

- `chapter_id`: `CH-P02-CALCULUS-BACKPROP`
- Parte: `P02`, Matematica, informazione e calcolo
- Titolo: Calcolo differenziale e backpropagation
- Profilo: fondamento matematico e algoritmo di differenziazione
- Oggetto continuo: una rete scalare `x -> z -> h -> y_hat -> loss`
- Domanda centrale: come attribuiamo una piccola variazione della loss a ciascun parametro che ha contribuito al calcolo?

## Prerequisiti

- funzioni elementari;
- vettori e shape;
- prodotto e somma;
- Python e PyTorch soltanto per lo snippet.

## Concetti differiti

- ottimizzatori e dinamica del training;
- Hessiane e metodi del secondo ordine;
- differenziazione implicita;
- gradienti stocastici e stime Monte Carlo;
- checkpointing e sistemi distribuiti.

## Oggetto numerico

```text
x = 2,0
w1 = 1,5
b1 = -0,5
z = w1*x + b1
h = tanh(z)
w2 = -0,7
b2 = 0,2
y_hat = w2*h + b2
target = 0,4
loss = 0,5*(y_hat-target)^2
```

## Stato finale del lettore

Il lettore sa:

1. interpretare derivata e derivata parziale come sensibilità locale;
2. distinguere gradiente, Jacobiana e derivata direzionale;
3. applicare regole di somma, prodotto e catena;
4. leggere un grafo computazionale;
5. eseguire forward pass e backward pass sullo stesso grafo;
6. spiegare perché reverse mode è adatto a una loss scalare con molti parametri;
7. distinguere backpropagation, automatic differentiation e optimizer step;
8. usare `requires_grad`, `backward`, `grad` e `gradcheck` entro il perimetro documentato;
9. riconoscere accumulo dei gradienti, grafo liberato e operazioni in-place rischiose.

## Progressione

1. Una piccola variazione e la pendenza locale.
2. Derivate parziali e gradiente.
3. La regola della catena.
4. Forward pass sul grafo numerico.
5. Derivate locali di loss, affine e tanh.
6. Backward pass da destra verso sinistra.
7. Jacobiane e prodotti vettore-Jacobiana.
8. Forward mode e reverse mode.
9. Autograd PyTorch.
10. Verifica con differenze finite e `gradcheck`.
11. Accumulo, detach, no_grad e confini operativi.

## Codice

### `SNIP-CALC-001`

- calcolo manuale di forward e gradienti;
- calcolo PyTorch con autograd;
- confronto con differenze finite centrali;
- `torch.autograd.gradcheck` in float64;
- dimostrazione separata dell'accumulo in `.grad`.

## Visuali

### `CALC-01`. Forward e backward sullo stesso grafo

Mostra valori in avanti sopra le frecce e gradienti all'indietro sotto le frecce, senza far sembrare che il backward modifichi i valori del forward.

### `CALC-02`. Reverse mode come composizione di derivate locali

Mostra il gradiente in arrivo, la derivata locale e il gradiente in uscita per ogni nodo; distingue la fase di differenziazione dall'optimizer step.

## Gate specifici

- derivata locale e cambiamento finito non vengono confusi;
- la chain rule è applicata prima di nominare backpropagation;
- backpropagation non viene presentata come optimizer;
- autograd non viene descritto come differenziazione simbolica;
- `backward()` viene collegato all'accumulo nei tensori foglia;
- una loss non scalare richiede un gradiente esterno o una riduzione;
- differenze finite sono un controllo numerico, non la procedura di training;
- `gradcheck` viene usato in float64 con tolleranze documentate;
- gradienti e valori eseguiti devono coincidere tra testo, codice e visuali.
