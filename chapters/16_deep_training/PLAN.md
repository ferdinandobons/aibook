# Piano editoriale. Capitolo 16

## Obiettivo didattico

Seguire **Addestrare reti profonde** da x_l con shape [batch, d] e norma misurata a x_{l+1} con la stessa o con una nuova shape dichiarata, osservando un blocco, una normalizzazione o un percorso residuale senza oltrepassare questo limite: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 15: Dal percettrone alle reti multilayer

## Percorso della lezione

1. **Segnali che attraversano molti layer.** Attivazioni e gradienti possono crescere o ridursi lungo la profondità. Inizializzazione, attivazioni e residual determinano la scala osservata. Prova: SRC-16-001.
2. **Inizializzazione.** Xavier e He initialization collegano la varianza dei pesi al fan-in o fan-out. Le formule presuppongono attivazioni e indipendenze approssimate. Prova: SRC-16-002.
3. **Normalizzazione.** BatchNorm, LayerNorm e RMSNorm normalizzano assi e statistiche differenti. Non sono sostituibili senza considerare batch, sequenza e architettura. Prova: SRC-16-003.
4. **Residual e profondità.** Un residual path conserva un percorso identità e facilita il trasporto di informazione. La somma richiede shape compatibili e una scala controllata. Prova: SRC-16-004.
5. **Regolarizzazione e diagnostica.** Dropout, weight decay, data augmentation ed early stopping agiscono in punti diversi. Curve, norme e slice aiutano a distinguere underfitting, overfitting e instabilità. Prova: SRC-16-001.

## Prove e artefatti

- riferimento minimo: `code/snip_16_contract.py`; test: `code/test_16_contract.py`; output: `code/outputs/SNIP-16-001.txt`.
- visuali candidate: TRAINING-01, TRAINING-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
