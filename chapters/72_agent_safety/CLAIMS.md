# Registro dei claim. Capitolo 72

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-72-01

- Affermazione esatta: Ogni tool riceve soltanto gli scope necessari. Credenziali e filesystem devono essere separati per task e tenant.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Least privilege».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-72-02

- Affermazione esatta: Codice e browser vengono eseguiti in ambienti isolati con rete, processi e risorse limitate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sandbox».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-72-03

- Affermazione esatta: Azioni ad alto impatto richiedono conferma con anteprima, differenza e destinatario espliciti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Human approval».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-72-04

- Affermazione esatta: Transaction log, snapshot e operazioni compensative permettono di ricostruire e correggere una traiettoria.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Rollback e audit».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-72-05

- Affermazione esatta: Contenuti esterni possono tentare di cambiare il piano. Dati non fidati e istruzioni di sistema devono restare separati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-72-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Prompt injection».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-72-CODE

- Affermazione esatta: `snip_72_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_72_contract.py, code/test_72_contract.py e code/outputs/SNIP-72-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
