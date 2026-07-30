# Piano interno. Capitolo 3

## Identità

- `chapter_id`: `CH-P01-LIFECYCLE`
- Parte: `P01`, Campo, metodo e storia dell'AI
- Numero visualizzato: 3
- Titolo: `Il ciclo di vita di un sistema di AI`
- Profilo: processo e sistema
- Stato: `research`
- Domanda centrale: quali artefatti, decisioni e controlli collegano dati, training, valutazione, deployment, monitoraggio e ritiro?
- Oggetto continuo: il sistema di assistenza per la richiesta `Il pacco non è arrivato`, seguito dalla raccolta dei dati fino al monitoraggio in produzione
- Output finale: il lettore distingue ciclo del modello e ciclo del sistema, localizza i principali artefatti e comprende perché una buona metrica offline non conclude la valutazione

## Prerequisiti

- Capitoli 1 e 2;
- concetti di modello, sistema, training, inference e dataset;
- nessun prerequisito di MLOps.

## Progressione prevista

1. definire il risultato desiderato e i confini operativi;
2. acquisire, documentare e dividere i dati;
3. addestrare e registrare configurazione e checkpoint;
4. valutare su dati separati e rispetto a una baseline;
5. integrare il modello in un sistema con interfacce, retrieval, regole e autorizzazioni;
6. distribuire una versione identificabile;
7. monitorare qualità, distribuzioni, costi e incidenti;
8. gestire rollback, aggiornamento e ritiro;
9. distinguere feedback utile da feedback che altera il problema;
10. ricostruire il ciclo come processo iterativo e governato.

## Visuali previste

### `LIFE-01`. Ciclo di vita e artefatti

- processo circolare con fasi, output e gate;
- ogni fase produce un artefatto verificabile;
- deployment non coincide con la fine del ciclo.

### `LIFE-02`. Modello e sistema hanno perimetri diversi

- modello al centro;
- dati, prompt, retrieval, tool, policy, interfaccia e monitoraggio attorno;
- evidenziare che una modifica del sistema può cambiare il comportamento senza cambiare il checkpoint.

## Codice previsto

### `SNIP-LIFE-001`

- piccolo classificatore con split train, validation e test;
- training soltanto sul train set;
- scelta della configurazione sulla validation;
- risultato finale sul test;
- monitoraggio illustrativo della media delle feature su un batch successivo;
- test che impedisce la sovrapposizione degli indici tra gli split.

## Gate specifici

- non usare `deployment` come sinonimo di inference;
- distinguere metrica del modello, metrica del prodotto e vincolo operativo;
- evitare che test set o dati futuri entrino nel training;
- distinguere drift osservato da degradazione causale dimostrata;
- dichiarare che monitorare una distribuzione non garantisce di rilevare ogni errore;
- separare rollback del sistema e ripristino del checkpoint;
- usare fonti istituzionali, paper primari e documentazione ufficiale;
- mantenere il testo accessibile senza trasformarlo in una checklist MLOps.
