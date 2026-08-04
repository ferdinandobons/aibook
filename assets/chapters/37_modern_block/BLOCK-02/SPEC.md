# Specifica visuale BLOCK-02

- modello compositivo: residual_stack
- domanda principale: Quale controllo collega «SwiGLU» a «Ordine e parallelismo» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: un residual stream dentro un blocco moderno
- input: h di shape [batch, length, d] e norma misurata
- output: h' con shape preservata e statistiche confrontabili
- nodi locali: SwiGLU: Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione…; Ordine e parallelismo: Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a…
- limite visualizzato: ordine dei sottolayer e shape sono parte del blocco
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
