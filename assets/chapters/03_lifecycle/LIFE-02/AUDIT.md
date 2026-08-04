# Audit visuale `LIFE-02`

## Stato

- File: `candidate-v1.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Audit semantico

- [x] Il modello è rappresentato come componente interno al confine del sistema.
- [x] Il checkpoint e i parametri sono distinti dalla versione distribuita completa.
- [x] Input, prompt, retrieval, strumenti, regole, output e monitoraggio sono separati e nominati.
- [x] Le frecce non suggeriscono che il checkpoint contenga dati esterni o autorizzazioni.
- [x] Il footer esplicita che modifiche esterne al modello possono cambiare il comportamento osservato.
- [x] La figura non attribuisce al modello azioni eseguite da strumenti o policy.

## Audit geometrico e di contenimento

- [x] Sfondo bianco puro.
- [x] Tutto il testo resta nei rispettivi contenitori.
- [x] Nessuna freccia attraversa una label.
- [x] I collegamenti raggiungono il modello o il componente previsto senza incroci ambigui.
- [x] Il confine esterno del sistema è visibile e non tocca il footer.
- [x] Titolo, sottotitolo e simboli sono leggibili alla dimensione prevista.

## Provenienza

La figura è generata da `scripts/generate_lifecycle_visuals.py` con composizione deterministica e valori testuali controllati.

## Verdetto

La figura può essere inclusa nella candidatura del Capitolo 3. Resta `candidate-v1.png` fino all'approvazione autoriale.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
