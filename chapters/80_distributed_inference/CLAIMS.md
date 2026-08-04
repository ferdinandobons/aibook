# Registro dei claim. Capitolo 80

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-80-01

- Affermazione esatta: Pesi e layer vengono divisi quando il modello non entra in un singolo dispositivo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Tensor e pipeline parallelism».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-80-02

- Affermazione esatta: MoE distribuisce esperti e usa all-to-all durante l'inference.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Expert parallelism».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-80-03

- Affermazione esatta: Cluster distinti ottimizzano prompt lunghi e generazione token-by-token, scambiando KV cache attraverso la rete.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Prefill-decode disaggregation».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-80-04

- Affermazione esatta: Modello, adapter, lunghezza e stato della cache guidano il placement. Spostare una richiesta può richiedere trasferimenti costosi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Routing».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-80-05

- Affermazione esatta: Replica, retry e idempotency devono evitare duplicazione degli output e perdita dello stato di sessione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-80-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Fault tolerance».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-80-CODE

- Affermazione esatta: `snip_80_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_80_contract.py, code/test_80_contract.py e code/outputs/SNIP-80-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
