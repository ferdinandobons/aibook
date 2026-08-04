# Specifica visuale PROJECT-02

- modello compositivo: rollback_path
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Deployment da Documentazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un sistema ML che attraversa sviluppo, rilascio e monitoraggio
- input: problema, dati, modello, eval, deployment e rollback
- output: servizio versionato con metriche e piano di ritorno
- nodi locali: Deployment: Versioni, secret, rollback, observability e incident response vengono esercitati prima del.; Documentazione: Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiorna.
- limite visualizzato: un modello che passa un test offline non è automaticamente pronto in produzione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
