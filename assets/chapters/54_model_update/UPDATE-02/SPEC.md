# Specifica visuale UPDATE-02

- modello compositivo: side_effect_trace
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Model editing da Versioning e rollback?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: versioni di pesi e modifiche localizzate del modello
- input: base model, delta, task e rollback point
- output: versione nuova, diff e test di regressione
- nodi locali: Model editing: ROME, MEMIT e famiglie affini cercano modifiche localizzate.; Versioning e rollback: Un update produce un nuovo artefatto con fonti, test e dipendenze.
- limite visualizzato: un merge senza valutazione può introdurre regressioni invisibili
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
