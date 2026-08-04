# Registro dei claim. Capitolo 29

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-29-01

- Affermazione esatta: Il Transformer combina embedding, posizione, attention, feed-forward, residual e normalizzazione. Ogni componente mantiene un contratto di shape.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «La mappa completa».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-29-02

- Affermazione esatta: L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le posizioni.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Encoder».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-29-03

- Affermazione esatta: Il decoder usa self-attention causale e, nelle architetture encoder-decoder, cross-attention verso l'encoder.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Decoder».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-29-04

- Affermazione esatta: Le head applicano proiezioni differenti e vengono concatenate. La proiezione finale riporta alla dimensione del modello.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Multi-head attention».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-29-05

- Affermazione esatta: Layer ripetuti aggiornano il residual stream. La head di output trasforma la rappresentazione in logits sul vocabolario.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-29-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Residual stream e output».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-29-CODE

- Affermazione esatta: `snip_29_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_29_contract.py, code/test_29_contract.py e code/outputs/SNIP-29-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
