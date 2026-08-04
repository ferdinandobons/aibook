# Specifica visuale FLOWS-01

- modello compositivo: invertible_flow
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Cambio di variabile a Invertibilità e architettura nel capitolo 24?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un dato trasformato da una mappa invertibile
- input: x, log-determinante e variabile latente z
- output: log-likelihood, z e campione ricostruito
- nodi locali: Cambio di variabile: Una trasformazione invertibile collega una distribuzione semplice ai dati.; Coupling layer: RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante eff.; Invertibilità e architettura: L'invertibilità limita operazioni e dimensioni.
- limite visualizzato: l'inversione richiede una trasformazione e un log-determinante coerenti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
