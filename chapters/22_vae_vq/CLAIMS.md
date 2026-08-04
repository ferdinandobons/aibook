# Registro dei claim. Capitolo 22

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-22-01

- Affermazione esatta: Il VAE introduce un encoder q(z|x) per approssimare il posterior. Il decoder modella p(x|z).
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Inferenza approssimata».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-22-02

- Affermazione esatta: L'evidence lower bound combina ricostruzione e KL verso il prior. Massimizzare l'ELBO non coincide necessariamente con massimizzare qualità percettiva.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «ELBO».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-22-03

- Affermazione esatta: Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Questo consente gradienti pathwise.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Reparameterization trick».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-22-04

- Affermazione esatta: Un decoder molto potente può ignorare z e avvicinare il posterior al prior. KL annealing e architettura possono modificare il fenomeno.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Posterior collapse».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-22-05

- Affermazione esatta: La quantizzazione vettoriale sostituisce il latent continuo con indici di un codebook. Commitment loss e aggiornamento del codebook richiedono controlli dedicati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-22-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «VQ-VAE».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-22-CODE

- Affermazione esatta: `snip_22_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_22_contract.py, code/test_22_contract.py e code/outputs/SNIP-22-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
