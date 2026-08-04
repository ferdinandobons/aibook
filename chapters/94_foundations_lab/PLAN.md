# Piano editoriale. Capitolo 94

## Obiettivo didattico

Seguire **Percorso pratico dai fondamenti** da seed, dataset piccolo, config, codice e versione a loss, metriche, manifest e limite, osservando run, test, valutazione e report senza oltrepassare questo limite: un run locale non equivale a una prova generale.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 12: Apprendimento supervisionato
- Capitolo 13: Apprendimento non supervisionato e auto-supervisionato

## Percorso della lezione

1. **Ambiente riproducibile.** Python, dipendenze, seed e struttura del progetto vengono fissati prima degli esperimenti. Prova: SRC-94-001.
2. **Dataset piccolo.** Un dataset controllabile permette di vedere preprocessing, split, batch e leakage. Prova: SRC-94-002.
3. **Modello e loss.** Una baseline lineare precede la rete. Shape, logits e loss vengono verificati con test. Prova: SRC-94-003.
4. **Training e valutazione.** Curve, checkpoint, validation e test seguono il protocollo costruito nel libro. Prova: SRC-94-004.
5. **Report.** Il laboratorio produce README, output, figure e limiti, non soltanto un notebook che termina senza audit. Prova: SRC-94-001.

## Prove e artefatti

- riferimento minimo: `code/snip_94_contract.py`; test: `code/test_94_contract.py`; output: `code/outputs/SNIP-94-001.txt`.
- laboratorio esteso: `code/foundations_lab.py`; test: `code/test_foundations_lab.py`; output: `code/outputs/FOUNDATIONS-LAB.txt`.
- visuali candidate: LAB-01, LAB-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
