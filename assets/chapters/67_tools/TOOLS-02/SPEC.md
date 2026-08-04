# Specifica visuale TOOLS-02

- modello compositivo: schema_gate
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Esecuzione e osservazione da Idempotenza e side effect?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: una chiamata a tool con schema e autorizzazione
- input: nome, argomenti, scope e stato
- output: risultato del tool o rifiuto tracciato
- nodi locali: Esecuzione e osservazione: Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato.; Idempotenza e side effect: Operazioni di lettura e scrittura hanno rischi differenti.
- limite visualizzato: schema valido non significa permesso di eseguire il side effect
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
