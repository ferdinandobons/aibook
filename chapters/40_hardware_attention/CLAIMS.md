# Registro dei claim. Capitolo 40

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `flash` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-40-01

- Affermazione esatta: Lo stesso operatore può avere traffico di memoria molto diverso.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; FlashAttention : Fast and Memory-Efficient Exact Attention with IO-Awareness; 2.2 Standard Attention Implementation; 3 FlashAttention : Algorithm, Analysis, and Extensions (claim collegato alla sezione «FLOP e movimento dei dati» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-40-02

- Affermazione esatta: Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; FlashAttention-2 : Faster Attention with Better Parallelism and Work Partitioning; 2.2 Standard Attention Implementation; 2.3 FlashAttention (claim collegato alla sezione «Tiling» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-40-03

- Affermazione esatta: Massimo, denominatore e numeratore vengono aggiornati blocco per blocco.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision; 2 Background: Multi-Head Attention and GPU Characteristics; 2.1 Multi-Head Attention (claim collegato alla sezione «Softmax online» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-40-04

- Affermazione esatta: Salvare meno intermedi scambia memoria con compute aggiuntivo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Backward e ricomputazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-40-05

- Affermazione esatta: FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; FlashAttention : Fast and Memory-Efficient Exact Attention with IO-Awareness; 2.2 Standard Attention Implementation; 3 FlashAttention : Algorithm, Analysis, and Extensions (claim collegato alla sezione «Backend» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-40-CODE

- Affermazione esatta: lo snippet snip_40_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_40_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
