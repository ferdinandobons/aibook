# Specifica visuale RLVR-01

- modello compositivo: rlvr_loop
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale percorso collega Reward verificabile a GRPO e policy update nel capitolo 51?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una risposta valutata da una regola verificabile
- input: prompt, rollout, gruppo di risposte e verifier
- output: reward, vantaggio e nuova policy
- nodi locali: Reward verificabile: Problemi con risposta controllabile, come codice o matematica, consentono reward da test.; Rollout e gruppi: La policy genera più soluzioni per la stessa richiesta.; GRPO e policy update: Algoritmi group-relative normalizzano reward all'interno di gruppi e aggiornano log-probab.
- limite visualizzato: la verificabilità vale solo per il dominio coperto dal verifier
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
