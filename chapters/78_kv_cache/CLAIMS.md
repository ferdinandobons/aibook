# Registro dei claim. Capitolo 78

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-78-01

- Affermazione esatta: Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache precedente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Prefill e decode».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-78-02

- Affermazione esatta: Layer, batch, KV head, token e head dimension determinano shape e byte. Contiguità e paginazione influenzano il kernel.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Layout».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-78-03

- Affermazione esatta: Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare sequenze di lunghezza diversa.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «PagedAttention».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-78-04

- Affermazione esatta: Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi sono compatibili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Prefix caching».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-78-05

- Affermazione esatta: Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano precisione o contesto disponibile.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-78-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Compressione ed eviction».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-78-CODE

- Affermazione esatta: `snip_78_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_78_contract.py, code/test_78_contract.py e code/outputs/SNIP-78-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
