# Audit visuale `SEARCH-01`

## Stato

- File revisionato localmente: `candidate-v2.png`
- Dimensioni: `1800 × 1000`
- SHA-256 locale: `505fd11d305e487a3f1d8aaa56074f2ea02fa11719e885c320ce612368ef1bb1`
- Esito tecnico: **validata tecnicamente**
- Collegamento in `CHAPTER.md`: eseguito
- Approvazione autoriale: aperta

## Iterazioni

### Image-gen

Respinta. La candidata mostrava una dashboard sullo stato del libro e inventava progressi editoriali. Non rappresentava uniform-cost, A* o il grafo richiesto.

### Raster v1

Respinta durante la review geometrica. Alcuni archi lunghi attraversavano l'area centrale e rendevano poco chiara la loro origine.

### Raster v2

I collegamenti lunghi sono stati instradati sopra o sotto i nodi. I costi sono contenuti in label separate e il cammino ottimo resta leggibile senza nascondere i rami alternativi.

## Verifica algoritmica

- [x] grafo coerente con `SNIP-SEARCH-001`;
- [x] costi `1, 2, 1, 2` sul cammino ottimo;
- [x] costo totale `6`;
- [x] ticket diretto di costo `7`;
- [x] rami di pagamento e agente con i costi registrati;
- [x] uniform-cost espande otto stati;
- [x] A* espande cinque stati;
- [x] entrambi restituiscono lo stesso piano.

## Verifica visuale

- [x] sfondo bianco puro;
- [x] nessun arco attraversa un nodo;
- [x] partenza e arrivo dei collegamenti lunghi identificabili;
- [x] costi interamente visibili;
- [x] testo contenuto nei box;
- [x] ordine di espansione leggibile;
- [x] nessun elemento editoriale estraneo;
- [x] colore non usato come unico segnale.

## Verdetto

`SEARCH-01/candidate-v2.png` è collegata alla sezione visuale del capitolo e resta candidata fino alla revisione autoriale.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
