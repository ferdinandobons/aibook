# Registro dei claim. Capitolo 89

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `injection` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-89-01

- Affermazione esatta: Contenuti recuperati, pagine e documenti sono dati non fidati. Non devono acquisire automaticamente la priorità delle istruzioni di sistema.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3. Attack Surface of LLM-Integrated Applications; 3.2.1. Attacks’ Targets.; 5.3. Other Attack Directions (claim collegato alla sezione «Istruzioni e dati» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-89-02

- Affermazione esatta: Una istruzione malevola può essere inserita in una fonte consultata dall'agente e attivarsi durante il retrieval o il browsing.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents; Benchmarking agents and prompt injections.; 3 Designing and Constructing AgentDojo (claim collegato alla sezione «Indirect prompt injection» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-89-03

- Affermazione esatta: Policy esterne validano tool, argomenti e destinazioni. Il modello propone, ma l'enforcement avviene fuori dal testo generato.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; OWASP Top 10 for Large Language Model Applications; About This Repository; OWASP GenAI Security Project (claim collegato alla sezione «Tool mediation» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-89-04

- Affermazione esatta: Segreti, memoria e risultati dei tool devono essere separati per scope. Output e URL possono diventare canali di esfiltrazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; AI Risk Management Framework; Quick Links; Overview of the AI RMF (claim collegato alla sezione «Data exfiltration» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-89-05

- Affermazione esatta: Canary, trace, allowlist, conferme e revoca delle credenziali supportano rilevamento, contenimento e recovery.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3. Attack Surface of LLM-Integrated Applications; 3.2.1. Attacks’ Targets.; 5.3. Other Attack Directions (claim collegato alla sezione «Test e incident response» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-89-CODE

- Affermazione esatta: lo snippet snip_89_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_89_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
