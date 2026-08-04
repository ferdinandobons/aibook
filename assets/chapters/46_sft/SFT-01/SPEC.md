# Specifica visuale SFT-01

- modello compositivo: loss_mask
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale percorso collega Dal pretraining alle istruzioni a Instruction mixture nel capitolo 46?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una coppia prompt-risposta nel formato di instruction tuning
- input: messaggi, target, mask delle label e mixture
- output: loss per token e comportamento adattato
- nodi locali: Dal pretraining alle istruzioni: Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora col.; Formati conversazionali: Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali p.; Instruction mixture: Compiti e domini vengono mescolati con pesi espliciti.
- limite visualizzato: il formato dei dati e le label decidono che cosa viene ottimizzato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
