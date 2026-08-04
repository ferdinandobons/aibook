# Audit visuale `INFO-02`

- file esaminato: `candidate-v1.png`
- dimensioni: `1800 × 1000`
- decodifica PNG: superata
- sfondo: bianco puro
- contenimento del testo e dei simboli: superato
- composizione: target e predizione alimentano la formula, poi la decomposizione è letta da sinistra a destra
- esito tecnico: **validata tecnicamente**
- approvazione autoriale: aperta

La notazione `q_i` e `p_i` è intenzionalmente ASCII nel raster per evitare glifi mancanti nei font di sistema, senza cambiare la formula descritta nella prosa.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
