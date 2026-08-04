# Specifica visuale FLASH-01

- modello compositivo: memory_tiling
- domanda principale: Come si passa da «FLOP e movimento dei dati» a «Softmax online» mantenendo osservabile il calcolo dell'attention e il suo movimento di dati?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: il calcolo dell'attention e il suo movimento di dati
- input: tile di Q, K, V, dtype e device
- output: stesso contratto matematico con memoria e latenza misurate
- nodi locali: FLOP e movimento dei dati: Lo stesso operatore può avere traffico di memoria molto diverso.; Tiling: Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti…; Softmax online: Massimo, denominatore e numeratore vengono aggiornati blocco per blocco.
- limite visualizzato: una misura hardware dipende da shape, backend e precisione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
