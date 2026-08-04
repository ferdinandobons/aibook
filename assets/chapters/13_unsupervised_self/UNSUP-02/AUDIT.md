# Audit visuale `UNSUP-02`

- file esaminato: `candidate-v1.png`
- dimensioni: `1800 × 1000`
- decodifica PNG: superata
- sfondo: bianco puro
- contenimento del testo e delle connessioni: superato
- composizione: dato → maschera → input corrotto → encoder → decoder → loss
- esito tecnico: **validata tecnicamente**
- approvazione autoriale: aperta

La connessione inferiore riporta il target originale alle sole posizioni mascherate e non confonde il target autogenerato con una categoria annotata da una persona.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
