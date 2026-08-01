# Piano interno. Capitolo 10

## Identità

- `chapter_id`: `CH-P03-SEARCH-PLANNING`
- Parte: `P03`, Apprendimento, ottimizzazione e decisione
- Titolo: `Ricerca, pianificazione e giochi`
- Maturità: `CORE`
- Stato: fonti, claim e codice in produzione
- Domanda centrale: come scegliere una sequenza di azioni quando non è possibile provare esplicitamente ogni possibilità?
- Oggetto continuo: la richiesta `Il pacco non è arrivato`, trasformata in uno spazio di stati e azioni fino al goal `ticket_opened`
- Output finale: il lettore sa modellare stati, azioni, costi e goal; distingue BFS, uniform-cost, A*, planning esplicito, minimax, alpha-beta e Monte Carlo tree search

## Prerequisiti

- grafi, vettori e funzioni elementari;
- probabilità di base, Capitolo 7;
- nessuna conoscenza di reinforcement learning richiesta.

## Concetti differiti

- processi decisionali di Markov e Bellman completi, Capitolo 14;
- policy e value function apprese, Capitolo 14;
- agenti con tool e loop operativi, Parte P11;
- ricerca durante il decoding, Capitoli 53, 76 e 77;
- planning in ambienti parzialmente osservabili, approfondimenti successivi.

## Progressione didattica

1. un problema viene trasformato in stato iniziale, azioni, transizioni, costi e goal;
2. un albero di ricerca può contenere più nodi che rappresentano lo stesso stato;
3. una graph search conserva il costo migliore noto e gestisce duplicati;
4. BFS minimizza il numero di passi soltanto quando i costi sono uniformi;
5. uniform-cost estende sempre il cammino dal costo accumulato minore;
6. una euristica stima il costo rimanente;
7. A* ordina la frontiera con `f(n)=g(n)+h(n)`;
8. ammissibilità e consistenza collegano la stima all'ottimalità;
9. planning esplicito rappresenta precondizioni ed effetti delle azioni;
10. dynamic programming riusa sottoproblemi e introduce il principio di Bellman;
11. nei giochi, il valore dipende anche dalle azioni dell'avversario;
12. minimax alterna massimizzazione e minimizzazione;
13. alpha-beta evita rami che non possono cambiare la decisione;
14. Monte Carlo tree search distribuisce un budget tra espansione ed esplorazione;
15. policy e value apprese possono guidare la ricerca senza sostituirne il contratto;
16. il lettore distingue correttezza, ottimalità, completezza e costo computazionale.

## Visuali previste

### `SEARCH-01`. Uniform-cost e A* sullo stesso grafo

- Domanda: come una euristica può ridurre gli stati espansi senza cambiare il cammino ottimo?
- Contenuto: grafo del workflow, costi, valori `g`, `h` e `f`, ordine di espansione dei due algoritmi.
- Invariante: stesso grafo e stesso costo ottimo `6`.
- Confine: il vantaggio dipende dalla qualità della euristica e dall'ordine dei pareggi.

### `SEARCH-02`. Minimax e potatura alpha-beta

- Domanda: come si evita di valutare un ramo che non può cambiare la scelta del giocatore MAX?
- Contenuto: radice MAX, tre nodi MIN, foglie `[3,5]`, `[2,9]`, `[4,4]`; ramo `9` potato dopo che MIN osserva `2` con alpha già pari a `3`.
- Invariante: minimax e alpha-beta restituiscono valore `4`.

## Codice

### `SNIP-SEARCH-001`

- implementa A* con coda di priorità, costo migliore, parent e ricostruzione;
- esegue uniform-cost usando euristica zero;
- verifica lo stesso piano ottimo di costo `6`;
- registra cinque stati espansi da A* e otto da uniform-cost nel grafo illustrativo;
- implementa minimax e alpha-beta sul piccolo albero;
- verifica valore `4`, sei foglie per minimax e cinque per alpha-beta.

## Gate specifici

- non confondere nodo di ricerca e stato del problema;
- dichiarare le ipotesi sui costi non negativi;
- non dire che BFS minimizza il costo con archi pesati;
- non attribuire ottimalità ad A* senza condizioni sull'euristica e sulla gestione dei duplicati;
- non presentare una euristica appresa come automaticamente ammissibile;
- distinguere planning da mera generazione di testo;
- non presentare alpha-beta come cambiamento del valore minimax;
- non generalizzare risultati AlphaGo oltre i setup dei paper;
- separare budget di ricerca, qualità della stima e correttezza del modello dell'ambiente.
