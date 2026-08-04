# Specifica visuale LAB-02

- modello compositivo: result_bundle
- domanda principale: Quale controllo collega «Training e valutazione» a «Report» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un esperimento didattico con ambiente e artefatti dichiarati
- input: seed, dataset piccolo, config, codice e versione
- output: loss, metriche, manifest e limite
- nodi locali: Training e valutazione: Curve, checkpoint, validation e test seguono il protocollo costruito nel libro.; Report: Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che…
- limite visualizzato: un run locale non equivale a una prova generale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
