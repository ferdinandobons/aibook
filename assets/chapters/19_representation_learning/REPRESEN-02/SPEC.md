# Specifica visuale REPRESEN-02

- modello compositivo: representation_map
- domanda principale: Quale controllo collega «Disentanglement e identifiability» a «Valutare una rappresentazione» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v49.png
- oggetto osservato: un vettore prodotto per un compito successivo
- input: u = [1, 2, 0] e v = [2, 1, 0]
- output: un vettore, una similarità o una predizione downstream
- nodi locali: Disentanglement e identifiability: Separare fattori latenti richiede ipotesi. Senza supervision o bias aggiuntivi, molte…; Valutare una rappresentazione: Linear probe, retrieval e fine-tuning misurano proprietà diverse. Una buona metrica…
- limite visualizzato: la geometria dipende da dati, obiettivo e normalizzazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
