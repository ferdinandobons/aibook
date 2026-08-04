# Specifica visuale MULTIMODAL-02

- modello compositivo: modality_routing
- orientamento: ramificato, radice in alto e foglie in basso
- domanda principale: Quale failure o confronto separa Any-to-any da Sincronizzazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: token interleaved e output di più modalità
- input: sequenza testo-immagine-audio con mask
- output: token o artefatto nella modalità richiesta
- nodi locali: Any-to-any: Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state re.; Sincronizzazione: Audio, video e testo possiedono frequenze differenti.
- limite visualizzato: ordine, durata e maschera della modalità devono essere espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
