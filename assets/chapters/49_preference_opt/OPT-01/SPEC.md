# Specifica visuale OPT-01

- modello compositivo: pairwise_objective
- orientamento: a grafo, nodi e archi separati
- domanda principale: Quale percorso collega Evitare un reward model esplicito a Temperatura beta nel capitolo 49?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una coppia chosen-rejected per l'ottimizzazione diretta
- input: prompt, log-probability della policy e riferimento
- output: loss di preferenza e policy aggiornata
- nodi locali: Evitare un reward model esplicito: DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferime.; Coppie chosen e rejected: Ogni esempio richiede la stessa condizione e due risposte confrontabili.; Temperatura beta: Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica.
- limite visualizzato: la preferenza osservata non è una verità assoluta
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
