# Registro dei claim. Capitolo 43

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `hybrid_memory` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-43-01

- Affermazione esatta: Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-43-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models; 2.4 Real-Gated Linear Recurrent Unit (RG-LRU); 3 Recurrent Models Scale as Efficiently as Transformers (claim collegato alla sezione «Ibridi tra layer» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-43-02

- Affermazione esatta: Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre la finestra.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-43-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Memory Perspective; 3.1 Long-term Memory; 3.2 How to Parallelize the Long-term Memory Training (claim collegato alla sezione «Attention locale e stato» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-43-03

- Affermazione esatta: Stati di segmenti precedenti possono essere riusati o compressi con stop-gradient e capacità limitata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-43-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Linear Attention (claim collegato alla sezione «Memoria segmentale» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-43-04

- Affermazione esatta: Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-43-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Memoria associativa» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-43-05

- Affermazione esatta: Lo stato neurale non coincide con retrieval documentale. Reset, isolamento e provenienza hanno contratti differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-43-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models; 2.4 Real-Gated Linear Recurrent Unit (RG-LRU); 3 Recurrent Models Scale as Efficiently as Transformers (claim collegato alla sezione «Memoria interna ed esterna» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-43-CODE

- Affermazione esatta: lo snippet snip_43_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_43_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
