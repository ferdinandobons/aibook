# Specifica visuale MEMORY-02

- modello compositivo: memory_lifecycle
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale failure o confronto separa Memoria episodica da Routing ibrido?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la decisione tra contesto, retrieval e memoria
- input: segmento, query, budget e durata
- output: contesto scelto, memoria aggiornata e costo
- nodi locali: Memoria episodica: Un sistema può salvare fatti o riassunti tra sessioni.; Routing ibrido: Una policy può scegliere cache, contesto, retrieval o memoria.
- limite visualizzato: memoria persistente e contesto temporaneo hanno politiche diverse
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
