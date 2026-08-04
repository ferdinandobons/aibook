# Specifica visuale FACTUALITY-02

- modello compositivo: calibration_map
- domanda principale: Quale controllo collega «Astensione» a «Verifica e retrieval» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una risposta con evidenza, confidenza e possibilità di errore
- input: claim, predizione, fonti e score di confidenza
- output: risposta supportata o astensione motivata
- nodi locali: Astensione: Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. Coverage e…; Verifica e retrieval: Fonti esterne possono aumentare supporto, ma retrieval e generazione hanno failure mode…
- limite visualizzato: confidenza alta non certifica la verità fattuale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
