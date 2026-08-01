# Fonti primarie e autorevoli. Capitolo 10

## Stato

- Ultima verifica web: 31 luglio 2026
- Ambito: shortest path, ricerca euristica, planning, game tree, Monte Carlo tree search e sistemi ibridi ricerca-reti neurali

## SRC-SEARCH-001. Dijkstra 1959

E. W. Dijkstra, *A Note on Two Problems in Connexion with Graphs*, Numerische Mathematik 1, 269-271, 1959.

DOI: https://doi.org/10.1007/BF01386390

Uso: cammini minimi con costi non negativi e principio della uniform-cost search.

## SRC-SEARCH-002. A*

Peter E. Hart, Nils J. Nilsson e Bertram Raphael, *A Formal Basis for the Heuristic Determination of Minimum Cost Paths*, IEEE Transactions on Systems Science and Cybernetics 4(2), 100-107, 1968.

DOI: https://doi.org/10.1109/TSSC.1968.300136

Uso: ricerca euristica, funzione di valutazione e proprietà di ottimalità nel perimetro del paper.

## SRC-SEARCH-003. Dynamic programming

Richard Bellman, *Dynamic Programming*, Princeton University Press, 1957.

Uso: principio di ottimalità e riuso dei sottoproblemi.

## SRC-SEARCH-004. STRIPS

Richard E. Fikes e Nils J. Nilsson, *STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving*, Artificial Intelligence 2, 189-208, 1971.

DOI: https://doi.org/10.1016/0004-3702(71)90010-5

Uso: stati, operatori, goal e pianificazione simbolica.

## SRC-SEARCH-005. PDDL

Drew McDermott et al., *PDDL: The Planning Domain Definition Language*, Technical Report, 1998.

Pagina ISI: https://www.isi.edu/results/publications/62624/pddl-the-planning-domain-definition-language/

Uso: separazione tra dominio, problema e descrizione delle azioni; standardizzazione dei benchmark di planning.

## SRC-SEARCH-006. Shannon 1950

Claude E. Shannon, *Programming a Computer for Playing Chess*, Philosophical Magazine 41(314), 256-275, 1950.

Uso: game tree, valutazione delle posizioni e ricerca selettiva nel gioco degli scacchi.

## SRC-SEARCH-007. Alpha-beta

Donald E. Knuth e Ronald W. Moore, *An Analysis of Alpha-Beta Pruning*, Artificial Intelligence 6(4), 293-326, 1975.

DOI: https://doi.org/10.1016/0004-3702(75)90019-3

Uso: correttezza e complessità della potatura alpha-beta.

## SRC-SEARCH-008. UCT

Levente Kocsis e Csaba Szepesvári, *Bandit Based Monte-Carlo Planning*, ECML 2006, 282-293.

DOI: https://doi.org/10.1007/11871842_29

Uso: Upper Confidence Bounds applied to Trees, consistenza e risultati nel perimetro del paper.

## SRC-SEARCH-009. AlphaGo

David Silver et al., *Mastering the Game of Go with Deep Neural Networks and Tree Search*, Nature 529, 484-489, 2016.

DOI: https://doi.org/10.1038/nature16961

Uso: integrazione di policy network, value network e Monte Carlo tree search.

## SRC-SEARCH-010. AlphaGo Zero

David Silver et al., *Mastering the Game of Go without Human Knowledge*, Nature 550, 354-359, 2017.

DOI: https://doi.org/10.1038/nature24270

Uso: self-play, rete policy-value e tree search nel setup del paper.

## SRC-SEARCH-011. Testo di riferimento

Stuart Russell e Peter Norvig, *Artificial Intelligence: A Modern Approach*, quarta edizione, Pearson, 2021.

Uso: tassonomia didattica di search, planning e games; non sostituisce i paper originali nei claim storici.

## Regola d'uso

- Le proprietà di ottimalità vengono dichiarate con le rispettive ipotesi.
- Un risultato su un gioco non viene generalizzato a planning in ambienti reali.
- Le euristiche apprese non vengono descritte come ammissibili senza prova.
- I valori eseguiti del capitolo derivano soltanto da `SNIP-SEARCH-001`.
