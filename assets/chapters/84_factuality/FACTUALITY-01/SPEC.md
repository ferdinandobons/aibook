# Specifica visuale FACTUALITY-01

- modello compositivo: claim_evidence
- domanda principale: Come si passa da «Correttezza e supporto» a «Calibrazione» mantenendo osservabile una risposta con evidenza, confidenza e possibilità di errore?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una risposta con evidenza, confidenza e possibilità di errore
- input: claim, predizione, fonti e score di confidenza
- output: risposta supportata o astensione motivata
- nodi locali: Correttezza e supporto: Una frase può essere vera senza essere sostenuta dal contesto fornito, oppure fedele al…; Hallucination: Il termine copre errori diversi: entità inventate, attribuzioni scorrette,…; Calibrazione: Probabilità del token, score di un verifier e frequenza empirica devono essere collegati…
- limite visualizzato: confidenza alta non certifica la verità fattuale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
