# Registro dei claim. Capitolo 81

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-81-01

- Affermazione esatta: Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Grafo e operatori».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-81-02

- Affermazione esatta: Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Kernel fusion».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-81-03

- Affermazione esatta: Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Triton e kernel custom».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-81-04

- Affermazione esatta: Tracing e guard permettono specializzazione dinamica. Python side effect o shape non supportate producono graph break.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «torch.compile e graph break».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-81-05

- Affermazione esatta: Tile, num warps e schedule ottimali dipendono dall'hardware. Un kernel corretto richiede test numerici e benchmark separati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-81-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Autotuning e portabilità».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-81-CODE

- Affermazione esatta: `snip_81_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_81_contract.py, code/test_81_contract.py e code/outputs/SNIP-81-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
