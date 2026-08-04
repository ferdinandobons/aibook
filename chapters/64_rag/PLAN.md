# Piano interno. Capitolo 64

- Domanda centrale: quale contratto costruisce Retrieval-Augmented Generation?
- Oggetto continuo: la pipeline che collega query, contesto e risposta; input guida: query, chunk, fonti e prompt.
- Prerequisito stabile: Capitolo 63, Information retrieval.
- Gap: chunking, retrieval, attribution e generazione.
- Output consegnato: risposta con evidenza e score end-to-end; consumer successivo: Capitolo 65, RAG adattivo, correttivo e basato su grafi.
- Invariante principale: contesto recuperato e testo generato devono restare distinguibili.
- Visuali: RAG-01 e RAG-02, con famiglie compositive variabili.
- Snippet: code/snip_64_contract.py; output: code/outputs/SNIP-64-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Una pipeline in due fasi

- Ultima affermazione stabile: la pipeline che collega query, contesto e risposta.
- Concetto nuovo: Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati.
- Input e shape: query, chunk, fonti e prompt.
- Operazione: chunking, retrieval, attribution e generazione.
- Output e shape: risposta con evidenza e score end-to-end.
- Che cosa cambia: il passaggio specifico di «Una pipeline in due fasi».
- Invariante: contesto recuperato e testo generato devono restare distinguibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due chunk citati e una frase che non compare nelle fonti; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Chunking.
- Prova: SRC-64-001 e sezione pubblica corrispondente.

## Transizione 2. Chunking

- Ultima affermazione stabile: la pipeline che collega query, contesto e risposta.
- Concetto nuovo: Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Un chunk non coincide sempre con una unità semantica.
- Input e shape: query, chunk, fonti e prompt.
- Operazione: chunking, retrieval, attribution e generazione.
- Output e shape: risposta con evidenza e score end-to-end.
- Che cosa cambia: il passaggio specifico di «Chunking».
- Invariante: contesto recuperato e testo generato devono restare distinguibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due chunk citati e una frase che non compare nelle fonti; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Prompt con fonti.
- Prova: SRC-64-002 e sezione pubblica corrispondente.

## Transizione 3. Prompt con fonti

- Ultima affermazione stabile: la pipeline che collega query, contesto e risposta.
- Concetto nuovo: Documenti, istruzioni e domanda devono avere confini espliciti. Il modello può ignorare, confondere o citare in modo scorretto il contesto.
- Input e shape: query, chunk, fonti e prompt.
- Operazione: chunking, retrieval, attribution e generazione.
- Output e shape: risposta con evidenza e score end-to-end.
- Che cosa cambia: il passaggio specifico di «Prompt con fonti».
- Invariante: contesto recuperato e testo generato devono restare distinguibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due chunk citati e una frase che non compare nelle fonti; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Attribution.
- Prova: SRC-64-003 e sezione pubblica corrispondente.

## Transizione 4. Attribution

- Ultima affermazione stabile: la pipeline che collega query, contesto e risposta.
- Concetto nuovo: Una risposta supportata deve essere collegabile a passaggi recuperati. Citazione presente e citazione corretta sono controlli differenti.
- Input e shape: query, chunk, fonti e prompt.
- Operazione: chunking, retrieval, attribution e generazione.
- Output e shape: risposta con evidenza e score end-to-end.
- Che cosa cambia: il passaggio specifico di «Attribution».
- Invariante: contesto recuperato e testo generato devono restare distinguibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due chunk citati e una frase che non compare nelle fonti; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Valutazione end-to-end.
- Prova: SRC-64-004 e sezione pubblica corrispondente.

## Transizione 5. Valutazione end-to-end

- Ultima affermazione stabile: la pipeline che collega query, contesto e risposta.
- Concetto nuovo: Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme.
- Input e shape: query, chunk, fonti e prompt.
- Operazione: chunking, retrieval, attribution e generazione.
- Output e shape: risposta con evidenza e score end-to-end.
- Che cosa cambia: il passaggio specifico di «Valutazione end-to-end».
- Invariante: contesto recuperato e testo generato devono restare distinguibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due chunk citati e una frase che non compare nelle fonti; provare anche una condizione incoerente e osservare il controllo.
- Consumer: RAG adattivo, correttivo e basato su grafi.
- Prova: SRC-64-001 e sezione pubblica corrispondente.
