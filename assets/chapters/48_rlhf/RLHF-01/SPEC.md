# Specifica visuale RLHF-01

- modello compositivo: preference_pipeline
- domanda principale: Come si passa da «Dalle dimostrazioni alle preferenze» a «Policy optimization» mantenendo osservabile dimostrazioni, preferenze, reward model e policy?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: dimostrazioni, preferenze, reward model e policy
- input: prompt, risposta scelta, rifiutata e score
- output: reward, log-probability e comportamento aggiornato
- nodi locali: Dalle dimostrazioni alle preferenze: Dati di confronto ordinano risposte alla stessa richiesta. Il protocollo deve registrare…; Reward model: Un modello assegna uno score alle risposte e viene addestrato con una loss di ranking.…; Policy optimization: PPO o algoritmi affini aggiornano la policy per aumentare reward mantenendo un vincolo…
- limite visualizzato: il reward è un proxy e può essere ottimizzato in modo scorretto
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
