# Registro dei claim. Capitolo 73

- Data di revisione: 4 agosto 2026
- Regola: ogni claim pubblico è collegato al locator registrato nel dossier e mantiene il proprio limite.
- Stati usati: verificata; corretta; aperta.

## CL-73-01

- Affermazione esatta: La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Teacher e student».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-73-02

- Affermazione esatta: Una temperatura più alta rivela relazioni tra classi o token. Hard target e soft target vengono pesati separatamente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-002, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Temperature e loss».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-73-03

- Affermazione esatta: Per modelli generativi, risposte del teacher diventano un nuovo dataset. Filtri e diversità determinano ciò che lo student vede.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-003, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Sequence distillation».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-73-04

- Affermazione esatta: Pesi, canali, head o layer possono essere rimossi. Sparsità nominale e accelerazione reale dipendono da kernel e hardware.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-004, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Pruning».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-73-05

- Affermazione esatta: Fine-tuning o calibration recuperano qualità dopo compressione. Il confronto deve includere memoria, latency e regressioni per slice.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-001, dossier `FONTI_PRIMARIE.md`.
- Sezione pubblica: «Recovery».
- Versione o data: revisione locale 4 agosto 2026; versione e data della fonte nel dossier.
- Controllo indipendente: la citazione è adiacente al claim; titolo, URL, locator, perimetro e limiti sono registrati nel dossier; nessun risultato quantitativo viene trasferito senza il relativo setup.
- Esito: verificata
- Note: esempi, derivazioni e output locali restano distinti dall'evidenza della fonte.

## CL-73-CODE

- Affermazione esatta: `snip_73_contract.py` produce l'output JSON versionato; il test controlla output atteso, determinismo, serializzazione, valori finiti e limite interpretativo.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_73_contract.py, code/test_73_contract.py e code/outputs/SNIP-73-001.txt.
- Versione o data: Python 3.13.12, CPU, 4 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest da processo separato.
- Esito: verificata
- Note: esempio delimitato e didattico; non è un benchmark di produzione.
