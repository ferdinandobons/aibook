# Audit visuale `SUP-02`

- file esaminato: `candidate-v1.png`
- dimensioni: `1800 × 1000`
- decodifica PNG: superata
- sfondo: bianco puro
- contenimento delle matrici e delle label: superato
- composizione: due pannelli comparabili e una fascia inferiore per le slice
- esito tecnico: **validata tecnicamente**
- approvazione autoriale: aperta

La differenza tra falsi positivi e falsi negativi è leggibile dalla posizione nelle matrici e dal costo riportato, non soltanto dal colore.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
