# Registro dei claim. Capitolo 23

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-23-01

- Affermazione esatta: Il generatore produce campioni; il discriminatore distingue dati reali e generati. L'obiettivo è un gioco, non una loss singola ottimizzata congiuntamente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-23-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Un gioco tra due modelli».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-23-02

- Affermazione esatta: La formulazione originale è collegata alla Jensen-Shannon divergence sotto un discriminatore ottimo. I gradienti pratici dipendono dalla loss scelta.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-23-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Divergenze e gradienti».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-23-03

- Affermazione esatta: Il generatore può produrre poche modalità convincenti. Diversità e fedeltà devono essere misurate separatamente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-23-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Mode collapse».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-23-04

- Affermazione esatta: WGAN usa una distanza legata a funzioni Lipschitz. Weight clipping e gradient penalty sono implementazioni differenti del vincolo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-23-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Wasserstein GAN».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-23-05

- Affermazione esatta: Bilanciare update, normalizzazioni e capacità è essenziale. FID è una metrica su feature e non sostituisce l'analisi dei campioni.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-23-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Stabilità e valutazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-23-CODE

- Affermazione esatta: `snip_23_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_23_contract.py, code/test_23_contract.py e code/outputs/SNIP-23-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
