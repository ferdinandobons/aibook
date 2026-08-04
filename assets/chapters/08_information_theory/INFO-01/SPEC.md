# Specifica visuale `INFO-01`

- capitolo: `CH-P02-INFORMATION-THEORY`
- sezione: dai logits alla cross-entropy
- famiglia: confronto numerico
- orientamento: orizzontale
- sfondo: bianco puro `#FFFFFF`
- file candidato: `candidate-v1.png`
- renderer: `scripts/generate_information_visuals.py`

## Domanda unica

Perché due distribuzioni con la stessa entropia possono produrre loss diverse quando il target resta fissato?

## Contenuto

- due vettori di logits, uno coerente e uno incoerente con la classe target `0`;
- softmax esplicita con le tre probabilità;
- probabilità assegnata al target;
- negative log-likelihood corrispondente;
- footer che separa entropia della distribuzione dalla cross-entropy rispetto al target.

## Invariante

Le due distribuzioni sono permutazioni: la loro entropia è la stessa, ma la classe target riceve probabilità diversa.
- domanda principale: Quale confronto o limite chiarisce «Entropia come informazione media»?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
