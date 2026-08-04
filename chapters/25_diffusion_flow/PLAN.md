# Piano editoriale. Capitolo 25

## Obiettivo didattico

Seguire **Diffusione, score matching e flow matching** da x_0, rumore epsilon e timestep t a stima del rumore e campione ricostruito, osservando forward noising, score o velocity e sampler senza oltrepassare questo limite: parametrizzazione e scheduler fanno parte del contratto.

## Prerequisiti reali

- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 20: Fondamenti della modellazione generativa

## Percorso della lezione

1. **Corrompere e ricostruire.** La diffusione forward aggiunge rumore secondo uno schedule. Il modello impara a invertire o a stimare una quantità equivalente. Prova: SRC-25-001.
2. **Score matching.** Lo score è il gradiente del log-density rispetto ai dati perturbati. Denoising score matching evita di conoscere la densità normale completa. Prova: SRC-25-002.
3. **Parametrizzazioni epsilon, x0 e v.** Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambiano scala e weighting del training. Prova: SRC-25-003.
4. **Sampler.** DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti. Meno step non garantiscono stessa distribuzione o qualità. Prova: SRC-25-004.
5. **Flow matching e rectified flow.** Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni. Rectified flow cerca traiettorie più rettilinee in setup specifici. Prova: SRC-25-001.

## Prove e artefatti

- riferimento minimo: `code/snip_25_contract.py`; test: `code/test_25_contract.py`; output: `code/outputs/SNIP-25-001.txt`.
- visuali candidate: FLOW-01, FLOW-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
