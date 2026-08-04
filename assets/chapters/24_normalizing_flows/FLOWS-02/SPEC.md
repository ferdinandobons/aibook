# Specifica visuale FLOWS-02

- modello compositivo: jacobian_stack
- domanda principale: Quale controllo collega «Continuous normalizing flow» a «Sampling e costo» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un dato trasformato da una mappa invertibile
- input: x, log-determinante e variabile latente z
- output: log-likelihood, z e campione ricostruito
- nodi locali: Continuous normalizing flow: Una ODE definisce una trasformazione continua. La likelihood usa la variazione del…; Sampling e costo: I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono…
- limite visualizzato: l'inversione richiede una trasformazione e un log-determinante coerenti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
