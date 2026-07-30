# Audit ATT-01

- File: `candidate-v1.png`
- Esito tecnico: **da modificare**
- Approvazione autoriale: aperta

## Controlli

- [x] Una sola differenza controllata.
- [x] I coefficienti di ogni riga sommano a 1.
- [x] Le sorgenti sono identiche nei due casi.
- [x] Le due query producono combinazioni diverse nel pannello destro.
- [x] Nessuna linea si incrocia in modo ambiguo.
- [x] Il colore non è l'unico significato.

## Nota di review

Difetto bloccante: le frecce dal vettore `c` verso i box `query q1/q2` possono suggerire che il contesto produca le query. La figura è inclusa soltanto per valutare il confronto concettuale; deve essere rigenerata prima di un uso finale, sostituendo i box con `consumer 1` e `consumer 2` oppure invertendo la rappresentazione causale.
