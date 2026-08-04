# Specifica visuale FACTUALITY-02

- modello compositivo: calibration_map
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale failure o confronto separa Astensione da Verifica e retrieval?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una risposta con evidenza, confidenza e possibilità di errore
- input: claim, predizione, fonti e score di confidenza
- output: risposta supportata o astensione motivata
- nodi locali: Astensione: Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto.; Verifica e retrieval: La provenienza deve restare tracciabile.
- limite visualizzato: confidenza alta non certifica la verità fattuale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
