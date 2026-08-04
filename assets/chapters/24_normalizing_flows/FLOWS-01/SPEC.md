# Specifica visuale FLOWS-01

- modello compositivo: invertible_flow
- domanda principale: Come si passa da «Cambio di variabile» a «Invertibilità e architettura» mantenendo osservabile un dato trasformato da una mappa invertibile?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un dato trasformato da una mappa invertibile
- input: x, log-determinante e variabile latente z
- output: log-likelihood, z e campione ricostruito
- nodi locali: Cambio di variabile: Una trasformazione invertibile collega una distribuzione semplice ai dati. La densità…; Coupling layer: RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante…; Invertibilità e architettura: L'invertibilità limita operazioni e dimensioni. Squeeze, split e permutazioni…
- limite visualizzato: l'inversione richiede una trasformazione e un log-determinante coerenti
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
