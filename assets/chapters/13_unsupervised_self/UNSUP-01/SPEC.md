# Specifica visuale `UNSUP-01`

- capitolo: `CH-P02-UNSUPERVISED-SELF-SUPERVISED`
- sezione: obiettivi senza label esterne
- famiglia: confronto di obiettivi
- orientamento: orizzontale
- sfondo: bianco puro `#FFFFFF`
- file candidato: `candidate-v1.png`
- renderer: `scripts/generate_unsupervised_visuals.py`

## Domanda unica

Quali segnali di training si possono costruire quando nessuna persona fornisce una label per ogni esempio?

## Contenuto

- clustering con centroidi;
- ricostruzione mascherata con target ricavato dall'input;
- contrasto tra viste o predizione di una parte del contesto;
- output e limite specifico di ciascun obiettivo.

## Invariante

L'assenza di label esterne non elimina l'obiettivo: cambia la procedura che costruisce il segnale supervisionante.
