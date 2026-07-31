# Specifica visuale `SEARCH-02`

## Domanda unica

Come può alpha-beta evitare una foglia senza modificare il valore minimax?

## Albero

```text
root MAX
├─ A, MIN -> [3, 5] -> 3
├─ B, MIN -> [2, 9] -> 2
└─ C, MIN -> [4, 4] -> 4
```

Dopo il ramo A, `alpha=3`. Nel ramo B, MIN osserva `2`; la foglia `9` non può rendere B preferibile ad A per MAX e viene potata.

## Contenuto obbligatorio

- radice `MAX · 4`;
- tre nodi `MIN` con valori 3, 2 e 4;
- sei foglie minimax;
- foglia `9` barrata o marcata come non valutata da alpha-beta;
- `minimax: 6 foglie`;
- `alpha-beta: 5 foglie`;
- nota che il valore resta `4`.

## Layout

- sfondo bianco puro;
- albero verticale;
- MAX blu, MIN viola, foglie verdi;
- ramo potato rosso tenue;
- linee con partenza e arrivo inequivocabili;
- nessun testo fuori dai box.

## Stato

Storyboard completo. Renderer raster v1 presente; materializzazione e audit del raster ancora aperti.
