# Specifica visuale LOOP-01

- modello compositivo: agent_loop
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale percorso collega Osservare e aggiornare lo stato a Agire nel capitolo 69?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato di una traiettoria agentica
- input: osservazione, piano, azione e risultato del tool
- output: stato successivo o arresto motivato
- nodi locali: Osservare e aggiornare lo stato: Un agente riceve input, risultato dei tool e memoria.; Pianificare: Un piano scompone il compito in passi e dipendenze.; Agire: Ogni azione usa un tool o modifica un ambiente.
- limite visualizzato: ogni side effect deve avere precondizioni e verifica
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
