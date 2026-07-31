# Registro dei claim. Capitolo 11

| ID | Claim sostenibile | Prova | Stato |
|---|---|---|---|
| `CLM-KNOW-001` | Una base di conoscenza contiene espressioni interpretate secondo una semantica dichiarata; la sola sintassi non stabilisce ciò che esse implicano. | `SRC-KNOW-001`, `SRC-KNOW-002` | verificato |
| `CLM-KNOW-002` | Una interpretazione assegna significato ai simboli e stabilisce se una formula è vera in quel modello. | `SRC-KNOW-001` | verificato |
| `CLM-KNOW-003` | `KB |= α` significa che ogni modello che soddisfa `KB` soddisfa anche `α`. | `SRC-KNOW-001`, `SRC-KNOW-007` | verificato |
| `CLM-KNOW-004` | Soundness e completeness descrivono il rapporto tra una procedura di prova e la conseguenza semantica, non la correttezza generica di un sistema. | `SRC-KNOW-001`, `SRC-KNOW-002` | verificato |
| `CLM-KNOW-005` | La logica proposizionale tratta proposizioni atomiche senza struttura interna; la logica del primo ordine aggiunge predicati, variabili, funzioni e quantificatori. | `SRC-KNOW-001` | verificato |
| `CLM-KNOW-006` | Una clausola di Horn contiene al massimo un letterale positivo; una clausola definita ne contiene esattamente uno. | `SRC-KNOW-003`, `SRC-KNOW-002` | verificato |
| `CLM-KNOW-007` | Le clausole definite possono essere lette come regole con una conclusione positiva e premesse congiunte. | `SRC-KNOW-004`, `SRC-KNOW-005` | verificato |
| `CLM-KNOW-008` | Nel caso finito e positivo del capitolo, il forward chaining aggiunge fatti finché raggiunge un fixpoint. | `SRC-KNOW-002`, `SRC-KNOW-005` | verificato con perimetro |
| `CLM-KNOW-009` | Il forward chaining positivo del capitolo è monotono: i fatti derivati non vengono ritirati quando vengono aggiunti altri fatti. | `SRC-KNOW-005` | verificato con perimetro |
| `CLM-KNOW-010` | Nel run illustrativo vengono derivati `possible_delay(order_42)`, `needs_review(order_42)` ed `eligible_for_delay_workflow(order_42)`. | `SNIP-KNOW-001`, test | eseguito |
| `CLM-KNOW-011` | Nel run illustrativo, applicare nuovamente le regole al fixpoint non cambia l'insieme dei fatti. | test `test_forward_chain_is_idempotent` | eseguito |
| `CLM-KNOW-012` | L'assenza di `delivered(order_42)` non produce `not_delivered(order_42)` nel motore positivo del capitolo. | `SNIP-KNOW-001`, test | eseguito |
| `CLM-KNOW-013` | La logica classica, RDF e OWL usano una semantica monotona; un fatto mancante non è automaticamente falso. | `SRC-KNOW-007`, `SRC-KNOW-008` | verificato |
| `CLM-KNOW-014` | Sistemi basati su closed-world assumption o negation-as-failure possono trattare l'assenza in modo diverso; la scelta deve essere esplicita. | `SRC-KNOW-008`, `SRC-KNOW-009`, `SRC-KNOW-002` | verificato |
| `CLM-KNOW-015` | Un grafo RDF è un insieme di triple soggetto-predicato-oggetto; i nodi possono includere IRI, literal e blank node secondo le posizioni ammesse. | `SRC-KNOW-006` | verificato |
| `CLM-KNOW-016` | RDF definisce un modello dati e una semantica di base; non equivale automaticamente a una ontologia ricca o a un motore applicativo. | `SRC-KNOW-006`, `SRC-KNOW-007` | verificato |
| `CLM-KNOW-017` | OWL 2 permette di descrivere classi, proprietà, individui e assiomi con significato formalmente definito. | `SRC-KNOW-008` | verificato |
| `CLM-KNOW-018` | SPARQL interroga graph pattern RDF; `NOT EXISTS` verifica l'assenza di un match nel dataset e non prova una negazione ontologica generale. | `SRC-KNOW-009` | verificato |
| `CLM-KNOW-019` | Il termine `knowledge graph` copre pratiche e modelli differenti; nel libro non viene identificato automaticamente con RDF, OWL o un database specifico. | `SRC-KNOW-010` | verificato con convenzione editoriale |
| `CLM-KNOW-020` | Una rete bayesiana è un grafo diretto aciclico associato a distribuzioni locali che fattorizzano la distribuzione congiunta. | `SRC-KNOW-011`, `SRC-KNOW-012`, `SRC-KNOW-013` | verificato |
| `CLM-KNOW-021` | Nella rete del capitolo, `P(H,M,T)=P(H)P(M|H)P(T|H)`. | derivazione; `SRC-KNOW-013` | verificato |
| `CLM-KNOW-022` | La fattorizzazione del capitolo assume che `M` e `T` siano indipendenti condizionatamente a `H`. | modello dichiarato; `SRC-KNOW-013` | verificato |
| `CLM-KNOW-023` | Nel run illustrativo, la distribuzione congiunta sulle tre variabili binarie somma a uno. | `SNIP-KNOW-001`, test | eseguito |
| `CLM-KNOW-024` | Nel run illustrativo, `P(H=1|M=1,T=1)=0,875`. | `SNIP-KNOW-001`, test | eseguito |
| `CLM-KNOW-025` | Nel run illustrativo, l'assenza di entrambi i segnali porta il posterior a circa `0,020408`, inferiore al prior `0,20`. | `SNIP-KNOW-001`, test | eseguito |
| `CLM-KNOW-026` | Un arco in una rete bayesiana non riceve automaticamente una interpretazione causale; servono ipotesi e semantica aggiuntive. | `SRC-KNOW-012`, `SRC-KNOW-013` | verificato |
| `CLM-KNOW-027` | Un Markov network usa un grafo non diretto e fattori o potenziali; non possiede la stessa fattorizzazione orientata di una rete bayesiana. | `SRC-KNOW-012`, `SRC-KNOW-013` | verificato |
| `CLM-KNOW-028` | Un factor graph rappresenta in forma bipartita variabili e fattori di una funzione globale. | `SRC-KNOW-014` | verificato |
| `CLM-KNOW-029` | Il sum-product calcola margini esatti sugli alberi; su grafi con cicli, il message passing iterativo può essere usato come metodo approssimato senza garanzia universale di convergenza o esattezza. | `SRC-KNOW-014`, `SRC-KNOW-013` | verificato con limite |
| `CLM-KNOW-030` | La complessità dell'inferenza esatta dipende dalla struttura del grafo e può crescere esponenzialmente con la larghezza delle eliminazioni. | `SRC-KNOW-013`, `SRC-KNOW-015` | verificato |
| `CLM-KNOW-031` | Regole logiche e modelli probabilistici rispondono a domande differenti e possono essere combinati, ma una traduzione tra i due richiede una semantica esplicita. | `SRC-KNOW-002`, `SRC-KNOW-012`, `SRC-KNOW-014` | verificato |

## Claim esclusi

- un fatto rappresentato non è automaticamente vero nel mondo reale;
- una prova sintattica non è identica alla definizione semantica di entailment;
- l'assenza di un dato non è automaticamente negazione;
- ogni knowledge graph non usa necessariamente RDF o OWL;
- una ontologia non garantisce dati completi o corretti;
- un arco bayesiano non prova causalità;
- conditional independence non è dedotta dai numeri senza un modello;
- belief propagation su grafi con cicli non è sempre esatta;
- il posterior `0,875` non è una stima di un servizio reale;
- un sistema ibrido logico-probabilistico non eredita automaticamente le garanzie di entrambe le componenti.
