# Specifica visuale LINATT-01

- modello compositivo: recurrent_attention
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale percorso collega Kernel fattorizzabile a Normalizzazione nel capitolo 41?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: uno stato causale che sostituisce il prodotto quadratico
- input: sequenza x_t, kernel fattorizzabile e stato
- output: h_t e predizione con costo dichiarato
- nodi locali: Kernel fattorizzabile: Una feature map permette di riassociare i prodotti senza una matrice completa di score.; Recurrence causale: Statistiche S e z vengono aggiornate per token e hanno dimensione indipendente dalla lungh.; Normalizzazione: Il denominatore controlla la scala e richiede feature e stabilizzazione coerenti.
- limite visualizzato: la fattorizzazione cambia memoria e capacità di interazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
