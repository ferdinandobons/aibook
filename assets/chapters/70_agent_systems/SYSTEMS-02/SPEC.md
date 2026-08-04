# Specifica visuale SYSTEMS-02

- modello compositivo: orchestration_boundary
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Multi-agent da Confronto con un singolo workflow?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una traiettoria composta da agenti e strumenti
- input: task, ruoli, browser, codice e handoff
- output: risultato con responsabilità e log per componente
- nodi locali: Multi-agent: Ruoli distinti possono parallelizzare o criticare, ma introducono comunicazione, ridondanz.; Confronto con un singolo workflow: Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budge.
- limite visualizzato: più agenti ampliano anche superficie e costo dell'errore
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
