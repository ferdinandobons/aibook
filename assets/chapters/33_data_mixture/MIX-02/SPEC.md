# Specifica visuale MIX-02

- modello compositivo: contamination_gate
- domanda principale: Quale controllo collega «Curriculum» a «Dati sintetici» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: la miscela effettiva di sorgenti durante il training
- input: pesi, temperatura, curriculum e conteggio dei token
- output: probabilità effettive e mix osservato
- nodi locali: Curriculum: Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione.; Dati sintetici: Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare…
- limite visualizzato: peso nominale e esposizione effettiva non sono la stessa misura
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
