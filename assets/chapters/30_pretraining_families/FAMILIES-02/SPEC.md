# Specifica visuale FAMILIES-02

- modello compositivo: objective_map
- domanda principale: Quale controllo collega «Masked, causal e span corruption» a «Architettura e obiettivo» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una famiglia architetturale legata al proprio obiettivo
- input: sequenza, mask e target di pretraining
- output: rappresentazione o distribuzione predittiva
- nodi locali: Masked, causal e span corruption: Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss.; Architettura e obiettivo: La forma del modello e l'obiettivo sono assi separati. Confrontarli richiede dati,…
- limite visualizzato: architettura e objective non possono essere scambiati senza cambiare il compito
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
