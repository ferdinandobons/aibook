# Piano interno. Capitolo 94

- Domanda centrale: quale contratto costruisce Percorso pratico dai fondamenti?
- Oggetto continuo: un esperimento didattico con ambiente e artefatti dichiarati; input guida: seed, dataset piccolo, config, codice e versione.
- Prerequisito stabile: Capitolo 93, Diritto, governance e sostenibilità.
- Gap: run, test, valutazione e report.
- Output consegnato: loss, metriche, manifest e limite; consumer successivo: Capitolo 95, Costruire un piccolo language model.
- Invariante principale: un run locale non equivale a una prova generale.
- Visuali: LAB-01 e LAB-02, con famiglie compositive variabili.
- Snippet: code/snip_94_contract.py; output: code/outputs/SNIP-94-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Ambiente riproducibile

- Ultima affermazione stabile: un esperimento didattico con ambiente e artefatti dichiarati.
- Concetto nuovo: Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti.
- Input e shape: seed, dataset piccolo, config, codice e versione.
- Operazione: run, test, valutazione e report.
- Output e shape: loss, metriche, manifest e limite.
- Che cosa cambia: il passaggio specifico di «Ambiente riproducibile».
- Invariante: un run locale non equivale a una prova generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: seed, split e dtype salvati prima dell'esecuzione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Dataset piccolo.
- Prova: SRC-94-001 e sezione pubblica corrispondente.

## Transizione 2. Dataset piccolo

- Ultima affermazione stabile: un esperimento didattico con ambiente e artefatti dichiarati.
- Concetto nuovo: Un dataset controllabile permette di vedere preprocessing, split, batch e leakage.
- Input e shape: seed, dataset piccolo, config, codice e versione.
- Operazione: run, test, valutazione e report.
- Output e shape: loss, metriche, manifest e limite.
- Che cosa cambia: il passaggio specifico di «Dataset piccolo».
- Invariante: un run locale non equivale a una prova generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: seed, split e dtype salvati prima dell'esecuzione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Modello e loss.
- Prova: SRC-94-002 e sezione pubblica corrispondente.

## Transizione 3. Modello e loss

- Ultima affermazione stabile: un esperimento didattico con ambiente e artefatti dichiarati.
- Concetto nuovo: Una baseline lineare precede la rete. Shape, logits e loss vengono verificati con test.
- Input e shape: seed, dataset piccolo, config, codice e versione.
- Operazione: run, test, valutazione e report.
- Output e shape: loss, metriche, manifest e limite.
- Che cosa cambia: il passaggio specifico di «Modello e loss».
- Invariante: un run locale non equivale a una prova generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: seed, split e dtype salvati prima dell'esecuzione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Training e valutazione.
- Prova: SRC-94-003 e sezione pubblica corrispondente.

## Transizione 4. Training e valutazione

- Ultima affermazione stabile: un esperimento didattico con ambiente e artefatti dichiarati.
- Concetto nuovo: Curve, checkpoint, validation e test seguono il protocollo costruito nel libro.
- Input e shape: seed, dataset piccolo, config, codice e versione.
- Operazione: run, test, valutazione e report.
- Output e shape: loss, metriche, manifest e limite.
- Che cosa cambia: il passaggio specifico di «Training e valutazione».
- Invariante: un run locale non equivale a una prova generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: seed, split e dtype salvati prima dell'esecuzione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Report.
- Prova: SRC-94-004 e sezione pubblica corrispondente.

## Transizione 5. Report

- Ultima affermazione stabile: un esperimento didattico con ambiente e artefatti dichiarati.
- Concetto nuovo: Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit.
- Input e shape: seed, dataset piccolo, config, codice e versione.
- Operazione: run, test, valutazione e report.
- Output e shape: loss, metriche, manifest e limite.
- Che cosa cambia: il passaggio specifico di «Report».
- Invariante: un run locale non equivale a una prova generale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: seed, split e dtype salvati prima dell'esecuzione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Costruire un piccolo language model.
- Prova: SRC-94-001 e sezione pubblica corrispondente.
