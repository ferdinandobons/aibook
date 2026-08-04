# Specifica visuale RLHF-01

- modello compositivo: preference_pipeline
- orientamento: orizzontale, lettura da sinistra a destra
- domanda principale: Quale percorso collega Dalle dimostrazioni alle preferenze a Policy optimization nel capitolo 48?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: dimostrazioni, preferenze, reward model e policy
- input: prompt, risposta scelta, rifiutata e score
- output: reward, log-probability e comportamento aggiornato
- nodi locali: Dalle dimostrazioni alle preferenze: Dati di confronto ordinano risposte alla stessa richiesta.; Reward model: Un modello assegna uno score alle risposte e viene addestrato con una loss di ranking.; Policy optimization: PPO o algoritmi affini aggiornano la policy per aumentare reward mantenendo un vincolo ris.
- limite visualizzato: il reward è un proxy e può essere ottimizzato in modo scorretto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
