# Specifica visuale FAIRNESS-02

- modello compositivo: cohort_boundary
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Bias nei dati e nel sistema da Machine unlearning?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un dato personale e il comportamento del sistema su gruppi diversi
- input: record, membership, gruppo, label e budget privacy
- output: utility, leakage, disparità e verifica di rimozione
- nodi locali: Bias nei dati e nel sistema: Rappresentazione, label, soglie e policy possono produrre disparità anche con lo stesso mo.; Machine unlearning: Rimuovere l'influenza di dati richiede un criterio e una verifica.
- limite visualizzato: privacy, fairness e utility richiedono metriche e trade-off espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
