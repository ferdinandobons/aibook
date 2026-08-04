# Audit visuale `INFO-01`

- file esaminato: `candidate-v1.png`
- dimensioni: `1800 × 1000`
- decodifica PNG: superata
- sfondo: bianco puro
- contenimento del testo: superato
- composizione: due righe parallele con ordine logits → softmax → probabilità target → NLL
- esito tecnico: **validata tecnicamente**
- approvazione autoriale: aperta

La revisione raster conferma che il caso corretto e quello errato sono confrontabili senza sovrapposizioni. La differenza di loss è attribuita alla probabilità della classe target, non al solo colore.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
