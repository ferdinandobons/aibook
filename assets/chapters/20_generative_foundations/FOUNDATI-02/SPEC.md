# Specifica visuale FOUNDATI-02

- modello compositivo: evaluation_lenses
- domanda principale: Quale controllo collega «Energy-based model» a «Qualità, copertura e valutazione» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: una distribuzione sui dati o su una variabile latente
- input: un dato x, un rumore epsilon o una variabile z
- output: una probabilità, un punteggio o un campione
- nodi locali: Energy-based model: Una energia non normalizzata assegna punteggi alle configurazioni. La costante di…; Qualità, copertura e valutazione: Campioni plausibili non garantiscono copertura. Likelihood e precision-recall generativa…
- limite visualizzato: un campione plausibile non dimostra copertura dell'intera distribuzione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
