# Audit ATT-02

- File: `candidate-v1.png`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Ricalcolo

- `qK^T = [1,0,1]`.
- divisione per `sqrt(2)`: `[0,7071,0,0,7071]`.
- softmax: `[0,40111209, 0,19777581, 0,40111209]`.
- output con `V=[[1,0],[0,1],[1,1]]`: `[0,80222418, 0,59888791]`.

## Controlli

- [x] Valori coerenti con il codice eseguito.
- [x] Frecce in ordine sinistra-destra.
- [x] Nessun collegamento ambiguo.
- [x] Scaling applicato agli score, non a `V`.
- [x] Shape finale dichiarata.
