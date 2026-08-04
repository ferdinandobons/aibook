# Specifica visuale KV-02

- modello compositivo: kv_layout
- domanda principale: Quale controllo collega «Local e sparse attention» a «MLA e cache» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: le teste di query e key-value che alimentano l'attention
- input: Q con h_q teste e KV con h_kv teste
- output: score, cache e pattern di comunicazione
- nodi locali: Local e sparse attention: Finestre e pattern selezionati riducono le coppie ma cambiano la connettività.; MLA e cache: Compressione latente e numero di KV head sono strategie differenti. La memoria dipende…
- limite visualizzato: raggruppamento delle teste e costo della KV cache restano espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
