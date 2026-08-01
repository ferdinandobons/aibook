# Specifica visuale `LIFE-02`

## Identità

- Capitolo: `CH-P01-LIFECYCLE`
- Sezione: dal checkpoint al sistema distribuito
- Famiglia: architettura di sistema
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Perché il comportamento osservato di un sistema può cambiare anche quando il checkpoint del modello resta identico?

## Centro

```text
MODELLO
checkpoint
parametri θ
inference
```

## Componenti del sistema

- input e validazione;
- prompt e configurazione;
- retrieval e dati esterni;
- strumenti;
- regole e autorizzazioni;
- output e interfaccia;
- versione distribuita;
- telemetria e monitoraggio.

## Relazioni

Le frecce mostrano quali componenti forniscono input o configurazione al modello e quali ricevono o governano il risultato. Il confine esterno include l'intero sistema, non soltanto il checkpoint.

## Invariante e confine

Il checkpoint può restare invariato mentre cambiano dati, strumenti, regole, autorizzazioni e interfacce. La figura non afferma che ogni sistema debba contenere tutti i componenti mostrati.

## Contenimento

- testo integralmente nei box;
- nessuna freccia attraversa una label;
- componenti esterni separati dal modello;
- colori usati insieme a titoli e posizione, non come unico significato;
- footer leggibile e non sovrapposto al confine del sistema.
