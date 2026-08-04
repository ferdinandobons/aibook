# Registro dei claim. Capitolo 44

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-44-01

- Affermazione esatta: Un router assegna probabilità agli esperti e attiva un sottoinsieme per token.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Router top-k».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-44-02

- Affermazione esatta: Ogni esperto riceve un limite di token. Overflow, rerouting o dropping devono essere dichiarati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Capacità».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-44-03

- Affermazione esatta: Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Load balancing».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-44-04

- Affermazione esatta: Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Expert parallelism».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-44-05

- Affermazione esatta: Un MoE può avere molti parametri totali e pochi parametri attivi per token. FLOP, memoria e comunicazione vanno riportati separatamente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Parametri totali e attivi».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-44-CODE

- Affermazione esatta: `snip_44_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_44_contract.py, code/test_44_contract.py e code/outputs/SNIP-44-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
