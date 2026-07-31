# Codice. Capitolo 10

## `SNIP-SEARCH-001`

Il file `snip_search_001_astar_minimax.py` contiene due esempi:

1. uniform-cost e A* sullo stesso grafo di azioni;
2. minimax e alpha-beta sullo stesso albero di gioco.

## Esecuzione

```bash
python snip_search_001_astar_minimax.py
python -m unittest -v test_search_planning.py
```

## Contratti verificati

- costi degli archi non negativi;
- stessa soluzione ottima per uniform-cost e A*;
- euristica ammissibile e consistente nel grafo illustrativo;
- A* espande meno stati nello specifico esempio;
- alpha-beta preserva il valore minimax;
- una foglia viene potata nell'ordine fissato.

## Confini

- il numero di espansioni non è un risultato generale;
- l'euristica è costruita a mano per il grafo del capitolo;
- nessun algoritmo appreso viene eseguito;
- il game tree è deterministico, a somma zero e perfettamente osservabile;
- il codice usa soltanto la standard library.
