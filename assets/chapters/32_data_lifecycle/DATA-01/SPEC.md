# Specifica visuale DATA-01

- modello compositivo: data_lineage
- domanda principale: Come si passa da «Sorgenti e provenienza» a «Filtri» mantenendo osservabile un record di dataset dalla sorgente al manifest?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v47.png
- oggetto osservato: un record di dataset dalla sorgente al manifest
- input: testo grezzo, metadati, split e digest
- output: record ammesso, conteggi e manifest
- nodi locali: Sorgenti e provenienza: Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo…; Parsing e normalizzazione: Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e…; Filtri: Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono…
- limite visualizzato: ogni trasformazione deve restare ricostruibile e ordinata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
