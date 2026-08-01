# Audit visuale `INFO-01`

## Stato

- File esaminato localmente: `candidate-v1.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Verifica numerica

- [x] logits corretti `[2,0; 0,5; -1,0]`;
- [x] probabilità corrette `0,7856`, `0,1753`, `0,0391`;
- [x] probabilità target `0,785597`;
- [x] NLL corretta `0,241311`;
- [x] logits errati `[-1,0; 0,5; 2,0]`;
- [x] probabilità errate permutate;
- [x] probabilità target `0,039113`;
- [x] NLL errata `3,241311`.

## Verifica semantica

- [x] target invariato tra le due righe;
- [x] entropia uguale per permutazione della distribuzione;
- [x] cross-entropy collegata alla classe osservata;
- [x] previsione confidentemente errata non confusa con alta entropia;
- [x] logits distinti dalle probabilità.

## Verifica visuale

- [x] sfondo bianco puro;
- [x] ordine target, logits, softmax, `p(target)`, NLL;
- [x] frecce prive di incroci;
- [x] testo interamente contenuto;
- [x] decimali convertiti alla virgola dopo la prima revisione;
- [x] footer separato dai pannelli.

## Verdetto

`INFO-01/candidate-v1.png` può essere sottoposta alla revisione autoriale.
