# Registro dei claim. Capitolo 21

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-21-01

- Affermazione esatta: La chain rule scompone la probabilità con un ordine. Ogni fattore condiziona sugli elementi precedenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Fattorizzare una sequenza».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-21-02

- Affermazione esatta: Durante il training il modello riceve il prefisso reale e predice il passo successivo. Durante la generazione riceve anche i propri output.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Teacher forcing».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-21-03

- Affermazione esatta: La causal mask impedisce a una posizione di usare target futuri. Un errore nella maschera produce leakage pur con loss numericamente valida.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Maschera causale».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-21-04

- Affermazione esatta: Ogni scelta modifica il contesto successivo. Errori iniziali possono spostare la traiettoria verso regioni poco viste nel training.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sampling e accumulo degli errori».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-21-05

- Affermazione esatta: L'autoregressione non è limitata al testo. Una sequenza può rappresentare pixel, code audio o latent discreti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Immagini, audio e token discreti».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-21-CODE

- Affermazione esatta: `snip_21_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_21_contract.py, code/test_21_contract.py e code/outputs/SNIP-21-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
