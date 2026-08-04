# Specifica visuale GAN-02

- modello compositivo: failure_balance
- domanda principale: Quale controllo collega «Wasserstein GAN» a «Stabilità e valutazione» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la partita tra generatore e discriminatore
- input: un dato reale, un campione e due score
- output: score, gradiente e campione
- nodi locali: Wasserstein GAN: WGAN usa una distanza legata a funzioni Lipschitz. Weight clipping e gradient penalty…; Stabilità e valutazione: Bilanciare update, normalizzazioni e capacità è essenziale. FID è una metrica su feature…
- limite visualizzato: un equilibrio locale non prova copertura né stabilità
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
