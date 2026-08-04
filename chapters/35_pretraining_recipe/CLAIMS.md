# Registro dei claim. Capitolo 35

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-35-01

- Affermazione esatta: Packing, padding e mask determinano quanti token validi contribuiscono alla loss.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Batch di token».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-35-02

- Affermazione esatta: Scala dei pesi e residual deve restare coerente con profondità, norm e dtype.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Inizializzazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-35-03

- Affermazione esatta: Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «AdamW».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-35-04

- Affermazione esatta: Il learning rate dipende da step o token e deve riprendere dal contatore corretto.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Warmup e schedule».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-35-05

- Affermazione esatta: Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Checkpoint e recovery».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-35-CODE

- Affermazione esatta: `snip_35_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_35_contract.py, code/test_35_contract.py e code/outputs/SNIP-35-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
