# Specifica visuale POS-02

- modello compositivo: context_window
- domanda principale: Quale controllo collega «ALiBi» a «Estensione e valutazione» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: la relazione tra posizione e rappresentazione del token
- input: query, key e indice di posizione
- output: score dipendente dalla posizione
- nodi locali: ALiBi: Bias lineari penalizzano distanze maggiori con slope per head.; Estensione e valutazione: Positional interpolation e metodi affini estendono gli indici, ma l'uso effettivo del…
- limite visualizzato: estendere il contesto richiede una misura fuori dalla lunghezza addestrata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
