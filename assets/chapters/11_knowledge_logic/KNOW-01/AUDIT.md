# Audit visuale `KNOW-01`

## Stato

- File revisionato localmente: `candidate-v2.png`
- Dimensioni: `1800 × 1000`
- SHA-256 locale: `722a865a9b23c63c8cb2d147db5938a16041fbe03e1b82aa0b35cc47f04b7a7d`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Iterazioni

### Image-gen

Respinta. La candidata mostrava una dashboard sul completamento del libro e inventava percentuali e capitoli. Non rappresentava fatti, regole o conclusioni.

### Raster v1

Respinta. Il predicato lungo del primo fatto e il testo della seconda regola invadevano le aree riservate alle etichette `F1` e `R2`.

### Raster v2

I predicati lunghi sono stati spezzati in punti semantici e le aree testuali sono state spostate. Tutto il testo resta contenuto.

## Verifica logica

- [x] tre fatti iniziali corretti;
- [x] tre regole coerenti con lo snippet;
- [x] variabile `?ordine` usata in modo consistente;
- [x] tre conclusioni corrette;
- [x] ordine delle iterazioni compatibile con il forward chaining;
- [x] assenza distinta dalla negazione;
- [x] nessuna relazione causale suggerita.

## Verifica visuale

- [x] sfondo bianco puro;
- [x] tre colonne separate;
- [x] frecce orizzontali prive di incroci;
- [x] testo dentro i box;
- [x] etichette `F`, `R` e `D` leggibili;
- [x] predicati lunghi senza clipping;
- [x] footer separato dal flusso;
- [x] colore affiancato da titoli e label.

## Verdetto

`KNOW-01/candidate-v2.png` può essere inserita nella candidatura del capitolo e sottoposta alla revisione autoriale.
