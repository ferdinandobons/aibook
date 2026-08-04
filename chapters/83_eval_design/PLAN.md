# Piano interno. Capitolo 83

- Domanda centrale: quale contratto costruisce Progettare una valutazione?
- Oggetto continuo: un claim valutativo e il protocollo che lo rende misurabile; input guida: task, dataset, predizioni, riferimento e metriche.
- Prerequisito stabile: Capitolo 82, LLMOps, edge, costo ed energia.
- Gap: scelta della metrica, giudice, slice e report.
- Output consegnato: stima, intervallo, errori e decisione; consumer successivo: Capitolo 84, Fattualità, incertezza e affidabilità.
- Invariante principale: una metrica risponde solo alla domanda per cui è stata progettata.
- Visuali: DESIGN-01 e DESIGN-02, con famiglie compositive variabili.
- Snippet: code/snip_83_contract.py; output: code/outputs/SNIP-83-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Decisione e claim

- Ultima affermazione stabile: un claim valutativo e il protocollo che lo rende misurabile.
- Concetto nuovo: Una valutazione parte dalla decisione che deve sostenere. Il claim deve nominare popolazione, condizioni, metrica e incertezza.
- Input e shape: task, dataset, predizioni, riferimento e metriche.
- Operazione: scelta della metrica, giudice, slice e report.
- Output e shape: stima, intervallo, errori e decisione.
- Che cosa cambia: il passaggio specifico di «Decisione e claim».
- Invariante: una metrica risponde solo alla domanda per cui è stata progettata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: accuracy media accompagnata da una slice fallita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Task e dataset.
- Prova: SRC-83-001 e sezione pubblica corrispondente.

## Transizione 2. Task e dataset

- Ultima affermazione stabile: un claim valutativo e il protocollo che lo rende misurabile.
- Concetto nuovo: Prompt, input, reference e rubric devono rappresentare l'uso previsto. Split e cutoff impediscono contaminazione intenzionale.
- Input e shape: task, dataset, predizioni, riferimento e metriche.
- Operazione: scelta della metrica, giudice, slice e report.
- Output e shape: stima, intervallo, errori e decisione.
- Che cosa cambia: il passaggio specifico di «Task e dataset».
- Invariante: una metrica risponde solo alla domanda per cui è stata progettata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: accuracy media accompagnata da una slice fallita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Metriche.
- Prova: SRC-83-002 e sezione pubblica corrispondente.

## Transizione 3. Metriche

- Ultima affermazione stabile: un claim valutativo e il protocollo che lo rende misurabile.
- Concetto nuovo: Metriche automatiche, giudizi umani e verificatori misurano proprietà differenti. Aggregazione e slice devono essere predefinite.
- Input e shape: task, dataset, predizioni, riferimento e metriche.
- Operazione: scelta della metrica, giudice, slice e report.
- Output e shape: stima, intervallo, errori e decisione.
- Che cosa cambia: il passaggio specifico di «Metriche».
- Invariante: una metrica risponde solo alla domanda per cui è stata progettata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: accuracy media accompagnata da una slice fallita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Giudici modello.
- Prova: SRC-83-003 e sezione pubblica corrispondente.

## Transizione 4. Giudici modello

- Ultima affermazione stabile: un claim valutativo e il protocollo che lo rende misurabile.
- Concetto nuovo: LLM-as-a-judge può scalare confronti, ma è sensibile a posizione, stile, modello e rubric. Serve calibrazione con giudizi indipendenti.
- Input e shape: task, dataset, predizioni, riferimento e metriche.
- Operazione: scelta della metrica, giudice, slice e report.
- Output e shape: stima, intervallo, errori e decisione.
- Che cosa cambia: il passaggio specifico di «Giudici modello».
- Invariante: una metrica risponde solo alla domanda per cui è stata progettata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: accuracy media accompagnata da una slice fallita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Report.
- Prova: SRC-83-004 e sezione pubblica corrispondente.

## Transizione 5. Report

- Ultima affermazione stabile: un claim valutativo e il protocollo che lo rende misurabile.
- Concetto nuovo: Intervalli, fallimenti, costi e limiti accompagnano il punteggio. Una leaderboard non sostituisce il protocollo.
- Input e shape: task, dataset, predizioni, riferimento e metriche.
- Operazione: scelta della metrica, giudice, slice e report.
- Output e shape: stima, intervallo, errori e decisione.
- Che cosa cambia: il passaggio specifico di «Report».
- Invariante: una metrica risponde solo alla domanda per cui è stata progettata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: accuracy media accompagnata da una slice fallita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Fattualità, incertezza e affidabilità.
- Prova: SRC-83-001 e sezione pubblica corrispondente.
