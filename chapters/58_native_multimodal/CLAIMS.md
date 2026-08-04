# Registro dei claim. Capitolo 58

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-58-01

- Affermazione esatta: Sequenze possono alternare testo, immagini, audio e marker. Il tokenizer multimodale definisce unità e ordine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Token interleaved».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-58-02

- Affermazione esatta: Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Backbone condiviso».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-58-03

- Affermazione esatta: La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Output multimodale».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-58-04

- Affermazione esatta: Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Any-to-any».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-58-05

- Affermazione esatta: Audio, video e testo possiedono frequenze differenti. Allineamento temporale e turn-taking diventano parte dell'architettura.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sincronizzazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-58-CODE

- Affermazione esatta: `snip_58_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_58_contract.py, code/test_58_contract.py e code/outputs/SNIP-58-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
