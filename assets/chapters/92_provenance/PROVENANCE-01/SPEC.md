# Specifica visuale PROVENANCE-01

- modello compositivo: provenance_chain
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Provenienza crittografica a Watermarking nel capitolo 92?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un contenuto e la sua attestazione di provenienza
- input: payload, metadata, manifest e chiave o watermark
- output: record verificabile e stato di rilevazione
- nodi locali: Provenienza crittografica: Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chi.; C2PA: Credenziali di contenuto registrano asserzioni e ingredienti.; Watermarking: Un generatore può modulare token o segnali per consentire rilevamento statistico.
- limite visualizzato: provenienza dell'artefatto non certifica la verità del contenuto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
