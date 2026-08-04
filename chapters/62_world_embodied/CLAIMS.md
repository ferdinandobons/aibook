# Registro dei claim. Capitolo 62

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-62-01

- Affermazione esatta: Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-62-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Modello della dinamica».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-62-02

- Affermazione esatta: Traiettorie candidate vengono simulate e valutate prima di agire. Errori del modello possono essere sfruttati dal planner.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-62-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Planning nel modello».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-62-03

- Affermazione esatta: Un agente fisico collega camera, propriocezione, linguaggio e coordinate. Latenza e calibrazione influenzano ogni azione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-62-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Embodied perception».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-62-04

- Affermazione esatta: VLA mappa osservazioni e istruzioni a token o controlli di azione. Frequenza e discretizzazione devono essere dichiarate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-62-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Vision-language-action».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-62-05

- Affermazione esatta: Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-62-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sicurezza e sim-to-real».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-62-CODE

- Affermazione esatta: `snip_62_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_62_contract.py, code/test_62_contract.py e code/outputs/SNIP-62-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
