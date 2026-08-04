# Specifica visuale FACTUALITY-01

- modello compositivo: claim_evidence
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale percorso collega Correttezza e supporto a Calibrazione nel capitolo 84?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una risposta con evidenza, confidenza e possibilità di errore
- input: claim, predizione, fonti e score di confidenza
- output: risposta supportata o astensione motivata
- nodi locali: Correttezza e supporto: Una frase può essere vera senza essere sostenuta dal contesto fornito, oppure fedele al co.; Hallucination: La tassonomia deve precedere la metrica.; Calibrazione: Probabilità del token, score di un verifier e frequenza empirica devono essere collegati c.
- limite visualizzato: confidenza alta non certifica la verità fattuale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
