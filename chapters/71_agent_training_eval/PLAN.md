# Piano interno. Capitolo 71

- Domanda centrale: quale contratto costruisce Training e valutazione degli agenti?
- Oggetto continuo: traiettorie agentiche usate come dati e valutazione; input guida: task, trace, policy, outcome e costo.
- Prerequisito stabile: Capitolo 70, Multi-agent, browser, computer e code agents.
- Gap: SFT, RL, benchmark e harness.
- Output consegnato: score di task, violazioni e failure per step; consumer successivo: Capitolo 72, Sicurezza operativa degli agenti.
- Invariante principale: task riuscito e traiettoria sicura sono criteri distinti.
- Visuali: EVAL-01 e EVAL-02, con famiglie compositive variabili.
- Snippet: code/snip_71_contract.py; output: code/outputs/SNIP-71-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Traiettorie come dati

- Ultima affermazione stabile: traiettorie agentiche usate come dati e valutazione.
- Concetto nuovo: Osservazioni, azioni, tool result e reward formano esempi sequenziali. Logging incompleto rende impossibile ricostruire il fallimento.
- Input e shape: task, trace, policy, outcome e costo.
- Operazione: SFT, RL, benchmark e harness.
- Output e shape: score di task, violazioni e failure per step.
- Che cosa cambia: il passaggio specifico di «Traiettorie come dati».
- Invariante: task riuscito e traiettoria sicura sono criteri distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due traiettorie con stesso esito ma una violazione di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Imitation e SFT.
- Prova: SRC-71-001 e sezione pubblica corrispondente.

## Transizione 2. Imitation e SFT

- Ultima affermazione stabile: traiettorie agentiche usate come dati e valutazione.
- Concetto nuovo: Traiettorie riuscite possono essere imitate. Il dataset deve includere recovery, errori e decisioni di non agire.
- Input e shape: task, trace, policy, outcome e costo.
- Operazione: SFT, RL, benchmark e harness.
- Output e shape: score di task, violazioni e failure per step.
- Che cosa cambia: il passaggio specifico di «Imitation e SFT».
- Invariante: task riuscito e traiettoria sicura sono criteri distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due traiettorie con stesso esito ma una violazione di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: RL in ambienti.
- Prova: SRC-71-002 e sezione pubblica corrispondente.

## Transizione 3. RL in ambienti

- Ultima affermazione stabile: traiettorie agentiche usate come dati e valutazione.
- Concetto nuovo: Reward verificabili o simulati aggiornano policy multi-step. Il modello può sfruttare bug dell'ambiente o del checker.
- Input e shape: task, trace, policy, outcome e costo.
- Operazione: SFT, RL, benchmark e harness.
- Output e shape: score di task, violazioni e failure per step.
- Che cosa cambia: il passaggio specifico di «RL in ambienti».
- Invariante: task riuscito e traiettoria sicura sono criteri distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due traiettorie con stesso esito ma una violazione di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Benchmark agentici.
- Prova: SRC-71-003 e sezione pubblica corrispondente.

## Transizione 4. Benchmark agentici

- Ultima affermazione stabile: traiettorie agentiche usate come dati e valutazione.
- Concetto nuovo: Success rate, step, costo e side effect devono essere misurati. Task statici rischiano contaminazione e overfitting.
- Input e shape: task, trace, policy, outcome e costo.
- Operazione: SFT, RL, benchmark e harness.
- Output e shape: score di task, violazioni e failure per step.
- Che cosa cambia: il passaggio specifico di «Benchmark agentici».
- Invariante: task riuscito e traiettoria sicura sono criteri distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due traiettorie con stesso esito ma una violazione di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Evaluation harness.
- Prova: SRC-71-004 e sezione pubblica corrispondente.

## Transizione 5. Evaluation harness

- Ultima affermazione stabile: traiettorie agentiche usate come dati e valutazione.
- Concetto nuovo: Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale.
- Input e shape: task, trace, policy, outcome e costo.
- Operazione: SFT, RL, benchmark e harness.
- Output e shape: score di task, violazioni e failure per step.
- Che cosa cambia: il passaggio specifico di «Evaluation harness».
- Invariante: task riuscito e traiettoria sicura sono criteri distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due traiettorie con stesso esito ma una violazione di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sicurezza operativa degli agenti.
- Prova: SRC-71-001 e sezione pubblica corrispondente.
