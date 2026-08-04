# Registro dei claim. Capitolo 37

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `modern_block` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-37-01

- Affermazione esatta: Ogni sottolayer produce un aggiornamento sommato a un percorso identità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Attention Is All You Need; 1 Introduction; 2 Background (claim collegato alla sezione «Residual stream» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-37-02

- Affermazione esatta: La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; On Layer Normalization in the Transformer Architecture; 3 Optimization for the Transformer; 3.1 Transformer with Post-Layer Normalization (claim collegato alla sezione «Pre-norm e post-norm» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-37-03

- Affermazione esatta: RMSNorm scala usando la media quadratica e non sottrae la media.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Root Mean Square Layer Normalization (claim collegato alla sezione «RMSNorm» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-37-04

- Affermazione esatta: Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; GLU Variants Improve Transformer; 3 Experiments on Text-to-Text Transfer Transformer (T5) (claim collegato alla sezione «SwiGLU» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-37-05

- Affermazione esatta: Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Attention Is All You Need; 1 Introduction; 2 Background (claim collegato alla sezione «Ordine e parallelismo» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-37-CODE

- Affermazione esatta: lo snippet snip_37_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_37_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
