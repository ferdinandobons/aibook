# Specifica visuale RLHF-02

- modello compositivo: reward_loop
- domanda principale: Quale controllo collega «KL e reward hacking» a «Valutazione e sicurezza» senza superare il limite dichiarato?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: dimostrazioni, preferenze, reward model e policy
- input: prompt, risposta scelta, rifiutata e score
- output: reward, log-probability e comportamento aggiornato
- nodi locali: KL e reward hacking: Il termine KL limita lo spostamento della policy. Un reward imperfetto può essere…; Valutazione e sicurezza: Win rate, reward e giudizi automatici devono essere affiancati da controlli…
- limite visualizzato: il reward è un proxy e può essere ottimizzato in modo scorretto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
