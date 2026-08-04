# Specifica visuale LINATT-02

- modello compositivo: mechanism_compare
- domanda principale: Quale controllo collega «Fast weights» a «Delta rule» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: uno stato causale che sostituisce il prodotto quadratico
- input: sequenza x_t, kernel fattorizzabile e stato
- output: h_t e predizione con costo dichiarato
- nodi locali: Fast weights: Lo stato può essere letto come memoria associativa che accumula coppie key-value.; Delta rule: L'update corregge l'errore tra value desiderato e value recuperato, riducendo la…
- limite visualizzato: la fattorizzazione cambia memoria e capacità di interazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
