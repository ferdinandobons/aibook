# Specifica visuale NATIVE-02

- modello compositivo: accumulator_stack
- domanda principale: Quale controllo collega «Accumulazione» a «Co-design hardware» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un peso low-bit e il suo accumulo numerico
- input: peso reale, codice ternario, scala e attivazione
- output: peso ricostruito, gradiente e costo hardware
- nodi locali: Accumulazione: Prodotti low-bit possono accumulare in precisione maggiore. Storage, compute e…; Co-design hardware: Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato.…
- limite visualizzato: bit nominali e precisione effettiva dell'accumulo sono distinti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
