# Registro dei claim. Capitolo 72

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `agent_safety` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-72-01

- Affermazione esatta: Ogni tool riceve soltanto gli scope necessari. Credenziali e filesystem devono essere separati per task e tenant.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents; Benchmarking agents and prompt injections.; 3 Designing and Constructing AgentDojo (claim collegato alla sezione «Least privilege» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-72-02

- Affermazione esatta: Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; OWASP Top 10 for Large Language Model Applications; About This Repository; OWASP GenAI Security Project (claim collegato alla sezione «Sandbox» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-72-03

- Affermazione esatta: Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3. Attack Surface of LLM-Integrated Applications; 3.2.1. Attacks’ Targets.; 5.3. Other Attack Directions (claim collegato alla sezione «Human approval» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-72-04

- Affermazione esatta: Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; AI Risk Management Framework; Quick Links; Overview of the AI RMF (claim collegato alla sezione «Rollback e audit» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-72-05

- Affermazione esatta: Contenuti esterni possono tentare di cambiare il piano. Dati non fidati e istruzioni di sistema devono restare separati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents; Benchmarking agents and prompt injections.; 3 Designing and Constructing AgentDojo (claim collegato alla sezione «Prompt injection» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-72-CODE

- Affermazione esatta: lo snippet snip_72_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_72_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
