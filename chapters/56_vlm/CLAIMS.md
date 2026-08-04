# Registro dei claim. Capitolo 56

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-56-01

- Affermazione esatta: Una immagine viene trasformata in patch o feature. Risoluzione, positional encoding e pooling definiscono la sequenza visiva.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Patch e vision encoder».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-56-02

- Affermazione esatta: CLIP allinea immagine e testo con una loss contrastiva. I due encoder supportano retrieval efficiente ma interagiscono tardi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Dual encoder».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-56-03

- Affermazione esatta: Architetture modulari proiettano feature visive nella dimensione del language model. Il projector stabilisce capacità e numero di visual token.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Projector».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-56-04

- Affermazione esatta: Query apprese possono estrarre un insieme compatto di feature. Altre architetture inseriscono cross-attention dedicata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Q-Former e cross-attention».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-56-05

- Affermazione esatta: Descrivere una immagine non garantisce localizzare oggetti o relazioni. Grounding, OCR e affidabilità richiedono test specifici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-56-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Grounding e hallucination».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-56-CODE

- Affermazione esatta: `snip_56_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_56_contract.py, code/test_56_contract.py e code/outputs/SNIP-56-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
