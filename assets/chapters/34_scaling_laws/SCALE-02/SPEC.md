# Specifica visuale SCALE-02

- modello compositivo: budget_allocation
- domanda principale: Quale controllo collega «Extrapolation» a «Training e inference cost» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una curva empirica tra scala, compute e loss
- input: punti con parametri, token, FLOP e loss
- output: stima con intervallo osservato e costo
- nodi locali: Extrapolation: Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala.; Training e inference cost: Una scelta compute-optimal per il training può non minimizzare costo e latenza del…
- limite visualizzato: un fit fuori dominio non è una legge garantita
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
