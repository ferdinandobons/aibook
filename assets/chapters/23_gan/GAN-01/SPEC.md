# Specifica visuale GAN-01

- modello compositivo: adversarial_loop
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale percorso collega Un gioco tra due modelli a Mode collapse nel capitolo 23?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la partita tra generatore e discriminatore
- input: un dato reale, un campione e due score
- output: score, gradiente e campione
- nodi locali: Un gioco tra due modelli: Il generatore produce campioni; il discriminatore distingue dati reali e generati.; Divergenze e gradienti: I gradienti pratici dipendono dalla loss scelta.; Mode collapse: Il generatore può produrre poche modalità convincenti.
- limite visualizzato: un equilibrio locale non prova copertura né stabilità
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
