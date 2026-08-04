# Piano interno. Capitolo 21

- Domanda centrale: quale contratto costruisce Modelli autoregressivi?
- Oggetto continuo: la sequenza di token e la distribuzione del prossimo elemento; input guida: un prefisso di tre token e una mask causale.
- Prerequisito stabile: Capitolo 20, Fondamenti della modellazione generativa.
- Gap: fattorizzazione, teacher forcing e decoding.
- Output consegnato: logits, token scelto e traiettoria; consumer successivo: Capitolo 22, Variational Autoencoder e latent discreti.
- Invariante principale: nessuna posizione futura entra nella predizione causale.
- Visuali: AUTOREGR-01 e AUTOREGR-02, con famiglie compositive variabili.
- Snippet: code/snip_21_contract.py; output: code/outputs/SNIP-21-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Fattorizzare una sequenza

- Ultima affermazione stabile: la sequenza di token e la distribuzione del prossimo elemento.
- Concetto nuovo: La chain rule scompone la probabilità con un ordine. Ogni fattore condiziona sugli elementi precedenti.
- Input e shape: un prefisso di tre token e una mask causale.
- Operazione: fattorizzazione, teacher forcing e decoding.
- Output e shape: logits, token scelto e traiettoria.
- Che cosa cambia: il passaggio specifico di «Fattorizzare una sequenza».
- Invariante: nessuna posizione futura entra nella predizione causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due passi di teacher forcing confrontati con un passo campionato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Teacher forcing.
- Prova: SRC-21-001 e sezione pubblica corrispondente.

## Transizione 2. Teacher forcing

- Ultima affermazione stabile: la sequenza di token e la distribuzione del prossimo elemento.
- Concetto nuovo: Durante il training il modello riceve il prefisso reale e predice il passo successivo. Durante la generazione riceve anche i propri output.
- Input e shape: un prefisso di tre token e una mask causale.
- Operazione: fattorizzazione, teacher forcing e decoding.
- Output e shape: logits, token scelto e traiettoria.
- Che cosa cambia: il passaggio specifico di «Teacher forcing».
- Invariante: nessuna posizione futura entra nella predizione causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due passi di teacher forcing confrontati con un passo campionato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Maschera causale.
- Prova: SRC-21-002 e sezione pubblica corrispondente.

## Transizione 3. Maschera causale

- Ultima affermazione stabile: la sequenza di token e la distribuzione del prossimo elemento.
- Concetto nuovo: La causal mask impedisce a una posizione di usare target futuri. Un errore nella maschera produce leakage pur con loss numericamente valida.
- Input e shape: un prefisso di tre token e una mask causale.
- Operazione: fattorizzazione, teacher forcing e decoding.
- Output e shape: logits, token scelto e traiettoria.
- Che cosa cambia: il passaggio specifico di «Maschera causale».
- Invariante: nessuna posizione futura entra nella predizione causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due passi di teacher forcing confrontati con un passo campionato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sampling e accumulo degli errori.
- Prova: SRC-21-003 e sezione pubblica corrispondente.

## Transizione 4. Sampling e accumulo degli errori

- Ultima affermazione stabile: la sequenza di token e la distribuzione del prossimo elemento.
- Concetto nuovo: Ogni scelta modifica il contesto successivo. Errori iniziali possono spostare la traiettoria verso regioni poco viste nel training.
- Input e shape: un prefisso di tre token e una mask causale.
- Operazione: fattorizzazione, teacher forcing e decoding.
- Output e shape: logits, token scelto e traiettoria.
- Che cosa cambia: il passaggio specifico di «Sampling e accumulo degli errori».
- Invariante: nessuna posizione futura entra nella predizione causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due passi di teacher forcing confrontati con un passo campionato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Immagini, audio e token discreti.
- Prova: SRC-21-004 e sezione pubblica corrispondente.

## Transizione 5. Immagini, audio e token discreti

- Ultima affermazione stabile: la sequenza di token e la distribuzione del prossimo elemento.
- Concetto nuovo: L'autoregressione non è limitata al testo. Una sequenza può rappresentare pixel, code audio o latent discreti.
- Input e shape: un prefisso di tre token e una mask causale.
- Operazione: fattorizzazione, teacher forcing e decoding.
- Output e shape: logits, token scelto e traiettoria.
- Che cosa cambia: il passaggio specifico di «Immagini, audio e token discreti».
- Invariante: nessuna posizione futura entra nella predizione causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due passi di teacher forcing confrontati con un passo campionato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Variational Autoencoder e latent discreti.
- Prova: SRC-21-001 e sezione pubblica corrispondente.
