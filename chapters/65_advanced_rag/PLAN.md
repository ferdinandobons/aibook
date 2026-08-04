# Piano interno. Capitolo 65

- Domanda centrale: quale contratto costruisce RAG adattivo, correttivo e basato su grafi?
- Oggetto continuo: una query instradata tra retriever e grafo; input guida: domanda multi-hop, nodi, archi e documenti.
- Prerequisito stabile: Capitolo 64, Retrieval-Augmented Generation.
- Gap: query transformation, routing e corrective retrieval.
- Output consegnato: sottoquery, percorso e contesto selezionato; consumer successivo: Capitolo 66, Contesto lungo, retrieval e memoria.
- Invariante principale: un router può sbagliare anche quando il generatore è corretto.
- Visuali: RAG-01 e RAG-02, con famiglie compositive variabili.
- Snippet: code/snip_65_contract.py; output: code/outputs/SNIP-65-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Query transformation

- Ultima affermazione stabile: una query instradata tra retriever e grafo.
- Concetto nuovo: Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval. Ogni trasformazione può migliorare recall o introdurre drift.
- Input e shape: domanda multi-hop, nodi, archi e documenti.
- Operazione: query transformation, routing e corrective retrieval.
- Output e shape: sottoquery, percorso e contesto selezionato.
- Che cosa cambia: il passaggio specifico di «Query transformation».
- Invariante: un router può sbagliare anche quando il generatore è corretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una domanda divisa in due sottoquery con un arco mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Retrieval adattivo.
- Prova: SRC-65-001 e sezione pubblica corrispondente.

## Transizione 2. Retrieval adattivo

- Ultima affermazione stabile: una query instradata tra retriever e grafo.
- Concetto nuovo: Il sistema decide se recuperare, quante volte e con quale sorgente. La decisione è un componente da valutare, non un comportamento gratuito del modello.
- Input e shape: domanda multi-hop, nodi, archi e documenti.
- Operazione: query transformation, routing e corrective retrieval.
- Output e shape: sottoquery, percorso e contesto selezionato.
- Che cosa cambia: il passaggio specifico di «Retrieval adattivo».
- Invariante: un router può sbagliare anche quando il generatore è corretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una domanda divisa in due sottoquery con un arco mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Corrective RAG.
- Prova: SRC-65-002 e sezione pubblica corrispondente.

## Transizione 3. Corrective RAG

- Ultima affermazione stabile: una query instradata tra retriever e grafo.
- Concetto nuovo: Documenti vengono valutati, filtrati o sostituiti prima della generazione. Confidence e web fallback richiedono soglie e autorizzazioni.
- Input e shape: domanda multi-hop, nodi, archi e documenti.
- Operazione: query transformation, routing e corrective retrieval.
- Output e shape: sottoquery, percorso e contesto selezionato.
- Che cosa cambia: il passaggio specifico di «Corrective RAG».
- Invariante: un router può sbagliare anche quando il generatore è corretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una domanda divisa in due sottoquery con un arco mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Graph RAG.
- Prova: SRC-65-003 e sezione pubblica corrispondente.

## Transizione 4. Graph RAG

- Ultima affermazione stabile: una query instradata tra retriever e grafo.
- Concetto nuovo: Entità, relazioni e comunità permettono query e sintesi multi-hop. Il grafo dipende da estrazione, normalizzazione e aggiornamento.
- Input e shape: domanda multi-hop, nodi, archi e documenti.
- Operazione: query transformation, routing e corrective retrieval.
- Output e shape: sottoquery, percorso e contesto selezionato.
- Che cosa cambia: il passaggio specifico di «Graph RAG».
- Invariante: un router può sbagliare anche quando il generatore è corretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una domanda divisa in due sottoquery con un arco mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: RAG agentico.
- Prova: SRC-65-004 e sezione pubblica corrispondente.

## Transizione 5. RAG agentico

- Ultima affermazione stabile: una query instradata tra retriever e grafo.
- Concetto nuovo: Un agente può pianificare retrieval successivi. Più step aumentano copertura e contemporaneamente costo, errori e superficie di attacco.
- Input e shape: domanda multi-hop, nodi, archi e documenti.
- Operazione: query transformation, routing e corrective retrieval.
- Output e shape: sottoquery, percorso e contesto selezionato.
- Che cosa cambia: il passaggio specifico di «RAG agentico».
- Invariante: un router può sbagliare anche quando il generatore è corretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una domanda divisa in due sottoquery con un arco mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Contesto lungo, retrieval e memoria.
- Prova: SRC-65-001 e sezione pubblica corrispondente.
