# Specifica visuale SSM-02

- modello compositivo: sequence_stack
- domanda principale: Quale controllo collega «Hyena e long convolution» a «RWKV, RetNet, xLSTM e Griffin» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: lo stato dinamico di un modello state-space
- input: x_t, stato s_t e matrici A, B, C
- output: stato e uscita per ogni posizione
- nodi locali: Hyena e long convolution: Kernel lunghi impliciti e gate collegano posizioni distanti senza score pairwise.; RWKV, RetNet, xLSTM e Griffin: Recurrence moderne e ibridi usano stati e gate differenti; il confronto richiede budget…
- limite visualizzato: stabilità e discretizzazione fanno parte dell'implementazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
