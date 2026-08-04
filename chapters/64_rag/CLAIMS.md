# Registro dei claim. Capitolo 64

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `rag` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-64-01

- Affermazione esatta: Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks; 3.3 Jeopardy Question Generation; 4.3 Jeopardy Question Generation (claim collegato alla sezione «Una pipeline in due fasi» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-64-02

- Affermazione esatta: Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Un chunk non coincide sempre con una unità semantica.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Dense Passage Retrieval for Open-Domain Question Answering; 3 Dense Passage Retriever (DPR); 5 Experiments: Passage Retrieval (claim collegato alla sezione «Chunking» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-64-03

- Affermazione esatta: Documenti, istruzioni e domanda devono avere confini espliciti. Il modello può ignorare, confondere o citare in modo scorretto il contesto.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Self-Rag: Self-reflective Retrieval augmented Generation (claim collegato alla sezione «Prompt con fonti» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-64-04

- Affermazione esatta: Una risposta supportata deve essere collegabile a passaggi recuperati. Citazione presente e citazione corretta sono controlli differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Measuring Attribution in Natural Language Generation Models; 3.1 An Initial Definition of AIS: Attribution of Standalone Propositions; 3.2 Extending AIS: Attribution of Sentences in Context (claim collegato alla sezione «Attribution» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-64-05

- Affermazione esatta: Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks; 3.3 Jeopardy Question Generation; 4.3 Jeopardy Question Generation (claim collegato alla sezione «Valutazione end-to-end» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-64-CODE

- Affermazione esatta: lo snippet snip_64_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_64_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
