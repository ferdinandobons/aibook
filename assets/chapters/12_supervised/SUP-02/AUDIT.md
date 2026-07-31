# Audit visuale `SUP-02`

## Stato

- File esaminato: `candidate-v1.png`
- Dimensioni: `1800 × 1000`
- Esito tecnico: **validata tecnicamente dopo seconda iterazione**
- Approvazione autoriale: aperta

## Prima iterazione

La prima composizione mostrava i costi `13` e `21`, ma non dichiarava nel pannello il rapporto `FN=5`, `FP=1`. Il lettore non poteva ricostruire il calcolo senza tornare al testo.

## Correzione

È stata aggiunta nella fascia delle slice la nota:

```text
costo: falso negativo = 5, falso positivo = 1
```

## Verifica numerica

- [x] soglia `0,30`: `21+24=45` corretti, `3+2=5` errori;
- [x] costo `2×5 + 3×1 = 13`;
- [x] soglia `0,50`: `19+26=45` corretti, `1+4=5` errori;
- [x] costo `4×5 + 1×1 = 21`;
- [x] entrambe le accuracy `45/50=0,900`;
- [x] slice `34+16=50`;
- [x] metriche slice coerenti con il run.

## Verifica semantica

- [x] target sulle righe e predizione sulle colonne;
- [x] stessa accuracy distinta da stesso comportamento;
- [x] soglia scelta sulla validation distinta dalla soglia predefinita;
- [x] costo dichiarato come illustrativo;
- [x] slice non presentate come stime precise.

## Verifica visuale

- [x] sfondo bianco puro;
- [x] testo contenuto;
- [x] box paralleli e allineati;
- [x] nessun collegamento ambiguo;
- [x] contrasto sufficiente;
- [x] label leggibili senza dipendere dal colore.

## Verdetto

La figura può entrare nella candidatura del capitolo e passare alla revisione autoriale.
