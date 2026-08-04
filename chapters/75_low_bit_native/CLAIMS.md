# Registro dei claim. Capitolo 75

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-75-01

- Affermazione esatta: Un modello low-bit nativo incorpora il formato ridotto nella ricetta, invece di comprimere un checkpoint floating point al termine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Training nativo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-75-02

- Affermazione esatta: BitNet b1.58 usa pesi in {-1,0,1} con attivazioni e scaling specifici. Il numero medio di bit non descrive da solo il kernel.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Pesi ternari e 1.58-bit».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-75-03

- Affermazione esatta: Operazioni discrete usano gradienti surrogati. La derivata applicata nel backward non è la derivata classica della quantizzazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Straight-through estimator».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-75-04

- Affermazione esatta: Prodotti low-bit possono accumulare in precisione maggiore. Storage, compute e accumulator dtype devono essere separati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Accumulazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-75-05

- Affermazione esatta: Il vantaggio richiede kernel, packing e unità aritmetiche che sfruttino il formato. Benchmark su hardware non ottimizzato possono nasconderlo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-75-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Co-design hardware».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-75-CODE

- Affermazione esatta: `snip_75_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_75_contract.py, code/test_75_contract.py e code/outputs/SNIP-75-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
