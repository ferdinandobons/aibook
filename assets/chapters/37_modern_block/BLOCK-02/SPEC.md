# Specifica visuale BLOCK-02

- modello compositivo: residual_stack
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale failure o confronto separa SwiGLU da Ordine e parallelismo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: un residual stream dentro un blocco moderno
- input: h di shape [batch, length, d] e norma misurata
- output: h' con shape preservata e statistiche confrontabili
- nodi locali: SwiGLU: Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down.; Ordine e parallelismo: Attention e MLP possono essere sequenziali o paralleli.
- limite visualizzato: ordine dei sottolayer e shape sono parte del blocco
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
