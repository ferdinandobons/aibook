# Registro dei claim. Capitolo 94

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-94-01

- Affermazione esatta: Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-94-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Ambiente riproducibile».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-94-02

- Affermazione esatta: Un dataset controllabile permette di vedere preprocessing, split, batch e leakage.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-94-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Dataset piccolo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-94-03

- Affermazione esatta: Una baseline lineare precede la rete. Shape, logits e loss vengono verificati con test.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-94-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Modello e loss».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-94-04

- Affermazione esatta: Curve, checkpoint, validation e test seguono il protocollo costruito nel libro.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-94-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Training e valutazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-94-05

- Affermazione esatta: Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-94-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Report».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-94-CODE

- Affermazione esatta: `snip_94_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo. Il laboratorio esteso usa code/foundations_lab.py, code/test_foundations_lab.py e code/outputs/FOUNDATIONS-LAB.txt.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_94_contract.py, code/test_94_contract.py e code/outputs/SNIP-94-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
