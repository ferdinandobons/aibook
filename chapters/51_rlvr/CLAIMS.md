# Registro dei claim. Capitolo 51

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-51-01

- Affermazione esatta: Problemi con risposta controllabile, come codice o matematica, consentono reward da test, parser o esecutori.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Reward verificabile».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-51-02

- Affermazione esatta: La policy genera più soluzioni per la stessa richiesta. Il reward confronta traiettorie e costruisce advantage o ranking.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Rollout e gruppi».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-51-03

- Affermazione esatta: Algoritmi group-relative normalizzano reward all'interno di gruppi e aggiornano log-probability con vincoli di stabilità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «GRPO e policy update».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-51-04

- Affermazione esatta: Un risultato finale corretto non identifica quali passaggi siano utili. Exploration, curriculum e shaping cambiano la densità del segnale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sparse reward».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-51-05

- Affermazione esatta: Un test incompleto può premiare exploit. Il reward verificabile è affidabile soltanto nel perimetro del verificatore.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-51-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Verificabilità limitata».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-51-CODE

- Affermazione esatta: `snip_51_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_51_contract.py, code/test_51_contract.py e code/outputs/SNIP-51-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
