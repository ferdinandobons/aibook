# Specifica visuale `SUP-02`

- capitolo: `CH-P02-SUPERVISED`
- sezione: soglia e costo decisionale
- famiglia: confronto matriciale
- orientamento: orizzontale
- sfondo: bianco puro `#FFFFFF`
- file candidato: `candidate-v1.png`
- renderer: `scripts/generate_supervised_visuals.py`

## Domanda unica

Come possono due soglie avere la stessa accuracy ma costi e distribuzioni di errore differenti?

## Contenuto

- due matrici di confusione sulla stessa numerosità;
- soglia `0,30` e soglia `0,50`;
- pannello centrale con accuracy comune;
- footer che separa le slice con tracking disponibile e mancante.
- domanda principale: Quale confronto o limite chiarisce «Predittore, loss e rischio empirico»?
