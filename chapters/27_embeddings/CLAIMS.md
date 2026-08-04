# Registro dei claim. Capitolo 27

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-27-01

- Affermazione esatta: Una embedding table seleziona una riga per token. La dimensione del vettore è una scelta architetturale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Da ID a vettore».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-27-02

- Affermazione esatta: Word2vec e GloVe usano statistiche distributive con obiettivi differenti. Similarità geometrica riflette dati e obiettivo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Word embedding».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-27-03

- Affermazione esatta: In un Transformer, la rappresentazione di un token cambia con il contesto. La stessa stringa può produrre vettori diversi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Embedding contestuale».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-27-04

- Affermazione esatta: Pooling o training contrastivo producono vettori per frasi e documenti. La metrica deve corrispondere all'uso previsto.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sentence embedding».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-27-05

- Affermazione esatta: Cosine similarity è una convenzione, non una misura universale di significato. Normalizzazione e distribuzione dello spazio influenzano il ranking.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-27-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Ricerca e anisotropia».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-27-CODE

- Affermazione esatta: `snip_27_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_27_contract.py, code/test_27_contract.py e code/outputs/SNIP-27-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
