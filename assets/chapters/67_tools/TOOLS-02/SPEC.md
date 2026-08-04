# Specifica visuale TOOLS-02

- modello compositivo: schema_gate
- domanda principale: Quale controllo collega «Esecuzione e osservazione» a «Idempotenza e side effect» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: una chiamata a tool con schema e autorizzazione
- input: nome, argomenti, scope e stato
- output: risultato del tool o rifiuto tracciato
- nodi locali: Esecuzione e osservazione: Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato.…; Idempotenza e side effect: Operazioni di lettura e scrittura hanno rischi differenti. Conferma, deduplicazione e…
- limite visualizzato: schema valido non significa permesso di eseguire il side effect
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
