# Specifica visuale GAN-02

- modello compositivo: failure_balance
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale failure o confronto separa Wasserstein GAN da Stabilità e valutazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: la partita tra generatore e discriminatore
- input: un dato reale, un campione e due score
- output: score, gradiente e campione
- nodi locali: Wasserstein GAN: WGAN usa una distanza legata a funzioni Lipschitz.; Stabilità e valutazione: Bilanciare update, normalizzazioni e capacità è essenziale.
- limite visualizzato: un equilibrio locale non prova copertura né stabilità
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
