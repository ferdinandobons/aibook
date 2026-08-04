# Registro dei claim. Capitolo 82

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `llmops` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-82-01

- Affermazione esatta: Checkpoint, tokenizer, adapter, prompt e tool schema devono essere versionati come un'unica release di sistema.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Hidden Technical Debt in Machine Learning Systems (claim collegato alla sezione «Dalla versione al deployment» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-82-02

- Affermazione esatta: Log, trace, metriche e feedback collegano input, modello, retrieval, tool e output senza esporre dati oltre il necessario.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; AI Risk Management Framework; Quick Links; Overview of the AI RMF (claim collegato alla sezione «Osservabilità» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-82-03

- Affermazione esatta: Dispositivi locali impongono memoria, batteria, termica e compatibilità dei kernel. Offline e privacy possono motivare il deployment locale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract; sections on model cards and reporting context (claim collegato alla sezione «Edge» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: publisher metadata and official article record opened via web research; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-82-04

- Affermazione esatta: Costo per token, richiesta, utente e risultato utile sono metriche differenti. Cache e batching modificano l'allocazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Green AI; 1 Introduction and Motivation; 2 Red AI (claim collegato alla sezione «Costo» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-82-05

- Affermazione esatta: Potenza, tempo, utilizzo hardware e mix energetico influenzano l'impatto. Stime devono dichiarare confini e metodologia.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Hidden Technical Debt in Machine Learning Systems (claim collegato alla sezione «Energia e sostenibilità» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-82-CODE

- Affermazione esatta: lo snippet snip_82_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_82_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
