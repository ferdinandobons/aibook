# Registro dei claim. Capitolo 81

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `compiler` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-81-01

- Affermazione esatta: Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Evaluating Large Language Models Trained on Code; 1 Introduction; 2 Evaluation Framework (claim collegato alla sezione «Grafo e operatori» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-81-02

- Affermazione esatta: Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Kernel fusion» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-81-03

- Affermazione esatta: Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; XLA Stay organized with collections Save and categorize content based on your preferences.; Key benefits; Documentation (claim collegato alla sezione «Triton e kernel custom» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-81-04

- Affermazione esatta: Tracing e guard permettono specializzazione dinamica. Python side effect o shape non supportate producono graph break.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Intel OpenMP Runtime Library ( libiomp ) # (claim collegato alla sezione «torch.compile e graph break» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-81-05

- Affermazione esatta: Tile, num warps e schedule ottimali dipendono dall'hardware. Un kernel corretto richiede test numerici e benchmark separati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Evaluating Large Language Models Trained on Code; 1 Introduction; 2 Evaluation Framework (claim collegato alla sezione «Autotuning e portabilità» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-81-CODE

- Affermazione esatta: lo snippet snip_81_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_81_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
