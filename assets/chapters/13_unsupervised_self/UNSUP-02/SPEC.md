# Specifica visuale `UNSUP-02`

- capitolo: `CH-P02-UNSUPERVISED-SELF-SUPERVISED`
- sezione: auto-supervisione attraverso una parte nascosta
- famiglia: pipeline di ricostruzione
- orientamento: orizzontale
- sfondo: bianco puro `#FFFFFF`
- file candidato: `candidate-v1.png`
- renderer: `scripts/generate_unsupervised_visuals.py`

## Domanda unica

Come nasce una label dal dato stesso in un obiettivo masked modeling?

## Contenuto

- dato originale e maschera;
- input corrotto;
- encoder e decoder con shape dichiarate;
- loss calcolata soltanto sulle posizioni mascherate;
- target autogenerato e confini del pretraining.
- domanda principale: Quale confronto o limite chiarisce «Cercare gruppi con k-means»?
