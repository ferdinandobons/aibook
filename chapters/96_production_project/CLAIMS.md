# Registro dei claim. Capitolo 96

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-96-01

- Affermazione esatta: Use case, utenti, output, autorizzazioni e costi degli errori precedono la scelta del modello.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-96-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Definizione del problema».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-96-02

- Affermazione esatta: Modello, retrieval, tool, storage e policy sono separati da interfacce e schemi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-96-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Architettura».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-96-03

- Affermazione esatta: Dataset offline, test end-to-end, canary e monitoraggio coprono livelli differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-96-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Valutazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-96-04

- Affermazione esatta: Versioni, secret, rollback, observability e incident response vengono esercitati prima del traffico reale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-96-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Deployment».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-96-05

- Affermazione esatta: Model card, data card, runbook e decision log rendono il progetto revisionabile e aggiornabile.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-96-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Documentazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-96-CODE

- Affermazione esatta: `snip_96_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo. Il laboratorio esteso usa code/production_pipeline.py, code/test_production_pipeline.py e code/outputs/PRODUCTION-PIPELINE.txt.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_96_contract.py, code/test_96_contract.py e code/outputs/SNIP-96-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
