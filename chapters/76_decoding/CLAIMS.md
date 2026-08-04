# Registro dei claim. Capitolo 76

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-76-01

- Affermazione esatta: Greedy sceglie il massimo locale; beam mantiene più prefissi secondo score accumulati e criteri di lunghezza.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Greedy e beam search».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-76-02

- Affermazione esatta: Temperature, top-k e top-p modificano la distribuzione prima dell'estrazione. Seed e backend influenzano la riproducibilità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sampling».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-76-03

- Affermazione esatta: Repetition penalty, stop sequence e minimum length intervengono in punti differenti e possono interagire.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Penalità e stop».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-76-04

- Affermazione esatta: Grammar, automi e schema limitano i token ammessi. Validità strutturale non garantisce argomenti corretti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Constrained decoding».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-76-05

- Affermazione esatta: Qualità, diversità, latency, token per secondo e probabilità della sequenza devono essere letti insieme.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Metriche».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-76-CODE

- Affermazione esatta: `snip_76_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_76_contract.py, code/test_76_contract.py e code/outputs/SNIP-76-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
