# Specifica visuale EVAL-01

- modello compositivo: trajectory_eval
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale percorso collega Traiettorie come dati a RL in ambienti nel capitolo 71?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: traiettorie agentiche usate come dati e valutazione
- input: task, trace, policy, outcome e costo
- output: score di task, violazioni e failure per step
- nodi locali: Traiettorie come dati: Osservazioni, azioni, tool result e reward formano esempi sequenziali.; Imitation e SFT: Traiettorie riuscite possono essere imitate.; RL in ambienti: Reward verificabili o simulati aggiornano policy multi-step.
- limite visualizzato: task riuscito e traiettoria sicura sono criteri distinti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
