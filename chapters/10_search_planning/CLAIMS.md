# Registro dei claim. Capitolo 10

## Stato

- Data: 31 luglio 2026
- Claim aperti: 0
- Risultati eseguiti: `SNIP-SEARCH-001`

| ID | Claim | Prova | Condizioni e limiti |
|---|---|---|---|
| `CLM-SEARCH-001` | Un problema di ricerca può essere descritto con stato iniziale, azioni, modello di transizione, costo e goal. | AIMA; STRIPS per il caso di planning | Tassonomia didattica, non unica formalizzazione possibile. |
| `CLM-SEARCH-002` | Un nodo dell'albero di ricerca contiene anche il cammino; lo stesso stato può comparire in nodi differenti. | AIMA | La graph search può unificare duplicati secondo il contratto. |
| `CLM-SEARCH-003` | BFS trova un cammino con il minor numero di archi quando ogni azione ha costo uniforme. | Risultato standard; AIMA | Non minimizza costi arbitrari. |
| `CLM-SEARCH-004` | Uniform-cost espande il nodo di frontiera con costo accumulato minimo. | Dijkstra 1959; AIMA | Richiede costi non negativi per la garanzia standard. |
| `CLM-SEARCH-005` | A* usa `f(n)=g(n)+h(n)`. | Hart, Nilsson e Raphael 1968 | La gestione dei duplicati è parte dell'algoritmo completo. |
| `CLM-SEARCH-006` | Una euristica ammissibile non sovrastima il costo ottimo rimanente. | Hart et al.; AIMA | Proprietà rispetto a un problema e a un goal specifici. |
| `CLM-SEARCH-007` | Una euristica consistente soddisfa una disuguaglianza triangolare lungo ogni transizione. | Hart et al.; AIMA | La consistenza implica ammissibilità nelle condizioni standard. |
| `CLM-SEARCH-008` | Con costi non negativi e gestione appropriata della frontiera, A* graph search con euristica consistente restituisce un cammino ottimo. | Hart et al.; AIMA | Non vale per qualunque implementazione denominata A*. |
| `CLM-SEARCH-009` | Una euristica più informativa può ridurre le espansioni, ma il vantaggio dipende anche dai pareggi e dal grafo. | Teoria A*; esempio eseguito | Non è una garanzia di riduzione per ogni istanza. |
| `CLM-SEARCH-010` | STRIPS rappresenta azioni tramite condizioni e cambiamenti dello stato per cercare una sequenza che soddisfi il goal. | Fikes e Nilsson 1971 | Le formulazioni moderne possono essere più espressive. |
| `CLM-SEARCH-011` | PDDL è stato introdotto per descrivere domini e problemi di planning in una notazione comparabile. | McDermott et al. 1998 | Versioni successive estendono la lingua. |
| `CLM-SEARCH-012` | Il principio di Bellman collega una soluzione ottima a sottosoluzioni ottime. | Bellman 1957 | Richiede una decomposizione appropriata dello stato. |
| `CLM-SEARCH-013` | Minimax assume alternanza tra un giocatore MAX e un giocatore MIN in un gioco a somma zero perfettamente osservabile nel caso base. | Shannon 1950; AIMA | Giochi stocastici o imperfetti richiedono estensioni. |
| `CLM-SEARCH-014` | Alpha-beta può evitare rami che non possono cambiare il valore minimax. | Knuth e Moore 1975 | Il numero di tagli dipende fortemente dall'ordine delle mosse. |
| `CLM-SEARCH-015` | Alpha-beta restituisce lo stesso valore di minimax quando implementato correttamente sullo stesso albero. | Knuth e Moore 1975 | La potatura cambia il lavoro, non la funzione obiettivo. |
| `CLM-SEARCH-016` | Monte Carlo tree search costruisce l'albero selettivamente usando simulazioni e statistiche accumulate. | Kocsis e Szepesvári 2006; Silver et al. 2016 | Esistono molte varianti. |
| `CLM-SEARCH-017` | UCT applica un principio da multi-armed bandit alla selezione nei nodi dell'albero. | Kocsis e Szepesvári 2006 | Le garanzie dipendono dalle ipotesi del paper. |
| `CLM-SEARCH-018` | AlphaGo combina policy network, value network e tree search nel sistema descritto nel paper. | Silver et al. 2016 | Non è una proprietà di ogni sistema neurale. |
| `CLM-SEARCH-019` | AlphaGo Zero usa self-play, una rete policy-value e MCTS partendo dalle regole del gioco. | Silver et al. 2017 | Risultato specifico del gioco e del setup descritto. |
| `CLM-SEARCH-020` | Una policy appresa può ordinare o proporre azioni, mentre una value può stimare stati; nessuna delle due garantisce da sola l'ottimalità della ricerca. | Silver et al.; inferenza editoriale esplicitata come distinzione di contratto | Garanzie richiedono condizioni aggiuntive. |
| `CLM-SEARCH-021` | Nel run registrato, A* e uniform-cost trovano lo stesso piano di costo `6`. | `SNIP-SEARCH-001` | Grafo illustrativo con costi non negativi. |
| `CLM-SEARCH-022` | Nel run registrato, A* espande cinque stati e uniform-cost otto. | `SNIP-SEARCH-001` | Dipende dal grafo, dall'euristica e dai pareggi. |
| `CLM-SEARCH-023` | Nel run registrato, minimax visita sei foglie e alpha-beta cinque, restituendo entrambi valore `4`. | `SNIP-SEARCH-001` | Albero e ordine dei figli fissati. |

## Regola di propagazione

Una modifica al grafo, ai costi, all'euristica, all'ordine dei figli o alle condizioni di ottimalità riapre codice, visuali e audit.
