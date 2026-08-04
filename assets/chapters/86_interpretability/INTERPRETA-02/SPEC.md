# Specifica visuale INTERPRETA-02

- modello compositivo: causal_boundary
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Causal intervention da Circuiti?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un comportamento del modello e l'intervento che lo modifica
- input: attivazioni, probe, attribution e baseline
- output: effetto osservato con controllo e confondenti
- nodi locali: Causal intervention: Ablation, activation patching e path patching modificano componenti e misurano effetti sul.; Circuiti: Sufficienza e necessità richiedono test separati.
- limite visualizzato: correlazione di una feature non prova causalità
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
