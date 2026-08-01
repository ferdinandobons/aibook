# Specifica visuale `SUP-01`

## Identità

- Capitolo: `CH-P03-SUPERVISED`
- Famiglia: processo e separazione dei ruoli
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Come attraversano training, validation e test lo stesso dataset senza svolgere lo stesso ruolo?

## Contenuto obbligatorio

- dataset etichettato con coppie `(x,y)`;
- train, validation e test separati;
- train che aggiorna i parametri;
- modello appreso;
- validation che sceglie la soglia con costo `FN=5`, `FP=1`;
- soglia `0,30`;
- test usato soltanto dopo aver fissato modello e soglia;
- risultato test `accuracy=0,900`, `recall=0,913`, `costo=13`;
- nota che il test non deve rientrare nel tuning.

## Collegamenti

- dataset verso i tre sottoinsiemi;
- train verso training e modello;
- modello verso selezione sulla validation;
- validation verso selezione;
- modello e soglia verso valutazione finale;
- test verso valutazione finale.

## Regole

- nessuna freccia deve far pensare che la validation aggiorni i parametri;
- nessuna freccia deve far pensare che il test scelga la soglia;
- `model learned -> threshold` indica applicazione del modello sulla validation, non un update;
- colori: blu training, viola validation, verde test;
- ogni ruolo è indicato anche dal testo;
- nessun contenuto fuori dai box.

## Provenienza

Numeri da `SNIP-SUP-001`. PNG raster generato da `scripts/generate_supervised_visuals.py`; nessun SVG.
