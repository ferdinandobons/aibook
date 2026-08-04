# Registro dei claim. Capitolo 89

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-89-01

- Affermazione esatta: Contenuti recuperati, pagine e documenti sono dati non fidati. Non devono acquisire automaticamente la priorità delle istruzioni di sistema.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Istruzioni e dati».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-89-02

- Affermazione esatta: Una istruzione malevola può essere inserita in una fonte consultata dall'agente e attivarsi durante il retrieval o il browsing.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Indirect prompt injection».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-89-03

- Affermazione esatta: Policy esterne validano tool, argomenti e destinazioni. Il modello propone, ma l'enforcement avviene fuori dal testo generato.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Tool mediation».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-89-04

- Affermazione esatta: Segreti, memoria e risultati dei tool devono essere separati per scope. Output e URL possono diventare canali di esfiltrazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Data exfiltration».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-89-05

- Affermazione esatta: Canary, trace, allowlist, conferme e revoca delle credenziali supportano rilevamento, contenimento e recovery.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-89-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Test e incident response».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-89-CODE

- Affermazione esatta: `snip_89_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_89_contract.py, code/test_89_contract.py e code/outputs/SNIP-89-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
