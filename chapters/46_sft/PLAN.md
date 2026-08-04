# Piano interno. Capitolo 46

- Domanda centrale: quale contratto costruisce Supervised fine-tuning e instruction tuning?
- Oggetto continuo: una coppia prompt-risposta nel formato di instruction tuning; input guida: messaggi, target, mask delle label e mixture.
- Prerequisito stabile: Capitolo 45, Byte, predizione multi-token e language diffusion.
- Gap: teacher forcing e aggiornamento supervisionato.
- Output consegnato: loss per token e comportamento adattato; consumer successivo: Capitolo 47, Fine-tuning efficiente.
- Invariante principale: il formato dei dati e le label decidono che cosa viene ottimizzato.
- Visuali: SFT-01 e SFT-02, con famiglie compositive variabili.
- Snippet: code/snip_46_contract.py; output: code/outputs/SNIP-46-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Dal pretraining alle istruzioni

- Ultima affermazione stabile: una coppia prompt-risposta nel formato di instruction tuning.
- Concetto nuovo: Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate.
- Input e shape: messaggi, target, mask delle label e mixture.
- Operazione: teacher forcing e aggiornamento supervisionato.
- Output e shape: loss per token e comportamento adattato.
- Che cosa cambia: il passaggio specifico di «Dal pretraining alle istruzioni».
- Invariante: il formato dei dati e le label decidono che cosa viene ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un messaggio utente e una risposta con loss solo sulla risposta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Formati conversazionali.
- Prova: SRC-46-001 e sezione pubblica corrispondente.

## Transizione 2. Formati conversazionali

- Ultima affermazione stabile: una coppia prompt-risposta nel formato di instruction tuning.
- Concetto nuovo: Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente.
- Input e shape: messaggi, target, mask delle label e mixture.
- Operazione: teacher forcing e aggiornamento supervisionato.
- Output e shape: loss per token e comportamento adattato.
- Che cosa cambia: il passaggio specifico di «Formati conversazionali».
- Invariante: il formato dei dati e le label decidono che cosa viene ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un messaggio utente e una risposta con loss solo sulla risposta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Instruction mixture.
- Prova: SRC-46-002 e sezione pubblica corrispondente.

## Transizione 3. Instruction mixture

- Ultima affermazione stabile: una coppia prompt-risposta nel formato di instruction tuning.
- Concetto nuovo: Compiti e domini vengono mescolati con pesi espliciti. La quantità di esempi non coincide automaticamente con il loro contributo utile.
- Input e shape: messaggi, target, mask delle label e mixture.
- Operazione: teacher forcing e aggiornamento supervisionato.
- Output e shape: loss per token e comportamento adattato.
- Che cosa cambia: il passaggio specifico di «Instruction mixture».
- Invariante: il formato dei dati e le label decidono che cosa viene ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un messaggio utente e una risposta con loss solo sulla risposta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Teacher forcing e generalizzazione.
- Prova: SRC-46-003 e sezione pubblica corrispondente.

## Transizione 4. Teacher forcing e generalizzazione

- Ultima affermazione stabile: una coppia prompt-risposta nel formato di instruction tuning.
- Concetto nuovo: Durante il training il modello vede il prefisso corretto. La capacità di seguire istruzioni nuove deve essere valutata su template e domini separati.
- Input e shape: messaggi, target, mask delle label e mixture.
- Operazione: teacher forcing e aggiornamento supervisionato.
- Output e shape: loss per token e comportamento adattato.
- Che cosa cambia: il passaggio specifico di «Teacher forcing e generalizzazione».
- Invariante: il formato dei dati e le label decidono che cosa viene ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un messaggio utente e una risposta con loss solo sulla risposta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Catastrophic forgetting e controllo.
- Prova: SRC-46-004 e sezione pubblica corrispondente.

## Transizione 5. Catastrophic forgetting e controllo

- Ultima affermazione stabile: una coppia prompt-risposta nel formato di instruction tuning.
- Concetto nuovo: Learning rate, durata e replay influenzano la perdita di capacità precedenti. Base model, modello SFT e sistema devono restare identificabili.
- Input e shape: messaggi, target, mask delle label e mixture.
- Operazione: teacher forcing e aggiornamento supervisionato.
- Output e shape: loss per token e comportamento adattato.
- Che cosa cambia: il passaggio specifico di «Catastrophic forgetting e controllo».
- Invariante: il formato dei dati e le label decidono che cosa viene ottimizzato.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un messaggio utente e una risposta con loss solo sulla risposta; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Fine-tuning efficiente.
- Prova: SRC-46-001 e sezione pubblica corrispondente.
