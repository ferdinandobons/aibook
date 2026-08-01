# Audit del codice. Capitolo 13

## Stato

- Snippet: `SNIP-UNSUP-001`
- Ambiente: Python 3.13.5, PyTorch 2.10.0+cpu, CPU
- Test: 9 superati
- Data: 31 luglio 2026
- Esito: **superato**

## K-means

- [x] gruppi segreti esclusi dall'algoritmo;
- [x] inizializzazione farthest-first deterministica;
- [x] distanze calcolate con `torch.cdist`;
- [x] assegnamento al centroide più vicino;
- [x] aggiornamento tramite media;
- [x] cluster vuoto trattato come errore nel toy example;
- [x] obiettivo finale ricalcolato;
- [x] storia non crescente testata.

## Masked autoencoder

- [x] input originale shape `[N,4]`;
- [x] input del modello shape `[N,8]`, valori corrotti più mask;
- [x] embedding shape `[N,2]`;
- [x] decoder output shape `[N,4]`;
- [x] loss soltanto sugli elementi mascherati;
- [x] almeno un elemento visibile e uno nascosto per riga;
- [x] maschere diverse durante il training;
- [x] test mask fissata;
- [x] baseline costruita dalla media del training;
- [x] test loss inferiore alla baseline nel run fissato.

## Revisioni del codice

La prima versione usava una mask fissa in training e non forniva la mask al modello. Sul test otteneva `2,272978`, peggio della baseline zero `2,252569`. La candidata è stata respinta.

La versione corrente:

- concatena mask e valori corrotti;
- varia la mask durante il training;
- usa una baseline media più pertinente;
- ottiene test loss `0,391415` contro `1,900604` della baseline.

## Limiti

- un singolo seed;
- nessuna selezione di iperparametri;
- gruppi sintetici bilanciati;
- nessun claim su interpretabilità dell'embedding;
- nessun confronto con PCA o metodi contrastivi;
- float64 scelta per stabilità del toy example, non come raccomandazione generale.

## Verdetto

Il codice sostiene i claim eseguiti e rende osservabili due contratti distinti senza usare label esterne nel training.
