# Specifica visuale `LIFE-01`

## Identità

- Capitolo: `CH-P01-LIFECYCLE`
- Sezione: apertura e ricostruzione del ciclo di vita
- Famiglia: processo ciclico
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Quali fasi attraversa un sistema di AI e quale artefatto verificabile deve restare associato a ciascuna fase?

## Ordine di lettura

```text
1 Definire
-> 2 Dati
-> 3 Training
-> 4 Valutazione
-> 5 Integrare
-> 6 Deployment
-> 7 Monitoraggio
-> 8 Aggiornare o ritirare
-> ritorno alla definizione del problema
```

## Contenuto obbligatorio

- definizione: specifica, utenti e azioni consentite;
- dati: dataset, schema, datasheet e versione;
- training: configurazione, log, ambiente e checkpoint;
- valutazione: baseline, metriche, slice e model card;
- integrazione: prompt, retrieval, tool, policy e interfacce;
- deployment: release identificabile e configurazione;
- monitoraggio: telemetria, feedback, incidenti e soglie;
- aggiornamento o ritiro: rollback, nuova versione o record di ritiro.

## Invariante e confine

Ogni fase produce decisioni e versioni rintracciabili. Il diagramma non impone una pipeline identica a ogni organizzazione e non presenta il feedback di produzione come dato di training automatico.

## Contenimento

- testo integralmente nei box;
- padding visibile;
- nessuna freccia attraversa una label;
- direzione del ciclo inequivocabile;
- nessuna fase appare come conclusione definitiva del processo.
- domanda principale: Quale trasformazione centrale rende osservabile «Prima del modello viene il problema» nel capitolo 3?
