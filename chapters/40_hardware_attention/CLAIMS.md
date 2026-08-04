# Registro dei claim. Capitolo 40

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-40-01

- Affermazione esatta: Lo stesso operatore può avere traffico di memoria molto diverso.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «FLOP e movimento dei dati».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-40-02

- Affermazione esatta: Blocchi di Q, K e V vengono elaborati nella memoria on-chip senza materializzare tutti gli score.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Tiling».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-40-03

- Affermazione esatta: Massimo, denominatore e numeratore vengono aggiornati blocco per blocco.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Softmax online».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-40-04

- Affermazione esatta: Salvare meno intermedi scambia memoria con compute aggiuntivo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Backward e ricomputazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-40-05

- Affermazione esatta: FlashAttention, backend memory-efficient e math rispettano la stessa API entro tolleranze numeriche e condizioni diverse.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-40-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Backend».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-40-CODE

- Affermazione esatta: `snip_40_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_40_contract.py, code/test_40_contract.py e code/outputs/SNIP-40-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
