# Registro dei claim. Capitolo 75

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `low_bit` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-75-01

- Affermazione esatta: Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits; 1 The Era of 1-bit LLMs; 2 BitNet b1.58 (claim collegato alla sezione «Training nativo» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-75-02

- Affermazione esatta: BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici. Il numero medio di bit non descrive da solo il kernel.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; BitNet: Scaling 1-bit Transformers for Large Language Models; 2 BitNet; 2.1 BitLinear (claim collegato alla sezione «Pesi ternari e 1.58-bit» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-75-03

- Affermazione esatta: Operazioni discrete usano gradienti surrogati. La derivata applicata nel backward non è la derivata classica della quantizzazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Introduction; 1 Binarized Neural Networks; 1.1 Deterministic vs Stochastic Binarization (claim collegato alla sezione «Straight-through estimator» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-75-04

- Affermazione esatta: Prodotti low-bit possono accumulare in precisione maggiore. Storage, compute e accumulator dtype devono essere separati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Computer Science > Computer Vision and Pattern Recognition; Title: Lets keep it simple, Using simple architectures to outperform deeper and more complex architectures; Submission history (claim collegato alla sezione «Accumulazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-75-05

- Affermazione esatta: Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato. Benchmark su hardware non ottimizzato possono nasconderlo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits; 1 The Era of 1-bit LLMs; 2 BitNet b1.58 (claim collegato alla sezione «Co-design hardware» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-75-CODE

- Affermazione esatta: lo snippet snip_75_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_75_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
