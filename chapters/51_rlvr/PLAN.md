# Piano editoriale. Capitolo 51

## Obiettivo didattico

Seguire **Reinforcement learning con reward verificabili** da prompt, rollout, gruppo di risposte e verifier a reward, vantaggio e nuova policy, osservando reward verificabile, policy update e gestione di reward sparso senza oltrepassare questo limite: la verificabilità vale solo per il dominio coperto dal verifier.

## Prerequisiti reali

- Capitolo 14: Reinforcement learning
- Capitolo 50: Process supervision, outcome supervision e verifier

## Percorso della lezione

1. **Reward verificabile.** Problemi con risposta controllabile, come codice o matematica, consentono reward da test, parser o esecutori. Prova: SRC-51-001.
2. **Rollout e gruppi.** La policy genera più soluzioni per la stessa richiesta. Il reward confronta traiettorie e costruisce advantage o ranking. Prova: SRC-51-001.
3. **GRPO e policy update.** Algoritmi group-relative normalizzano reward all'interno di gruppi e aggiornano log-probability con vincoli di stabilità. Prova: SRC-51-002.
4. **Sparse reward.** Un risultato finale corretto non identifica quali passaggi siano utili. Exploration, curriculum e shaping cambiano la densità del segnale. Prova: SRC-51-003.
5. **Verificabilità limitata.** Un test incompleto può premiare exploit. Il reward verificabile è affidabile soltanto nel perimetro del verificatore. Prova: SRC-51-004.

## Prove e artefatti

- riferimento minimo: `code/snip_51_contract.py`; test: `code/test_51_contract.py`; output: `code/outputs/SNIP-51-001.txt`.
- visuali candidate: RLVR-01, RLVR-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
