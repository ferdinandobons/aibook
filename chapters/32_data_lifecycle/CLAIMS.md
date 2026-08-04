# Registro dei claim. Capitolo 32

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-32-01

- Affermazione esatta: Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-32-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sorgenti e provenienza».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-32-02

- Affermazione esatta: Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono essere versionate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-32-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Parsing e normalizzazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-32-03

- Affermazione esatta: Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statistiche prima e dopo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-32-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Filtri».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-32-04

- Affermazione esatta: Hash esatti e similarità approssimata rilevano forme differenti di duplicazione. I benchmark richiedono controlli separati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-32-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Deduplicazione e contaminazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-32-05

- Affermazione esatta: Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-32-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Split, tokenizzazione e manifest».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-32-CODE

- Affermazione esatta: `snip_32_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_32_contract.py, code/test_32_contract.py e code/outputs/SNIP-32-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
