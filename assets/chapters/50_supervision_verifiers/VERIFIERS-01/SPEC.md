# Specifica visuale VERIFIERS-01

- modello compositivo: verifier_funnel
- domanda principale: Come si passa da «Supervisionare il risultato» a «Verifier» mantenendo osservabile una traiettoria e il segnale di un verifier?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una traiettoria e il segnale di un verifier
- input: passaggi, risposta finale, criterio e indipendenza
- output: score verificato e failure localizzata
- nodi locali: Supervisionare il risultato: Outcome supervision assegna un segnale alla risposta finale e non localizza…; Supervisionare il processo: Process supervision etichetta passaggi intermedi. La validità dipende da come il…; Verifier: Un verifier valuta candidate rispetto a un criterio. Può essere una regola, un…
- limite visualizzato: un verifier può ereditare bias o essere ottimizzato
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
