# Specifica visuale HYBRID-01

- modello compositivo: hybrid_route
- domanda principale: Come si passa da «Ibridi tra layer» a «Memoria segmentale» mantenendo osservabile informazione distribuita tra attenzione locale e memoria?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: informazione distribuita tra attenzione locale e memoria
- input: segmento corrente, stato e memoria persistente
- output: stato aggiornato e contenuto recuperato
- nodi locali: Ibridi tra layer: Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati.; Attention locale e stato: Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre…; Memoria segmentale: Stati di segmenti precedenti possono essere riusati o compressi con stop-gradient e…
- limite visualizzato: durata e provenienza della memoria devono essere separate
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
