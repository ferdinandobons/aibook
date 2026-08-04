# Specifica visuale RLVR-02

- modello compositivo: reward_gate
- orientamento: a zone, esterno-controllo-effetto
- domanda principale: Quale failure o confronto separa Sparse reward da Verificabilità limitata?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v48.png
- oggetto osservato: una risposta valutata da una regola verificabile
- input: prompt, rollout, gruppo di risposte e verifier
- output: reward, vantaggio e nuova policy
- nodi locali: Sparse reward: Un risultato finale corretto non identifica quali passaggi siano utili.; Verificabilità limitata: Un test incompleto può premiare exploit.
- limite visualizzato: la verificabilità vale solo per il dominio coperto dal verifier
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
