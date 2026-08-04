# Specifica visuale PEFT-01

- modello compositivo: low_rank_update
- domanda principale: Come si passa da «Parametri congelati e adattamento» a «LoRA» mantenendo osservabile l'aggiornamento adattivo rispetto ai pesi congelati?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: l'aggiornamento adattivo rispetto ai pesi congelati
- input: peso W, matrice A e B, rank e quantizzazione
- output: delta W e checkpoint adattatore
- nodi locali: Parametri congelati e adattamento: PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando…; Adapter: Blocchi bottleneck vengono inseriti nel percorso residuale. Posizione, dimensione e…; LoRA: Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può…
- limite visualizzato: il delta non è il modello completo e va valutato sullo stesso base model
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
