# Specifica visuale `SEARCH-01`

## Domanda unica

Come può A* espandere meno stati di uniform-cost mantenendo lo stesso piano ottimo?

## Contenuto obbligatorio

- stesso grafo e stessi costi dello snippet;
- piano ottimo evidenziato: `message_received -> order_identified -> tracking_checked -> delay_confirmed -> ticket_opened`;
- costo totale `6`;
- uniform-cost: otto stati espansi;
- A*: cinque stati espansi;
- costi `g`, euristica `h` o priorità `f` leggibili almeno sui nodi del cammino ottimo;
- nota che il conteggio dipende da grafo, euristica e tie-breaking.

## Layout

- sfondo bianco puro;
- grafo a sinistra, confronto degli ordini a destra;
- archi non ottimali in grigio;
- cammino ottimo in verde o blu-verde;
- nessun arco attraversa un nodo;
- eventuali collegamenti lunghi devono usare percorsi ortogonali o essere riportati in una legenda separata;
- testo integralmente nei contenitori.

## Stato

Storyboard completo. Prima candidata dello strumento immagini respinta perché mostrava una dashboard del progetto. Renderer raster v1 presente, ma il raster deve ancora essere materializzato e sottoposto a audit geometrico prima dell'uso nel capitolo.
