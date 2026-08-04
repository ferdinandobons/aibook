# Specifica visuale JAILBREAK-02

- modello compositivo: jailbreak_boundary
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Difese da Valutazione adattiva?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: una superficie di attacco e il comportamento sotto perturbazione
- input: threat model, prompt, budget e risposta
- output: success rate, failure mode e costo della difesa
- nodi locali: Difese: Training, filtri, classificatori e refusal possono ridurre alcuni attacchi e introdurre fa.; Valutazione adattiva: Una difesa deve essere testata da attaccanti che conoscono il metodo, entro un protocollo.
- limite visualizzato: un test superato non copre minacce non incluse nel protocollo
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
