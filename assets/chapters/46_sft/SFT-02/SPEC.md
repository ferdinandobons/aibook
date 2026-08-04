# Specifica visuale SFT-02

- modello compositivo: supervision_pipeline
- domanda principale: Quale controllo collega «Teacher forcing e generalizzazione» a «Catastrophic forgetting e controllo» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una coppia prompt-risposta nel formato di instruction tuning
- input: messaggi, target, mask delle label e mixture
- output: loss per token e comportamento adattato
- nodi locali: Teacher forcing e generalizzazione: Durante il training il modello vede il prefisso corretto. La capacità di seguire…; Catastrophic forgetting e controllo: Learning rate, durata e replay influenzano la perdita di capacità precedenti. Base…
- limite visualizzato: il formato dei dati e le label decidono che cosa viene ottimizzato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
