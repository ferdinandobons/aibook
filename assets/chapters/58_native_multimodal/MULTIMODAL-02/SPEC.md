# Specifica visuale MULTIMODAL-02

- modello compositivo: modality_routing
- domanda principale: Quale controllo collega «Any-to-any» a «Sincronizzazione» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: token interleaved e output di più modalità
- input: sequenza testo-immagine-audio con mask
- output: token o artefatto nella modalità richiesta
- nodi locali: Any-to-any: Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state…; Sincronizzazione: Audio, video e testo possiedono frequenze differenti. Allineamento temporale e…
- limite visualizzato: ordine, durata e maschera della modalità devono essere espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
