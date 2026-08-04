# Specifica visuale SSM-01

- modello compositivo: state_space_scan
- domanda principale: Come si passa da «State-space model» a «Mamba» mantenendo osservabile lo stato dinamico di un modello state-space?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: lo stato dinamico di un modello state-space
- input: x_t, stato s_t e matrici A, B, C
- output: stato e uscita per ogni posizione
- nodi locali: State-space model: Uno stato lineare ammette forma ricorrente e, in condizioni tempo-invarianti, forma…; S4: Parametrizzazioni strutturate rendono gestibili kernel lunghi e dinamiche stabili.; Mamba: Parametri selettivi dipendenti dall'input modificano lo stato mediante una scan…
- limite visualizzato: stabilità e discretizzazione fanno parte dell'implementazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
