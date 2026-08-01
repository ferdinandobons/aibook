# Audit visuale `INFO-02`

## Stato

- File esaminato localmente: `candidate-v1.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Verifica numerica

- [x] target `q=[0,90; 0,05; 0,05]`;
- [x] predizione `p=[0,7856; 0,1753; 0,0391]`;
- [x] `H(q)=0,394398`;
- [x] `KL(q||p)=0,071914`;
- [x] `H(q,p)=0,466311`;
- [x] somma dei primi due valori uguale al terzo entro l'arrotondamento.

## Verifica semantica

- [x] entropia del target separata dalla divergenza;
- [x] orientamento della KL corretto;
- [x] cross-entropy riceve entrambe le distribuzioni;
- [x] KL non chiamata distanza;
- [x] caso one-hot presentato come caso particolare;
- [x] NLL collegata al target one-hot.

## Verifica visuale

- [x] sfondo bianco puro;
- [x] barre proporzionali ai valori;
- [x] frecce non ambigue;
- [x] formula centrale contenuta;
- [x] fascia inferiore allineata;
- [x] nessun testo o simbolo troncato;
- [x] decimali con virgola nelle formule principali.

## Verdetto

`INFO-02/candidate-v1.png` può essere sottoposta alla revisione autoriale.
