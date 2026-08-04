# Specifica visuale FAIRNESS-02

- modello compositivo: cohort_boundary
- domanda principale: Quale controllo collega «Bias nei dati e nel sistema» a «Machine unlearning» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un dato personale e il comportamento del sistema su gruppi diversi
- input: record, membership, gruppo, label e budget privacy
- output: utility, leakage, disparità e verifica di rimozione
- nodi locali: Bias nei dati e nel sistema: Rappresentazione, label, soglie e policy possono produrre disparità anche con lo stesso…; Machine unlearning: Rimuovere l'influenza di dati richiede un criterio e una verifica. Cancellare un record…
- limite visualizzato: privacy, fairness e utility richiedono metriche e trade-off espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
