# Specifica visuale DATA-02

- modello compositivo: tokenization_grid
- domanda principale: Quale controllo collega «Packing e confini» a «Lunghezza, lingua e costi» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: il testo prima e dopo la tokenizzazione
- input: una stringa Unicode con byte e token speciali
- output: ID, confini, mask e costo in token
- nodi locali: Packing e confini: Più documenti possono condividere una sequenza. Attention mask e loss mask devono…; Lunghezza, lingua e costi: Token per carattere variano tra lingue e formati. La lunghezza in token influenza…
- limite visualizzato: stringa, encoding e tokenizer devono restare dichiarati
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
