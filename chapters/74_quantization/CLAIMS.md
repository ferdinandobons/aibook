# Registro dei claim. Capitolo 74

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `quantization` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-74-01

- Affermazione esatta: Una mappa affine converte valori floating point in interi. Granularità per tensor, channel o group cambia errore e metadata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers (claim collegato alla sezione «Scala e zero point» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-74-02

- Affermazione esatta: Post-training quantization usa calibration senza riaddestrare completamente. La rappresentatività dei dati di calibration è essenziale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models; 3 Review of Quantization Difficulty; Migrate the quantization difficulty from activations to weights. (claim collegato alla sezione «PTQ» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-74-03

- Affermazione esatta: Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2 AWQ: Activation-aware Weight Quantization; 2.1 Improving LLM Quantization by Preserving 1% Salient Weights; 2.2 Protecting Salient Weights by Activation-aware Scaling (claim collegato alla sezione «QAT» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-74-04

- Affermazione esatta: Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; QLoRA : Efficient Finetuning of Quantized LLMs; Low-rank Adapters; Memory Requirement of Parameter-Efficient Finetuning (claim collegato alla sezione «Weight-only e activation quantization» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-74-05

- Affermazione esatta: GPTQ, AWQ, SmoothQuant e famiglie affini gestiscono salienza e outlier con contratti differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers (claim collegato alla sezione «Metodi per LLM» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-74-CODE

- Affermazione esatta: lo snippet snip_74_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_74_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
