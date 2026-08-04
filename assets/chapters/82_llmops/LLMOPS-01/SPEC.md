# Specifica visuale LLMOPS-01

- modello compositivo: llmops_loop
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale percorso collega Dalla versione al deployment a Edge nel capitolo 82?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un servizio LLM dalla versione al consumo
- input: modello, richieste, device, energia e monitor
- output: versione attiva, costo per richiesta e alert
- nodi locali: Dalla versione al deployment: Checkpoint, tokenizer, adapter, prompt e tool schema devono essere versionati come un'unic.; Osservabilità: Log, trace, metriche e feedback collegano input, modello, retrieval, tool e output senza e.; Edge: Dispositivi locali impongono memoria, batteria, termica e compatibilità dei kernel.
- limite visualizzato: un costo locale non descrive l'intero ciclo di vita
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
