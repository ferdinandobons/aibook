# Specifica visuale NATIVE-02

- modello compositivo: accumulator_stack
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale failure o confronto separa Accumulazione da Co-design hardware?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un peso low-bit e il suo accumulo numerico
- input: peso reale, codice ternario, scala e attivazione
- output: peso ricostruito, gradiente e costo hardware
- nodi locali: Accumulazione: Prodotti low-bit possono accumulare in precisione maggiore.; Co-design hardware: Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato.
- limite visualizzato: bit nominali e precisione effettiva dell'accumulo sono distinti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
