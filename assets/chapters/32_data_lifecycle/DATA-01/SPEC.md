# Specifica visuale DATA-01

- modello compositivo: data_lineage
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Sorgenti e provenienza a Filtri nel capitolo 32?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: un record di dataset dalla sorgente al manifest
- input: testo grezzo, metadati, split e digest
- output: record ammesso, conteggi e manifest
- nodi locali: Sorgenti e provenienza: Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shar.; Parsing e normalizzazione: Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono.; Filtri: Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statis.
- limite visualizzato: ogni trasformazione deve restare ricostruibile e ordinata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
