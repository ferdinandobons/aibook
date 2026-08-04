# Piano interno. Capitolo 57

- Domanda centrale: quale contratto costruisce Generazione e modifica delle immagini?
- Oggetto continuo: un contenuto immagine e la condizione che lo modifica; input guida: latent, prompt, mask e rumore.
- Prerequisito stabile: Capitolo 56, Vision encoder e Vision-Language Model.
- Gap: denoising, guidance, editing o inpainting.
- Output consegnato: immagine, score e metadati di provenienza; consumer successivo: Capitolo 58, Modelli multimodali nativi e any-to-any.
- Invariante principale: controllo dell'immagine e verità del contenuto sono proprietà diverse.
- Visuali: GENERATION-01 e GENERATION-02, con famiglie compositive variabili.
- Snippet: code/snip_57_contract.py; output: code/outputs/SNIP-57-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Latent diffusion

- Ultima affermazione stabile: un contenuto immagine e la condizione che lo modifica.
- Concetto nuovo: Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente. Il decoder ricostruisce pixel al termine.
- Input e shape: latent, prompt, mask e rumore.
- Operazione: denoising, guidance, editing o inpainting.
- Output e shape: immagine, score e metadati di provenienza.
- Che cosa cambia: il passaggio specifico di «Latent diffusion».
- Invariante: controllo dell'immagine e verità del contenuto sono proprietà diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una regione mascherata modificata lasciando il resto fissato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Conditioning.
- Prova: SRC-57-001 e sezione pubblica corrispondente.

## Transizione 2. Conditioning

- Ultima affermazione stabile: un contenuto immagine e la condizione che lo modifica.
- Concetto nuovo: Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati.
- Input e shape: latent, prompt, mask e rumore.
- Operazione: denoising, guidance, editing o inpainting.
- Output e shape: immagine, score e metadati di provenienza.
- Che cosa cambia: il passaggio specifico di «Conditioning».
- Invariante: controllo dell'immagine e verità del contenuto sono proprietà diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una regione mascherata modificata lasciando il resto fissato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Classifier-free guidance.
- Prova: SRC-57-002 e sezione pubblica corrispondente.

## Transizione 3. Classifier-free guidance

- Ultima affermazione stabile: un contenuto immagine e la condizione che lo modifica.
- Concetto nuovo: Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione.
- Input e shape: latent, prompt, mask e rumore.
- Operazione: denoising, guidance, editing o inpainting.
- Output e shape: immagine, score e metadati di provenienza.
- Che cosa cambia: il passaggio specifico di «Classifier-free guidance».
- Invariante: controllo dell'immagine e verità del contenuto sono proprietà diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una regione mascherata modificata lasciando il resto fissato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Editing e inpainting.
- Prova: SRC-57-003 e sezione pubblica corrispondente.

## Transizione 4. Editing e inpainting

- Ultima affermazione stabile: un contenuto immagine e la condizione che lo modifica.
- Concetto nuovo: Una mask stabilisce regioni modificabili. La coerenza con le aree conservate dipende da noise schedule e condition.
- Input e shape: latent, prompt, mask e rumore.
- Operazione: denoising, guidance, editing o inpainting.
- Output e shape: immagine, score e metadati di provenienza.
- Che cosa cambia: il passaggio specifico di «Editing e inpainting».
- Invariante: controllo dell'immagine e verità del contenuto sono proprietà diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una regione mascherata modificata lasciando il resto fissato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Controllo e provenienza.
- Prova: SRC-57-004 e sezione pubblica corrispondente.

## Transizione 5. Controllo e provenienza

- Ultima affermazione stabile: un contenuto immagine e la condizione che lo modifica.
- Concetto nuovo: ControlNet, adapter e reference image aggiungono vincoli. Dataset, diritti e metadati restano parte del sistema.
- Input e shape: latent, prompt, mask e rumore.
- Operazione: denoising, guidance, editing o inpainting.
- Output e shape: immagine, score e metadati di provenienza.
- Che cosa cambia: il passaggio specifico di «Controllo e provenienza».
- Invariante: controllo dell'immagine e verità del contenuto sono proprietà diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una regione mascherata modificata lasciando il resto fissato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Modelli multimodali nativi e any-to-any.
- Prova: SRC-57-001 e sezione pubblica corrispondente.
