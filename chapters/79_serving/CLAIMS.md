# Registro dei claim. Capitolo 79

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-79-01

- Affermazione esatta: Prompt e output hanno lunghezze differenti. Un batch statico spreca slot quando alcune sequenze terminano.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Richieste eterogenee».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-79-02

- Affermazione esatta: Il scheduler inserisce nuove richieste tra iterazioni di decode e rimuove quelle concluse.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Continuous batching».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-79-03

- Affermazione esatta: Aumentare batch migliora utilizzo ma può aumentare time-to-first-token e inter-token latency.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Throughput e latency».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-79-04

- Affermazione esatta: Memoria KV, priorità, deadline e fairness determinano quali richieste entrano nel sistema.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Admission control».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-79-05

- Affermazione esatta: TTFT, TPOT, goodput, queue time, error rate e costo devono essere osservati per tenant e classe di richiesta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-79-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Metriche di servizio».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-79-CODE

- Affermazione esatta: `snip_79_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_79_contract.py, code/test_79_contract.py e code/outputs/SNIP-79-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
