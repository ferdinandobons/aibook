# Specifica visuale SCALE-01

- modello compositivo: scaling_balance
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale percorso collega Fit empirico a Esperimenti isoFLOP nel capitolo 34?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una curva empirica tra scala, compute e loss
- input: punti con parametri, token, FLOP e loss
- output: stima con intervallo osservato e costo
- nodi locali: Fit empirico: Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misura.; Allocazione compute-optimal: A budget fissato, modello e token competono.; Esperimenti isoFLOP: Configurazioni con compute simile rendono osservabile la loss minima per budget.
- limite visualizzato: un fit fuori dominio non è una legge garantita
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
