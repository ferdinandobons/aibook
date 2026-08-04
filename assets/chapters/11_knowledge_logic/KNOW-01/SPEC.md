# Specifica visuale `KNOW-01`

- capitolo: `CH-P02-KNOWLEDGE-LOGIC`
- sezione: da un testo a fatti dichiarati e conclusioni
- famiglia: processo di inferenza
- orientamento: orizzontale
- sfondo: bianco puro `#FFFFFF`
- file candidato: `candidate-v2.png`
- renderer: `scripts/generate_knowledge_visuals.py`

## Domanda unica

Come il forward chaining trasforma fatti iniziali e regole positive in fatti derivati?

## Contenuto

- tre fatti iniziali relativi a `order_42`;
- tre regole di Horn applicate in sequenza;
- tre fatti derivati e numerazione delle applicazioni;
- footer che distingue assenza di un fatto e negazione esplicita.

## Invariante

Ogni fatto derivato deve essere sostenuto da una regola e dai fatti disponibili prima della sua applicazione.
