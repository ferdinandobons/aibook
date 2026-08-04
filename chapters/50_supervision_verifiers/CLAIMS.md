# Registro dei claim. Capitolo 50

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-50-01

- Affermazione esatta: Outcome supervision assegna un segnale alla risposta finale e non localizza necessariamente il passaggio che ha prodotto l'errore.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-50-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Supervisionare il risultato».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-50-02

- Affermazione esatta: Process supervision etichetta passaggi intermedi. La validità dipende da come il processo viene reso osservabile e annotato.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-50-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Supervisionare il processo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-50-03

- Affermazione esatta: Un verifier valuta candidate rispetto a un criterio. Può essere una regola, un esecutore, un modello o una combinazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-50-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Verifier».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-50-04

- Affermazione esatta: Punteggi per step possono guidare ricerca e training, ma possono introdurre preferenze per forme superficiali del ragionamento.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-50-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Reward model di processo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-50-05

- Affermazione esatta: Ottimizzare contro lo stesso verifier usato per la valutazione favorisce overfitting. Servono test e verificatori indipendenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-50-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Goodhart e indipendenza».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-50-CODE

- Affermazione esatta: `snip_50_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_50_contract.py, code/test_50_contract.py e code/outputs/SNIP-50-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
