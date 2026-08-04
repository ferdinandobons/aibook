# Registro dei claim. Capitolo 71

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-71-01

- Affermazione esatta: Osservazioni, azioni, tool result e reward formano esempi sequenziali. Logging incompleto rende impossibile ricostruire il fallimento.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Traiettorie come dati».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-71-02

- Affermazione esatta: Traiettorie riuscite possono essere imitate. Il dataset deve includere recovery, errori e decisioni di non agire.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Imitation e SFT».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-71-03

- Affermazione esatta: Reward verificabili o simulati aggiornano policy multi-step. Il modello può sfruttare bug dell'ambiente o del checker.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «RL in ambienti».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-71-04

- Affermazione esatta: Success rate, step, costo e side effect devono essere misurati. Task statici rischiano contaminazione e overfitting.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Benchmark agentici».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-71-05

- Affermazione esatta: Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Evaluation harness».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-71-CODE

- Affermazione esatta: `snip_71_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_71_contract.py, code/test_71_contract.py e code/outputs/SNIP-71-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
