# Registro dei claim. Capitolo 63

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-63-01

- Affermazione esatta: Un sistema di retrieval ordina documenti rispetto a una query. La rilevanza dipende dal bisogno informativo e dalle label disponibili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Documenti, query e rilevanza».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-63-02

- Affermazione esatta: La ricerca lessicale combina frequenza del termine, rarità nel corpus e normalizzazione della lunghezza. Tokenizzazione e campi modificano il punteggio.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «BM25».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-63-03

- Affermazione esatta: Un bi-encoder mappa query e documenti in vettori e usa una similarità. L'addestramento dipende da positivi, negativi e in-batch sampling.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Dense retrieval».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-63-04

- Affermazione esatta: Approximate nearest neighbor riduce il costo rispetto al confronto esaustivo. Recall, memoria e latenza dipendono dalla struttura e dai parametri.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Indici ANN».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-63-05

- Affermazione esatta: Un cross-encoder valuta coppie query-documento con maggiore interazione, ma viene applicato a un insieme candidato più piccolo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-63-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Reranking».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-63-CODE

- Affermazione esatta: `snip_63_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_63_contract.py, code/test_63_contract.py e code/outputs/SNIP-63-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
