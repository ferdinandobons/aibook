# Specifica visuale ALT-02

- modello compositivo: prediction_pipeline
- domanda principale: Quale controllo collega «Diffusione linguistica» a «Assi separati» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: unità di predizione dal byte al token multiplo
- input: byte, gerarchia, target e numero di passi
- output: unità predette, loss e durata di decoding
- nodi locali: Diffusione linguistica: Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi.; Assi separati: Unità del testo, architettura e obiettivo di predizione sono scelte distinte che…
- limite visualizzato: granularità della rappresentazione e parallelismo sono assi distinti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
