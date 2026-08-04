# Audit ATT-02

## Stato

- File esaminato: `candidate-v2.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta
- Versione precedente: `candidate-v1.png`, rimossa perché corrotta e non revisionabile

## Domanda unica

Come una query produce un output attraverso prodotto scalare, scaling, softmax e somma pesata delle value?

## Ricalcolo indipendente

- `qK^T = [1, 0, 1]`.
- divisione per `sqrt(2)`: `[0,70710678, 0, 0,70710678]`.
- softmax: `[0,40111209, 0,19777581, 0,40111209]`.
- output con `V=[[1,0],[0,1],[1,1]]`: `[0,80222418, 0,59888791]`.
- valori visualizzati, arrotondati a tre decimali: `[0,401; 0,198; 0,401]` e `[0,802; 0,599]`.

## Registro delle iterazioni

| Versione | Esito | Problemi individuati | Correzioni applicate |
|---|---|---|---|
| v1 | respinta come file | Blob PNG corrotto; testo e numeri troppo vicini ai bordi in alcuni box | Rimossa dal branch |
| v2 | validata tecnicamente | Nessun difetto bloccante rilevato dopo il secondo audit completo | Sei passaggi separati; box ampliati; ritorni a capo intenzionali; output e shape separati; padding verificato |

## Audit tecnico

- [x] I prodotti scalari sono corretti.
- [x] Lo scaling è applicato agli score e non alle value.
- [x] I tre pesi della softmax sono non negativi.
- [x] I pesi arrotondati sommano a `1,000`.
- [x] La somma pesata produce l'output indicato.
- [x] La shape dell'output è `[d_v] = [2]`.
- [x] Le frecce seguono un solo ordine, da sinistra verso destra.
- [x] Nessun collegamento attraversa un box o suggerisce una dipendenza diversa da quella reale.

## Audit di contenimento del testo

- [x] Tutti i caratteri restano dentro il proprio contenitore.
- [x] Nessuna label tocca o oltrepassa un bordo.
- [x] Le righe di key e value hanno celle separate e padding visibile.
- [x] I valori di score, scaling e softmax sono completamente leggibili.
- [x] La formula della somma pesata resta interamente dentro il pannello.
- [x] Pedici, apici, simboli e accenti sono integralmente visibili.
- [x] Il controllo è stato eseguito sull'immagine raster effettiva.

## Provenienza della produzione

La composizione è stata iterata con lo strumento immagini. Per garantire valori, testo e collegamenti esatti, il candidato revisionabile è stato rasterizzato in PNG con il renderer deterministico `scripts/render_attention_visuals.py`. Il renderer interrompe l'esecuzione quando un testo non entra nel proprio box.

## Verdetto

`ATT-02` può essere sottoposta alla revisione autoriale. Il nome resta `candidate-v2.png` finché non viene approvata dal committente; soltanto dopo l'approvazione potrà diventare `final.png`.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
