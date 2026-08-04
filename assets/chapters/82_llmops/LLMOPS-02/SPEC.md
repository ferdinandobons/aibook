# Specifica visuale LLMOPS-02

- modello compositivo: rollback_path
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Costo da Energia e sostenibilità?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un servizio LLM dalla versione al consumo
- input: modello, richieste, device, energia e monitor
- output: versione attiva, costo per richiesta e alert
- nodi locali: Costo: Costo per token, richiesta, utente e risultato utile sono metriche differenti.; Energia e sostenibilità: Potenza, tempo, utilizzo hardware e mix energetico influenzano l'impatto.
- limite visualizzato: un costo locale non descrive l'intero ciclo di vita
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
