# Codice del Capitolo 7

## `SNIP-PROB-001`

File:

```text
snip_prob_001_bayes_sampling.py
```

Mostra:

- aggiornamento di Bayes con uno stato binario;
- aggiornamento sequenziale con una seconda evidenza;
- MLE Bernoulli come media campionaria;
- log-likelihood tramite `torch.distributions.Bernoulli`;
- media e varianza teoriche;
- campionamento con `n=10`, `100` e `10 000`.

## Esecuzione

```bash
python snip_prob_001_bayes_sampling.py
python -m unittest -v
```

Gli output registrati sono in `outputs/`. L'ambiente è in `environments/python-pytorch.txt`.

## Confini

- le probabilità del caso di consegna sono illustrative;
- il secondo aggiornamento usa una ipotesi dichiarata di indipendenza condizionata;
- il seed rende riproducibile il run registrato, non stabilisce un risultato generale;
- la simulazione non sostituisce legge dei grandi numeri o teorema centrale del limite;
- non viene stimato un prodotto reale.
