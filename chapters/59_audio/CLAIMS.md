# Registro dei claim. Capitolo 59

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-59-01

- Affermazione esatta: Il segnale audio è campionato nel tempo. STFT e mel filterbank producono rappresentazioni tempo-frequenza con parametri espliciti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Waveform e spettrogramma».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-59-02

- Affermazione esatta: Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer. Streaming e offline hanno vincoli diversi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «ASR».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-59-03

- Affermazione esatta: Sintesi vocale trasforma testo in acoustic representation e waveform. Durata, prosodia e vocoder sono componenti distinti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «TTS».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-59-04

- Affermazione esatta: Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Neural codec».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-59-05

- Affermazione esatta: Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Musica e dialogo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-59-CODE

- Affermazione esatta: `snip_59_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_59_contract.py, code/test_59_contract.py e code/outputs/SNIP-59-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
