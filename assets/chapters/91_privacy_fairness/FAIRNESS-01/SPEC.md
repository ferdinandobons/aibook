# Specifica visuale FAIRNESS-01

- modello compositivo: privacy_fairness_matrix
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale percorso collega Memorizzazione e leakage a Fairness nel capitolo 91?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: un dato personale e il comportamento del sistema su gruppi diversi
- input: record, membership, gruppo, label e budget privacy
- output: utility, leakage, disparità e verifica di rimozione
- nodi locali: Memorizzazione e leakage: Un modello può riprodurre sequenze rare.; Differential privacy: DP limita l'influenza di un record mediante clipping e rumore, con parametri epsilon e del.; Fairness: Il contesto decisionale guida la scelta.
- limite visualizzato: privacy, fairness e utility richiedono metriche e trade-off espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
