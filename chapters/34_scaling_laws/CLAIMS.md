# Registro dei claim. Capitolo 34

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-34-01

- Affermazione esatta: Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Fit empirico».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-34-02

- Affermazione esatta: A budget fissato, modello e token competono. Il risultato dipende da ricetta e qualità dei dati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Allocazione compute-optimal».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-34-03

- Affermazione esatta: Configurazioni con compute simile rendono osservabile la loss minima per budget.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Esperimenti isoFLOP».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-34-04

- Affermazione esatta: Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Extrapolation».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-34-05

- Affermazione esatta: Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Training e inference cost».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-34-CODE

- Affermazione esatta: `snip_34_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_34_contract.py, code/test_34_contract.py e code/outputs/SNIP-34-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
