# Registro dei claim. Capitolo 78

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `kv_cache` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-78-01

- Affermazione esatta: Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache precedente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Efficient Memory Management for Large Language Model Serving with PagedAttention; 3. Memory Challenges in LLM Serving; 3.1. Memory Management in Existing Systems (claim collegato alla sezione «Prefill e decode» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-78-02

- Affermazione esatta: Layer, batch, KV head, token e head dimension determinano shape e byte. Contiguità e paginazione influenzano il kernel.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3.2 Rolling KV Cache with Attention Sinks (claim collegato alla sezione «Layout» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-78-03

- Affermazione esatta: Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare sequenze di lunghezza diversa.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Efficiently Programming Large Language Models using SGLang; 1 Introduction; 2 Background (claim collegato alla sezione «PagedAttention» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-78-04

- Affermazione esatta: Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi sono compatibili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; FlashAttention : Fast and Memory-Efficient Exact Attention with IO-Awareness; 2.2 Standard Attention Implementation; 3 FlashAttention : Algorithm, Analysis, and Extensions (claim collegato alla sezione «Prefix caching» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-78-05

- Affermazione esatta: Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano precisione o contesto disponibile.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Efficient Memory Management for Large Language Model Serving with PagedAttention; 3. Memory Challenges in LLM Serving; 3.1. Memory Management in Existing Systems (claim collegato alla sezione «Compressione ed eviction» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-78-CODE

- Affermazione esatta: lo snippet snip_78_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_78_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
