# Specifica visuale VERIFIERS-01

- modello compositivo: verifier_funnel
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale percorso collega Supervisionare il risultato a Verifier nel capitolo 50?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una traiettoria e il segnale di un verifier
- input: passaggi, risposta finale, criterio e indipendenza
- output: score verificato e failure localizzata
- nodi locali: Supervisionare il risultato: Outcome supervision assegna un segnale alla risposta finale e non localizza necessariament.; Supervisionare il processo: Process supervision etichetta passaggi intermedi.; Verifier: Un verifier valuta candidate rispetto a un criterio.
- limite visualizzato: un verifier può ereditare bias o essere ottimizzato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
