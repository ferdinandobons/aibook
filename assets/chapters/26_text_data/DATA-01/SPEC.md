# Specifica visuale DATA-01

- modello compositivo: data_lineage
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Unicode e byte a Token speciali nel capitolo 26?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: il testo prima e dopo la tokenizzazione
- input: una stringa Unicode con byte e token speciali
- output: ID, confini, mask e costo in token
- nodi locali: Unicode e byte: Il testo è una sequenza di code point codificata in byte.; Tokenizzazione: BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti.; Token speciali: BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi.
- limite visualizzato: stringa, encoding e tokenizer devono restare dichiarati
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
