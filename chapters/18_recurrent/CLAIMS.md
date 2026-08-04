# Registro dei claim. Capitolo 18

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-18-01

- Affermazione esatta: Una RNN aggiorna uno stato nascosto con input e stato precedente. Lo stesso insieme di parametri viene riutilizzato a ogni passo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Uno stato che attraversa la sequenza».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-18-02

- Affermazione esatta: Il grafo ricorrente viene srotolato nel tempo. Gradienti molto lunghi possono svanire o esplodere.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Backpropagation through time».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-18-03

- Affermazione esatta: Gate di input, forget e output controllano il flusso della memoria. GRU usa una parametrizzazione più compatta, con un contratto differente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «LSTM e GRU».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-18-04

- Affermazione esatta: Una rete bidirezionale usa anche il futuro ed è adatta a encoding offline. Non può essere usata direttamente per generazione causale streaming.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Bidirezionalità e causalità».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-18-05

- Affermazione esatta: La recurrence mantiene memoria compatta; l'attention accede a rappresentazioni esplicite. I due meccanismi possono essere complementari.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «RNN, attention e stato».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-18-CODE

- Affermazione esatta: `snip_18_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_18_contract.py, code/test_18_contract.py e code/outputs/SNIP-18-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
