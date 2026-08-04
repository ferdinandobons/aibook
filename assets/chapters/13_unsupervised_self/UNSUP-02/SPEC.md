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

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
