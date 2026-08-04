# Specifica visuale NATIVE-01

- modello compositivo: low_bit_path
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale percorso collega Training nativo a Straight-through estimator nel capitolo 75?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un peso low-bit e il suo accumulo numerico
- input: peso reale, codice ternario, scala e attivazione
- output: peso ricostruito, gradiente e costo hardware
- nodi locali: Training nativo: Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere.; Pesi ternari e 1.58-bit: BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici.; Straight-through estimator: Operazioni discrete usano gradienti surrogati.
- limite visualizzato: bit nominali e precisione effettiva dell'accumulo sono distinti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
