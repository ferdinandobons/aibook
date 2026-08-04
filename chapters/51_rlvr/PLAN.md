# Piano interno. Capitolo 51

- Domanda centrale: quale contratto costruisce Reinforcement learning con reward verificabili?
- Oggetto continuo: una risposta valutata da una regola verificabile; input guida: prompt, rollout, gruppo di risposte e verifier.
- Prerequisito stabile: Capitolo 50, Process supervision, outcome supervision e verifier.
- Gap: reward verificabile, policy update e gestione di reward sparso.
- Output consegnato: reward, vantaggio e nuova policy; consumer successivo: Capitolo 52, Addestrare e distillare il reasoning.
- Invariante principale: la verificabilità vale solo per il dominio coperto dal verifier.
- Visuali: RLVR-01 e RLVR-02, con famiglie compositive variabili.
- Snippet: code/snip_51_contract.py; output: code/outputs/SNIP-51-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Reward verificabile

- Ultima affermazione stabile: una risposta valutata da una regola verificabile.
- Concetto nuovo: Problemi con risposta controllabile, come codice o matematica, consentono reward da test, parser o esecutori.
- Input e shape: prompt, rollout, gruppo di risposte e verifier.
- Operazione: reward verificabile, policy update e gestione di reward sparso.
- Output e shape: reward, vantaggio e nuova policy.
- Che cosa cambia: il passaggio specifico di «Reward verificabile».
- Invariante: la verificabilità vale solo per il dominio coperto dal verifier.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre rollout con due risposte che passano una regola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Rollout e gruppi.
- Prova: SRC-51-001 e sezione pubblica corrispondente.

## Transizione 2. Rollout e gruppi

- Ultima affermazione stabile: una risposta valutata da una regola verificabile.
- Concetto nuovo: La policy genera più soluzioni per la stessa richiesta. Il reward confronta traiettorie e costruisce advantage o ranking.
- Input e shape: prompt, rollout, gruppo di risposte e verifier.
- Operazione: reward verificabile, policy update e gestione di reward sparso.
- Output e shape: reward, vantaggio e nuova policy.
- Che cosa cambia: il passaggio specifico di «Rollout e gruppi».
- Invariante: la verificabilità vale solo per il dominio coperto dal verifier.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre rollout con due risposte che passano una regola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: GRPO e policy update.
- Prova: SRC-51-001 e sezione pubblica corrispondente.

## Transizione 3. GRPO e policy update

- Ultima affermazione stabile: una risposta valutata da una regola verificabile.
- Concetto nuovo: Algoritmi group-relative normalizzano reward all'interno di gruppi e aggiornano log-probability con vincoli di stabilità.
- Input e shape: prompt, rollout, gruppo di risposte e verifier.
- Operazione: reward verificabile, policy update e gestione di reward sparso.
- Output e shape: reward, vantaggio e nuova policy.
- Che cosa cambia: il passaggio specifico di «GRPO e policy update».
- Invariante: la verificabilità vale solo per il dominio coperto dal verifier.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre rollout con due risposte che passano una regola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sparse reward.
- Prova: SRC-51-002 e sezione pubblica corrispondente.

## Transizione 4. Sparse reward

- Ultima affermazione stabile: una risposta valutata da una regola verificabile.
- Concetto nuovo: Un risultato finale corretto non identifica quali passaggi siano utili. Exploration, curriculum e shaping cambiano la densità del segnale.
- Input e shape: prompt, rollout, gruppo di risposte e verifier.
- Operazione: reward verificabile, policy update e gestione di reward sparso.
- Output e shape: reward, vantaggio e nuova policy.
- Che cosa cambia: il passaggio specifico di «Sparse reward».
- Invariante: la verificabilità vale solo per il dominio coperto dal verifier.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre rollout con due risposte che passano una regola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Verificabilità limitata.
- Prova: SRC-51-003 e sezione pubblica corrispondente.

## Transizione 5. Verificabilità limitata

- Ultima affermazione stabile: una risposta valutata da una regola verificabile.
- Concetto nuovo: Un test incompleto può premiare exploit. Il reward verificabile è affidabile soltanto nel perimetro del verificatore.
- Input e shape: prompt, rollout, gruppo di risposte e verifier.
- Operazione: reward verificabile, policy update e gestione di reward sparso.
- Output e shape: reward, vantaggio e nuova policy.
- Che cosa cambia: il passaggio specifico di «Verificabilità limitata».
- Invariante: la verificabilità vale solo per il dominio coperto dal verifier.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre rollout con due risposte che passano una regola; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Addestrare e distillare il reasoning.
- Prova: SRC-51-004 e sezione pubblica corrispondente.
