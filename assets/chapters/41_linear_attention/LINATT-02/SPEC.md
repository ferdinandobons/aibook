# Specifica visuale LINATT-02

- modello compositivo: mechanism_compare
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale failure o confronto separa Fast weights da Delta rule?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: uno stato causale che sostituisce il prodotto quadratico
- input: sequenza x_t, kernel fattorizzabile e stato
- output: h_t e predizione con costo dichiarato
- nodi locali: Fast weights: Lo stato può essere letto come memoria associativa che accumula coppie key-value.; Delta rule: L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascri.
- limite visualizzato: la fattorizzazione cambia memoria e capacità di interazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
