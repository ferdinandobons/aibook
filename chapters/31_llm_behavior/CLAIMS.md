# Registro dei claim. Capitolo 31

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-31-01

- Affermazione esatta: Un LLM autoregressivo produce logits condizionati sul prefisso. La softmax costruisce una distribuzione, non una risposta già scelta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Distribuzione del token successivo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-31-02

- Affermazione esatta: Istruzioni ed esempi entrano nel contesto senza un optimizer step. Il checkpoint resta invariato durante in-context learning.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Prompt e dimostrazioni».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-31-03

- Affermazione esatta: Greedy, sampling, temperature e truncation trasformano la distribuzione in una traiettoria.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Decoding».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-31-04

- Affermazione esatta: Probabilità del token, confidenza espressa e correttezza fattuale sono quantità differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Calibrazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-31-05

- Affermazione esatta: Post-training, messaggi di sistema, strumenti e filtri contribuiscono al comportamento osservato.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-31-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Modello e sistema».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-31-CODE

- Affermazione esatta: `snip_31_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_31_contract.py, code/test_31_contract.py e code/outputs/SNIP-31-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
