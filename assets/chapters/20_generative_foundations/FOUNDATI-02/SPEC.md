# Specifica visuale FOUNDATI-02

- modello compositivo: evaluation_lenses
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale failure o confronto separa Energy-based model da Qualità, copertura e valutazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: una distribuzione sui dati o su una variabile latente
- input: un dato x, un rumore epsilon o una variabile z
- output: una probabilità, un punteggio o un campione
- nodi locali: Energy-based model: Una energia non normalizzata assegna punteggi alle configurazioni.; Qualità, copertura e valutazione: Campioni plausibili non garantiscono copertura.
- limite visualizzato: un campione plausibile non dimostra copertura dell'intera distribuzione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
