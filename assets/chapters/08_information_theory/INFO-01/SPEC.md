# Specifica visuale `INFO-01`

## Identità

- Capitolo: `CH-P02-INFORMATION-THEORY`
- Sezione: Dai logits alle probabilità
- Famiglia: confronto numerico
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Perché due distribuzioni con la stessa entropia possono ricevere cross-entropy molto diversa rispetto allo stesso target?

## Riga corretta

```text
target: classe 0
logits: [2,0; 0,5; -1,0]
probabilità: [0,7856; 0,1753; 0,0391]
p(target): 0,785597
NLL: 0,241311
```

## Riga errata

```text
target: classe 0
logits: [-1,0; 0,5; 2,0]
probabilità: [0,0391; 0,1753; 0,7856]
p(target): 0,039113
NLL: 3,241311
```

## Layout

- due righe parallele;
- target, logits, softmax, probabilità della classe target e NLL;
- barre colorate per le tre classi;
- frecce da sinistra a destra;
- footer sulla stessa entropia e diversa collocazione della massa.

## Regole

- le due distribuzioni devono essere permutazioni esatte;
- il target resta classe zero in entrambe le righe;
- colore verde per il caso corretto, rosso per quello errato;
- il colore non sostituisce label e numeri;
- i decimali visibili usano la virgola;
- nessuna freccia attraversa i box.

## Provenienza

Valori da `SNIP-INFO-001`. PNG raster generato da `scripts/generate_information_visuals.py`; nessun SVG.
