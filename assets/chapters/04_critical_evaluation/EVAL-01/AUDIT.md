# Audit visuale `EVAL-01`

## Stato

- File: `candidate-v1.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Audit semantico

- [x] Gli otto controlli sono presentati in ordine causale.
- [x] La baseline precede la conclusione sul miglioramento.
- [x] Slice e costi restano distinti dalla metrica aggregata.
- [x] Variabilità e controlli precedono il claim.
- [x] Il footer chiarisce che un punteggio corretto può sostenere un claim troppo ampio.
- [x] Nessun box è presentato come garanzia isolata di validità.

## Audit geometrico e stilistico

- [x] Sfondo bianco puro.
- [x] Testo interamente nei contenitori.
- [x] Padding visibile.
- [x] Frecce senza incroci o giunzioni ambigue.
- [x] Ordine di lettura evidente dalla riga superiore a quella inferiore.
- [x] Titolo, sottotitolo e footer leggibili alla dimensione editoriale.

## Provenienza

La figura è generata da `scripts/generate_evaluation_visuals.py` mediante layout e testo deterministici.

## Verdetto

La figura può essere inclusa nella candidatura del Capitolo 4. Resta `candidate-v1.png` fino all'approvazione autoriale.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
