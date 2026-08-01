# Audit visuale `SUP-01`

## Stato

- File esaminato: `candidate-v1.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente dopo seconda iterazione**
- Approvazione autoriale: aperta

## Prima iterazione

La composizione iniziale distingueva i tre split, ma non rendeva abbastanza visibile che il modello appreso viene applicato anche alla validation e poi al test. Il collegamento poteva far leggere la selezione della soglia come un processo indipendente dal modello.

## Correzione

- aggiunta una freccia verticale dal modello appreso alla soglia selezionata;
- aggiunta una freccia dalla soglia al test finale;
- mantenute separate le frecce provenienti da validation e test;
- nessun collegamento rientra nel training.

## Verifica semantica

- [x] train aggiorna i parametri;
- [x] validation sceglie configurazione e soglia;
- [x] test valuta dopo la selezione;
- [x] il modello è fissato prima della validation;
- [x] la soglia è fissata prima del test;
- [x] nessun claim di generalizzazione reale.

## Verifica numerica

- [x] train `120`;
- [x] validation `50`;
- [x] test `50`;
- [x] soglia `0,30`;
- [x] costo `FN=5`, `FP=1`;
- [x] accuracy test `0,900`;
- [x] recall test `0,913`;
- [x] costo test `13`.

## Verifica visuale

- [x] sfondo bianco puro;
- [x] testo contenuto;
- [x] frecce senza incroci;
- [x] colori coerenti e non unici portatori del significato;
- [x] padding sufficiente;
- [x] ordine di lettura chiaro.

## Verdetto

La figura può entrare nella candidatura del capitolo e passare alla revisione autoriale.
