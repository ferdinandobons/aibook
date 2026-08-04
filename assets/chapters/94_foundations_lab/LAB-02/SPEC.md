# Specifica visuale LAB-02

- modello compositivo: result_bundle
- orientamento: a livelli, dalla base alla decisione
- domanda principale: Quale failure o confronto separa Training e valutazione da Report?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un esperimento didattico con ambiente e artefatti dichiarati
- input: seed, dataset piccolo, config, codice e versione
- output: loss, metriche, manifest e limite
- nodi locali: Training e valutazione: Curve, checkpoint, validation e test seguono il protocollo costruito nel libro.; Report: Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termi.
- limite visualizzato: un run locale non equivale a una prova generale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
