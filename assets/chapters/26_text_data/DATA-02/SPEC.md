# Specifica visuale DATA-02

- modello compositivo: tokenization_grid
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale failure o confronto separa Packing e confini da Lunghezza, lingua e costi?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: il testo prima e dopo la tokenizzazione
- input: una stringa Unicode con byte e token speciali
- output: ID, confini, mask e costo in token
- nodi locali: Packing e confini: Più documenti possono condividere una sequenza.; Lunghezza, lingua e costi: Token per carattere variano tra lingue e formati.
- limite visualizzato: stringa, encoding e tokenizer devono restare dichiarati
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
