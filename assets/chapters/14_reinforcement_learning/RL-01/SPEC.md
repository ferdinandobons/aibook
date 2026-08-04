# Specifica visuale RL-01

- modello compositivo: interaction_loop
- domanda principale: Come si passa da «Dalle predizioni alle azioni» a «Value function e Bellman» mantenendo osservabile lo stato s_t della spedizione e la scelta a_t?
- formato: PNG raster 1800x1000, RGB
- sfondo: #FFFFFF
- file candidato: candidate-v51.png
- oggetto osservato: lo stato s_t della spedizione e la scelta a_t
- input: s_t = (in_transito, ritardo=1)
- output: la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}
- nodi locali: Dalle predizioni alle azioni: Un agente osserva uno stato, sceglie un'azione e riceve un reward. Il dato centrale non…; MDP e ritorno: Un Markov Decision Process specifica stati, azioni, transizioni, reward e fattore di…; Value function e Bellman: La value function riassume il ritorno atteso. Le equazioni di Bellman collegano il…
- limite visualizzato: un reward osservato non diventa automaticamente una misura del servizio reale
- valori quantitativi: nessun benchmark inventato; la figura mostra relazioni qualitative o output versionati
- accessibilita: ordine leggibile, label testuali, significato non affidato al solo colore
- generatore: scripts/generate_visuals_v2.py
- approvazione autoriale: aperta
