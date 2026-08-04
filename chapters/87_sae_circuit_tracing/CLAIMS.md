# Registro dei claim. Capitolo 87

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-87-01

- Affermazione esatta: Più feature possono condividere le stesse dimensioni di attivazione. La sparsità offre una ipotesi per separarle.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-87-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Superposition».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-87-02

- Affermazione esatta: Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream. Loss e sparsity coefficient determinano il dizionario.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-87-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sparse autoencoder».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-87-03

- Affermazione esatta: Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-87-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Dead e splitting features».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-87-04

- Affermazione esatta: Feature e attribution graph possono collegare input, computazione e output. Il grafo resta una approssimazione del calcolo completo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-87-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Circuit tracing».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-87-05

- Affermazione esatta: Interpretabilità automatica, causal intervention e coverage devono essere misurate. Una etichetta leggibile non prova monosemanticità universale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-87-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Valutazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-87-CODE

- Affermazione esatta: `snip_87_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_87_contract.py, code/test_87_contract.py e code/outputs/SNIP-87-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
