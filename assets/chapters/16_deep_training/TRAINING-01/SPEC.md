# Specifica visuale TRAINING-01

- modello compositivo: training_loop
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale percorso collega Segnali che attraversano molti layer a Normalizzazione nel capitolo 16?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: il segnale che attraversa una rete profonda
- input: x_l con shape [batch, d] e norma misurata
- output: x_{l+1} con la stessa o con una nuova shape dichiarata
- nodi locali: Segnali che attraversano molti layer: Attivazioni e gradienti possono crescere o ridursi lungo la profondità.; Inizializzazione: Xavier e He initialization collegano la varianza dei pesi al fan-in o fan-out.; Normalizzazione: BatchNorm, LayerNorm e RMSNorm normalizzano assi e statistiche differenti.
- limite visualizzato: una somma residuale richiede shape compatibili e non prova da sola stabilità del training
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
