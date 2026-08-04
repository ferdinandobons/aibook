# Piano interno. Capitolo 63

- Domanda centrale: quale contratto costruisce Information retrieval?
- Oggetto continuo: query e documenti ordinati per rilevanza; input guida: query, corpus, termini e indice.
- Prerequisito stabile: Capitolo 62, World model, embodied AI e vision-language-action.
- Gap: BM25, dense retrieval, ANN e reranking.
- Output consegnato: ranking con score e documento recuperato; consumer successivo: Capitolo 64, Retrieval-Augmented Generation.
- Invariante principale: rilevanza del ranking e correttezza della risposta sono misure separate.
- Visuali: RETRIEVAL-01 e RETRIEVAL-02, con famiglie compositive variabili.
- Snippet: code/snip_63_contract.py; output: code/outputs/SNIP-63-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Documenti, query e rilevanza

- Ultima affermazione stabile: query e documenti ordinati per rilevanza.
- Concetto nuovo: Un sistema di retrieval ordina documenti rispetto a una query. La rilevanza dipende dal bisogno informativo e dalle label disponibili.
- Input e shape: query, corpus, termini e indice.
- Operazione: BM25, dense retrieval, ANN e reranking.
- Output e shape: ranking con score e documento recuperato.
- Che cosa cambia: il passaggio specifico di «Documenti, query e rilevanza».
- Invariante: rilevanza del ranking e correttezza della risposta sono misure separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre documenti ordinati per sovrapposizione di termini; provare anche una condizione incoerente e osservare il controllo.
- Consumer: BM25.
- Prova: SRC-63-001 e sezione pubblica corrispondente.

## Transizione 2. BM25

- Ultima affermazione stabile: query e documenti ordinati per rilevanza.
- Concetto nuovo: La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza. Tokenizzazione e campi modificano il punteggio.
- Input e shape: query, corpus, termini e indice.
- Operazione: BM25, dense retrieval, ANN e reranking.
- Output e shape: ranking con score e documento recuperato.
- Che cosa cambia: il passaggio specifico di «BM25».
- Invariante: rilevanza del ranking e correttezza della risposta sono misure separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre documenti ordinati per sovrapposizione di termini; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Dense retrieval.
- Prova: SRC-63-002 e sezione pubblica corrispondente.

## Transizione 3. Dense retrieval

- Ultima affermazione stabile: query e documenti ordinati per rilevanza.
- Concetto nuovo: Un bi-encoder mappa query e documenti in vettori e usa una similarità. L'addestramento dipende da positivi, negativi e in-batch sampling.
- Input e shape: query, corpus, termini e indice.
- Operazione: BM25, dense retrieval, ANN e reranking.
- Output e shape: ranking con score e documento recuperato.
- Che cosa cambia: il passaggio specifico di «Dense retrieval».
- Invariante: rilevanza del ranking e correttezza della risposta sono misure separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre documenti ordinati per sovrapposizione di termini; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Indici ANN.
- Prova: SRC-63-003 e sezione pubblica corrispondente.

## Transizione 4. Indici ANN

- Ultima affermazione stabile: query e documenti ordinati per rilevanza.
- Concetto nuovo: Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo. Recall, memoria e latenza dipendono dalla struttura e dai parametri.
- Input e shape: query, corpus, termini e indice.
- Operazione: BM25, dense retrieval, ANN e reranking.
- Output e shape: ranking con score e documento recuperato.
- Che cosa cambia: il passaggio specifico di «Indici ANN».
- Invariante: rilevanza del ranking e correttezza della risposta sono misure separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre documenti ordinati per sovrapposizione di termini; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Reranking.
- Prova: SRC-63-004 e sezione pubblica corrispondente.

## Transizione 5. Reranking

- Ultima affermazione stabile: query e documenti ordinati per rilevanza.
- Concetto nuovo: Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo.
- Input e shape: query, corpus, termini e indice.
- Operazione: BM25, dense retrieval, ANN e reranking.
- Output e shape: ranking con score e documento recuperato.
- Che cosa cambia: il passaggio specifico di «Reranking».
- Invariante: rilevanza del ranking e correttezza della risposta sono misure separate.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre documenti ordinati per sovrapposizione di termini; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Retrieval-Augmented Generation.
- Prova: SRC-63-001 e sezione pubblica corrispondente.
