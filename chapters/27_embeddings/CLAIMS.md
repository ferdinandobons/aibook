# Registro dei claim. Capitolo 27

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `embeddings` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-27-01

- Affermazione esatta: Una embedding table seleziona una riga per token. La dimensione del vettore è una scelta architetturale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Efficient Estimation of Word Representations in Vector Space; 4.5 Microsoft Research Sentence Completion Challenge (claim collegato alla sezione «Da ID a vettore» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-27-02

- Affermazione esatta: Word2vec e GloVe usano statistiche distributive con obiettivi differenti. Similarità geometrica riflette dati e obiettivo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Input/Output Representations; Task #2: Next Sentence Prediction (NSP); Next Sentence Prediction (claim collegato alla sezione «Word embedding» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-27-03

- Affermazione esatta: In un Transformer, la rappresentazione di un token cambia con il contesto. La stessa stringa può produrre vettori diversi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks (claim collegato alla sezione «Embedding contestuale» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-27-04

- Affermazione esatta: Pooling o training contrastivo producono vettori per frasi e documenti. La metrica deve corrispondere all'uso previsto.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; SimCSE: Simple Contrastive Learning of Sentence Embeddings (claim collegato alla sezione «Sentence embedding» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-27-05

- Affermazione esatta: Cosine similarity è una convenzione, non una misura universale di significato. Normalizzazione e distribuzione dello spazio influenzano il ranking.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Efficient Estimation of Word Representations in Vector Space; 4.5 Microsoft Research Sentence Completion Challenge (claim collegato alla sezione «Ricerca e anisotropia» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-27-CODE

- Affermazione esatta: lo snippet snip_27_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_27_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
