# Audit del testo. Capitolo 3

## Stato

- Capitolo: `CH-P01-LIFECYCLE`
- Versione candidata: `0.2.0-rc1`
- Data: 30 luglio 2026
- Protocollo: `docs/02_STILE_E_QA_TESTO.md`
- Fonti e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale: **superato**
- Esito didattico: **superato**
- Esito editoriale e linguistico: **superato**
- Esito per lettore non esperto: **superato**
- Codice: **quattro test superati**
- Visuali: **validate tecnicamente**
- Review autoriale: aperta

## Oggetto continuo

La richiesta `Il pacco non è arrivato` attraversa definizione del problema, dati, training, valutazione, integrazione, deployment, monitoraggio, aggiornamento e ritiro. Il capitolo non sostituisce l'esempio con una pipeline astratta nei passaggi centrali.

## Review didattica

- [x] Il problema viene definito prima di scegliere dati o architettura.
- [x] Dataset e split vengono spiegati prima dello snippet.
- [x] Training, validation e test hanno ruoli distinti.
- [x] Deployment, serving e inference non sono usati come sinonimi.
- [x] Il checkpoint resta distinto dalla versione completa del sistema.
- [x] Drift e perdita di qualità non vengono trattati come equivalenti.
- [x] Aggiornamento, rollback e ritiro chiudono il ciclo senza presentare il deployment come fase finale.
- [x] Il lettore può ricostruire il ciclo saltando codice e note avanzate.

## Review editoriale e linguistica

- [x] Le sezioni seguono problemi reali e non campi di una checklist.
- [x] I periodi alternano spiegazione, esempio e conseguenza.
- [x] Il gergo viene definito nel punto d'uso.
- [x] Le cautele tecniche sono collocate vicino al claim che limitano.
- [x] Le fonti non interrompono il filo più del necessario.
- [x] Il testo distingue chiaramente fatti documentati, convenzioni editoriali ed esempio sintetico.
- [x] La lettura ad alta voce non ha evidenziato calchi o periodi eccessivamente compressi.

## Audit fattuale e temporale

- [x] NIST AI RMF è usato come framework di gestione del rischio e non come unica tassonomia possibile.
- [x] Datasheets e model cards sono descritti come documentazione, non come garanzia di qualità.
- [x] I lavori su debito tecnico e pratica industriale sostengono le dipendenze di sistema citate.
- [x] TFX è presentato come caso di piattaforma, non come requisito universale.
- [x] Le definizioni di data drift e concept drift non trasformano un segnale statistico in prova causale.
- [x] I risultati numerici del capitolo sono marcati come sintetici e illustrativi.

## Audit matematico e del codice

- [x] Train, validation e test sono disgiunti e coprono l'insieme previsto.
- [x] Il learning rate viene scelto sulla validation.
- [x] Il test viene consultato dopo la selezione del candidato.
- [x] La metrica di spostamento standardizzato usa media di training e deviazione standard con soglia minima.
- [x] Il testo non presenta la metrica come dimostrazione di concept drift o perdita di accuratezza.
- [x] Quattro test automatici risultano superati nel run registrato.
- [x] Nessuna nuova esecuzione è dichiarata dopo modifiche esclusivamente editoriali.

## Audit delle visuali

- [x] `LIFE-01` rappresenta otto fasi e relativi artefatti.
- [x] `LIFE-01` mostra il ritorno dall'aggiornamento alla definizione del problema.
- [x] `LIFE-02` contiene il modello dentro il confine del sistema.
- [x] `LIFE-02` separa checkpoint, versione distribuita, dati, strumenti, regole e monitoraggio.
- [x] Sfondo, contenimento, frecce e gerarchia tipografica rispettano `docs/03_VISUALI.md`.

## Difetti bloccanti rimasti

Nessuno noto nella candidatura interna. Rimane l'approvazione autoriale del testo, delle visuali e del livello di dettaglio.

## Esito

Il Capitolo 3 può passare alla revisione autoriale come candidatura `0.2.0-rc1`. Ogni modifica sostanziale successiva riapre audit incrociato, review linguistica e controllo delle visuali.
