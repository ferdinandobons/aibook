# Registro dei claim. Capitolo 63

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `retrieval` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-63-01

- Affermazione esatta: Un sistema di retrieval ordina documenti rispetto a una query. La rilevanza dipende dal bisogno informativo e dalle label disponibili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract; Section 1 introduction; sections on BM25 and probabilistic relevance (claim collegato alla sezione «Documenti, query e rilevanza» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: publisher/index record opened via web research; scope and title checked; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-63-02

- Affermazione esatta: La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza. Tokenizzazione e campi modificano il punteggio.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Dense Passage Retrieval for Open-Domain Question Answering; 3 Dense Passage Retriever (DPR); 5 Experiments: Passage Retrieval (claim collegato alla sezione «BM25» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-63-03

- Affermazione esatta: Un bi-encoder mappa query e documenti in vettori e usa una similarità. L'addestramento dipende da positivi, negativi e in-batch sampling.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3.5. Top- k 𝑘 k Re-ranking with ColBERT; 3.6. End-to-end Top- k 𝑘 k Retrieval with ColBERT; 4.2. Quality–Cost Tradeoff: Top- k 𝑘 k Re-ranking (claim collegato alla sezione «Dense retrieval» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-63-04

- Affermazione esatta: Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo. Recall, memoria e latenza dipendono dalla struttura e dai parametri.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Billion-scale similarity search with GPUs; 1 Introduction; 2 Problem statement (claim collegato alla sezione «Indici ANN» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-63-05

- Affermazione esatta: Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract; Section 1 introduction; sections on BM25 and probabilistic relevance (claim collegato alla sezione «Reranking» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: publisher/index record opened via web research; scope and title checked; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-63-CODE

- Affermazione esatta: lo snippet snip_63_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_63_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
