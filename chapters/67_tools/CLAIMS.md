# Registro dei claim. Capitolo 67

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `tools` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-67-01

- Affermazione esatta: JSON Schema, grammar o tipi stabiliscono campi e vincoli. Validità sintattica non garantisce correttezza semantica.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-67-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Toolformer: Language Models Can Teach Themselves to Use Tools; 3 Tools; Appendix A API Details (claim collegato alla sezione «Schema dell'output» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-67-02

- Affermazione esatta: Il modello sceglie una funzione tra opzioni descritte. Nomi, descrizioni e autorizzazioni influenzano la decisione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-67-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; D.2.3 ReAct-IM trajectory (claim collegato alla sezione «Selezione del tool» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-67-03

- Affermazione esatta: Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione. Campi mancanti richiedono chiarimento o fallback.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-67-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Gorilla: Large Language Model Connected with Massive APIs; 3.3 Verifying APIs; 4.1 AST Accuracy on API call (claim collegato alla sezione «Argomenti» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-67-04

- Affermazione esatta: Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato. Timeout ed errori devono essere rappresentati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-67-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs; 2.1 API Collection; 3.3 Out-of-Distribution (OOD) Generalization to APIBench (Patil et al., 2023 ) (claim collegato alla sezione «Esecuzione e osservazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-67-05

- Affermazione esatta: Operazioni di lettura e scrittura hanno rischi differenti. Conferma, deduplicazione e transaction ID impediscono ripetizioni non desiderate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-67-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Toolformer: Language Models Can Teach Themselves to Use Tools; 3 Tools; Appendix A API Details (claim collegato alla sezione «Idempotenza e side effect» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-67-CODE

- Affermazione esatta: lo snippet snip_67_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_67_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
