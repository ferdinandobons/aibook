# Registro dei claim. Capitolo 91

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-91-01

- Affermazione esatta: Un modello può riprodurre sequenze rare. Membership inference e extraction misurano rischi differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-91-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Memorizzazione e leakage».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-91-02

- Affermazione esatta: DP limita l'influenza di un record mediante clipping e rumore, con parametri epsilon e delta e un costo di utilità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-91-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Differential privacy».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-91-03

- Affermazione esatta: Metriche di parità, equalized odds e calibration possono essere incompatibili sotto distribuzioni differenti. Il contesto decisionale guida la scelta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-91-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Fairness».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-91-04

- Affermazione esatta: Rappresentazione, label, soglie e policy possono produrre disparità anche con lo stesso modello.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-91-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Bias nei dati e nel sistema».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-91-05

- Affermazione esatta: Rimuovere l'influenza di dati richiede un criterio e una verifica. Cancellare un record dal corpus non modifica automaticamente il checkpoint.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-91-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Machine unlearning».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-91-CODE

- Affermazione esatta: `snip_91_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_91_contract.py, code/test_91_contract.py e code/outputs/SNIP-91-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
