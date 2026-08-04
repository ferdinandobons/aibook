# Specifica visuale KV-02

- modello compositivo: kv_layout
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale failure o confronto separa Local e sparse attention da MLA e cache?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: le teste di query e key-value che alimentano l'attention
- input: Q con h_q teste e KV con h_kv teste
- output: score, cache e pattern di comunicazione
- nodi locali: Local e sparse attention: Finestre e pattern selezionati riducono le coppie ma cambiano la connettività.; MLA e cache: Compressione latente e numero di KV head sono strategie differenti.
- limite visualizzato: raggruppamento delle teste e costo della KV cache restano espliciti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
