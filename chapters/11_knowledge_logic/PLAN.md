# Piano interno. Capitolo 11

## Identità

- `chapter_id`: `CH-P03-KNOWLEDGE-LOGIC`
- Parte: `P03`, Apprendimento, ottimizzazione e decisione
- Titolo: **Conoscenza, logica e modelli probabilistici**
- Profilo: rappresentazione simbolica, inferenza deduttiva e ragionamento probabilistico
- Oggetto continuo: `order_42`, associato alla richiesta «Il pacco non è arrivato»
- Domanda centrale: come possiamo rappresentare fatti, regole e incertezza in modo che una conclusione sia ricostruibile e verificabile?

## Prerequisiti

- insiemi e funzioni;
- probabilità condizionata e Bayes;
- grafi diretti;
- codice Python elementare.

## Concetti differiti

- SAT, SMT e theorem proving avanzato;
- description logic complete e profili OWL;
- answer set programming e default logic;
- probabilistic programming;
- Markov logic network;
- apprendimento della struttura dei grafi;
- causal inference;
- knowledge graph embedding e graph neural network;
- inferenza approssimata avanzata.

## Oggetto logico

### Fatti iniziali

```text
message_mentions_missing_delivery(order_42)
tracking_stalled(order_42)
delivery_date_passed(order_42)
```

### Regole positive

```text
tracking_stalled(?order)
AND delivery_date_passed(?order)
-> possible_delay(?order)

message_mentions_missing_delivery(?order)
AND possible_delay(?order)
-> needs_review(?order)

needs_review(?order)
-> eligible_for_delay_workflow(?order)
```

### Fatti derivati

```text
possible_delay(order_42)
needs_review(order_42)
eligible_for_delay_workflow(order_42)
```

Il sistema non deriva `not_delivered(order_42)` dall'assenza di `delivered(order_42)`.

## Oggetto probabilistico

```text
H = ritardo reale
M = segnale di mancata consegna nel messaggio
T = tracking fermo

P(H=1) = 0,20
P(M=1|H=1) = 0,80
P(M=1|H=0) = 0,10
P(T=1|H=1) = 0,70
P(T=1|H=0) = 0,20
```

Assunzione illustrativa:

```text
M e T sono indipendenti condizionatamente a H
```

Risultato eseguito:

```text
P(H=1|M=1,T=1) = 0,875
```

## Stato finale del lettore

Il lettore sa:

1. distinguere sintassi, interpretazione, modello, soddisfacibilità ed entailment;
2. distinguere una prova da una conseguenza semantica;
3. leggere proposizioni, predicati, variabili e quantificatori;
4. riconoscere una clausola di Horn e una clausola definita;
5. eseguire forward chaining su regole positive;
6. spiegare monotonicità, fixpoint e limite della negazione per assenza;
7. distinguere open-world e closed-world assumption;
8. leggere triple RDF e comprendere il ruolo di una ontologia OWL;
9. evitare di identificare automaticamente knowledge graph, database, ontologia e motore di inferenza;
10. leggere una rete bayesiana come fattorizzazione della congiunta;
11. ricostruire il posterior dell'esempio;
12. spiegare che l'indipendenza condizionata è una proprietà del modello;
13. distinguere rete bayesiana, Markov network e factor graph;
14. capire che un arco probabilistico non implica automaticamente causalità;
15. scegliere tra regole, probabilità o una combinazione in base alla domanda.

## Progressione

1. Dal dato alla conoscenza dichiarata.
2. Sintassi e semantica.
3. Propositional logic e first-order logic.
4. Fatti, regole e clausole di Horn.
5. Forward chaining e least fixpoint.
6. Monotonicità, negazione e mondo aperto.
7. RDF, knowledge graph e ontologie.
8. Quando la verità binaria non basta.
9. Reti bayesiane e fattorizzazione.
10. Indipendenza condizionata e inferenza.
11. Markov network e factor graph.
12. Sistemi ibridi e confini.
13. Codice eseguito.
14. Riepilogo ed esercizi.

## Codice

### `SNIP-KNOW-001`

- motore minimale di forward chaining su regole positive;
- sostituzione delle variabili;
- iterazione fino a fixpoint;
- controllo che l'assenza non generi negazione;
- rete bayesiana binaria `H -> M`, `H -> T`;
- enumerazione esatta della congiunta;
- posterior con due segnali;
- sette test.

## Visuali

### `KNOW-01`. Dai fatti alle conclusioni

Tre colonne: fatti iniziali, regole di Horn, fatti derivati. Il footer separa assenza e negazione.

### `KNOW-02`. Una rete bayesiana fattorizza la congiunta

Grafo `H -> M`, `H -> T`, tabelle condizionali, fattorizzazione e calcolo del posterior `0,875`.

## Gate specifici

- simboli e fatti non vengono confusi con le entità del mondo;
- entailment e procedura di prova restano distinti;
- soundness e completeness non vengono attribuite a ogni algoritmo senza condizioni;
- forward chaining viene limitato a regole positive del caso illustrativo;
- assenza e negazione restano separate;
- open-world non viene descritto come proprietà universale di ogni knowledge graph;
- RDF, OWL e SPARQL ricevono contratti distinti;
- la rete bayesiana fattorizza una distribuzione e non viene presentata automaticamente come modello causale;
- l'indipendenza condizionata è dichiarata;
- il posterior deriva dalle probabilità illustrative, non da dati reali;
- factor graph e Bayesian network non vengono trattati come sinonimi;
- testo, codice e visuali usano gli stessi nomi e numeri.
