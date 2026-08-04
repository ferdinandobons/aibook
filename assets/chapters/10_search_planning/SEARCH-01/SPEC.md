# Specifica visuale `SEARCH-01`

## Identità

- Capitolo: `CH-P03-SEARCH-PLANNING`
- Famiglia: grafo tecnico con confronto algoritmico
- Orientamento: orizzontale
- File candidato: `candidate-v2.png`
- Canvas: `1800 × 1000`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Come può A* espandere meno stati di uniform-cost mantenendo lo stesso piano ottimo?

## Contenuto obbligatorio

- stesso grafo e stessi costi dello snippet;
- piano ottimo evidenziato: `message_received -> order_identified -> tracking_checked -> delay_confirmed -> ticket_opened`;
- costo totale `6`;
- uniform-cost: otto stati espansi;
- A*: cinque stati espansi;
- rami alternativi e costi leggibili;
- nota che il conteggio dipende dal grafo, dall'euristica e dal tie-breaking.

## Layout

- grafo a sinistra;
- confronto degli ordini di espansione a destra;
- cammino ottimo in verde;
- nodi del cammino in blu e goal in verde;
- archi alternativi in grigio, ticket diretto in ambra;
- collegamenti lunghi instradati fuori dai nodi;
- etichette dei costi separate dagli archi;
- testo integralmente nei contenitori.

## Provenienza

I dati derivano da `SNIP-SEARCH-001` e dai relativi test. Il PNG raster è prodotto da `scripts/generate_search_visuals.py`; non viene usato SVG.
- domanda principale: Quale trasformazione centrale rende osservabile «Dal problema allo spazio degli stati» nel capitolo 10?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
