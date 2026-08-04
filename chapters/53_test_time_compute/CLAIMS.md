# Registro dei claim. Capitolo 53

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-53-01

- Affermazione esatta: Il sistema può generare più candidate, approfondire una traiettoria o usare ricerca prima di restituire la risposta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Più compute dopo il training».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-53-02

- Affermazione esatta: Un proposer genera n candidate e un verifier seleziona. Il beneficio dipende dalla diversità e dalla qualità del ranking.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Best-of-n».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-53-03

- Affermazione esatta: Stati parziali vengono espansi, valutati e potati. Branching factor, profondità e budget definiscono il costo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Tree search».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-53-04

- Affermazione esatta: Problemi differenti ricevono budget differenti secondo confidenza, difficoltà o policy. La stima di difficoltà può essere errata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Adaptive compute».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-53-05

- Affermazione esatta: Accuracy o reward devono essere riportati insieme a token, forward, latenza e fallimenti del verifier.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-53-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Metriche costo-qualità».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-53-CODE

- Affermazione esatta: `snip_53_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_53_contract.py, code/test_53_contract.py e code/outputs/SNIP-53-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
