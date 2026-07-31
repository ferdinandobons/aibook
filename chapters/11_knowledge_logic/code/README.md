# Codice. Capitolo 11

## `SNIP-KNOW-001`

File:

```text
snip_knowledge_001_rules_bayes.py
```

Il programma contiene due esempi separati:

1. un motore minimale di forward chaining su fatti ground e regole positive;
2. una rete bayesiana binaria fattorizzata come `P(H)P(M|H)P(T|H)`.

## Esecuzione

```bash
python snip_knowledge_001_rules_bayes.py
python -m unittest -v test_knowledge_logic.py
```

## Ambiente registrato

```text
Python 3.13.5
standard library
CPU
```

## Contratti verificati

- le tre conclusioni logiche attese vengono derivate;
- il fixpoint è idempotente;
- l'assenza non crea una negazione;
- la congiunta probabilistica somma a uno;
- il posterior con i due segnali vale `0,875`;
- l'assenza dei segnali riduce il posterior sotto il prior;
- la fattorizzazione condizionale coincide con le tabelle dichiarate.

## Limiti

Il codice non implementa:

- un theorem prover completo;
- negation-as-failure;
- unification con termini funzionali;
- RDF, SPARQL o un reasoner OWL;
- una libreria generale per Bayesian network;
- causal inference;
- belief propagation o inferenza approssimata.

Gli output sono illustrativi e non descrivono un servizio reale.
