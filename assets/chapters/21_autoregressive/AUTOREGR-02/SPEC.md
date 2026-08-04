# Specifica visuale AUTOREGR-02

- modello compositivo: sampling_tree
- orientamento: ramificato, radice in alto e foglie in basso
- domanda principale: Quale failure o confronto separa Sampling e accumulo degli errori da Immagini, audio e token discreti?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: la sequenza di token e la distribuzione del prossimo elemento
- input: un prefisso di tre token e una mask causale
- output: logits, token scelto e traiettoria
- nodi locali: Sampling e accumulo degli errori: Ogni scelta modifica il contesto successivo.; Immagini, audio e token discreti: L'autoregressione non è limitata al testo.
- limite visualizzato: nessuna posizione futura entra nella predizione causale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
