# Audit visuale `CALC-02`

## Stato

- File esaminato localmente: `candidate-v2.png`
- Dimensioni: `1800 × 1000`
- Sfondo: `#FFFFFF`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Iterazioni

| Versione | Esito | Difetto | Correzione |
|---|---|---|---|
| raster v1 | respinta | il footer copriva parzialmente i box `in uscita` | ridotte e riallineate le sezioni; aumentata la zona di sicurezza |
| raster v2 | validata | nessun difetto bloccante rilevato | candidata revisionabile |

## Verifica semantica

- [x] ogni nodo mostra gradiente in arrivo, derivata locale e gradiente in uscita;
- [x] il nodo affine distribuisce il gradiente a `h`, `w2` e `b2`;
- [x] le frecce `VJP` collegano nodi distinti senza attraversarli;
- [x] la differenziazione è separata dall'optimizer step;
- [x] nessun elemento suggerisce che l'optimizer calcoli le derivate.

## Verifica numerica

- [x] seme iniziale `1`;
- [x] `dL/dy_hat = -0,890630`;
- [x] `dL/dh = 0,623441`;
- [x] `dL/dw2 = -0,878708`;
- [x] `dL/db2 = -0,890630`;
- [x] `dh/dz = 0,026592`;
- [x] `dL/dz = 0,016579`.

I valori coincidono con `SNIP-CALC-001`.

## Verifica del contenimento

- [x] nessun testo esce dai box;
- [x] i segni negativi e i pedici sono interamente visibili;
- [x] il footer non sovrappone i pannelli;
- [x] le tre colonne mantengono la stessa gerarchia tipografica;
- [x] leggibilità verificata sul raster effettivo.

## Verdetto

`CALC-02/candidate-v2.png` può essere sottoposta alla revisione autoriale. Diventerà `final.png` soltanto dopo approvazione.
