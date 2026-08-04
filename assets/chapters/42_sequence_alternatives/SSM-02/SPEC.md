# Specifica visuale SSM-02

- modello compositivo: sequence_stack
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale failure o confronto separa Hyena e long convolution da RWKV, RetNet, xLSTM e Griffin?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: lo stato dinamico di un modello state-space
- input: x_t, stato s_t e matrici A, B, C
- output: stato e uscita per ogni posizione
- nodi locali: Hyena e long convolution: Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise.; RWKV, RetNet, xLSTM e Griffin: Recurrence moderne e ibridi usano stati e gate differenti.
- limite visualizzato: stabilità e discretizzazione fanno parte dell'implementazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
