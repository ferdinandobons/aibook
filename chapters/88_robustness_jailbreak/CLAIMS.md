# Registro dei claim. Capitolo 88

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-88-01

- Affermazione esatta: Attaccante, accesso, obiettivo, budget e superficie definiscono il test. Un jailbreak testuale e un attacco ai pesi hanno contratti diversi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-88-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Threat model».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-88-02

- Affermazione esatta: Typo, parafrasi, encoding e contenuti multimodali possono aggirare filtri superficiali.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-88-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Perturbazioni».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-88-03

- Affermazione esatta: Suffix e prompt vengono cercati per aumentare una loss di attacco. Trasferibilità e query budget devono essere riportati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-88-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Ottimizzazione adversarial».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-88-04

- Affermazione esatta: Training, filtri, classificatori e refusal possono ridurre alcuni attacchi e introdurre falsi positivi o nuove bypass.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-88-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Difese».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-88-05

- Affermazione esatta: Una difesa deve essere testata da attaccanti che conoscono il metodo, entro un protocollo sicuro e autorizzato.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-88-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Valutazione adattiva».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-88-CODE

- Affermazione esatta: `snip_88_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_88_contract.py, code/test_88_contract.py e code/outputs/SNIP-88-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
