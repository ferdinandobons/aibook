# Registro dei claim. Capitolo 16

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-16-01

- Affermazione esatta: Attivazioni e gradienti possono crescere o ridursi lungo la profondità. Inizializzazione, attivazioni e residual determinano la scala osservata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Segnali che attraversano molti layer».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-16-02

- Affermazione esatta: Xavier e He initialization collegano la varianza dei pesi al fan-in o fan-out. Le formule presuppongono attivazioni e indipendenze approssimate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Inizializzazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-16-03

- Affermazione esatta: BatchNorm, LayerNorm e RMSNorm normalizzano assi e statistiche differenti. Non sono sostituibili senza considerare batch, sequenza e architettura.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Normalizzazione».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-16-04

- Affermazione esatta: Un residual path conserva un percorso identità e facilita il trasporto di informazione. La somma richiede shape compatibili e una scala controllata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Residual e profondità».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-16-05

- Affermazione esatta: Dropout, weight decay, data augmentation ed early stopping agiscono in punti diversi. Curve, norme e slice aiutano a distinguere underfitting, overfitting e instabilità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Regolarizzazione e diagnostica».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-16-CODE

- Affermazione esatta: `snip_16_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_16_contract.py, code/test_16_contract.py e code/outputs/SNIP-16-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
