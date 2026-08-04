# Piano editoriale. Capitolo 21

## Obiettivo didattico

Seguire **Modelli autoregressivi** da un prefisso di tre token e una mask causale a logits, token scelto e traiettoria, osservando fattorizzazione, teacher forcing e decoding senza oltrepassare questo limite: nessuna posizione futura entra nella predizione causale.

## Prerequisiti reali

- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 8: Teoria dell'informazione e funzioni obiettivo
- Capitolo 20: Fondamenti della modellazione generativa

## Percorso della lezione

1. **Fattorizzare una sequenza.** La chain rule scompone la probabilità con un ordine. Ogni fattore condiziona sugli elementi precedenti. Prova: SRC-21-001.
2. **Teacher forcing.** Durante il training il modello riceve il prefisso reale e predice il passo successivo. Durante la generazione riceve anche i propri output. Prova: SRC-21-002.
3. **Maschera causale.** La causal mask impedisce a una posizione di usare target futuri. Un errore nella maschera produce leakage pur con loss numericamente valida. Prova: SRC-21-003.
4. **Sampling e accumulo degli errori.** Ogni scelta modifica il contesto successivo. Errori iniziali possono spostare la traiettoria verso regioni poco viste nel training. Prova: SRC-21-004.
5. **Immagini, audio e token discreti.** L'autoregressione non è limitata al testo. Una sequenza può rappresentare pixel, code audio o latent discreti. Prova: SRC-21-001.

## Prove e artefatti

- riferimento minimo: `code/snip_21_contract.py`; test: `code/test_21_contract.py`; output: `code/outputs/SNIP-21-001.txt`.
- visuali candidate: AUTOREGR-01, AUTOREGR-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
