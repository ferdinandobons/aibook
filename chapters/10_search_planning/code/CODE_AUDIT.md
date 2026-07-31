# Audit del codice. Capitolo 10

## Stato

- Snippet: `SNIP-SEARCH-001`
- Ambiente: Python 3.13.5, standard library, CPU
- Test: 6 superati
- Data: 31 luglio 2026
- Esito: **superato**

## A* e uniform-cost

- [x] coda di priorità con tie-break deterministico;
- [x] costo migliore registrato per stato;
- [x] entry obsolete della frontiera ignorate;
- [x] parent e azioni usati per ricostruire il piano;
- [x] costi negativi rifiutati;
- [x] euristica definita per ogni stato;
- [x] ammissibilità verificata rispetto ai costi ottimi del grafo;
- [x] consistenza verificata su ogni arco;
- [x] uniform-cost ottenuta con euristica zero;
- [x] stesso costo ottimo `6`;
- [x] conteggio delle espansioni registrato.

## Minimax e alpha-beta

- [x] alternanza MAX/MIN esplicita;
- [x] foglie numeriche distinte dai nodi;
- [x] minimax visita sei foglie;
- [x] alpha-beta restituisce lo stesso valore `4`;
- [x] alpha-beta visita cinque foglie nell'ordine fissato;
- [x] nessun claim generale derivato dal singolo conteggio.

## Limiti

- il grafo è piccolo e deterministico;
- non sono misurati tempi di esecuzione;
- il vantaggio di A* dipende dall'euristica e dai pareggi;
- la potatura alpha-beta dipende dall'ordine dei figli;
- non sono trattati costi negativi, probabilità di transizione o osservabilità parziale;
- non vengono eseguiti MCTS, policy network o value network.

## Verdetto

Il codice sostiene i claim eseguiti e rende visibili i contratti algoritmici senza trasformare il toy example in una prova generale.
