# Specifica visuale FLOW-01

- modello compositivo: noise_path
- domanda principale: Come si passa da «Corrompere e ricostruire» a «Parametrizzazioni epsilon, x0 e v» mantenendo osservabile un dato corrotto e il percorso di denoising?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un dato corrotto e il percorso di denoising
- input: x_0, rumore epsilon e timestep t
- output: stima del rumore e campione ricostruito
- nodi locali: Corrompere e ricostruire: La diffusione forward aggiunge rumore secondo uno schedule. Il modello impara a…; Score matching: Lo score è il gradiente del log-density rispetto ai dati perturbati. Denoising score…; Parametrizzazioni epsilon, x0 e v: Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma…
- limite visualizzato: parametrizzazione e scheduler fanno parte del contratto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
