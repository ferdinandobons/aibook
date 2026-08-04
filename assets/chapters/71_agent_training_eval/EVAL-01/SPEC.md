# Specifica visuale EVAL-01

- modello compositivo: trajectory_eval
- domanda principale: Come si passa da «Traiettorie come dati» a «RL in ambienti» mantenendo osservabile traiettorie agentiche usate come dati e valutazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: traiettorie agentiche usate come dati e valutazione
- input: task, trace, policy, outcome e costo
- output: score di task, violazioni e failure per step
- nodi locali: Traiettorie come dati: Osservazioni, azioni, tool result e reward formano esempi sequenziali. Logging…; Imitation e SFT: Traiettorie riuscite possono essere imitate. Il dataset deve includere recovery, errori…; RL in ambienti: Reward verificabili o simulati aggiornano policy multi-step. Il modello può sfruttare…
- limite visualizzato: task riuscito e traiettoria sicura sono criteri distinti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
