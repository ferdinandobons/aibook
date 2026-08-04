# Specifica visuale TOOLS-01

- modello compositivo: tool_call_route
- domanda principale: Come si passa da «Schema dell'output» a «Argomenti» mantenendo osservabile una chiamata a tool con schema e autorizzazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una chiamata a tool con schema e autorizzazione
- input: nome, argomenti, scope e stato
- output: risultato del tool o rifiuto tracciato
- nodi locali: Schema dell'output: JSON Schema, grammar o tipi stabiliscono campi e vincoli. Validità sintattica non…; Selezione del tool: Il modello sceglie una funzione tra opzioni descritte. Nomi, descrizioni e…; Argomenti: Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione. Campi…
- limite visualizzato: schema valido non significa permesso di eseguire il side effect
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
