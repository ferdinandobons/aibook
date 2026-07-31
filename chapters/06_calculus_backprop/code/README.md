# Codice. Capitolo 6

`SNIP-CALC-001` calcola la stessa rete scalare in tre modi:

1. forward e backward manuali;
2. PyTorch autograd;
3. differenze finite centrate.

Esegue inoltre `torch.autograd.gradcheck` in doppia precisione e mostra che due chiamate consecutive a `backward()` accumulano i gradienti nel tensore foglia quando `.grad` non viene azzerato.

## Rete

```text
x -> z = w1*x+b1 -> h=tanh(z)
  -> y_hat=w2*h+b2 -> loss=0,5*(y_hat-target)^2
```

## Esecuzione

```bash
python snip_calc_001_manual_autograd.py
python -m unittest -v
```

Lo snippet non esegue un optimizer step. Calcola soltanto valori e gradienti, così backpropagation e aggiornamento dei parametri restano distinti.
