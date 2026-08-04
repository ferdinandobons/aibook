# Specifica visuale EVAL-02

- modello compositivo: slice_scorecard
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale failure o confronto separa Agenti da Evaluation in production?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un sistema composto da modello, contesto, tool e interfaccia
- input: task, componenti, trace e policy
- output: score di sistema, failure e regressione
- nodi locali: Agenti: Successo, step, costo, side effect e recovery vengono misurati in ambienti versionati e re.; Evaluation in production: Shadow traffic, canary e monitoraggio collegano benchmark offline a distribuzioni reali se.
- limite visualizzato: misurare il modello isolato non misura il comportamento del sistema
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
