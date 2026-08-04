# Specifica visuale AUTOREGR-02

- modello compositivo: sampling_tree
- domanda principale: Quale controllo collega «Sampling e accumulo degli errori» a «Immagini, audio e token discreti» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: la sequenza di token e la distribuzione del prossimo elemento
- input: un prefisso di tre token e una mask causale
- output: logits, token scelto e traiettoria
- nodi locali: Sampling e accumulo degli errori: Ogni scelta modifica il contesto successivo. Errori iniziali possono spostare la…; Immagini, audio e token discreti: L'autoregressione non è limitata al testo. Una sequenza può rappresentare pixel, code…
- limite visualizzato: nessuna posizione futura entra nella predizione causale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
