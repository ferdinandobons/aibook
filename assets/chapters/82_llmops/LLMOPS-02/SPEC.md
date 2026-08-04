# Specifica visuale LLMOPS-02

- modello compositivo: rollback_path
- domanda principale: Quale controllo collega «Costo» a «Energia e sostenibilità» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: un servizio LLM dalla versione al consumo
- input: modello, richieste, device, energia e monitor
- output: versione attiva, costo per richiesta e alert
- nodi locali: Costo: Costo per token, richiesta, utente e risultato utile sono metriche differenti. Cache e…; Energia e sostenibilità: Potenza, tempo, utilizzo hardware e mix energetico influenzano l'impatto. Stime devono…
- limite visualizzato: un costo locale non descrive l'intero ciclo di vita
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
