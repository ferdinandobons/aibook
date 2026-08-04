# Audit visuale `CALC-01`

## Stato

- File esaminato localmente: `candidate-v1.png`
- Dimensioni: `1800 × 1000`
- Sfondo: `#FFFFFF`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Iterazioni

| Iterazione | Esito | Problema | Decisione |
|---|---|---|---|
| image-gen 1 | respinta | dashboard sul completamento del libro, nessun grafo differenziale | scartata |
| image-gen 2 | respinta | dashboard editoriale con informazioni false sul progetto | scartata |
| image-gen 3 | respinta | nuova dashboard, nonostante la richiesta di sostituzione completa | scartata |
| raster v1 | validata | nessun difetto bloccante rilevato | candidata revisionabile |

## Verifica matematica

- [x] `z = 2,500000`.
- [x] `h = 0,986614`.
- [x] `y_hat = -0,490630`.
- [x] `L = 0,396611`.
- [x] `dL/dy_hat = -0,890630`.
- [x] `dL/dh = 0,623441`.
- [x] `dh/dz = 0,026592`.
- [x] `dL/dz = 0,016579`.
- [x] `dL/dw2 = -0,878708`.
- [x] `dL/db2 = -0,890630`.
- [x] `dL/dw1 = 0,033157`.
- [x] `dL/db1 = 0,016579`.

I valori sono stati confrontati con `SNIP-CALC-001`.

## Verifica dei collegamenti

- [x] forward orientato da sinistra a destra;
- [x] backward orientato da destra a sinistra;
- [x] derivate locali allineate alle operazioni corrette;
- [x] nessuna freccia attraversa un contenitore;
- [x] nessuna freccia sembra modificare un valore del forward;
- [x] optimizer separato dal grafo differenziale.

## Verifica del contenimento

- [x] nessun testo esce dai box;
- [x] nessun pedice o simbolo è troncato;
- [x] padding visibile;
- [x] footer separato dai gradienti;
- [x] leggibilità verificata sul raster effettivo.

## Verdetto

`CALC-01/candidate-v1.png` può essere sottoposta alla revisione autoriale. Diventerà `final.png` soltanto dopo approvazione.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
