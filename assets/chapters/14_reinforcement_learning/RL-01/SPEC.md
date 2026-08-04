# Specifica visuale RL-01

- modello compositivo: interaction_loop
- orientamento: radiale, lettura in senso orario
- domanda principale: Quale percorso collega Dalle predizioni alle azioni a Value function e Bellman nel capitolo 14?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v51.png
- oggetto osservato: lo stato s_t della spedizione e la scelta a_t
- input: s_t = (in_transito, ritardo=1)
- output: la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}
- nodi locali: Dalle predizioni alle azioni: Un agente osserva uno stato, sceglie un'azione e riceve un reward.; MDP e ritorno: Il ritorno somma reward futuri pesati e dipende dalla policy seguita.; Value function e Bellman: La value function riassume il ritorno atteso.
- limite visualizzato: un reward osservato non diventa automaticamente una misura del servizio reale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- contenimento: safe margin 20 px; distanza minima tra elementi 8 px
- geometria: `GEOMETRY.json`, nessuna intersezione o tangenza tra elementi fratelli
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
