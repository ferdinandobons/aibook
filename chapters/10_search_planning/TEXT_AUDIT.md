# Audit del testo. Capitolo 10

## Stato

- Versione corrente: `0.2.0-rc1`
- Data: 31 luglio 2026
- Esito fattuale: **superato**
- Esito algoritmico: **superato**
- Esito del codice: **superato, sei test**
- Esito didattico: **superato dopo seconda lettura**
- Gate anti-template: **superato**
- Esito editoriale e linguistico: **superato**
- Chiarezza per lettore non esperto: **superata**
- Visuali: **validate tecnicamente dopo iterazione**
- Revisione autoriale: aperta

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

## Review editoriale e linguistica

Correzioni applicate:

- evitata una rassegna enciclopedica di algoritmi;
- usato il workflow della spedizione come oggetto continuo;
- riuniti completezza, ottimalità e costo nei rispettivi contesti;
- separati planning, generazione di testo ed esecuzione;
- limitati i dettagli storici alle transizioni necessarie;
- mantenuto il caso base prima di chance nodes e informazione incompleta;
- spiegata MCTS prima di citare le reti neurali;
- rimossi confronti di prestazione non misurati;
- controllati ritmo, referenti e leggibilità ad alta voce;
- mantenuta una struttura in prosa, senza esporre lo scaffold interno.

## Controllo incrociato

- [x] grafo, costi ed euristica coincidono con lo snippet;
- [x] piano ottimo e ordine delle espansioni coincidono con l'output;
- [x] ammissibilità e consistenza sono testate;
- [x] game tree e ordine dei figli coincidono con il codice;
- [x] conteggi 6 e 5 delle foglie sono testati;
- [x] claim storici associati a fonti primarie;
- [x] concetti differiti non sono anticipati come meccanismi completi;
- [x] testo, visuali e codice usano gli stessi stati, costi e valori.

## Visuali

La candidata image-gen è stata respinta perché mostrava una dashboard del progetto e inventava progressi editoriali.

### `SEARCH-01`

- il raster iniziale è stato respinto per collegamenti lunghi ambigui;
- la seconda composizione instrada gli archi sopra o sotto i nodi;
- costi, cammino ottimo e ordini di espansione sono verificati;
- esito tecnico positivo.

### `SEARCH-02`

- il raster iniziale nascondeva il valore della foglia potata;
- la seconda composizione mantiene leggibile il valore 9 e distingue il ramo non visitato;
- valori propagati e conteggi delle foglie sono verificati;
- esito tecnico positivo.

## Codice

Lo snippet e i test sono stati rieseguiti in un processo Python pulito il 31 luglio 2026. Sei test risultano superati. Il caso non viene presentato come benchmark generale.

## Elementi aperti

- materializzazione automatica dei due PNG nel feature branch;
- revisione autoriale del testo e delle figure;
- eventuali correzioni;
- rinomina in `final.png`;
- congelamento con data e commit.

## Verdetto

La candidatura `0.2.0-rc1` supera i gate fattuali, algoritmici, didattici, anti-template, editoriali, linguistici, di accessibilità e di coerenza interna. Può essere sottoposta alla revisione autoriale non appena i PNG generati dal workflow risultano presenti nel branch.
