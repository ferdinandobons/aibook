# Piano editoriale. Capitolo 62

## Obiettivo didattico

Seguire **World model, embodied AI e vision-language-action** da osservazione, stato, azione e dinamica a azione, stato previsto e risultato fisico, osservando world model, planning, VLA e controllo senza oltrepassare questo limite: sim-to-real richiede una misura sul sistema reale.

## Prerequisiti reali

- Capitolo 14: Reinforcement learning
- Capitolo 55: Fondamenti della multimodalità
- Capitolo 61: 3D, spazio e rappresentazione delle scene

## Percorso della lezione

1. **Modello della dinamica.** Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione. Prova: SRC-62-001.
2. **Planning nel modello.** Traiettorie candidate vengono simulate e valutate prima di agire. Errori del modello possono essere sfruttati dal planner. Prova: SRC-62-002.
3. **Embodied perception.** Un agente fisico collega camera, propriocezione, linguaggio e coordinate. Latenza e calibrazione influenzano ogni azione. Prova: SRC-62-003.
4. **Vision-language-action.** VLA mappa osservazioni e istruzioni a token o controlli di azione. Frequenza e discretizzazione devono essere dichiarate. Prova: SRC-62-004.
5. **Sicurezza e sim-to-real.** Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale. Prova: SRC-62-001.

## Prove e artefatti

- riferimento minimo: `code/snip_62_contract.py`; test: `code/test_62_contract.py`; output: `code/outputs/SNIP-62-001.txt`.
- visuali candidate: EMBODIED-01, EMBODIED-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
