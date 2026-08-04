# Registro dei claim. Capitolo 74

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-74-01

- Affermazione esatta: Una mappa affine converte valori floating point in interi. La granularità per tensor o per channel cambia scale, errore e metadati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Scala e zero point».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-74-02

- Affermazione esatta: Post-training quantization usa calibration senza riaddestrare completamente. La rappresentatività dei dati di calibration è essenziale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «PTQ».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-74-03

- Affermazione esatta: Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «QAT».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-74-04

- Affermazione esatta: Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-003; SRC-74-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Weight-only e activation quantization».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-74-05

- Affermazione esatta: GPTQ, AWQ e SmoothQuant ottimizzano oggetti differenti: ricostruzione, canali salienti e outlier delle attivazioni. I loro contratti non sono intercambiabili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-74-004; SRC-74-003; SRC-74-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Metodi per LLM».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-74-CODE

- Affermazione esatta: `snip_74_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_74_contract.py, code/test_74_contract.py e code/outputs/SNIP-74-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
