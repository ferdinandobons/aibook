# Specifica visuale JAILBREAK-02

- modello compositivo: jailbreak_boundary
- domanda principale: Quale controllo collega «Difese» a «Valutazione adattiva» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: una superficie di attacco e il comportamento sotto perturbazione
- input: threat model, prompt, budget e risposta
- output: success rate, failure mode e costo della difesa
- nodi locali: Difese: Training, filtri, classificatori e refusal possono ridurre alcuni attacchi e introdurre…; Valutazione adattiva: Una difesa deve essere testata da attaccanti che conoscono il metodo, entro un…
- limite visualizzato: un test superato non copre minacce non incluse nel protocollo
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
