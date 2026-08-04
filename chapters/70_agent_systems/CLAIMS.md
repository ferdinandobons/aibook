# Registro dei claim. Capitolo 70

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-70-01

- Affermazione esatta: L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da istruzioni autorizzate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-70-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Browser agent».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-70-02

- Affermazione esatta: Screenshot, coordinate e azioni di input formano un loop percettivo. Risoluzione, focus e stato dell'interfaccia possono cambiare.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-70-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Computer use».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-70-03

- Affermazione esatta: Repository, test, shell e diff definiscono l'ambiente. Modifiche devono essere limitate, testate e revisionabili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-70-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Code agent».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-70-04

- Affermazione esatta: Ruoli distinti possono parallelizzare o criticare, ma introducono comunicazione, ridondanza e propagazione degli errori.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-70-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Multi-agent».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-70-05

- Affermazione esatta: Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-70-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Confronto con un singolo workflow».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-70-CODE

- Affermazione esatta: `snip_70_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_70_contract.py, code/test_70_contract.py e code/outputs/SNIP-70-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
