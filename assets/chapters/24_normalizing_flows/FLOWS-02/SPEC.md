# Specifica visuale FLOWS-02

- modello compositivo: jacobian_stack
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale failure o confronto separa Continuous normalizing flow da Sampling e costo?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un dato trasformato da una mappa invertibile
- input: x, log-determinante e variabile latente z
- output: log-likelihood, z e campione ricostruito
- nodi locali: Continuous normalizing flow: Una ODE definisce una trasformazione continua.; Sampling e costo: I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richieder.
- limite visualizzato: l'inversione richiede una trasformazione e un log-determinante coerenti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
