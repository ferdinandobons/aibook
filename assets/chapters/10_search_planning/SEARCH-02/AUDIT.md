# Audit visuale `SEARCH-02`

## Stato

- File revisionato localmente: `candidate-v2.png`
- Dimensioni: `1800 × 1000`
- SHA-256 locale della composizione approvata: `a7428bd13c1c7fb786f2b90e97c933ae7b429573d0b9e49595730aa7034e3bb5`
- Esito tecnico: **validata tecnicamente**
- Collegamento in `CHAPTER.md`: eseguito
- Approvazione autoriale: aperta

## Iterazioni

### Image-gen

Respinta. La candidata mostrava una dashboard editoriale invece dell'albero minimax richiesto.

### Raster v1

Il ramo potato era visibile, ma la croce copriva il valore `9`. Questo rendeva difficile confrontare l'albero minimax completo con il lavoro effettivamente svolto da alpha-beta.

### Raster v2

Il valore `9` è ora leggibile in un box rosso. Il ramo è tratteggiato e una label esplicita indica `ramo potato`. Le croci ai margini non coprono il numero.

## Verifica algoritmica

- [x] radice MAX con valore 4;
- [x] nodi MIN con valori 3, 2 e 4;
- [x] foglie A pari a 3 e 5;
- [x] foglie B pari a 2 e 9;
- [x] foglie C pari a 4 e 4;
- [x] dopo A, `alpha=3`;
- [x] nel ramo B, il valore 2 rende irrilevante la visita della foglia 9;
- [x] minimax visita sei foglie;
- [x] alpha-beta ne visita cinque;
- [x] valore finale invariato, pari a 4.

## Verifica visuale

- [x] sfondo bianco puro;
- [x] gerarchia MAX, MIN e foglie leggibile;
- [x] ramo potato distinto dai rami valutati;
- [x] valore della foglia potata ancora visibile;
- [x] nessuna linea attraversa un box;
- [x] testo interamente contenuto;
- [x] conteggi separati dal corpo dell'albero;
- [x] nessun elemento editoriale estraneo.

## Verdetto

`SEARCH-02/candidate-v2.png` è collegata alla sezione visuale del capitolo e resta candidata fino alla revisione autoriale.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
