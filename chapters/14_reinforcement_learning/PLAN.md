# Piano editoriale. Capitolo 14

## Obiettivo didattico

Seguire **Reinforcement learning** da s_t = (in_transito, ritardo=1) a la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}, osservando la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1} senza oltrepassare questo limite: un reward osservato non diventa automaticamente una misura del servizio reale.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 12: Apprendimento supervisionato

## Percorso della lezione

1. **Dalle predizioni alle azioni.** Un agente osserva uno stato, sceglie un'azione e riceve un reward. Il dato centrale non è una label statica, ma una traiettoria prodotta dall'interazione. Prova: SRC-14-001.
2. **MDP e ritorno.** Un Markov Decision Process specifica stati, azioni, transizioni, reward e fattore di sconto. Il ritorno somma reward futuri pesati e dipende dalla policy seguita. Prova: SRC-14-002.
3. **Value function e Bellman.** La value function riassume il ritorno atteso. Le equazioni di Bellman collegano il valore corrente a reward immediato e valore degli stati successivi. Prova: SRC-14-003.
4. **Policy gradient e actor-critic.** Il policy gradient aggiorna direttamente una policy stocastica. Actor-critic combina una policy con una stima di valore che riduce la varianza del segnale. Prova: SRC-14-004.
5. **Esplorazione e valutazione.** Esplorare significa raccogliere informazione su azioni non ancora ben valutate. Una policy deve essere misurata su ritorno, varianza, sicurezza e condizioni dell'ambiente. Prova: SRC-14-001.

## Prove e artefatti

- riferimento minimo: `code/snip_14_contract.py`; test: `code/test_14_contract.py`; output: `code/outputs/SNIP-14-001.txt`.
- visuali candidate: RL-01, RL-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
