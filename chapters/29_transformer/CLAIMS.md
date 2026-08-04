# Registro dei claim. Capitolo 29

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `transformer` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-29-01

- Affermazione esatta: Il Transformer combina embedding, posizione, attention, feed-forward, residual e normalizzazione. Ogni componente mantiene un contratto di shape.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Attention Is All You Need; 1 Introduction; 2 Background (claim collegato alla sezione «La mappa completa» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-29-02

- Affermazione esatta: L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le posizioni.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Input/Output Representations; Task #2: Next Sentence Prediction (NSP); Next Sentence Prediction (claim collegato alla sezione «Encoder» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-29-03

- Affermazione esatta: Il decoder usa self-attention causale e, nelle architetture encoder-decoder, cross-attention verso l'encoder.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Why unsupervised learning; Drawbacks; Future; Appendix: Dataset examples; Compute (claim collegato alla sezione «Decoder» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: official OpenAI page and linked author paper opened via web research; legacy URL redirects to current index; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-29-04

- Affermazione esatta: Le head applicano proiezioni differenti e vengono concatenate. La proiezione finale riporta alla dimensione del modello.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; On Layer Normalization in the Transformer Architecture; 3 Optimization for the Transformer; 3.1 Transformer with Post-Layer Normalization (claim collegato alla sezione «Multi-head attention» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-29-05

- Affermazione esatta: Layer ripetuti aggiornano il residual stream. La head di output trasforma la rappresentazione in logits sul vocabolario.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Attention Is All You Need; 1 Introduction; 2 Background (claim collegato alla sezione «Residual stream e output» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-29-CODE

- Affermazione esatta: lo snippet snip_29_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_29_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
