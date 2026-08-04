# Specifica visuale PROJECT-01

- modello compositivo: release_pipeline
- domanda principale: Come si passa da «Definizione del problema» a «Valutazione» mantenendo osservabile un sistema ML che attraversa sviluppo, rilascio e monitoraggio?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un sistema ML che attraversa sviluppo, rilascio e monitoraggio
- input: problema, dati, modello, eval, deployment e rollback
- output: servizio versionato con metriche e piano di ritorno
- nodi locali: Definizione del problema: Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del…; Architettura: Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi.; Valutazione: Dataset offline, test end-to-end, canary e monitoraggio coprono livelli differenti.
- limite visualizzato: un modello che passa un test offline non è automaticamente pronto in produzione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
