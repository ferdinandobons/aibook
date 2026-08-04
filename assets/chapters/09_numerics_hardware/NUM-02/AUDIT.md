# Audit visuale `NUM-02`

## Stato

- Candidata: `candidate-v1.png`
- Dimensioni previste: `1800 × 1000`
- Esito tecnico: **validata dopo seconda iterazione locale**
- Materializzazione nel branch: eseguita e collegata a `chapters/09_numerics_hardware/CHAPTER.md`
- Approvazione autoriale: aperta

## Prima iterazione raster

La struttura era corretta, ma il loop inferiore poteva essere interpretato in modo ambiguo:

- la freccia rossa non dichiarava esplicitamente che trasportava gradienti;
- la freccia blu poteva sembrare diretta anche all'input, anziché ai pesi.

## Seconda iterazione

Sono state aggiunte le etichette:

- `gradienti` sul collegamento backward-optimizer;
- `pesi aggiornati` sul ritorno optimizer-parametri.

## Audit tecnico

- [x] autocast distinto da loss scaling;
- [x] precisione ridotta associata agli operatori idonei;
- [x] riduzioni e loss indicate come possibili operazioni fp32;
- [x] backward separato dall'optimizer;
- [x] master weights e stato sensibile associati all'optimizer;
- [x] loop di aggiornamento attribuito ai pesi;
- [x] footer dichiara che il contratto non è universale.

## Audit compositivo

- [x] sfondo bianco puro;
- [x] ordine di lettura da sinistra a destra;
- [x] frecce principali non attraversano box;
- [x] label dei loop leggibili;
- [x] nessun testo fuori dal contenitore;
- [x] colori coerenti con lo standard;
- [x] nessun riferimento a prestazioni non misurate.

## Verdetto

La seconda iterazione è tecnicamente idonea. Resta candidata fino all'approvazione autoriale.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
