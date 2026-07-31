# Audit del testo. Capitolo 10

## Stato

- Versione corrente: `0.1.0-draft1`
- Data: 31 luglio 2026
- Esito fattuale: **superato per il testo corrente**
- Esito algoritmico: **superato**
- Esito del codice: **superato, sei test**
- Esito didattico: **superato dopo seconda lettura**
- Esito editoriale e linguistico: **superato per la bozza**
- Visuali: storyboard e renderer presenti, raster da materializzare e revisionare
- Review autoriale: non aperta

## Review tecnica

- [x] stato distinto da nodo di ricerca;
- [x] tree search distinta da graph search;
- [x] BFS limitata ai costi uniformi per la garanzia sul costo;
- [x] uniform-cost associata a costi non negativi;
- [x] A* definita con `f=g+h`;
- [x] ammissibilità distinta dalla consistenza;
- [x] ottimalità dichiarata con ipotesi e gestione dei duplicati;
- [x] euristiche apprese non presentate come automaticamente ammissibili;
- [x] planning descritto con precondizioni ed effetti;
- [x] piano distinto dall'esecuzione e dal monitoraggio;
- [x] principio di Bellman usato nel caso deterministico e come ponte;
- [x] minimax limitato al caso base dichiarato;
- [x] alpha-beta descritta come riduzione del lavoro, non del valore;
- [x] MCTS presentata come famiglia selettiva con budget;
- [x] UCT associata alle condizioni del paper;
- [x] AlphaGo e AlphaGo Zero limitati ai rispettivi setup.

## Review per lettore non esperto

Il lettore deve poter ricostruire:

1. uno stato descrive una situazione, un nodo conserva anche il cammino;
2. meno azioni non significa sempre minor costo;
3. uniform-cost considera ciò che è già stato pagato;
4. A* aggiunge una stima di ciò che resta;
5. planning descrive azioni riutilizzabili e verificabili;
6. minimax considera la risposta dell'avversario;
7. alpha-beta evita lavoro che non cambia la decisione;
8. MCTS distribuisce un budget tra alternative.

Esito: positivo. I termini compaiono dopo il caso concreto e le formule non sono l'unico accesso ai concetti.

## Review editoriale

Correzioni applicate:

- evitata una rassegna enciclopedica di algoritmi;
- usato il workflow della spedizione come oggetto continuo;
- riuniti completezza, ottimalità e costo nei rispettivi contesti;
- separati planning, generazione di testo ed esecuzione;
- limitati i dettagli storici alle transizioni necessarie;
- mantenuto il caso base prima di chance nodes e informazione incompleta;
- spiegata MCTS prima di citare le reti neurali;
- rimossi confronti di prestazione non misurati.

## Controllo incrociato

- [x] grafo, costi ed euristica coincidono con lo snippet;
- [x] piano ottimo e ordine delle espansioni coincidono con l'output;
- [x] ammissibilità e consistenza sono testate;
- [x] game tree e ordine dei figli coincidono con il codice;
- [x] conteggi 6 e 5 delle foglie sono testati;
- [x] claim storici associati a fonti primarie;
- [x] concetti differiti non sono anticipati come meccanismi completi.

## Visuali

La candidata image-gen è stata respinta perché mostrava una dashboard del progetto e inventava progressi editoriali. `SEARCH-01` e `SEARCH-02` dispongono di renderer raster e storyboard, ma non sono ancora approvate:

- `SEARCH-01` richiede controllo geometrico degli archi e delle label;
- `SEARCH-02` richiede verifica del ramo potato e del conteggio delle foglie.

## Elementi aperti

- materializzare i due PNG nel feature branch;
- eseguire audit sul raster effettivo;
- rigenerare in caso di linee ambigue o overflow;
- inserire le figure nel capitolo;
- ripetere la lettura integrale;
- aprire la revisione autoriale.

## Verdetto

Testo, fonti, claim e codice sono pronti. Il capitolo resta una bozza completa ma non una release candidate finché le visuali non superano il gate.
