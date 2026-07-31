# Audit visuale `KNOW-02`

## Stato

- File revisionato localmente: `candidate-v3.png`
- Dimensioni: `1800 × 1000`
- SHA-256 locale: `f0eefab8d1ebe74c626c194ba4497c4f20badf13d9d38e127d5eb528830c9d60`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Iterazioni

### Raster v1

Il file era decodificabile localmente, ma la prima esportazione non veniva aperta dal visualizzatore del container. È stata riesportata senza ottimizzazione per escludere un problema del file.

### Raster v2

Respinta semanticamente. Il box `P(H=1)=0,20` era collocato tra `H` e i figli e poteva essere interpretato come un nodo della rete. Il footer usava inoltre un simbolo non disponibile nel font.

### Raster v3

Il prior è diventato una annotazione laterale collegata con linea tratteggiata. Le frecce vanno direttamente da `H` a `M` e `T`. Il footer usa una frase in italiano invece del simbolo non supportato.

## Verifica numerica

- [x] prior `0,20`;
- [x] likelihood del messaggio `0,80` e `0,10`;
- [x] likelihood del tracking `0,70` e `0,20`;
- [x] numeratore `0,112` per `H=1`;
- [x] numeratore `0,016` per `H=0`;
- [x] denominator `0,128`;
- [x] posterior `0,875`.

## Verifica semantica

- [x] grafo `H -> M`, `H -> T`;
- [x] prior distinto da un nodo casuale;
- [x] tabelle condizionali associate ai figli;
- [x] indipendenza condizionata dichiarata come assunzione;
- [x] nessun claim causale automatico;
- [x] evidenza distinta dai parametri del modello.

## Verifica visuale

- [x] sfondo bianco puro;
- [x] frecce con direzione chiara;
- [x] nessuna linea attraversa i box;
- [x] testo contenuto;
- [x] formule e decimali leggibili;
- [x] footer separato;
- [x] nessun glifo mancante.

## Verdetto

`KNOW-02/candidate-v3.png` può essere inserita nella candidatura del capitolo e sottoposta alla revisione autoriale.
