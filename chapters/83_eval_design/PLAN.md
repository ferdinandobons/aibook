# Piano editoriale. Capitolo 83

## Obiettivo didattico

Seguire **Progettare una valutazione** da task, dataset, predizioni, riferimento e metriche a stima, intervallo, errori e decisione, osservando scelta della metrica, giudice, slice e report senza oltrepassare questo limite: una metrica risponde solo alla domanda per cui è stata progettata.

## Prerequisiti reali

- Capitolo 4: Come valutare criticamente un risultato di AI
- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 31: Dalla rappresentazione linguistica agli LLM

## Percorso della lezione

1. **Decisione e claim.** Una valutazione parte dalla decisione che deve sostenere. Il claim deve nominare popolazione, condizioni, metrica e incertezza. Prova: SRC-83-001.
2. **Task e dataset.** Prompt, input, reference e rubric devono rappresentare l'uso previsto. Split e cutoff impediscono contaminazione intenzionale. Prova: SRC-83-002.
3. **Metriche.** Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti. Aggregazione e slice devono essere predefinite. Prova: SRC-83-003.
4. **Giudici modello.** LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric. Serve calibrazione con giudizi indipendenti. Prova: SRC-83-004.
5. **Report.** Intervalli, fallimenti, costi e limiti accompagnano il punteggio. Una leaderboard non sostituisce il protocollo. Prova: SRC-83-001.

## Prove e artefatti

- riferimento minimo: `code/snip_83_contract.py`; test: `code/test_83_contract.py`; output: `code/outputs/SNIP-83-001.txt`.
- visuali candidate: DESIGN-01, DESIGN-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
