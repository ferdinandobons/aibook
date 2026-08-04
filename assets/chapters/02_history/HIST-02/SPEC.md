# Specifica visuale `HIST-02`

## Identità

- Capitolo: `CH-P01-HISTORY`
- Famiglia: confronto a pannelli
- Orientamento: orizzontale
- File: `candidate-v1.png`
- Stato: `validata tecnicamente`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Come cambia il percorso dalla stessa richiesta all'output quando cambia il paradigma tecnico?

## Input comune

```text
Il pacco non è arrivato
```

## Pannelli

1. `Regole e ricerca`: stati e transizioni, ricerca di un percorso, azione prevista.
2. `Sistema esperto`: knowledge base, motore di inferenza, raccomandazione motivata dalle regole.
3. `Modello appreso`: feature o vettori appresi, parametri scelti nel training, categoria o predizione.
4. `Sistema con foundation model`: modello preaddestrato e contesto, retrieval, strumenti e policy, risposta o azione controllata.

## Invariante

L'input esterno resta lo stesso. I paradigmi possono convivere nella stessa applicazione.

## Vincoli

- pannelli paralleli e non gerarchici;
- una sola freccia dall'input a ciascun pannello;
- nessuna freccia tra i pannelli;
- nessuna dichiarazione secondo cui il quarto pannello è sempre preferibile;
- testo interamente contenuto;
- nessun watermark o branding.

## Produzione

- generazione esplorativa con lo strumento immagini;
- composizione raster revisionabile: `scripts/generate_history_visuals.py`;
- decodifica verificata nel workflow `generate-book-visuals.yml`.
- domanda principale: Quale confronto o limite chiarisce «Descrivere il problema con simboli e ricerca»?
