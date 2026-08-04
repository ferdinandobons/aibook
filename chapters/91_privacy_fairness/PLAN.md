# Piano editoriale. Capitolo 91

## Obiettivo didattico

Seguire **Privacy, fairness e unlearning** da record, membership, gruppo, label e budget privacy a utility, leakage, disparità e verifica di rimozione, osservando DP, fairness evaluation e unlearning senza oltrepassare questo limite: privacy, fairness e utility richiedono metriche e trade-off espliciti.

## Prerequisiti reali

- Capitolo 4: Come valutare criticamente un risultato di AI
- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 32: Il ciclo di vita dei dati

## Percorso della lezione

1. **Memorizzazione e leakage.** Un modello può riprodurre sequenze rare. Membership inference e extraction misurano rischi differenti. Prova: SRC-91-001.
2. **Differential privacy.** DP limita l'influenza di un record mediante clipping e rumore, con parametri epsilon e delta e un costo di utilità. Prova: SRC-91-002.
3. **Fairness.** Metriche di parità, equalized odds e calibration possono essere incompatibili sotto distribuzioni differenti. Il contesto decisionale guida la scelta. Prova: SRC-91-003.
4. **Bias nei dati e nel sistema.** Rappresentazione, label, soglie e policy possono produrre disparità anche con lo stesso modello. Prova: SRC-91-004.
5. **Machine unlearning.** Rimuovere l'influenza di dati richiede un criterio e una verifica. Cancellare un record dal corpus non modifica automaticamente il checkpoint. Prova: SRC-91-001.

## Prove e artefatti

- riferimento minimo: `code/snip_91_contract.py`; test: `code/test_91_contract.py`; output: `code/outputs/SNIP-91-001.txt`.
- visuali candidate: FAIRNESS-01, FAIRNESS-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
