# Specifica visuale INTERPRETA-01

- modello compositivo: observation_inference
- orientamento: a due colonne, confronto parallelo
- domanda principale: Quale percorso collega Oggetto dell'interpretazione a Attribution nel capitolo 86?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un comportamento del modello e l'intervento che lo modifica
- input: attivazioni, probe, attribution e baseline
- output: effetto osservato con controllo e confondenti
- nodi locali: Oggetto dell'interpretazione: Pesi, attivazioni, feature, head e comportamento sono livelli differenti.; Probing: Un probe misura informazione decodificabile da una rappresentazione.; Attribution: Gradienti, integrated gradients e perturbazioni assegnano importanza secondo definizioni d.
- limite visualizzato: correlazione di una feature non prova causalità
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
