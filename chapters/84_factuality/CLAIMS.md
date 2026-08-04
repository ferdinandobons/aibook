# Registro dei claim. Capitolo 84

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-84-01

- Affermazione esatta: Una frase può essere vera senza essere sostenuta dal contesto fornito, oppure fedele al contesto ma riferita a una fonte errata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-84-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Correttezza e supporto».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-84-02

- Affermazione esatta: Il termine copre errori diversi: entità inventate, attribuzioni scorrette, contraddizioni e citazioni inesistenti. La tassonomia deve precedere la metrica.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-84-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Hallucination».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-84-03

- Affermazione esatta: Probabilità del token, score di un verifier e frequenza empirica devono essere collegati con un protocollo di calibrazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-84-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Calibrazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-84-04

- Affermazione esatta: Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. Coverage e accuracy conditional vanno riportate insieme.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-84-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Astensione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-84-05

- Affermazione esatta: Fonti esterne possono aumentare supporto, ma retrieval e generazione hanno failure mode separati. La provenienza deve restare tracciabile.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-84-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Verifica e retrieval».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-84-CODE

- Affermazione esatta: `snip_84_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_84_contract.py, code/test_84_contract.py e code/outputs/SNIP-84-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
