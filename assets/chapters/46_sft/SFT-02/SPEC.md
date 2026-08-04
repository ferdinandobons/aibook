# Specifica visuale SFT-02

- modello compositivo: supervision_pipeline
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale failure o confronto separa Teacher forcing e generalizzazione da Catastrophic forgetting e controllo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una coppia prompt-risposta nel formato di instruction tuning
- input: messaggi, target, mask delle label e mixture
- output: loss per token e comportamento adattato
- nodi locali: Teacher forcing e generalizzazione: Durante il training il modello vede il prefisso corretto.; Catastrophic forgetting e controllo: Learning rate, durata e replay influenzano la perdita di capacità precedenti.
- limite visualizzato: il formato dei dati e le label decidono che cosa viene ottimizzato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
