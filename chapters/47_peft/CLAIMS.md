# Registro dei claim. Capitolo 47

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-47-01

- Affermazione esatta: PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Parametri congelati e adattamento».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-47-02

- Affermazione esatta: Blocchi bottleneck vengono inseriti nel percorso residuale. Posizione, dimensione e inizializzazione determinano l'interfaccia con il modello base.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Adapter».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-47-03

- Affermazione esatta: Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «LoRA».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-47-04

- Affermazione esatta: Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Prompt, prefix e IA3».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-47-05

- Affermazione esatta: Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili. Formato, tokenizer e architettura devono corrispondere.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «QLoRA e compatibilità».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-47-CODE

- Affermazione esatta: `snip_47_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_47_contract.py, code/test_47_contract.py e code/outputs/SNIP-47-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
