# Specifica visuale DIST-02

- modello compositivo: communication_graph
- domanda principale: Quale controllo collega «Topologia e fault tolerance» a «Continued pretraining» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: gradienti e stato distribuiti tra worker
- input: microbatch, worker, shard e topologia
- output: gradiente ridotto, stato sincronizzato e fault osservato
- nodi locali: Topologia e fault tolerance: Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta.; Continued pretraining: Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di…
- limite visualizzato: la riduzione e il conteggio del batch devono essere dichiarati
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
