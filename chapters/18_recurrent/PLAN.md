# Piano editoriale. Capitolo 18

## Obiettivo didattico

Seguire **Reti ricorrenti e modelli sequenziali** da x_1, x_2, x_3 e h_0 = 0 a h_t e, se richiesto, una predizione per il passo, osservando ogni passo combina input corrente e stato precedente con gli stessi pesi senza oltrepassare questo limite: lo stato precedente deve essere consumato prima di produrre quello successivo.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 15: Dal percettrone alle reti multilayer

## Percorso della lezione

1. **Uno stato che attraversa la sequenza.** Una RNN aggiorna uno stato nascosto con input e stato precedente. Lo stesso insieme di parametri viene riutilizzato a ogni passo. Prova: SRC-18-001.
2. **Backpropagation through time.** Il grafo ricorrente viene srotolato nel tempo. Gradienti molto lunghi possono svanire o esplodere. Prova: SRC-18-002.
3. **LSTM e GRU.** Gate di input, forget e output controllano il flusso della memoria. GRU usa una parametrizzazione più compatta, con un contratto differente. Prova: SRC-18-003.
4. **Bidirezionalità e causalità.** Una rete bidirezionale usa anche il futuro ed è adatta a encoding offline. Non può essere usata direttamente per generazione causale streaming. Prova: SRC-18-004.
5. **RNN, attention e stato.** La recurrence mantiene memoria compatta; l'attention accede a rappresentazioni esplicite. I due meccanismi possono essere complementari. Prova: SRC-18-001.

## Prove e artefatti

- riferimento minimo: `code/snip_18_contract.py`; test: `code/test_18_contract.py`; output: `code/outputs/SNIP-18-001.txt`.
- visuali candidate: RECURREN-01, RECURREN-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
