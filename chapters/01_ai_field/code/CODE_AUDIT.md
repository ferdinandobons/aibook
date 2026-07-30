# Audit del codice. Capitolo 1

## Stato

- Data: 30 luglio 2026
- Python eseguito: `3.13.5`
- PyTorch eseguito: `2.10.0+cpu`
- Documentazione API ricontrollata: stable `2.13`
- Device: CPU
- Dtype: `torch.float32`
- Seed: `7`
- Esito: **superato tecnicamente per la bozza**

## Controlli statici

- [x] Import completi e minimi.
- [x] Nessuna dipendenza da notebook o stato esterno.
- [x] Seed dichiarato.
- [x] Input, target, modello, loss e optimizer espliciti.
- [x] Training ed inference separati.
- [x] `model.eval()` e `torch.inference_mode()` usati con ruoli distinti.
- [x] Nessun output inventato nel capitolo.

## Esecuzione

- [x] Script eseguito da processo pulito.
- [x] Loss iniziale: `0.641941`.
- [x] Loss finale: `0.045580`.
- [x] Almeno un parametro modificato dal training.
- [x] Nessun parametro modificato dall'inference.
- [x] Logit di inference con shape `[1,2]`.
- [x] Classe prevista: `0`.

## Test

- [x] `test_training_reduces_loss_and_updates_parameters`.
- [x] `test_inference_keeps_parameters_fixed`.
- [x] `test_inference_output_contract`.
- [x] Tre test superati.

## Coerenza con il capitolo

- [x] Il codice mostra soltanto il concetto già stabilizzato in prosa.
- [x] Le variabili coincidono con le descrizioni del testo.
- [x] Il risultato è dichiarato come esempio eseguito, non come benchmark.
- [x] La diminuzione della loss non viene presentata come prova di generalizzazione.

## Limiti

- Il dataset è illustrativo e contiene quattro esempi.
- Non esistono validation o test set separati.
- Il layer lineare non contiene Dropout o BatchNorm; `eval()` non cambia il suo forward, ma viene usato per mostrare il contratto corretto.
- Nessuna GPU disponibile nel run registrato.
- Nessuna esecuzione locale sotto PyTorch `2.13`.
- Piccole differenze numeriche possono apparire in altri ambienti o versioni; i test portanti verificano proprietà e shape.

## Esito finale

Il codice è approvato tecnicamente per la candidatura del capitolo. Una modifica del testo che cambi input, output o interpretazione riapre questo audit.
