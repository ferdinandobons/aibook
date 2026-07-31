# Revisione autoriale. Capitolo 11

## Candidatura

- `chapter_id`: `CH-P03-KNOWLEDGE-LOGIC`
- Titolo: **Conoscenza, logica e modelli probabilistici**
- Versione prevista: `0.2.0-rc1`
- Stato: candidatura completa dopo la materializzazione delle visuali

## Ordine consigliato

1. [`CHAPTER.md`](CHAPTER.md)
2. [`KNOW-01`](../../assets/chapters/11_knowledge_logic/KNOW-01/candidate-v2.png)
3. [`KNOW-02`](../../assets/chapters/11_knowledge_logic/KNOW-02/candidate-v3.png)
4. [`code/README.md`](code/README.md)
5. [`TEXT_AUDIT.md`](TEXT_AUDIT.md)
6. [`CLAIMS.md`](CLAIMS.md)
7. [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md)

## Punti da valutare

### Testo

- La distinzione tra fatto del sistema e fatto del mondo è sufficientemente chiara?
- Sintassi, modello, entailment e prova sono introdotti con il giusto ritmo?
- Le clausole di Horn sono comprensibili prima della lettura storica?
- Forward e backward chaining risultano distinti senza sovraccaricare il lettore?
- Open-world, closed-world e `NOT EXISTS` sono separati correttamente?
- RDF, knowledge graph e OWL sono presentati come oggetti diversi?
- La rete bayesiana risulta comprensibile senza attribuire causalità automatica agli archi?
- Markov network e factor graph sono abbastanza chiari come ponte?
- Il passaggio dai posterior alle policy evita di confondere stima e decisione?

### Visuali

- In `KNOW-01`, i predicati spezzati restano facili da leggere?
- È evidente che le frecce rappresentano iterazioni di inferenza e non eventi causali?
- Il footer su assenza e negazione è abbastanza visibile?
- In `KNOW-02`, il prior appare chiaramente come annotazione di `H`?
- Le frecce `H -> M` e `H -> T` sono inequivocabili?
- Il calcolo del posterior è leggibile senza testo troppo denso?

### Codice

- Il motore di regole è sufficientemente piccolo e trasparente?
- I limiti rispetto a un reasoner completo sono espliciti?
- La separazione tra forward chaining e inferenza probabilistica è netta?
- I sette test coprono le proprietà didattiche portanti?

## Gate aperti

- materializzazione dei PNG nel feature branch;
- approvazione autoriale del testo;
- approvazione autoriale delle visuali;
- eventuali correzioni;
- rinomina in `final.png`;
- congelamento con data e commit.
