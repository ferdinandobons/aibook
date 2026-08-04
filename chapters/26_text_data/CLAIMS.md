# Registro dei claim. Capitolo 26

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-26-01

- Affermazione esatta: Il testo è una sequenza di code point codificata in byte. Normalizzazione Unicode e decoding devono essere dichiarati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Unicode e byte».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-26-02

- Affermazione esatta: BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti. Il tokenizer fa parte dell'interfaccia del checkpoint.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Tokenizzazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-26-03

- Affermazione esatta: BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi. ID uguali richiedono la stessa convenzione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Token speciali».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-26-04

- Affermazione esatta: Più documenti possono condividere una sequenza. Attention mask e loss mask devono impedire dipendenze non desiderate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Packing e confini».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-26-05

- Affermazione esatta: Token per carattere variano tra lingue e formati. La lunghezza in token influenza contesto, costo e valutazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Lunghezza, lingua e costi».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-26-CODE

- Affermazione esatta: `snip_26_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_26_contract.py, code/test_26_contract.py e code/outputs/SNIP-26-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
