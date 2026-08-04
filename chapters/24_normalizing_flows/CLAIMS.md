# Registro dei claim. Capitolo 24

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-24-01

- Affermazione esatta: Una trasformazione invertibile collega una distribuzione semplice ai dati. La densità usa il determinante Jacobiano.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Cambio di variabile».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-24-02

- Affermazione esatta: RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Coupling layer».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-24-03

- Affermazione esatta: L'invertibilità limita operazioni e dimensioni. Squeeze, split e permutazioni riorganizzano l'informazione senza perderla.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Invertibilità e architettura».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-24-04

- Affermazione esatta: Una ODE definisce una trasformazione continua. La likelihood usa la variazione del log-density lungo il flusso.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Continuous normalizing flow».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-24-05

- Affermazione esatta: I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sampling e costo».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-24-CODE

- Affermazione esatta: `snip_24_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_24_contract.py, code/test_24_contract.py e code/outputs/SNIP-24-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
