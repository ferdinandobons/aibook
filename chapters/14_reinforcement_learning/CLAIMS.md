# Claim

- `CL-RL-001`. Dalle predizioni alle azioni: Un agente osserva uno stato, sceglie un'azione e riceve un reward. Il dato centrale non è una label statica, ma una traiettoria prodotta dall'interazione.
- `CL-RL-002`. MDP e ritorno: Un Markov Decision Process specifica stati, azioni, transizioni, reward e fattore di sconto. Il ritorno somma reward futuri pesati e dipende dalla policy seguita.
- `CL-RL-003`. Value function e Bellman: La value function riassume il ritorno atteso. Le equazioni di Bellman collegano il valore corrente a reward immediato e valore degli stati successivi.
- `CL-RL-004`. Policy gradient e actor-critic: Il policy gradient aggiorna direttamente una policy stocastica. Actor-critic combina una policy con una stima di valore che riduce la varianza del segnale.
- `CL-RL-005`. Esplorazione e valutazione: Esplorare significa raccogliere informazione su azioni non ancora ben valutate. Una policy deve essere misurata su ritorno, varianza, sicurezza e condizioni dell'ambiente.
