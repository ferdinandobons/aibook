# Piano interno. Capitolo 23

- Domanda centrale: quale contratto costruisce Generative Adversarial Network?
- Oggetto continuo: la partita tra generatore e discriminatore; input guida: un dato reale, un campione e due score.
- Prerequisito stabile: Capitolo 22, Variational Autoencoder e latent discreti.
- Gap: aggiornamento alternato e segnale di feedback.
- Output consegnato: score, gradiente e campione; consumer successivo: Capitolo 24, Normalizing flow e trasformazioni invertibili.
- Invariante principale: un equilibrio locale non prova copertura né stabilità.
- Visuali: GAN-01 e GAN-02, con famiglie compositive variabili.
- Snippet: code/snip_23_contract.py; output: code/outputs/SNIP-23-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Un gioco tra due modelli

- Ultima affermazione stabile: la partita tra generatore e discriminatore.
- Concetto nuovo: Il generatore produce campioni; il discriminatore distingue dati reali e generati. L'obiettivo è un gioco, non una loss singola ottimizzata congiuntamente.
- Input e shape: un dato reale, un campione e due score.
- Operazione: aggiornamento alternato e segnale di feedback.
- Output e shape: score, gradiente e campione.
- Che cosa cambia: il passaggio specifico di «Un gioco tra due modelli».
- Invariante: un equilibrio locale non prova copertura né stabilità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due score reali e sintetici con un aggiornamento alternato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Divergenze e gradienti.
- Prova: SRC-23-001 e sezione pubblica corrispondente.

## Transizione 2. Divergenze e gradienti

- Ultima affermazione stabile: la partita tra generatore e discriminatore.
- Concetto nuovo: La formulazione originale è collegata alla Jensen-Shannon divergence sotto un discriminatore ottimo. I gradienti pratici dipendono dalla loss scelta.
- Input e shape: un dato reale, un campione e due score.
- Operazione: aggiornamento alternato e segnale di feedback.
- Output e shape: score, gradiente e campione.
- Che cosa cambia: il passaggio specifico di «Divergenze e gradienti».
- Invariante: un equilibrio locale non prova copertura né stabilità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due score reali e sintetici con un aggiornamento alternato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Mode collapse.
- Prova: SRC-23-002 e sezione pubblica corrispondente.

## Transizione 3. Mode collapse

- Ultima affermazione stabile: la partita tra generatore e discriminatore.
- Concetto nuovo: Il generatore può produrre poche modalità convincenti. Diversità e fedeltà devono essere misurate separatamente.
- Input e shape: un dato reale, un campione e due score.
- Operazione: aggiornamento alternato e segnale di feedback.
- Output e shape: score, gradiente e campione.
- Che cosa cambia: il passaggio specifico di «Mode collapse».
- Invariante: un equilibrio locale non prova copertura né stabilità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due score reali e sintetici con un aggiornamento alternato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Wasserstein GAN.
- Prova: SRC-23-003 e sezione pubblica corrispondente.

## Transizione 4. Wasserstein GAN

- Ultima affermazione stabile: la partita tra generatore e discriminatore.
- Concetto nuovo: WGAN usa una distanza legata a funzioni Lipschitz. Weight clipping e gradient penalty sono implementazioni differenti del vincolo.
- Input e shape: un dato reale, un campione e due score.
- Operazione: aggiornamento alternato e segnale di feedback.
- Output e shape: score, gradiente e campione.
- Che cosa cambia: il passaggio specifico di «Wasserstein GAN».
- Invariante: un equilibrio locale non prova copertura né stabilità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due score reali e sintetici con un aggiornamento alternato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Stabilità e valutazione.
- Prova: SRC-23-004 e sezione pubblica corrispondente.

## Transizione 5. Stabilità e valutazione

- Ultima affermazione stabile: la partita tra generatore e discriminatore.
- Concetto nuovo: Bilanciare update, normalizzazioni e capacità è essenziale. FID è una metrica su feature e non sostituisce l'analisi dei campioni.
- Input e shape: un dato reale, un campione e due score.
- Operazione: aggiornamento alternato e segnale di feedback.
- Output e shape: score, gradiente e campione.
- Che cosa cambia: il passaggio specifico di «Stabilità e valutazione».
- Invariante: un equilibrio locale non prova copertura né stabilità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due score reali e sintetici con un aggiornamento alternato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Normalizing flow e trasformazioni invertibili.
- Prova: SRC-23-001 e sezione pubblica corrispondente.
