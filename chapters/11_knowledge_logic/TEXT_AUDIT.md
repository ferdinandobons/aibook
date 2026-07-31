# Audit del testo. Capitolo 11

## Stato

- Versione prevista dopo il workflow visuale: `0.2.0-rc1`
- Data: 31 luglio 2026
- Esito fattuale: **superato**
- Esito logico e probabilistico: **superato**
- Esito del codice: **superato, sette test**
- Esito didattico: **superato dopo seconda lettura**
- Gate anti-template: **superato**
- Esito editoriale e linguistico: **superato**
- Chiarezza per lettore non esperto: **superata**
- Visuali: **validate tecnicamente in locale**
- Revisione autoriale: aperta dopo la materializzazione dei PNG

## Prima lettura critica

Difetti individuati e corretti:

1. rischio di presentare i fatti del sistema come verità dirette sul mondo;
2. sintassi, modello ed entailment comparivano troppo vicini;
3. `|=` e `|-` richiedevano una distinzione prima di soundness e completeness;
4. la logica del primo ordine rischiava una esposizione troppo formale;
5. la clausola di Horn doveva essere letta prima come regola concreta;
6. forward chaining, backward chaining e Prolog rischiavano di apparire equivalenti;
7. la monotonicità positiva doveva restare limitata al frammento dichiarato;
8. assenza, negazione e `NOT EXISTS` richiedevano confini distinti;
9. RDF, knowledge graph e ontologia rischiavano di essere usati come sinonimi;
10. la rete bayesiana doveva dichiarare l'indipendenza condizionata;
11. gli archi probabilistici rischiavano una lettura causale automatica;
12. Bayesian network, Markov network e factor graph richiedevano una separazione più netta;
13. il passaggio a sistemi ibridi doveva distinguere stima e decisione;
14. i predicati lunghi della prima visuale uscivano dalle aree riservate;
15. il prior della seconda visuale appariva come nodo del grafo.

## Seconda lettura integrale

### Lettore non esperto

- [x] parte dalla stessa richiesta dei capitoli precedenti;
- [x] i fatti sono descritti come frasi del sistema, non come il mondo;
- [x] sintassi e semantica ricevono esempi prima dei simboli;
- [x] propositional e first-order logic sono distinte con lo stesso ordine;
- [x] le regole vengono eseguite su un caso concreto;
- [x] open-world e closed-world sono spiegate attraverso un dato mancante;
- [x] RDF e OWL compaiono dopo fatti, predicati e modelli;
- [x] Bayes riprende numeri già comprensibili dal Capitolo 7;
- [x] il codice arriva dopo i due meccanismi;
- [x] il riepilogo ricompone logica, grafi e probabilità.

### Lettore tecnico

- [x] entailment definito semanticamente;
- [x] prova e conseguenza distinte;
- [x] clausole di Horn e definite descritte correttamente;
- [x] fixpoint limitato al caso finito positivo;
- [x] monotonicità e non monotonicità non confuse;
- [x] RDF e OWL attribuiti alle Recommendations W3C;
- [x] `NOT EXISTS` limitato al dataset interrogato;
- [x] fattorizzazione bayesiana corretta;
- [x] posterior `0,875` ricostruito;
- [x] causalità non dedotta dal solo DAG;
- [x] factor graph e sum-product descritti con confini corretti;
- [x] complessità dell'inferenza esatta collegata alla struttura.

## Audit numerico

- [x] numeratore per `H=1`: `0,112`;
- [x] numeratore per `H=0`: `0,016`;
- [x] evidenza totale: `0,128`;
- [x] posterior: `0,875`;
- [x] posterior con segnali assenti: `0,020408`;
- [x] somma congiunta: `1,000000`.

## Audit delle fonti

- [x] logica su Enderton e Russell e Norvig;
- [x] Horn su paper del 1951;
- [x] programmazione logica su Kowalski e van Emden e Kowalski;
- [x] RDF, OWL e SPARQL su W3C;
- [x] knowledge graph su survey ACM;
- [x] reti bayesiane su Pearl;
- [x] graphical model su Koller e Friedman e Darwiche;
- [x] factor graph su Kschischang, Frey e Loeliger;
- [x] nessun numero illustrativo attribuito alle fonti.

## Audit linguistico

- [x] italiano scritto direttamente;
- [x] nessun em dash;
- [x] termini inglesi definiti nel punto d'uso;
- [x] paragrafi costruiti intorno a problemi e meccanismi;
- [x] nessun telaio ripetitivo con input, trasformazione e invariante come titoli;
- [x] formule introdotte e lette in prosa;
- [x] negazioni tecniche raccolte senza interrompere ogni paragrafo;
- [x] lettura ad alta voce superata internamente.

## Visuali

### `KNOW-01`

- image-gen respinta perché mostrava una dashboard editoriale falsa;
- raster v1 respinta per overflow dei predicati lunghi;
- raster v2 validata dopo spezzatura e riallineamento del testo;
- fatti, regole e conclusioni coerenti con lo snippet.

### `KNOW-02`

- prima esportazione rieseguita per compatibilità del file;
- raster v2 respinta perché il prior poteva sembrare un nodo del grafo;
- raster v3 validata con prior laterale e frecce dirette `H -> M`, `H -> T`;
- rimosso un glifo non supportato dal font;
- valori numerici coerenti con lo snippet.

## Codice

I sette test sono stati eseguiti in un processo Python pulito. Il motore logico è volutamente ristretto a fatti ground e regole positive; la rete bayesiana è binaria e codificata a mano. Questi limiti sono dichiarati nel testo e nell'audit del codice.

## Verdetto

Il testo supera i gate fattuali, logici, probabilistici, didattici, anti-template, editoriali, linguistici e di accessibilità. La candidatura può passare alla revisione autoriale quando il workflow ha materializzato i due PNG nel feature branch.
