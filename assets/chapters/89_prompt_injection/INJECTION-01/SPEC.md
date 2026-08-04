# Specifica visuale INJECTION-01

- modello compositivo: prompt_trust_boundary
- domanda principale: Come si passa da «Istruzioni e dati» a «Tool mediation» mantenendo osservabile istruzioni e dati che entrano in un sistema con tool?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v50.png
- oggetto osservato: istruzioni e dati che entrano in un sistema con tool
- input: prompt, documento non fidato, tool e scope
- output: azione autorizzata o rifiuto con traccia
- nodi locali: Istruzioni e dati: Contenuti recuperati, pagine e documenti sono dati non fidati. Non devono acquisire…; Indirect prompt injection: Una istruzione malevola può essere inserita in una fonte consultata dall'agente e…; Tool mediation: Policy esterne validano tool, argomenti e destinazioni. Il modello propone, ma…
- limite visualizzato: contenuto recuperato non diventa istruzione privilegiata
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
