# Registro dei claim. Capitolo 37

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-37-01

- Affermazione esatta: Ogni sottolayer produce un aggiornamento sommato a un percorso identità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Residual stream».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-37-02

- Affermazione esatta: La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Pre-norm e post-norm».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-37-03

- Affermazione esatta: RMSNorm scala usando la media quadratica e non sottrae la media.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «RMSNorm».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-37-04

- Affermazione esatta: Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «SwiGLU».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-37-05

- Affermazione esatta: Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-37-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Ordine e parallelismo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-37-CODE

- Affermazione esatta: `snip_37_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_37_contract.py, code/test_37_contract.py e code/outputs/SNIP-37-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
