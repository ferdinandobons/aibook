# Registro dei claim. Capitolo 64

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-64-01

- Affermazione esatta: Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Una pipeline in due fasi».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-64-02

- Affermazione esatta: Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Un chunk non coincide sempre con una unità semantica.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Chunking».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-64-03

- Affermazione esatta: Documenti, istruzioni e domanda devono avere confini espliciti. Il modello può ignorare, confondere o citare in modo scorretto il contesto.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Prompt con fonti».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-64-04

- Affermazione esatta: Una risposta supportata deve essere collegabile a passaggi recuperati. Citazione presente e citazione corretta sono controlli differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Attribution».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-64-05

- Affermazione esatta: Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-64-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Valutazione end-to-end».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-64-CODE

- Affermazione esatta: `snip_64_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_64_contract.py, code/test_64_contract.py e code/outputs/SNIP-64-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
