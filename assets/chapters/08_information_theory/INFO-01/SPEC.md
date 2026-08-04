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
