# Registro dei claim. Capitolo 46

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-46-01

- Affermazione esatta: Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-46-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Dal pretraining alle istruzioni».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-46-02

- Affermazione esatta: Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-46-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Formati conversazionali».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-46-03

- Affermazione esatta: Compiti e domini vengono mescolati con pesi espliciti. La quantità di esempi non coincide automaticamente con il loro contributo utile.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-46-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Instruction mixture».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-46-04

- Affermazione esatta: Durante il training il modello vede il prefisso corretto. La capacità di seguire istruzioni nuove deve essere valutata su template e domini separati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-46-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Teacher forcing e generalizzazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-46-05

- Affermazione esatta: Learning rate, durata e replay influenzano la perdita di capacità precedenti. Base model, modello SFT e sistema devono restare identificabili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-46-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Catastrophic forgetting e controllo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-46-CODE

- Affermazione esatta: `snip_46_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_46_contract.py, code/test_46_contract.py e code/outputs/SNIP-46-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
