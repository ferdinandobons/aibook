# Specifica visuale PROVENANCE-02

- modello compositivo: credential_layers
- orientamento: verticale, lettura dall'alto verso il basso
- domanda principale: Quale failure o confronto separa Detection da Policy e interfaccia?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un contenuto e la sua attestazione di provenienza
- input: payload, metadata, manifest e chiave o watermark
- output: record verificabile e stato di rilevazione
- nodi locali: Detection: Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift.; Policy e interfaccia: Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pip.
- limite visualizzato: provenienza dell'artefatto non certifica la verità del contenuto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
