# Claim

- `CL-TRAINING-001`. Segnali che attraversano molti layer: Attivazioni e gradienti possono crescere o ridursi lungo la profondità. Inizializzazione, attivazioni e residual determinano la scala osservata.
- `CL-TRAINING-002`. Inizializzazione: Xavier e He initialization collegano la varianza dei pesi al fan-in o fan-out. Le formule presuppongono attivazioni e indipendenze approssimate.
- `CL-TRAINING-003`. Normalizzazione: BatchNorm, LayerNorm e RMSNorm normalizzano assi e statistiche differenti. Non sono sostituibili senza considerare batch, sequenza e architettura.
- `CL-TRAINING-004`. Residual e profondità: Un residual path conserva un percorso identità e facilita il trasporto di informazione. La somma richiede shape compatibili e una scala controllata.
- `CL-TRAINING-005`. Regolarizzazione e diagnostica: Dropout, weight decay, data augmentation ed early stopping agiscono in punti diversi. Curve, norme e slice aiutano a distinguere underfitting, overfitting e instabilità.
