# Registro dei claim. Capitolo 61

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-61-01

- Affermazione esatta: Una scena 3D richiede sistemi di riferimento, intrinseci ed estrinseci della camera. Errori di coordinate cambiano il rendering.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Coordinate e camera».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-61-02

- Affermazione esatta: Una funzione neurale mappa posizione e direzione a densità e colore. Volume rendering integra campioni lungo i raggi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «NeRF».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-61-03

- Affermazione esatta: Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Gaussian splatting».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-61-04

- Affermazione esatta: Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Mesh, point cloud e voxel».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-61-05

- Affermazione esatta: Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Generazione e grounding spaziale».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-61-CODE

- Affermazione esatta: `snip_61_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_61_contract.py, code/test_61_contract.py e code/outputs/SNIP-61-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
