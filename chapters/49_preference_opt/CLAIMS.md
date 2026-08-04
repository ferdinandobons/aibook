# Registro dei claim. Capitolo 49

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-49-01

- Affermazione esatta: DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Evitare un reward model esplicito».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-49-02

- Affermazione esatta: Ogni esempio richiede la stessa condizione e due risposte confrontabili. Errori o stili spurii possono diventare scorciatoie.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Coppie chosen e rejected».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-49-03

- Affermazione esatta: Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Temperatura beta».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-49-04

- Affermazione esatta: Le varianti cambiano assunzioni, forma della loss o tipo di feedback. I nomi non rendono gli obiettivi intercambiabili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «IPO, KTO, ORPO e varianti».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-49-05

- Affermazione esatta: L'ottimizzazione resta limitata alla copertura del dataset. Nuove policy possono visitare risposte non rappresentate nelle coppie.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Offline preference data».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-49-CODE

- Affermazione esatta: `snip_49_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_49_contract.py, code/test_49_contract.py e code/outputs/SNIP-49-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
