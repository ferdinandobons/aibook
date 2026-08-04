# Registro dei claim. Capitolo 90

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-90-01

- Affermazione esatta: Campioni modificati possono alterare comportamento generale o target specifici. Provenienza e deduplicazione riducono alcune superfici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-90-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Data poisoning».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-90-02

- Affermazione esatta: Un trigger induce un comportamento nascosto mantenendo prestazioni normali altrove. Scanner e fine-tuning non garantiscono rimozione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-90-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Backdoor».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-90-03

- Affermazione esatta: Query e output possono permettere di imitare capacità o recuperare informazioni. Rate limit e watermark comportamentali hanno limiti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-90-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Model extraction».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-90-04

- Affermazione esatta: Checkpoint, tokenizer, codice e dipendenze richiedono hash, firma, SBOM e policy di caricamento sicuro.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-90-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Artifact security».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-90-05

- Affermazione esatta: File eseguibili, custom code e deserializzazione possono introdurre rischio indipendente dai pesi matematici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-90-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Repository e deployment».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-90-CODE

- Affermazione esatta: `snip_90_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_90_contract.py, code/test_90_contract.py e code/outputs/SNIP-90-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
