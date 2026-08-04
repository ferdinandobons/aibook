# Piano editoriale. Capitolo 60

## Obiettivo didattico

Seguire **Generazione video** da frame, latent video, testo e timestamp a frame coerenti e misura di flicker, osservando denoising, autoregressione e controllo temporale senza oltrepassare questo limite: qualità del singolo frame non dimostra coerenza tra frame.

## Prerequisiti reali

- Capitolo 25: Diffusione, score matching e flow matching
- Capitolo 55: Fondamenti della multimodalità
- Capitolo 59: Audio, parlato e musica

## Percorso della lezione

1. **Spazio e tempo.** Un video aggiunge una dimensione temporale alle immagini. Token, patch o latent devono conservare movimento e identità. Prova: SRC-60-001.
2. **Video diffusion.** Il denoiser opera su tensori spazio-temporali o latent compressi. Attention fattorizzata e convoluzioni riducono il costo. Prova: SRC-60-002.
3. **Autoregressione.** Frame, patch o token video possono essere generati in ordine. L'ordine scelto modifica dipendenze e cache. Prova: SRC-60-003.
4. **Coerenza.** Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame. Prova: SRC-60-004.
5. **Condizionamento e editing.** Testo, immagine iniziale, traiettoria o maschere guidano il video. Il controllo deve essere valutato nel tempo. Prova: SRC-60-001.

## Prove e artefatti

- riferimento minimo: `code/snip_60_contract.py`; test: `code/test_60_contract.py`; output: `code/outputs/SNIP-60-001.txt`.
- visuali candidate: VIDEO-01, VIDEO-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
