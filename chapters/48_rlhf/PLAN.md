# Piano editoriale. Capitolo 48

## Obiettivo didattico

Seguire **Preferenze, reward model e RLHF** da prompt, risposta scelta, rifiutata e score a reward, log-probability e comportamento aggiornato, osservando fit del reward, KL e aggiornamento della policy senza oltrepassare questo limite: il reward è un proxy e può essere ottimizzato in modo scorretto.

## Prerequisiti reali

- Capitolo 14: Reinforcement learning
- Capitolo 46: Supervised fine-tuning e instruction tuning

## Percorso della lezione

1. **Dalle dimostrazioni alle preferenze.** Dati di confronto ordinano risposte alla stessa richiesta. Il protocollo deve registrare istruzioni ai valutatori, accordo e slice. Prova: SRC-48-001.
2. **Reward model.** Un modello assegna uno score alle risposte e viene addestrato con una loss di ranking. Lo score è una stima del dataset di preferenze, non una misura universale di qualità. Prova: SRC-48-002.
3. **Policy optimization.** PPO o algoritmi affini aggiornano la policy per aumentare reward mantenendo un vincolo rispetto al modello di riferimento. Prova: SRC-48-003.
4. **KL e reward hacking.** Il termine KL limita lo spostamento della policy. Un reward imperfetto può essere sfruttato senza migliorare l'obiettivo umano. Prova: SRC-48-004.
5. **Valutazione e sicurezza.** Win rate, reward e giudizi automatici devono essere affiancati da controlli indipendenti, red teaming e analisi di regressione. Prova: SRC-48-001.

## Prove e artefatti

- riferimento minimo: `code/snip_48_contract.py`; test: `code/test_48_contract.py`; output: `code/outputs/SNIP-48-001.txt`.
- visuali candidate: RLHF-01, RLHF-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
