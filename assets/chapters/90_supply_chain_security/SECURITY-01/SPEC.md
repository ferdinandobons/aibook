# Specifica visuale SECURITY-01

- modello compositivo: supply_chain
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Data poisoning a Model extraction nel capitolo 90?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: gli artefatti che attraversano la supply chain del modello
- input: dataset, checkpoint, repository, digest e owner
- output: artefatto rilasciato, traccia e decisione di blocco
- nodi locali: Data poisoning: Campioni modificati possono alterare comportamento generale o target specifici.; Backdoor: Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove.; Model extraction: Query e output possono permettere di imitare capacità o recuperare informazioni.
- limite visualizzato: integrità del file non certifica assenza di contenuto malevolo
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
