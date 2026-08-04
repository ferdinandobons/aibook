# Audit visuale LA-01

## Stato

- File: candidate-v1.png
- Dimensioni: 1800 per 1000 pixel
- Esito tecnico: validata tecnicamente
- Approvazione autoriale: aperta

## Iterazioni respinte

Tre generazioni precedenti dello strumento immagini sono state respinte perché mostravano roadmap, indici e stato del progetto invece del prodotto matriciale richiesto. Nessuna è stata pubblicata come asset del capitolo.

## Audit matematico

- [x] X ha shape 3 per 4 e contiene i valori dello snippet.
- [x] La matrice dei pesi trasposta ha shape 4 per 3 e valori coerenti con W.
- [x] L'intermedio contiene X moltiplicato per la matrice dei pesi trasposta, senza bias.
- [x] Il bias contiene 0,2, -0,1 e 0,3.
- [x] L'output finale coincide con lo snippet.
- [x] La dimensione feature pari a quattro è indicata come asse contratto.
- [x] Batch e classe restano nell'output.

## Audit geometrico e linguistico

- [x] Sfondo bianco puro.
- [x] Testo e matrici interamente nei box.
- [x] Nessuna label tocca il bordo.
- [x] Frecce senza incroci o arrivi ambigui.
- [x] Il bias è separato dall'intermedio.
- [x] La nota finale ricorda che le shape non sostituiscono la semantica degli assi.

## Provenienza

Dopo il fallimento delle candidate generate automaticamente, la figura è stata rasterizzata in PNG dal renderer deterministico `scripts/generate_linear_algebra_visuals.py`, partendo dallo storyboard revisionato. Non viene usato SVG.

## Verdetto

La figura può essere inclusa nella candidatura del Capitolo 5. Resta candidate-v1.png fino all'approvazione autoriale.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
