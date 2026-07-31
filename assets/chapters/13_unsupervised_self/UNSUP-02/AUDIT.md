# Audit visuale `UNSUP-02`

## Stato

- File: `candidate-v1.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente**
- Approvazione autoriale: aperta

## Verifica semantica

- [x] dato originale separato dall'input corrotto;
- [x] maschera esplicita;
- [x] valori `b` e `d` nascosti;
- [x] encoder input coerente con il codice;
- [x] embedding shape `[2]`;
- [x] decoder output shape `[4]`;
- [x] loss soltanto sulle coordinate mascherate;
- [x] percorso target dal dato originale alla loss;
- [x] assenza di label umana dichiarata.

## Verifica geometrica

- [x] flusso principale da sinistra a destra;
- [x] percorso target sotto i box, senza incroci;
- [x] origine e arrivo delle frecce inequivocabili;
- [x] box allineati;
- [x] testo contenuto;
- [x] sfondo bianco puro.

## Confini

- la figura non sostiene che la ricostruzione produca semantica;
- linear probe e fine-tuning sono indicati come valutazioni successive;
- la mask stabilisce il compito, non una categoria del dato.

## Verdetto

La figura può entrare nella candidatura del capitolo.
