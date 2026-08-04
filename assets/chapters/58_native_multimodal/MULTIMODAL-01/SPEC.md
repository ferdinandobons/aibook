# Specifica visuale MULTIMODAL-01

- modello compositivo: native_fusion
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Token interleaved a Output multimodale nel capitolo 58?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: token interleaved e output di più modalità
- input: sequenza testo-immagine-audio con mask
- output: token o artefatto nella modalità richiesta
- nodi locali: Token interleaved: Sequenze possono alternare testo, immagini, audio e marker.; Backbone condiviso: Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e ad.; Output multimodale: La generazione di testo e media richiede head o decoder differenti, anche quando il backbo.
- limite visualizzato: ordine, durata e maschera della modalità devono essere espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
