# Piano interno. Capitolo 60

- Domanda centrale: quale contratto costruisce Generazione video?
- Oggetto continuo: una sequenza di frame condizionata nel tempo; input guida: frame, latent video, testo e timestamp.
- Prerequisito stabile: Capitolo 59, Audio, parlato e musica.
- Gap: denoising, autoregressione e controllo temporale.
- Output consegnato: frame coerenti e misura di flicker; consumer successivo: Capitolo 61, 3D, spazio e rappresentazione delle scene.
- Invariante principale: qualità del singolo frame non dimostra coerenza tra frame.
- Visuali: VIDEO-01 e VIDEO-02, con famiglie compositive variabili.
- Snippet: code/snip_60_contract.py; output: code/outputs/SNIP-60-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Spazio e tempo

- Ultima affermazione stabile: una sequenza di frame condizionata nel tempo.
- Concetto nuovo: Un video aggiunge una dimensione temporale alle immagini. Token, patch o latent devono conservare movimento e identità.
- Input e shape: frame, latent video, testo e timestamp.
- Operazione: denoising, autoregressione e controllo temporale.
- Output e shape: frame coerenti e misura di flicker.
- Che cosa cambia: il passaggio specifico di «Spazio e tempo».
- Invariante: qualità del singolo frame non dimostra coerenza tra frame.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre frame con un oggetto che deve mantenere posizione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Video diffusion.
- Prova: SRC-60-001 e sezione pubblica corrispondente.

## Transizione 2. Video diffusion

- Ultima affermazione stabile: una sequenza di frame condizionata nel tempo.
- Concetto nuovo: Il denoiser opera su tensori spazio-temporali o latent compressi. Attention fattorizzata e convoluzioni riducono il costo.
- Input e shape: frame, latent video, testo e timestamp.
- Operazione: denoising, autoregressione e controllo temporale.
- Output e shape: frame coerenti e misura di flicker.
- Che cosa cambia: il passaggio specifico di «Video diffusion».
- Invariante: qualità del singolo frame non dimostra coerenza tra frame.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre frame con un oggetto che deve mantenere posizione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Autoregressione.
- Prova: SRC-60-002 e sezione pubblica corrispondente.

## Transizione 3. Autoregressione

- Ultima affermazione stabile: una sequenza di frame condizionata nel tempo.
- Concetto nuovo: Frame, patch o token video possono essere generati in ordine. L'ordine scelto modifica dipendenze e cache.
- Input e shape: frame, latent video, testo e timestamp.
- Operazione: denoising, autoregressione e controllo temporale.
- Output e shape: frame coerenti e misura di flicker.
- Che cosa cambia: il passaggio specifico di «Autoregressione».
- Invariante: qualità del singolo frame non dimostra coerenza tra frame.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre frame con un oggetto che deve mantenere posizione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Coerenza.
- Prova: SRC-60-003 e sezione pubblica corrispondente.

## Transizione 4. Coerenza

- Ultima affermazione stabile: una sequenza di frame condizionata nel tempo.
- Concetto nuovo: Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame.
- Input e shape: frame, latent video, testo e timestamp.
- Operazione: denoising, autoregressione e controllo temporale.
- Output e shape: frame coerenti e misura di flicker.
- Che cosa cambia: il passaggio specifico di «Coerenza».
- Invariante: qualità del singolo frame non dimostra coerenza tra frame.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre frame con un oggetto che deve mantenere posizione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Condizionamento e editing.
- Prova: SRC-60-004 e sezione pubblica corrispondente.

## Transizione 5. Condizionamento e editing

- Ultima affermazione stabile: una sequenza di frame condizionata nel tempo.
- Concetto nuovo: Testo, immagine iniziale, traiettoria o maschere guidano il video. Il controllo deve essere valutato nel tempo.
- Input e shape: frame, latent video, testo e timestamp.
- Operazione: denoising, autoregressione e controllo temporale.
- Output e shape: frame coerenti e misura di flicker.
- Che cosa cambia: il passaggio specifico di «Condizionamento e editing».
- Invariante: qualità del singolo frame non dimostra coerenza tra frame.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre frame con un oggetto che deve mantenere posizione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: 3D, spazio e rappresentazione delle scene.
- Prova: SRC-60-001 e sezione pubblica corrispondente.
