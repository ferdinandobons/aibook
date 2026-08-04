# Registro dei claim. Capitolo 57

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-57-01

- Affermazione esatta: Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente. Il decoder ricostruisce pixel al termine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Latent diffusion».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-57-02

- Affermazione esatta: Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Conditioning».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-57-03

- Affermazione esatta: Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Classifier-free guidance».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-57-04

- Affermazione esatta: Una mask stabilisce regioni modificabili. La coerenza con le aree conservate dipende da noise schedule e condition.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Editing e inpainting».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-57-05

- Affermazione esatta: ControlNet, adapter e reference image aggiungono vincoli. Dataset, diritti e metadati restano parte del sistema.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Controllo e provenienza».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-57-CODE

- Affermazione esatta: `snip_57_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_57_contract.py, code/test_57_contract.py e code/outputs/SNIP-57-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
