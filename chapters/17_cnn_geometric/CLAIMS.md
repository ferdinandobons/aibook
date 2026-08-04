# Registro dei claim. Capitolo 17

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-17-01

- Affermazione esatta: Una convoluzione applica lo stesso kernel in posizioni differenti. Questa condivisione incorpora una ipotesi di regolarità locale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Condivisione locale dei pesi».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-17-02

- Affermazione esatta: Stride e padding determinano la griglia dell'output. Il receptive field cresce con layer, kernel e dilatazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Stride, padding e receptive field».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-17-03

- Affermazione esatta: La convoluzione è equivariant a traslazioni entro le condizioni del bordo. Pooling e aggregazione possono costruire una maggiore invariance.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Equivarianza e invariance».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-17-04

- Affermazione esatta: Patch embedding e attention offrono una geometria diversa. CNN e Transformer possono essere combinati, ma il confronto richiede stesso budget e dati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Vision Transformer e ibridi».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-17-05

- Affermazione esatta: Su un grafo, i vicini non sono disposti in una griglia regolare. Le GNN aggregano messaggi rispettando la struttura degli archi e le simmetrie dichiarate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Grafi e message passing».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-17-CODE

- Affermazione esatta: `snip_17_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_17_contract.py, code/test_17_contract.py e code/outputs/SNIP-17-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
