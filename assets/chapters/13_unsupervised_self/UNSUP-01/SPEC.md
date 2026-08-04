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
- domanda principale: Quale trasformazione centrale rende osservabile «Senza label non significa senza obiettivo» nel capitolo 13?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
