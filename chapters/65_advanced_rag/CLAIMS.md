# Registro dei claim. Capitolo 65

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `advanced_rag` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-65-01

- Affermazione esatta: Rewrite, expansion, decomposition e HyDE modificano la query prima del retrieval. Ogni trasformazione può migliorare recall o introdurre drift.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-65-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Self-Rag: Self-reflective Retrieval augmented Generation (claim collegato alla sezione «Query transformation» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-65-02

- Affermazione esatta: Il sistema decide se recuperare, quante volte e con quale sorgente. La decisione è un componente da valutare, non un comportamento gratuito del modello.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-65-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval; Why Retrieval?; Retrieval Methods; Appendix F Pseudocode for Retrieval Methods (claim collegato alla sezione «Retrieval adattivo» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-65-03

- Affermazione esatta: Documenti vengono valutati, filtrati o sostituiti prima della generazione. Confidence e web fallback richiedono soglie e autorizzazioni.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-65-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; From Local to Global: A Graph RAG Approach to Query-Focused Summarization; 2 Graph RAG Approach & Pipeline; 2.4 Element Summaries → → \rightarrow Graph Communities (claim collegato alla sezione «Corrective RAG» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-65-04

- Affermazione esatta: Entità, relazioni e comunità permettono query e sintesi multi-hop. Il grafo dipende da estrazione, normalizzazione e aggiornamento.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-65-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Precise Zero-Shot Dense Retrieval without Relevance Labels; 4.3 Low Resource Retrieval; 4.4 Multilingual Retrieval (claim collegato alla sezione «Graph RAG» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-65-05

- Affermazione esatta: Un agente può pianificare retrieval successivi. Più step aumentano copertura e contemporaneamente costo, errori e superficie di attacco.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-65-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Self-Rag: Self-reflective Retrieval augmented Generation (claim collegato alla sezione «RAG agentico» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-65-CODE

- Affermazione esatta: lo snippet snip_65_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_65_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
