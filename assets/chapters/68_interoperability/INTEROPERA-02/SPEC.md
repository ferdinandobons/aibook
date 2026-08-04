# Specifica visuale INTEROPERA-02

- modello compositivo: compatibility_boundary
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Identità e autorizzazione da Compatibilità ed evoluzione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un messaggio tra componenti con identità e versione
- input: capability, schema, token e policy
- output: messaggio accettato o errore di protocollo
- nodi locali: Identità e autorizzazione: Interoperabilità non implica fiducia.; Compatibilità ed evoluzione: Version e capability negotiation rendono esplicita l'incompatibilità.
- limite visualizzato: compatibilità sintattica non garantisce semantica o autorizzazione
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
