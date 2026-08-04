# Specifica visuale MIX-02

- modello compositivo: contamination_gate
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Curriculum da Dati sintetici?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: la miscela effettiva di sorgenti durante il training
- input: pesi, temperatura, curriculum e conteggio dei token
- output: probabilità effettive e mix osservato
- nodi locali: Curriculum: Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione.; Dati sintetici: Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feed.
- limite visualizzato: peso nominale e esposizione effettiva non sono la stessa misura
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
