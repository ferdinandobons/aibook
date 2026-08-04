# Specifica visuale `SEARCH-02`

## Identità

- Capitolo: `CH-P03-SEARCH-PLANNING`
- Famiglia: albero di gioco con potatura
- Orientamento: orizzontale
- File candidato: `candidate-v2.png`
- Canvas: `1800 × 1000`
- Sfondo: bianco puro `#FFFFFF`

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
- sei foglie del minimax completo;
- foglia `9` ancora leggibile ma marcata come non valutata da alpha-beta;
- `minimax: 6 foglie`;
- `alpha-beta: 5 foglie`;
- nota che il valore finale resta `4`.

## Layout

- albero verticale;
- MAX blu, MIN viola e foglie valutate verdi;
- ramo potato tratteggiato in rosso;
- valore `9` leggibile dentro un box barrato ai margini;
- linee con partenza e arrivo inequivocabili;
- nessun testo fuori dai box.

## Provenienza

Valori e ordine dei figli derivano da `SNIP-SEARCH-001`. Il PNG raster è prodotto da `scripts/generate_search_visuals.py`; non viene usato SVG.
- domanda principale: Quale confronto o limite chiarisce «La frontiera decide che cosa esplorare dopo»?
