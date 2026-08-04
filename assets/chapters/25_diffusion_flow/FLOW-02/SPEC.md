# Specifica visuale FLOW-02

- modello compositivo: sampler_path
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale failure o confronto separa Sampler da Flow matching e rectified flow?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un dato corrotto e il percorso di denoising
- input: x_0, rumore epsilon e timestep t
- output: stima del rumore e campione ricostruito
- nodi locali: Sampler: DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti.; Flow matching e rectified flow: Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni.
- limite visualizzato: parametrizzazione e scheduler fanno parte del contratto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
