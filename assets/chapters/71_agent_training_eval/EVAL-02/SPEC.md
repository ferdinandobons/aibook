# Specifica visuale EVAL-02

- modello compositivo: agent_scorecard
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale failure o confronto separa Benchmark agentici da Evaluation harness?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: traiettorie agentiche usate come dati e valutazione
- input: task, trace, policy, outcome e costo
- output: score di task, violazioni e failure per step
- nodi locali: Benchmark agentici: Success rate, step, costo e side effect devono essere misurati.; Evaluation harness: Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperime.
- limite visualizzato: task riuscito e traiettoria sicura sono criteri distinti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
