# Registro dei claim. Capitolo 68

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-68-01

- Affermazione esatta: Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-68-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Contratti tra componenti».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-68-02

- Affermazione esatta: MCP organizza risorse, prompt e tool esposti da server. La versione della specifica e il trasporto devono essere dichiarati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-68-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Model Context Protocol».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-68-03

- Affermazione esatta: Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-68-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Agent-to-agent».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-68-04

- Affermazione esatta: Interoperabilità non implica fiducia. Token, scope, provenance e policy devono attraversare ogni hop.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-68-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Identità e autorizzazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-68-05

- Affermazione esatta: Version e capability negotiation rendono esplicita l'incompatibilità. Una versione non supportata non deve proseguire silenziosamente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-68-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Compatibilità ed evoluzione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-68-CODE

- Affermazione esatta: `snip_68_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_68_contract.py, code/test_68_contract.py e code/outputs/SNIP-68-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
