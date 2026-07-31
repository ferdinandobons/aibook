# Codice. Capitolo 5

`SNIP-LA-001` usa lo stesso esempio del capitolo per collegare shape, prodotto matriciale, broadcasting, matrice di Gram, rango e SVD.

## Contratto

```text
X[3,4] @ W.T[4,3] + b[3]
-> scores[3,3]
```

Il bias viene confrontato con una espansione esplicita per verificare la semantica del broadcasting. La matrice di Gram contiene i prodotti scalari tra le righe di `X`.

Una seconda matrice ha la seconda riga uguale al doppio della prima, quindi possiede rango due. `torch.linalg.svd` produce tre valori singolari, di cui l'ultimo è numericamente vicino a zero, e ricostruisce la matrice entro la tolleranza dichiarata.

## Esecuzione

```bash
python snip_la_001_shapes_linear_svd.py
python -m unittest -v
```

Gli output sono risultati eseguiti nell'ambiente registrato. Il comportamento delle API è stato controllato separatamente nella documentazione PyTorch stable.
