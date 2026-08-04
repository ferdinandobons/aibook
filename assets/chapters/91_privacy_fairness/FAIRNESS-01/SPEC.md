# Specifica visuale FAIRNESS-01

- modello compositivo: privacy_fairness_matrix
- domanda principale: Come si passa da «Memorizzazione e leakage» a «Fairness» mantenendo osservabile un dato personale e il comportamento del sistema su gruppi diversi?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: un dato personale e il comportamento del sistema su gruppi diversi
- input: record, membership, gruppo, label e budget privacy
- output: utility, leakage, disparità e verifica di rimozione
- nodi locali: Memorizzazione e leakage: Un modello può riprodurre sequenze rare. Membership inference e extraction misurano…; Differential privacy: DP limita l'influenza di un record mediante clipping e rumore, con parametri epsilon e…; Fairness: Metriche di parità, equalized odds e calibration possono essere incompatibili sotto…
- limite visualizzato: privacy, fairness e utility richiedono metriche e trade-off espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
