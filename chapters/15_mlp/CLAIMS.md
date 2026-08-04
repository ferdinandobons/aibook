# Registro dei claim. Capitolo 15

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-15-01

- Affermazione esatta: Il percettrone combina feature con pesi e bias. Il confine risultante è lineare nello spazio delle feature.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Una decisione lineare».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-15-02

- Affermazione esatta: Una MLP alterna trasformazioni affini e funzioni non lineari. Senza non linearità, più layer affini collassano in una sola trasformazione affine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Strati nascosti».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-15-03

- Affermazione esatta: ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. La scelta deve essere letta insieme a inizializzazione e normalizzazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Attivazioni».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-15-04

- Affermazione esatta: Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Capacità ed espressività».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-15-05

- Affermazione esatta: Il forward produce logits e loss. Backpropagation e optimizer trasformano il segnale in aggiornamenti, secondo i contratti costruiti nei capitoli matematici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Dal forward al training».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-15-CODE

- Affermazione esatta: `snip_15_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_15_contract.py, code/test_15_contract.py e code/outputs/SNIP-15-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
