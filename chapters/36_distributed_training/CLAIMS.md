# Registro dei claim. Capitolo 36

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `distributed_training` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-36-01

- Affermazione esatta: Repliche elaborano sotto-batch e aggregano gradienti. Media e loss reduction devono essere coerenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism; 2.3 Data and Model Parallelism in Deep Learning; 4.1 Training Dataset (claim collegato alla sezione «Data parallelism» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-36-02

- Affermazione esatta: Parametri, gradienti e optimizer state vengono shardati tra worker.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; ZeRO: Memory Optimizations Toward Training Trillion Parameter Models; 2.1 Data, Model and Pipeline Parallelism; 3.1 Model States: Optimizer States, Gradients and Parameters (claim collegato alla sezione «ZeRO e FSDP» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-36-03

- Affermazione esatta: Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Tensor e pipeline parallelism» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-36-04

- Affermazione esatta: Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2. Modes of Parallelism; 2.1. Data Parallelism; 2.2. Pipeline Model Parallelism (claim collegato alla sezione «Topologia e fault tolerance» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-36-05

- Affermazione esatta: Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism; 2.3 Data and Model Parallelism in Deep Learning; 4.1 Training Dataset (claim collegato alla sezione «Continued pretraining» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-36-CODE

- Affermazione esatta: lo snippet snip_36_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_36_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
