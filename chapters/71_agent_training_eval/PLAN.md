# Piano editoriale. Capitolo 71

## Obiettivo didattico

Seguire **Training e valutazione degli agenti** da task, trace, policy, outcome e costo a score di task, violazioni e failure per step, osservando SFT, RL, benchmark e harness senza oltrepassare questo limite: task riuscito e traiettoria sicura sono criteri distinti.

## Prerequisiti reali

- Capitolo 4: Come valutare criticamente un risultato di AI
- Capitolo 69: Ciclo agentico, pianificazione e verifica
- Capitolo 70: Multi-agent, browser, computer e code agents

## Percorso della lezione

1. **Traiettorie come dati.** Osservazioni, azioni, tool result e reward formano esempi sequenziali. Logging incompleto rende impossibile ricostruire il fallimento. Prova: SRC-71-001.
2. **Imitation e SFT.** Traiettorie riuscite possono essere imitate. Il dataset deve includere recovery, errori e decisioni di non agire. Prova: SRC-71-002.
3. **RL in ambienti.** Reward verificabili o simulati aggiornano policy multi-step. Il modello può sfruttare bug dell'ambiente o del checker. Prova: SRC-71-003.
4. **Benchmark agentici.** Success rate, step, costo e side effect devono essere misurati. Task statici rischiano contaminazione e overfitting. Prova: SRC-71-004.
5. **Evaluation harness.** Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale. Prova: SRC-71-001.

## Prove e artefatti

- riferimento minimo: `code/snip_71_contract.py`; test: `code/test_71_contract.py`; output: `code/outputs/SNIP-71-001.txt`.
- visuali candidate: EVAL-01, EVAL-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
