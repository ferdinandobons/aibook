# Registro dei claim. Capitolo 36

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-36-01

- Affermazione esatta: Repliche elaborano sotto-batch e aggregano gradienti. Media e loss reduction devono essere coerenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Data parallelism».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-36-02

- Affermazione esatta: Parametri, gradienti e optimizer state vengono shardati tra worker.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «ZeRO e FSDP».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-36-03

- Affermazione esatta: Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Tensor e pipeline parallelism».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-36-04

- Affermazione esatta: Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Topologia e fault tolerance».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-36-05

- Affermazione esatta: Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-36-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Continued pretraining».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-36-CODE

- Affermazione esatta: `snip_36_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_36_contract.py, code/test_36_contract.py e code/outputs/SNIP-36-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
