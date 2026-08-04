# Piano editoriale. Capitolo 64

## Obiettivo didattico

Seguire **Retrieval-Augmented Generation** da query, chunk, fonti e prompt a risposta con evidenza e score end-to-end, osservando chunking, retrieval, attribution e generazione senza oltrepassare questo limite: contesto recuperato e testo generato devono restare distinguibili.

## Prerequisiti reali

- Capitolo 29: Il Transformer da zero
- Capitolo 31: Dalla rappresentazione linguistica agli LLM
- Capitolo 63: Information retrieval

## Percorso della lezione

1. **Una pipeline in due fasi.** Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati. Prova: SRC-64-001.
2. **Chunking.** Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Un chunk non coincide sempre con una unità semantica. Prova: SRC-64-002.
3. **Prompt con fonti.** Documenti, istruzioni e domanda devono avere confini espliciti. Il modello può ignorare, confondere o citare in modo scorretto il contesto. Prova: SRC-64-003.
4. **Attribution.** Una risposta supportata deve essere collegabile a passaggi recuperati. Citazione presente e citazione corretta sono controlli differenti. Prova: SRC-64-004.
5. **Valutazione end-to-end.** Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme. Prova: SRC-64-001.

## Prove e artefatti

- riferimento minimo: `code/snip_64_contract.py`; test: `code/test_64_contract.py`; output: `code/outputs/SNIP-64-001.txt`.
- visuali candidate: RAG-01, RAG-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
