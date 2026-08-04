# Specifica visuale RECIPE-01

- modello compositivo: recipe_pipeline
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Batch di token a AdamW nel capitolo 35?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato completo di una ricetta di pretraining
- input: batch, learning rate, seed, optimizer e checkpoint
- output: loss, parametri e checkpoint ripristinabile
- nodi locali: Batch di token: Packing, padding e mask determinano quanti token validi contribuiscono alla loss.; Inizializzazione: Scala dei pesi e residual deve restare coerente con profondità, norm e dtype.; AdamW: Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer.
- limite visualizzato: un checkpoint deve includere lo stato necessario a continuare il run
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
