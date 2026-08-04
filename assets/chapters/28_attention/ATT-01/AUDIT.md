# Audit ATT-01

## Stato

- File esaminato: `candidate-v4.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente dopo refake**
- Approvazione autoriale: aperta
- Versioni precedenti: `candidate-v1.png` corrotta; `candidate-v2.png` tecnicamente valida ma con lessico non più coerente con la prosa; `candidate-v3.png` respinta dopo la revisione raster per occlusione e composizione incoerente con il sorgente

## Domanda unica

Perché una rappresentazione fissa non basta quando posizioni diverse devono combinare gli stessi vettori in modo diverso?

## Registro delle iterazioni

| Versione | Esito | Problemi individuati | Correzioni applicate |
|---|---|---|---|
| v1 | respinta | blob PNG corrotto; frecce interpretabili come generazione delle query; testo troppo vicino ai contenitori | rimossa dal branch |
| v2 | validata tecnicamente | etichette `consumer 1/2` non coerenti con la nuova prosa | query trasformate in intestazioni di riga; connessioni separate; aperta la revisione lessicale |
| v3 | respinta | il raster effettivo mostrava un pannello sovrapposto e contenuto occluso, nonostante il controllo testuale del generatore risultasse positivo | sostituita da una nuova rasterizzazione code-native |
| v4 | validata tecnicamente | nessun difetto bloccante rilevato nel raster; coefficienti coerenti con la specifica | pannello sinistro e destro ricostruiti; q₂ normalizzata a `0,05`, `0,15`, `0,80`; RGB e dimensione standard `1800 × 1000` |

## Audit tecnico

- [x] I vettori disponibili sono identici nei due pannelli.
- [x] Il pannello sinistro mostra lo stesso vettore `c` usato da due posizioni.
- [x] Il pannello destro presenta `q₁` e `q₂` come righe separate.
- [x] I coefficienti della riga `q₁` sono `0,10`, `0,60`, `0,30` e sommano a `1,00`.
- [x] I coefficienti della riga `q₂` sono `0,05`, `0,15`, `0,80` e sommano a `1,00`.
- [x] Le due righe producono output distinti `c₁` e `c₂`.
- [x] Ogni linea parte e termina sul componente previsto.
- [x] Nessuna linea attraversa un box o sembra una giunzione non dichiarata.
- [x] L'invariante in fondo coincide con la prosa del capitolo.

## Audit di contenimento del testo

- [x] Tutti i caratteri restano dentro il proprio contenitore.
- [x] Nessuna label tocca o oltrepassa un bordo.
- [x] Nessun testo invade celle o box adiacenti.
- [x] Pedici e glifi sono integralmente visibili.
- [x] Il padding interno è visibile su tutti i lati.
- [x] Il controllo è stato eseguito sull'immagine raster effettiva.
- [x] Il testo resta leggibile alla dimensione prevista per la review GitHub.

## Provenienza della produzione

La composizione è stata iterata con lo strumento immagini. Per rendere esatti testo, coefficienti e collegamenti, la candidata revisionabile è stata rasterizzata e verificata con `scripts/generate_book_visuals.py`. Il generatore interrompe l'esecuzione quando un testo supera il numero di righe previsto e verifica che il PNG sia decodificabile.

## Verdetto

`ATT-01/candidate-v4.png` può essere sottoposta alla revisione autoriale. Il nome resta `candidate-v4.png` fino all'approvazione; soltanto dopo potrà diventare `final.png`.
