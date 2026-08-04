# Piano editoriale. Capitolo 57

## Obiettivo didattico

Seguire **Generazione e modifica delle immagini** da latent, prompt, mask e rumore a immagine, score e metadati di provenienza, osservando denoising, guidance, editing o inpainting senza oltrepassare questo limite: controllo dell'immagine e verità del contenuto sono proprietà diverse.

## Prerequisiti reali

- Capitolo 20: Fondamenti della modellazione generativa
- Capitolo 25: Diffusione, score matching e flow matching
- Capitolo 55: Fondamenti della multimodalità

## Percorso della lezione

1. **Latent diffusion.** Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente. Il decoder ricostruisce pixel al termine. Prova: SRC-57-001.
2. **Conditioning.** Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati. Prova: SRC-57-002.
3. **Classifier-free guidance.** Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione. Prova: SRC-57-003.
4. **Editing e inpainting.** Una mask stabilisce regioni modificabili. La coerenza con le aree conservate dipende da noise schedule e condition. Prova: SRC-57-004.
5. **Controllo e provenienza.** ControlNet, adapter e reference image aggiungono vincoli. Dataset, diritti e metadati restano parte del sistema. Prova: SRC-57-001.

## Prove e artefatti

- riferimento minimo: `code/snip_57_contract.py`; test: `code/test_57_contract.py`; output: `code/outputs/SNIP-57-001.txt`.
- visuali candidate: GENERATION-01, GENERATION-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
