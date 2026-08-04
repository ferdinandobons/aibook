# Registro dei claim. Capitolo 60

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-60-01

- Affermazione esatta: Un video aggiunge una dimensione temporale alle immagini. Token, patch o latent devono conservare movimento e identità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-60-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Spazio e tempo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-60-02

- Affermazione esatta: Il denoiser opera su tensori spazio-temporali o latent compressi. Attention fattorizzata e convoluzioni riducono il costo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-60-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Video diffusion».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-60-03

- Affermazione esatta: Frame, patch o token video possono essere generati in ordine. L'ordine scelto modifica dipendenze e cache.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-60-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Autoregressione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-60-04

- Affermazione esatta: Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-60-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Coerenza».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-60-05

- Affermazione esatta: Testo, immagine iniziale, traiettoria o maschere guidano il video. Il controllo deve essere valutato nel tempo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-60-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Condizionamento e editing».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-60-CODE

- Affermazione esatta: `snip_60_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_60_contract.py, code/test_60_contract.py e code/outputs/SNIP-60-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
