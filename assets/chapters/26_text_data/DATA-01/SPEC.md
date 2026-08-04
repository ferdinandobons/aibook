# Specifica visuale DATA-01

- modello compositivo: data_lineage
- domanda principale: Come si passa da «Unicode e byte» a «Token speciali» mantenendo osservabile il testo prima e dopo la tokenizzazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: il testo prima e dopo la tokenizzazione
- input: una stringa Unicode con byte e token speciali
- output: ID, confini, mask e costo in token
- nodi locali: Unicode e byte: Il testo è una sequenza di code point codificata in byte. Normalizzazione Unicode e…; Tokenizzazione: BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti. Il…; Token speciali: BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi. ID uguali…
- limite visualizzato: stringa, encoding e tokenizer devono restare dichiarati
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
