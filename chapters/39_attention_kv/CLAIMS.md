# Registro dei claim. Capitolo 39

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-39-01

- Affermazione esatta: Ogni query head possiede key e value dedicate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «MHA».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-39-02

- Affermazione esatta: Tutte le query head condividono una singola coppia key-value, riducendo la cache.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «MQA».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-39-03

- Affermazione esatta: Gruppi di query head condividono un numero intermedio di KV head.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «GQA».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-39-04

- Affermazione esatta: Finestre e pattern selezionati riducono le coppie ma cambiano la connettività.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Local e sparse attention».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-39-05

- Affermazione esatta: Compressione latente e numero di KV head sono strategie differenti. La memoria dipende anche da layer, dtype, batch e lunghezza.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-39-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «MLA e cache».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-39-CODE

- Affermazione esatta: `snip_39_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_39_contract.py, code/test_39_contract.py e code/outputs/SNIP-39-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
