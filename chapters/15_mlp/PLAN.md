# Piano editoriale. Capitolo 15

## Obiettivo didattico

Seguire **Dal percettrone alle reti multilayer** da x = [1, 2] con shape [2] a un nuovo vettore h con shape dichiarata, osservando una trasformazione affine seguita da una funzione di attivazione senza oltrepassare questo limite: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 12: Apprendimento supervisionato

## Percorso della lezione

1. **Una decisione lineare.** Il percettrone combina feature con pesi e bias. Il confine risultante è lineare nello spazio delle feature. Prova: SRC-15-001.
2. **Strati nascosti.** Una MLP alterna trasformazioni affini e funzioni non lineari. Senza non linearità, più layer affini collassano in una sola trasformazione affine. Prova: SRC-15-002.
3. **Attivazioni.** ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. La scelta deve essere letta insieme a inizializzazione e normalizzazione. Prova: SRC-15-003.
4. **Capacità ed espressività.** Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile. Prova: SRC-15-004.
5. **Dal forward al training.** Il forward produce logits e loss. Backpropagation e optimizer trasformano il segnale in aggiornamenti, secondo i contratti costruiti nei capitoli matematici. Prova: SRC-15-001.

## Prove e artefatti

- riferimento minimo: `code/snip_15_contract.py`; test: `code/test_15_contract.py`; output: `code/outputs/SNIP-15-001.txt`.
- visuali candidate: MLP-01, MLP-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
