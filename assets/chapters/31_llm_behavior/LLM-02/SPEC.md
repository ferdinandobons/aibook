# Specifica visuale LLM-02

- modello compositivo: evidence_map
- domanda principale: Quale controllo collega «Calibrazione» a «Modello e sistema» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un prompt e la distribuzione del token successivo
- input: prefisso tokenizzato, esempi e temperatura dichiarati
- output: logits, risposta e confidenza misurabile
- nodi locali: Calibrazione: Probabilità del token, confidenza espressa e correttezza fattuale sono quantità…; Modello e sistema: Post-training, messaggi di sistema, strumenti e filtri contribuiscono al comportamento…
- limite visualizzato: probabilità, comportamento osservato e correttezza non sono sinonimi
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
