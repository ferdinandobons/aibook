# Registro dei claim. Capitolo 30

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `pretraining_families` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-30-01

- Affermazione esatta: Modelli come BERT usano contesto bidirezionale e obiettivi masked. Sono naturali per encoding e classificazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-30-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Input/Output Representations; Task #2: Next Sentence Prediction (NSP); Next Sentence Prediction (claim collegato alla sezione «Encoder-only» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-30-02

- Affermazione esatta: Un decoder causale predice token successivi e supporta generazione incrementale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-30-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Decoder-only» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-30-03

- Affermazione esatta: T5 e famiglie affini trasformano una sequenza sorgente in una sequenza target con cross-attention.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-30-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer; B Converting WNLI to Our Text-to-Text Format (claim collegato alla sezione «Encoder-decoder» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-30-04

- Affermazione esatta: Obiettivi differenti stabiliscono quali token sono visibili e quali producono loss.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-30-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Language Model; Permuted Language Model; Masked Language Model (claim collegato alla sezione «Masked, causal e span corruption» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-30-05

- Affermazione esatta: La forma del modello e l'obiettivo sono assi separati. Confrontarli richiede dati, compute e task coerenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-30-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Input/Output Representations; Task #2: Next Sentence Prediction (NSP); Next Sentence Prediction (claim collegato alla sezione «Architettura e obiettivo» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-30-CODE

- Affermazione esatta: lo snippet snip_30_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_30_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
