# Specifica visuale OPT-01

- modello compositivo: pairwise_objective
- domanda principale: Come si passa da «Evitare un reward model esplicito» a «Temperatura beta» mantenendo osservabile una coppia chosen-rejected per l'ottimizzazione diretta?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una coppia chosen-rejected per l'ottimizzazione diretta
- input: prompt, log-probability della policy e riferimento
- output: loss di preferenza e policy aggiornata
- nodi locali: Evitare un reward model esplicito: DPO riscrive un obiettivo di preferenza usando log-probability della policy e del…; Coppie chosen e rejected: Ogni esempio richiede la stessa condizione e due risposte confrontabili. Errori o stili…; Temperatura beta: Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e…
- limite visualizzato: la preferenza osservata non è una verità assoluta
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
