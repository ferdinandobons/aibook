# Specifica visuale POS-01

- modello compositivo: position_geometry
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale percorso collega Posizione assoluta a RoPE nel capitolo 38?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: la relazione tra posizione e rappresentazione del token
- input: query, key e indice di posizione
- output: score dipendente dalla posizione
- nodi locali: Posizione assoluta: Embedding appresi o sinusoidali aggiungono un segnale legato all'indice.; Posizione relativa: Bias o rappresentazioni relative modificano i confronti in funzione della distanza.; RoPE: Rotazioni di query e key rendono il prodotto scalare dipendente dall'offset relativo.
- limite visualizzato: estendere il contesto richiede una misura fuori dalla lunghezza addestrata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
