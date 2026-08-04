# Registro dei claim. Capitolo 82

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-82-01

- Affermazione esatta: Checkpoint, tokenizer, adapter, prompt e tool schema devono essere versionati come un'unica release di sistema.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Dalla versione al deployment».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-82-02

- Affermazione esatta: Log, trace, metriche e feedback collegano input, modello, retrieval, tool e output senza esporre dati oltre il necessario.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Osservabilità».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-82-03

- Affermazione esatta: Dispositivi locali impongono memoria, batteria, termica e compatibilità dei kernel. Offline e privacy possono motivare il deployment locale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Edge».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-82-04

- Affermazione esatta: Costo per token, richiesta, utente e risultato utile sono metriche differenti. Cache e batching modificano l'allocazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Costo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-82-05

- Affermazione esatta: Potenza, tempo, utilizzo hardware e mix energetico influenzano l'impatto. Stime devono dichiarare confini e metodologia.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-82-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Energia e sostenibilità».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-82-CODE

- Affermazione esatta: `snip_82_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_82_contract.py, code/test_82_contract.py e code/outputs/SNIP-82-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
