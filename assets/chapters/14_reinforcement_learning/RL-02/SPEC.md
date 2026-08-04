# Specifica visuale RL-02

- modello compositivo: policy_branch
- orientamento: ramificato, radice in alto e foglie in basso
- domanda principale: Quale failure o confronto separa Policy gradient e actor-critic da Esplorazione e valutazione?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v52.png
- oggetto osservato: lo stato s_t della spedizione e la scelta a_t
- input: s_t = (in_transito, ritardo=1)
- output: la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}
- nodi locali: Policy gradient e actor-critic: Il policy gradient aggiorna direttamente una policy stocastica.; Esplorazione e valutazione: Esplorare significa raccogliere informazione su azioni non ancora ben valutate.
- limite visualizzato: un reward osservato non diventa automaticamente una misura del servizio reale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
