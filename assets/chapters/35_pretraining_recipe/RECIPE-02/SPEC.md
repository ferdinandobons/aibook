# Specifica visuale RECIPE-02

- modello compositivo: run_trace
- domanda principale: Quale controllo collega «Warmup e schedule» a «Checkpoint e recovery» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: lo stato completo di una ricetta di pretraining
- input: batch, learning rate, seed, optimizer e checkpoint
- output: loss, parametri e checkpoint ripristinabile
- nodi locali: Warmup e schedule: Il learning rate dipende da step o token e deve riprendere dal contatore corretto.; Checkpoint e recovery: Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume…
- limite visualizzato: un checkpoint deve includere lo stato necessario a continuare il run
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
