# Specifica visuale TRAINING-01

- modello compositivo: reasoning_curriculum
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale percorso collega Tracce e risposte a Self-consistency e rejection sampling nel capitolo 52?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una traccia di reasoning e la risposta che la segue
- input: prompt, trace del teacher, answer e costo in token
- output: traccia selezionata, risposta e misura di costo
- nodi locali: Tracce e risposte: Una traccia di ragionamento è testo prodotto dal modello.; Distillazione: Un teacher produce soluzioni o distribuzioni che diventano target per uno student.; Self-consistency e rejection sampling: Più candidate vengono generate e selezionate con voto o verifier.
- limite visualizzato: una traccia leggibile non prova faithfulness causale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
