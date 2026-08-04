# Specifica visuale JAILBREAK-01

- modello compositivo: perturbation_grid
- orientamento: a matrice, righe e colonne dichiarate
- domanda principale: Quale percorso collega Threat model a Ottimizzazione adversarial nel capitolo 88?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una superficie di attacco e il comportamento sotto perturbazione
- input: threat model, prompt, budget e risposta
- output: success rate, failure mode e costo della difesa
- nodi locali: Threat model: Attaccante, accesso, obiettivo, budget e superficie definiscono il test.; Perturbazioni: Typo, parafrasi, encoding e contenuti multimodali possono aggirare filtri superficiali.; Ottimizzazione adversarial: Suffix e prompt vengono cercati per aumentare una loss di attacco.
- limite visualizzato: un test superato non copre minacce non incluse nel protocollo
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
