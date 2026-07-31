# Revisione autoriale. Capitolo 10

## Candidatura

- `chapter_id`: `CH-P03-SEARCH-PLANNING`
- Titolo: **Ricerca, pianificazione e giochi**
- Versione: `0.2.0-rc1`
- Stato previsto dopo la materializzazione dei PNG: candidatura completa in revisione autoriale

## Ordine consigliato

1. [`CHAPTER.md`](CHAPTER.md)
2. [`SEARCH-01`](../../assets/chapters/10_search_planning/SEARCH-01/candidate-v2.png)
3. [`SEARCH-02`](../../assets/chapters/10_search_planning/SEARCH-02/candidate-v2.png)
4. [`code/README.md`](code/README.md)
5. [`TEXT_AUDIT.md`](TEXT_AUDIT.md)
6. [`CLAIMS.md`](CLAIMS.md)
7. [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md)

## Punti da valutare

### Testo

- La distinzione tra stato e nodo di ricerca è chiara?
- È evidente perché meno azioni non significa sempre minor costo?
- Uniform-cost e A* sono presentati con ipotesi e garanzie corrette?
- Ammissibilità e consistenza risultano distinguibili?
- Planning, esecuzione e generazione di testo restano separati?
- Minimax e alpha-beta sono comprensibili prima di MCTS?
- Il passaggio a policy e value network è un ponte, non una generalizzazione indebita?

### Visuali

- In `SEARCH-01`, ogni arco lungo ha origine e destinazione inequivocabili?
- Il cammino ottimo resta leggibile insieme ai rami alternativi?
- L'ordine di espansione è abbastanza grande e chiaro?
- In `SEARCH-02`, il valore 9 è leggibile ma marcato come non visitato da alpha-beta?
- Il confronto tra sei e cinque foglie è immediato?

### Codice

- Lo snippet è sufficientemente breve per il corpo del capitolo?
- I sei test coprono le proprietà didattiche portanti?
- È chiaro che i conteggi di espansioni e foglie appartengono al caso fissato?

## Gate aperti

- approvazione autoriale del testo;
- approvazione autoriale delle due visuali;
- eventuali correzioni;
- rinomina dei PNG approvati in `final.png`;
- congelamento con data e commit.
