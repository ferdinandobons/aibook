# Specifica visuale VERIFIERS-02

- modello compositivo: process_supervision
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale failure o confronto separa Reward model di processo da Goodhart e indipendenza?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una traiettoria e il segnale di un verifier
- input: passaggi, risposta finale, criterio e indipendenza
- output: score verificato e failure localizzata
- nodi locali: Reward model di processo: Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per.; Goodhart e indipendenza: Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting.
- limite visualizzato: un verifier può ereditare bias o essere ottimizzato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
