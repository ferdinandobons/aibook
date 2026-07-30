# Audit ATT-01

## Stato

- File esaminato: `candidate-v2.png`
- Dimensioni: `1600 × 900`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta
- Versione precedente: `candidate-v1.png`, rimossa perché corrotta e non revisionabile

## Domanda unica

Perché una rappresentazione fissa non basta quando query diverse devono combinare le stesse value in modo diverso?

## Registro delle iterazioni

| Versione | Esito | Problemi individuati | Correzioni applicate |
|---|---|---|---|
| v1 | respinta | Blob PNG corrotto; frecce dal contesto ai box `query q₁/q₂` interpretabili come generazione delle query; testo troppo vicino ai contenitori | Rimossa dal branch |
| v2 | validata tecnicamente | Nessun difetto bloccante rilevato dopo il secondo audit completo | Query trasformate in intestazioni di riga; contesto duplicato come `c per q₁` e `c per q₂`; box ampliati; testo ridisposto; connessioni separate |

## Audit tecnico

- [x] Le value disponibili sono identiche nei due pannelli.
- [x] Il pannello sinistro mostra lo stesso vettore `c` usato nei due casi, senza rappresentarlo come sorgente delle query.
- [x] Nel pannello destro `q₁` e `q₂` sono intestazioni di riga separate dai coefficienti.
- [x] I coefficienti della riga `q₁` sommano a `1,00`.
- [x] I coefficienti della riga `q₂` sommano a `1,00`.
- [x] Le due righe producono output distinti `c₁` e `c₂`.
- [x] Ogni linea parte e termina sul componente previsto.
- [x] Nessuna linea attraversa un box o sembra una giunzione non dichiarata.

## Audit di contenimento del testo

- [x] Tutti i caratteri restano dentro il proprio contenitore.
- [x] Nessuna label tocca o oltrepassa un bordo.
- [x] Nessun testo invade celle o box adiacenti.
- [x] Pedici e glifi sono integralmente visibili.
- [x] Il padding interno è visibile su tutti i lati.
- [x] Il controllo è stato eseguito sull'immagine raster effettiva.
- [x] Il testo resta leggibile alla dimensione prevista per la review GitHub.

## Provenienza della produzione

La composizione è stata iterata con lo strumento immagini. Per garantire testo, coefficienti e collegamenti esatti, il candidato revisionabile è stato rasterizzato in PNG con il renderer deterministico `scripts/render_attention_visuals.py`. Il renderer interrompe l'esecuzione quando un testo non entra nel proprio box.

## Verdetto

`ATT-01` può essere sottoposta alla revisione autoriale. Il nome resta `candidate-v2.png` finché non viene approvata dal committente; soltanto dopo l'approvazione potrà diventare `final.png`.
