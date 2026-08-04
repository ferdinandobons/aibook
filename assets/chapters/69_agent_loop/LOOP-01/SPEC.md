# Specifica visuale LOOP-01

- modello compositivo: agent_loop
- domanda principale: Come si passa da «Osservare e aggiornare lo stato» a «Agire» mantenendo osservabile lo stato di una traiettoria agentica?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato di una traiettoria agentica
- input: osservazione, piano, azione e risultato del tool
- output: stato successivo o arresto motivato
- nodi locali: Osservare e aggiornare lo stato: Un agente riceve input, risultato dei tool e memoria. Lo stato operativo deve essere…; Pianificare: Un piano scompone il compito in passi e dipendenze. Il piano iniziale può essere rivisto…; Agire: Ogni azione usa un tool o modifica un ambiente. Parametri, autorizzazioni e costo devono…
- limite visualizzato: ogni side effect deve avere precondizioni e verifica
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
