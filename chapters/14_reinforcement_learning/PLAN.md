# Piano interno. Capitolo 14

- Domanda centrale: quale contratto costruisce Reinforcement learning?
- Oggetto continuo: lo stato s_t della spedizione e la scelta a_t; input guida: s_t = (in_transito, ritardo=1).
- Prerequisito stabile: Capitolo 13, Apprendimento non supervisionato e auto-supervisionato.
- Gap: la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}.
- Output consegnato: la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}; consumer successivo: Capitolo 15, Dal percettrone alle reti multilayer.
- Invariante principale: un reward osservato non diventa automaticamente una misura del servizio reale.
- Visuali: RL-01 e RL-02, con famiglie compositive variabili.
- Snippet: code/snip_14_contract.py; output: code/outputs/SNIP-14-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Dalle predizioni alle azioni

- Ultima affermazione stabile: lo stato s_t della spedizione e la scelta a_t.
- Concetto nuovo: Un agente osserva uno stato, sceglie un'azione e riceve un reward. Il dato centrale non è una label statica, ma una traiettoria prodotta dall'interazione.
- Input e shape: s_t = (in_transito, ritardo=1).
- Operazione: la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}.
- Output e shape: la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}.
- Che cosa cambia: il passaggio specifico di «Dalle predizioni alle azioni».
- Invariante: un reward osservato non diventa automaticamente una misura del servizio reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: reward immediato 1, gamma 0,9 e valore futuro 0,5; provare anche una condizione incoerente e osservare il controllo.
- Consumer: MDP e ritorno.
- Prova: SRC-14-001 e sezione pubblica corrispondente.

## Transizione 2. MDP e ritorno

- Ultima affermazione stabile: lo stato s_t della spedizione e la scelta a_t.
- Concetto nuovo: Un Markov Decision Process specifica stati, azioni, transizioni, reward e fattore di sconto. Il ritorno somma reward futuri pesati e dipende dalla policy seguita.
- Input e shape: s_t = (in_transito, ritardo=1).
- Operazione: la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}.
- Output e shape: la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}.
- Che cosa cambia: il passaggio specifico di «MDP e ritorno».
- Invariante: un reward osservato non diventa automaticamente una misura del servizio reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: reward immediato 1, gamma 0,9 e valore futuro 0,5; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Value function e Bellman.
- Prova: SRC-14-002 e sezione pubblica corrispondente.

## Transizione 3. Value function e Bellman

- Ultima affermazione stabile: lo stato s_t della spedizione e la scelta a_t.
- Concetto nuovo: La value function riassume il ritorno atteso. Le equazioni di Bellman collegano il valore corrente a reward immediato e valore degli stati successivi.
- Input e shape: s_t = (in_transito, ritardo=1).
- Operazione: la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}.
- Output e shape: la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}.
- Che cosa cambia: il passaggio specifico di «Value function e Bellman».
- Invariante: un reward osservato non diventa automaticamente una misura del servizio reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: reward immediato 1, gamma 0,9 e valore futuro 0,5; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Policy gradient e actor-critic.
- Prova: SRC-14-003 e sezione pubblica corrispondente.

## Transizione 4. Policy gradient e actor-critic

- Ultima affermazione stabile: lo stato s_t della spedizione e la scelta a_t.
- Concetto nuovo: Il policy gradient aggiorna direttamente una policy stocastica. Actor-critic combina una policy con una stima di valore che riduce la varianza del segnale.
- Input e shape: s_t = (in_transito, ritardo=1).
- Operazione: la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}.
- Output e shape: la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}.
- Che cosa cambia: il passaggio specifico di «Policy gradient e actor-critic».
- Invariante: un reward osservato non diventa automaticamente una misura del servizio reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: reward immediato 1, gamma 0,9 e valore futuro 0,5; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Esplorazione e valutazione.
- Prova: SRC-14-004 e sezione pubblica corrispondente.

## Transizione 5. Esplorazione e valutazione

- Ultima affermazione stabile: lo stato s_t della spedizione e la scelta a_t.
- Concetto nuovo: Esplorare significa raccogliere informazione su azioni non ancora ben valutate. Una policy deve essere misurata su ritorno, varianza, sicurezza e condizioni dell'ambiente.
- Input e shape: s_t = (in_transito, ritardo=1).
- Operazione: la policy assegna probabilità alle azioni e l'ambiente restituisce r_{t+1}.
- Output e shape: la coppia (a_t, r_{t+1}) e il nuovo stato s_{t+1}.
- Che cosa cambia: il passaggio specifico di «Esplorazione e valutazione».
- Invariante: un reward osservato non diventa automaticamente una misura del servizio reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: reward immediato 1, gamma 0,9 e valore futuro 0,5; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Dal percettrone alle reti multilayer.
- Prova: SRC-14-001 e sezione pubblica corrispondente.
