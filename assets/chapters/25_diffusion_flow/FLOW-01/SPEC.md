# Specifica visuale FLOW-01

- modello compositivo: noise_path
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Corrompere e ricostruire a Parametrizzazioni epsilon, x0 e v nel capitolo 25?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un dato corrotto e il percorso di denoising
- input: x_0, rumore epsilon e timestep t
- output: stima del rumore e campione ricostruito
- nodi locali: Corrompere e ricostruire: La diffusione forward aggiunge rumore secondo uno schedule.; Score matching: Lo score è il gradiente del log-density rispetto ai dati perturbati.; Parametrizzazioni epsilon, x0 e v: Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambia.
- limite visualizzato: parametrizzazione e scheduler fanno parte del contratto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
