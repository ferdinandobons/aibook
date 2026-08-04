# Piano editoriale. Capitolo 55

## Obiettivo didattico

Seguire **Fondamenti della multimodalità** da testo, immagine, audio e maschere di modalità a spazio condiviso o output condizionato, osservando encoder, proiezione, alignment e fusion senza oltrepassare questo limite: allineamento misurato non equivale a comprensione generale.

## Prerequisiti reali

- Capitolo 19: Representation learning
- Capitolo 27: Embedding e spazio semantico

## Percorso della lezione

1. **Modalità e misure.** Testo, immagine, audio e azione hanno strutture e scale differenti. Ogni encoder produce una rappresentazione con assi dichiarati. Prova: SRC-55-001.
2. **Allineamento.** Coppie sincronizzate o semanticamente collegate forniscono un segnale comune. Corrispondenza temporale e semantica non coincidono sempre. Prova: SRC-55-002.
3. **Fusion.** Early, intermediate e late fusion combinano modalità in punti diversi e cambiano costo, dipendenze e disponibilità dei dati. Prova: SRC-55-003.
4. **Missing modality.** Un sistema deve definire cosa accade quando una modalità è assente, corrotta o non autorizzata. Prova: SRC-55-004.
5. **Valutazione.** Comprensione, retrieval, grounding e generazione richiedono benchmark distinti. Una media multimodale può nascondere una modalità debole. Prova: SRC-55-001.

## Prove e artefatti

- riferimento minimo: `code/snip_55_contract.py`; test: `code/test_55_contract.py`; output: `code/outputs/SNIP-55-001.txt`.
- visuali candidate: FOUNDATION-01, FOUNDATION-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
