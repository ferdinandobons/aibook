# Registro dei claim. Capitolo 31

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `llm_behavior` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-31-01

- Affermazione esatta: Un LLM autoregressivo produce logits condizionati sul prefisso. La softmax costruisce una distribuzione, non una risposta già scelta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Language Models are Few-Shot Learners; 3.1 Language Modeling, Cloze, and Completion Tasks; 3.1.1 Language Modeling (claim collegato alla sezione «Distribuzione del token successivo» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-31-02

- Affermazione esatta: Istruzioni ed esempi entrano nel contesto senza un optimizer step. Il checkpoint resta invariato durante in-context learning.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?; 5 Why does In-Context Learning work? (claim collegato alla sezione «Prompt e dimostrazioni» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-31-03

- Affermazione esatta: Greedy, sampling, temperature e truncation trasformano la distribuzione in una traiettoria.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3 Language Model Decoding; 4.3 Natural Language Does Not Maximize Probability (claim collegato alla sezione «Decoding» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-31-04

- Affermazione esatta: Probabilità del token, confidenza espressa e correttezza fattuale sono quantità differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; On Calibration of Modern Neural Networks; Supplementary Materials for: On Calibration of Modern Neural Networks; Expected Calibration Error (ECE). (claim collegato alla sezione «Calibrazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-31-05

- Affermazione esatta: Post-training, messaggi di sistema, strumenti e filtri contribuiscono al comportamento osservato.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Language Models are Few-Shot Learners; 3.1 Language Modeling, Cloze, and Completion Tasks; 3.1.1 Language Modeling (claim collegato alla sezione «Modello e sistema» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-31-CODE

- Affermazione esatta: lo snippet snip_31_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_31_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
