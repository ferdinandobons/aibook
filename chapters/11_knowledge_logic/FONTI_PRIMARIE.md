# Fonti primarie e autorevoli. Capitolo 11

## Stato

- Ultima verifica: 31 luglio 2026
- Ambito: logica, rappresentazione della conoscenza, RDF e OWL, reti bayesiane e factor graph

## SRC-KNOW-001. A Mathematical Introduction to Logic

Herbert B. Enderton, *A Mathematical Introduction to Logic*, seconda edizione, Academic Press, 2001.

Uso: sintassi, interpretazioni, soddisfacibilità, conseguenza logica, logica proposizionale e primo ordine.

Limite: procedure di inferenza implementative verificate separatamente.

## SRC-KNOW-002. Artificial Intelligence: A Modern Approach

Stuart Russell e Peter Norvig, *Artificial Intelligence: A Modern Approach*, quarta edizione, Pearson, 2021, capitoli su knowledge representation, logic e probabilistic reasoning.

Uso: knowledge base, logical agents, forward e backward chaining, soundness, completeness e quadro AI.

Limite: gli standard RDF e OWL vengono attribuiti ai documenti W3C.

## SRC-KNOW-003. Horn 1951

Alfred Horn, *On Sentences Which are True of Direct Unions of Algebras*, Journal of Symbolic Logic 16(1), 14-21, 1951. DOI: https://doi.org/10.2307/2268661

Uso: origine della famiglia di formule successivamente chiamate clausole di Horn.

Limite: il paper non è un manuale di programmazione logica moderna.

## SRC-KNOW-004. Predicate Logic as Programming Language

Robert A. Kowalski, *Predicate Logic as Programming Language*, IFIP Congress, 1974, pp. 569-574.

Uso: relazione tra clausole logiche e programmi dichiarativi.

Limite: il capitolo non ricostruisce l'intero modello operativo di Prolog.

## SRC-KNOW-005. Semantics of Predicate Logic as a Programming Language

Maarten H. van Emden e Robert A. Kowalski, *The Semantics of Predicate Logic as a Programming Language*, Journal of the ACM 23(4), 733-742, 1976. DOI: https://doi.org/10.1145/321978.321991

Uso: semantica declarativa e fixpoint delle clausole definite.

Limite: il motore Python del capitolo è più ristretto e lavora su fatti ground finiti.

## SRC-KNOW-006. RDF 1.1 Concepts and Abstract Syntax

W3C Recommendation, 25 febbraio 2014. URL: https://www.w3.org/TR/rdf-concepts/

Uso: triple soggetto-predicato-oggetto, grafi RDF, IRI, literal e blank node.

Limite: una serializzazione RDF non coincide con il modello astratto.

## SRC-KNOW-007. RDF 1.1 Semantics

W3C Recommendation, 25 febbraio 2014. URL: https://www.w3.org/TR/rdf11-mt/

Uso: model-theoretic semantics, entailment e monotonicità di RDF.

Limite: regole applicative e negation-as-failure non fanno parte della semantica RDF di base.

## SRC-KNOW-008. OWL 2 Overview e Primer

W3C Recommendations, seconda edizione, 11 dicembre 2012:

- https://www.w3.org/TR/owl2-overview/
- https://www.w3.org/TR/owl-primer/

Uso: ontologie, classi, proprietà, individui, assiomi, formal semantics e open-world assumption.

Limite: i profili e la complessità dei reasoner sono differiti.

## SRC-KNOW-009. SPARQL 1.1 Query Language

W3C Recommendation, 21 marzo 2013. URL: https://www.w3.org/TR/sparql11-query/

Uso: graph pattern, query RDF e test di assenza con `NOT EXISTS`.

Limite: il matching di un pattern assente non equivale a una negazione ontologica universale.

## SRC-KNOW-010. Knowledge Graphs

Aidan Hogan et al., *Knowledge Graphs*, ACM Computing Surveys 54(4), articolo 71, 2021. DOI: https://doi.org/10.1145/3447772

Uso: varietà dei modelli a grafo, schema, identità, query, validazione, deduzione e tecniche induttive.

Limite: il termine `knowledge graph` non riceve nel libro una definizione unica più forte di quella sostenuta dalla survey.

## SRC-KNOW-011. Bayesian Networks

Judea Pearl, *Bayesian Networks: A Model of Self-Activated Memory for Evidential Reasoning*, Proceedings of the Seventh Conference of the Cognitive Science Society, 1985, pp. 329-334. Versione UCLA: https://escholarship.org/uc/item/0vr7830n

Uso: rete bayesiana e propagazione di evidenza.

Limite: il capitolo usa una rete binaria molto più semplice.

## SRC-KNOW-012. Probabilistic Reasoning in Intelligent Systems

Judea Pearl, *Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference*, Morgan Kaufmann, 1988.

Uso: Bayesian network, Markov network, indipendenza e belief propagation.

Limite: causalità e interventi non sono dedotti automaticamente dalla sola struttura probabilistica.

## SRC-KNOW-013. Probabilistic Graphical Models

Daphne Koller e Nir Friedman, *Probabilistic Graphical Models: Principles and Techniques*, MIT Press, 2009.

Uso: fattorizzazione, conditional independence, inferenza esatta e approssimata, Bayesian e Markov network.

Limite: algoritmi avanzati e treewidth sono soltanto introdotti come confine.

## SRC-KNOW-014. Factor Graphs and the Sum-Product Algorithm

Frank R. Kschischang, Brendan J. Frey e Hans-Andrea Loeliger, *Factor Graphs and the Sum-Product Algorithm*, IEEE Transactions on Information Theory 47(2), 498-519, 2001. DOI: https://doi.org/10.1109/18.910572

Uso: factor graph come rappresentazione bipartita di una fattorizzazione e sum-product.

Limite: il capitolo non implementa message passing generalizzato.

## SRC-KNOW-015. Modeling and Reasoning with Bayesian Networks

Adnan Darwiche, *Modeling and Reasoning with Bayesian Networks*, Cambridge University Press, 2009.

Uso: semantica delle reti bayesiane, inferenza e complessità strutturale.

Limite: compilation, arithmetic circuit e metodi avanzati sono differiti.

## Regola d'uso

- Le definizioni logiche vengono controllate su Enderton e Russell e Norvig.
- Horn, Kowalski e van Emden e Kowalski sostengono il percorso delle regole positive e del fixpoint.
- RDF, OWL e SPARQL vengono attribuiti ai documenti W3C.
- Le reti bayesiane seguono Pearl, Koller e Friedman e Darwiche.
- I factor graph seguono Kschischang, Frey e Loeliger.
- I valori numerici derivano da `SNIP-KNOW-001`.
- Nessuna probabilità illustrativa viene presentata come stima di un sistema reale.
