# Piano interno. Capitolo 2

## Identità

- `chapter_id`: `CH-P01-HISTORY`
- Parte: `P01`, Campo, metodo e storia dell'AI
- Numero visualizzato: 2
- Titolo: `Dai simboli ai foundation model`
- Profilo: storico-concettuale
- Stato: `research`
- Domanda centrale: quali cambiamenti di rappresentazione, apprendimento, dati e calcolo hanno trasformato il campo senza cancellare i paradigmi precedenti?
- Oggetto continuo: la richiesta `Il pacco non è arrivato`, affrontata con regole, conoscenza esplicita, modelli appresi, reti profonde e un sistema costruito attorno a un foundation model
- Output finale: il lettore sa leggere la storia come successione di bottleneck e strumenti, non come una lista di modelli che si sostituiscono linearmente

## Prerequisiti

- Capitolo 1;
- idea generale di modello, sistema, training e inference;
- nessun prerequisito matematico avanzato.

## Confini

Il capitolo non ricostruisce ogni laboratorio, prodotto o controversia. Non usa una singola data come nascita universale dell'AI e non descrive la storia come progresso inevitabile. Approfondimenti su architetture, training, dati, scaling e sicurezza appartengono alle parti successive.

## Progressione interna

1. partire dalla stessa richiesta e mostrare che cambia il modo di rappresentare il problema;
2. Turing e Dartmouth come formulazioni iniziali di domande e programma di ricerca;
3. simboli, stati, regole e ricerca;
4. sistemi esperti e costo della conoscenza esplicita;
5. apprendimento statistico e feature progettate;
6. rappresentazioni apprese, backpropagation e reti profonde;
7. dataset, hardware e training su larga scala;
8. attention, Transformer e pretraining riutilizzabile;
9. scaling, few-shot prompting e foundation model;
10. ricostruzione: i paradigmi convivono e si combinano nei sistemi moderni.

## Visuali previste

### `HIST-01`. Cinque transizioni, quattro risorse

- Famiglia: timeline comparativa.
- Orientamento: orizzontale.
- Domanda: che cosa diventa il collo di bottiglia dominante nelle diverse fasi?
- Assi: rappresentazione, apprendimento, dati, calcolo.
- Vincolo: le fasce devono sovrapporsi; nessuna freccia deve suggerire sostituzione completa.

### `HIST-02`. La stessa richiesta attraverso paradigmi diversi

- Famiglia: confronto a pannelli.
- Orientamento: orizzontale.
- Domanda: come cambia il percorso dall'input all'output?
- Pannelli: regole e ricerca, sistema esperto, modello appreso, sistema con foundation model.
- Invariante: la richiesta esterna resta identica.

## Codice previsto

### `SNIP-HIST-001`

- Domanda: che cosa significa rappresentare esplicitamente stati, azioni e ricerca?
- Meccanismo: breadth-first search su un piccolo workflow di assistenza.
- Input: stato iniziale `request_received`.
- Goal: `ticket_opened`.
- Output: percorso minimo di stati e azioni.
- Test: raggiungimento del goal, assenza di stati ripetuti, percorso minimo noto.
- Confine: lo snippet illustra la ricerca simbolica; non riproduce un sistema storico specifico.

## Gate specifici

- distinguere data del documento e data dell'evento;
- attribuire le definizioni ai documenti originali;
- non presentare un paradigma come universalmente superiore;
- dichiarare che le periodizzazioni sono strumenti editoriali;
- evitare il racconto semplicistico di una sola `AI winter` con cause uniche;
- separare svolte scientifiche, disponibilità dei dati, hardware e organizzazione dei sistemi;
- mostrare continuità e ibridazione;
- mantenere italiano discorsivo e comprensibile a un lettore non esperto;
- verificare ogni data, numero e attribuzione in una fonte primaria o ufficiale.
