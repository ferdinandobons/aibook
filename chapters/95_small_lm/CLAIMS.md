# Registro dei claim. Capitolo 95

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-95-01

- Affermazione esatta: Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-95-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Corpus e tokenizer».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-95-02

- Affermazione esatta: Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-95-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Decoder Transformer».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-95-03

- Affermazione esatta: AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-95-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Training».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-95-04

- Affermazione esatta: Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-95-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sampling».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-95-05

- Affermazione esatta: Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-95-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Limiti».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-95-CODE

- Affermazione esatta: `snip_95_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo. Il laboratorio esteso usa code/tiny_transformer_lm.py, code/test_tiny_transformer_lm.py e code/outputs/TINY-TRANSFORMER-LM.txt.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_95_contract.py, code/test_95_contract.py e code/outputs/SNIP-95-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
