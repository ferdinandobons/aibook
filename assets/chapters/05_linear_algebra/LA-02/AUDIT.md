# Audit visuale LA-02

## Stato

- File: candidate-v1.png
- Dimensioni: 1800 per 1000 pixel
- Esito tecnico: validata tecnicamente
- Approvazione autoriale: aperta

## Audit matematico

- [x] La seconda riga è esattamente il doppio della prima.
- [x] Il pannello dichiara rango minore o uguale a due prima della stima numerica.
- [x] La decomposizione usa U, diagonale dei valori singolari e V trasposta.
- [x] Le shape mostrate sono corrette per la SVD ridotta della matrice quadrata 3 per 3.
- [x] I valori singolari corrispondono all'output eseguito dopo arrotondamento.
- [x] La terza componente è distinta come numericamente nulla, non esattamente assente in ogni precisione.
- [x] Il footer collega il rango numerico a scala, precisione e tolleranza.

## Audit geometrico e stilistico

- [x] Sfondo bianco puro.
- [x] Titoli, formule e valori restano nei contenitori.
- [x] Le barre non invadono le label.
- [x] Frecce senza incroci.
- [x] La terza componente è attraversata da una linea rossa e resta identificabile senza dipendere dal solo colore.
- [x] Il footer non si sovrappone ai pannelli.

## Provenienza

La figura è rasterizzata in PNG da `scripts/generate_linear_algebra_visuals.py` a partire dalla specifica revisionata. Non viene usato SVG.

## Verdetto

La figura può essere inclusa nella candidatura del Capitolo 5. Resta candidate-v1.png fino all'approvazione autoriale.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
