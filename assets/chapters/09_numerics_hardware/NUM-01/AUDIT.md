# Audit visuale `NUM-01`

## Stato

- Candidata: `candidate-v1.png`
- Dimensioni previste: `1800 × 1000`
- Esito tecnico: **validata dopo seconda iterazione locale**
- Materializzazione nel branch: eseguita e collegata a `chapters/09_numerics_hardware/CHAPTER.md`
- Approvazione autoriale: aperta

## Iterazioni

### Tentativo con strumento immagini

Respinto. L'output mostrava una dashboard che dichiarava falsamente il completamento del libro e non conteneva i quattro dtype richiesti.

Difetti bloccanti:

- domanda visuale ignorata;
- stato del progetto inventato;
- nessun confronto numerico;
- violazione del divieto di dashboard editoriale.

### Renderer raster v1

Respinto. I box del significando oltrepassavano il bordo destro delle schede e invadevano lo spazio adiacente.

### Renderer raster v2

Correzioni:

- ridotte le larghezze dei tre segmenti;
- eliminati i residui esterni ai pannelli;
- ripristinati i bordi verticali delle schede;
- ricontrollati valori e testi.

## Audit tecnico

- [x] quattro dtype presenti;
- [x] bit di segno, esponente e significando corretti;
- [x] byte per elemento corretti;
- [x] `eps` e massimo finito coerenti con `torch.finfo`;
- [x] bfloat16 non rappresentato come equivalente a float16;
- [x] nessuna promessa di prestazioni;
- [x] messaggio finale coerente con il capitolo.

## Audit compositivo

- [x] sfondo bianco puro;
- [x] schede parallele senza gerarchia falsa;
- [x] testo interamente nei contenitori;
- [x] padding visibile;
- [x] nessuna sovrapposizione tra schede;
- [x] colore non unico portatore del significato;
- [x] leggibilità alla dimensione di review.

## Verdetto

La seconda iterazione è tecnicamente idonea. Il file resta candidato fino all'approvazione autoriale.
