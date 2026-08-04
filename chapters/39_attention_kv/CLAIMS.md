# Registro dei claim. Capitolo 39

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `attention_variants` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-39-01

- Affermazione esatta: Ogni query head possiede key e value dedicate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2 Background: Neural Attention; 2.1 Dot-Product Attention; 2.2 Multi-head Attention (claim collegato alla sezione «MHA» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-39-02

- Affermazione esatta: Tutte le query head condividono una singola coppia key-value, riducendo la cache.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; GQA : Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints; 2.2 Grouped-query attention (claim collegato alla sezione «MQA» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-39-03

- Affermazione esatta: Gruppi di query head condividono un numero intermedio di KV head.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2.1 Multi-Head Latent Attention: Boosting Inference Efficiency; 2.1.1 Preliminaries: Standard Multi-Head Attention; Appendix D Ablation of Attention Mechanisms (claim collegato alla sezione «GQA» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-39-04

- Affermazione esatta: Finestre e pattern selezionati riducono le coppie ma cambiano la connettività.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3.1 Attention Pattern; 4.1 Attention Pattern (claim collegato alla sezione «Local e sparse attention» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-39-05

- Affermazione esatta: Compressione latente e numero di KV head sono strategie differenti. La memoria dipende anche da layer, dtype, batch e lunghezza.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2 Background: Neural Attention; 2.1 Dot-Product Attention; 2.2 Multi-head Attention (claim collegato alla sezione «MLA e cache» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-39-CODE

- Affermazione esatta: lo snippet snip_39_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_39_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
