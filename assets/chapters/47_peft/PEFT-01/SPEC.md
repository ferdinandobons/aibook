# Specifica visuale PEFT-01

- modello compositivo: low_rank_update
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Parametri congelati e adattamento a LoRA nel capitolo 47?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: l'aggiornamento adattivo rispetto ai pesi congelati
- input: peso W, matrice A e B, rank e quantizzazione
- output: delta W e checkpoint adattatore
- nodi locali: Parametri congelati e adattamento: PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata.; Adapter: Blocchi bottleneck vengono inseriti nel percorso residuale.; LoRA: Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può es.
- limite visualizzato: il delta non è il modello completo e va valutato sullo stesso base model
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
