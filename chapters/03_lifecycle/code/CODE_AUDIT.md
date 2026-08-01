# Audit del codice. Capitolo 3

## Stato

- Snippet: `SNIP-LIFE-001`
- Ambiente: Python 3.13.5, PyTorch 2.10.0+cpu, CPU
- Esito: **superato**
- Test: 4 superati
- Data: 30 luglio 2026

## Contratto

- Input: dataset sintetico con 120 osservazioni e due classi.
- Split: 72 train, 24 validation, 24 test.
- Training: `nn.Linear(2, 2)`, cross-entropy e SGD.
- Selezione: learning rate scelto mediante validation accuracy.
- Valutazione finale: test accuracy dopo la selezione.
- Monitoraggio illustrativo: differenza standardizzata della media delle feature.

## Controlli

- [x] split disgiunti;
- [x] copertura completa degli indici;
- [x] stessa inizializzazione per i candidati;
- [x] validation usata per la scelta;
- [x] test consultato dopo la selezione;
- [x] learning rate `0.1` migliore di `0.0005` sulla validation;
- [x] accuratezza test almeno `0.95` nel run deterministico;
- [x] shift della prima feature maggiore della seconda;
- [x] quattro test superati;
- [x] output registrato.

## Limiti

- dati sintetici e linearmente separabili;
- nessun intervallo di confidenza;
- nessun confronto con una baseline di prodotto;
- nessuna conclusione di generalizzazione esterna;
- la metrica di shift non prova una variazione della qualità;
- il codice non implementa deployment o serving.

## Esito

Lo snippet è coerente con il capitolo e rende visibili split, selezione, valutazione finale e un segnale di monitoraggio senza attribuire alla metrica un significato causale non dimostrato.
