# Specifica visuale TRAINING-01

- modello compositivo: reasoning_curriculum
- domanda principale: Come si passa da «Tracce e risposte» a «Self-consistency e rejection sampling» mantenendo osservabile una traccia di reasoning e la risposta che la segue?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una traccia di reasoning e la risposta che la segue
- input: prompt, trace del teacher, answer e costo in token
- output: traccia selezionata, risposta e misura di costo
- nodi locali: Tracce e risposte: Una traccia di ragionamento è testo prodotto dal modello. Può aiutare il training senza…; Distillazione: Un teacher produce soluzioni o distribuzioni che diventano target per uno student.…; Self-consistency e rejection sampling: Più candidate vengono generate e selezionate con voto o verifier. Il dataset risultante…
- limite visualizzato: una traccia leggibile non prova faithfulness causale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
