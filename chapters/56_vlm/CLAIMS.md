# Registro dei claim. Capitolo 56

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `vlm` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-56-01

- Affermazione esatta: Una immagine viene trasformata in patch o feature. Risoluzione, positional encoding e pooling definiscono la sequenza visiva.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (claim collegato alla sezione «Patch e vision encoder» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-56-02

- Affermazione esatta: CLIP allinea immagine e testo con una loss contrastiva. I due encoder supportano retrieval efficiente ma interagiscono tardi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models; 2.1 End-to-end Vision-Language Pre-training; 2.2 Modular Vision-Language Pre-training (claim collegato alla sezione «Dual encoder» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-56-03

- Affermazione esatta: Architetture modulari proiettano feature visive nella dimensione del language model. Il projector stabilisce capacità e numero di visual token.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Instructions for brief image description.; Instructions for detailed image description. (claim collegato alla sezione «Projector» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-56-04

- Affermazione esatta: Query apprese possono estrarre un insieme compatto di feature. Altre architetture inseriscono cross-attention dedicata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Flamingo: a Visual Language Model for Few-Shot Learning; 2.2 Conditioning frozen language models on visual representations; 2.3 Multi-visual input support: per-image/video attention masking (claim collegato alla sezione «Q-Former e cross-attention» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-56-05

- Affermazione esatta: Descrivere una immagine non garantisce localizzare oggetti o relazioni. Grounding, OCR e affidabilità richiedono test specifici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (claim collegato alla sezione «Grounding e hallucination» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-56-CODE

- Affermazione esatta: lo snippet snip_56_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_56_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
