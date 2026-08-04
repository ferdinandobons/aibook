# Specifica visuale POS-02

- modello compositivo: context_window
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale failure o confronto separa ALiBi da Estensione e valutazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: la relazione tra posizione e rappresentazione del token
- input: query, key e indice di posizione
- output: score dipendente dalla posizione
- nodi locali: ALiBi: Bias lineari penalizzano distanze maggiori con slope per head.; Estensione e valutazione: Positional interpolation e metodi affini estendono gli indici, ma l'uso effettivo del cont.
- limite visualizzato: estendere il contesto richiede una misura fuori dalla lunghezza addestrata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
