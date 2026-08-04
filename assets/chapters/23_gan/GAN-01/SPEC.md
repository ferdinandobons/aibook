# Specifica visuale GAN-01

- modello compositivo: adversarial_loop
- domanda principale: Come si passa da «Un gioco tra due modelli» a «Mode collapse» mantenendo osservabile la partita tra generatore e discriminatore?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la partita tra generatore e discriminatore
- input: un dato reale, un campione e due score
- output: score, gradiente e campione
- nodi locali: Un gioco tra due modelli: Il generatore produce campioni; il discriminatore distingue dati reali e generati.…; Divergenze e gradienti: La formulazione originale è collegata alla Jensen-Shannon divergence sotto un…; Mode collapse: Il generatore può produrre poche modalità convincenti. Diversità e fedeltà devono essere…
- limite visualizzato: un equilibrio locale non prova copertura né stabilità
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
