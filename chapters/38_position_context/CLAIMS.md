# Registro dei claim. Capitolo 38

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `position` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-38-01

- Affermazione esatta: Embedding appresi o sinusoidali aggiungono un segnale legato all'indice.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-38-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; RoFormer: Enhanced Transformer with Rotary Position Embedding; 2.2 Absolute position embedding; 2.3 Relative position embedding (claim collegato alla sezione «Posizione assoluta» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-38-02

- Affermazione esatta: Bias o rappresentazioni relative modificano i confronti in funzione della distanza.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-38-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation (claim collegato alla sezione «Posizione relativa» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-38-03

- Affermazione esatta: Rotazioni di query e key rendono il prodotto scalare dipendente dall'offset relativo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-38-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; YaRN: Efficient Context Window Extension of Large Language Models; 2.1 Rotary Position Embeddings; 2.2 Position Interpolation (claim collegato alla sezione «RoPE» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-38-04

- Affermazione esatta: Bias lineari penalizzano distanze maggiori con slope per head.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-38-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens; 2 Non-uniformity in Positional Interpolation; 2.2 Study on Non-uniform Positional Interpolation (claim collegato alla sezione «ALiBi» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-38-05

- Affermazione esatta: Positional interpolation e metodi affini estendono gli indici, ma l'uso effettivo del contesto deve essere misurato.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-38-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; RoFormer: Enhanced Transformer with Rotary Position Embedding; 2.2 Absolute position embedding; 2.3 Relative position embedding (claim collegato alla sezione «Estensione e valutazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-38-CODE

- Affermazione esatta: lo snippet snip_38_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_38_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
