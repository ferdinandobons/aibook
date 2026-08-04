# Registro dei claim. Capitolo 25

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-25-01

- Affermazione esatta: La diffusione forward aggiunge rumore secondo uno schedule. Il modello impara a invertire o a stimare una quantità equivalente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Corrompere e ricostruire».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-25-02

- Affermazione esatta: Lo score è il gradiente del log-density rispetto ai dati perturbati. Denoising score matching evita di conoscere la densità normale completa.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Score matching».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-25-03

- Affermazione esatta: Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambiano scala e weighting del training.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Parametrizzazioni epsilon, x0 e v».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-25-04

- Affermazione esatta: DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti. Meno step non garantiscono stessa distribuzione o qualità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sampler».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-25-05

- Affermazione esatta: Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni. Rectified flow cerca traiettorie più rettilinee in setup specifici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-25-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Flow matching e rectified flow».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-25-CODE

- Affermazione esatta: `snip_25_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_25_contract.py, code/test_25_contract.py e code/outputs/SNIP-25-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
