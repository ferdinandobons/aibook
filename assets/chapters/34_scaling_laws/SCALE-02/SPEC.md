# Specifica visuale SCALE-02

- modello compositivo: budget_allocation
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale failure o confronto separa Extrapolation da Training e inference cost?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una curva empirica tra scala, compute e loss
- input: punti con parametri, token, FLOP e loss
- output: stima con intervallo osservato e costo
- nodi locali: Extrapolation: Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala.; Training e inference cost: Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizi.
- limite visualizzato: un fit fuori dominio non è una legge garantita
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
