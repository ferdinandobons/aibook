# Piano editoriale. Capitolo 56

## Obiettivo didattico

Seguire **Vision encoder e Vision-Language Model** da immagine, patch, testo e query a token visivi, risposta e grounding, osservando vision encoder, projector e cross-attention senza oltrepassare questo limite: una risposta linguistica non certifica che il dettaglio sia nell'immagine.

## Prerequisiti reali

- Capitolo 27: Embedding e spazio semantico
- Capitolo 29: Il Transformer da zero
- Capitolo 55: Fondamenti della multimodalità

## Percorso della lezione

1. **Patch e vision encoder.** Una immagine viene trasformata in patch o feature. Risoluzione, positional encoding e pooling definiscono la sequenza visiva. Prova: SRC-56-001.
2. **Dual encoder.** CLIP allinea immagine e testo con una loss contrastiva. I due encoder supportano retrieval efficiente ma interagiscono tardi. Prova: SRC-56-002.
3. **Projector.** Architetture modulari proiettano feature visive nella dimensione del language model. Il projector stabilisce capacità e numero di visual token. Prova: SRC-56-003.
4. **Q-Former e cross-attention.** Query apprese possono estrarre un insieme compatto di feature. Altre architetture inseriscono cross-attention dedicata. Prova: SRC-56-004.
5. **Grounding e hallucination.** Descrivere una immagine non garantisce localizzare oggetti o relazioni. Grounding, OCR e affidabilità richiedono test specifici. Prova: SRC-56-001.

## Prove e artefatti

- riferimento minimo: `code/snip_56_contract.py`; test: `code/test_56_contract.py`; output: `code/outputs/SNIP-56-001.txt`.
- visuali candidate: VLM-01, VLM-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
