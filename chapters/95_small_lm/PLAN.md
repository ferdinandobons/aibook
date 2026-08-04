# Piano interno. Capitolo 95

- Domanda centrale: quale contratto costruisce Costruire un piccolo language model?
- Oggetto continuo: un piccolo language model dalla stringa ai logits; input guida: corpus, tokenizer, batch di sequenze e target.
- Prerequisito stabile: Capitolo 94, Percorso pratico dai fondamenti.
- Gap: embedding, decoder causale, cross-entropy e sampling.
- Output consegnato: logits, loss, token generati e checkpoint; consumer successivo: Capitolo 96, Progetto di produzione completo.
- Invariante principale: tokenizer, mask, target shift e sampling devono essere coerenti.
- Visuali: LM-01 e LM-02, con famiglie compositive variabili.
- Snippet: code/snip_95_contract.py; output: code/outputs/SNIP-95-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Corpus e tokenizer

- Ultima affermazione stabile: un piccolo language model dalla stringa ai logits.
- Concetto nuovo: Un corpus ridotto e un tokenizer identificabile costruiscono sequenze e split verificabili.
- Input e shape: corpus, tokenizer, batch di sequenze e target.
- Operazione: embedding, decoder causale, cross-entropy e sampling.
- Output e shape: logits, loss, token generati e checkpoint.
- Che cosa cambia: il passaggio specifico di «Corpus e tokenizer».
- Invariante: tokenizer, mask, target shift e sampling devono essere coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due sequenze, target spostato di un token e loss calcolata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Decoder Transformer.
- Prova: SRC-95-001 e sezione pubblica corrispondente.

## Transizione 2. Decoder Transformer

- Ultima affermazione stabile: un piccolo language model dalla stringa ai logits.
- Concetto nuovo: Embedding, posizione, causal attention, MLP, norm e head di output vengono assemblati con test di shape.
- Input e shape: corpus, tokenizer, batch di sequenze e target.
- Operazione: embedding, decoder causale, cross-entropy e sampling.
- Output e shape: logits, loss, token generati e checkpoint.
- Che cosa cambia: il passaggio specifico di «Decoder Transformer».
- Invariante: tokenizer, mask, target shift e sampling devono essere coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due sequenze, target spostato di un token e loss calcolata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Training.
- Prova: SRC-95-002 e sezione pubblica corrispondente.

## Transizione 3. Training

- Ultima affermazione stabile: un piccolo language model dalla stringa ai logits.
- Concetto nuovo: AdamW, schedule, gradient clipping e checkpoint producono un run riproducibile su CPU o singola GPU.
- Input e shape: corpus, tokenizer, batch di sequenze e target.
- Operazione: embedding, decoder causale, cross-entropy e sampling.
- Output e shape: logits, loss, token generati e checkpoint.
- Che cosa cambia: il passaggio specifico di «Training».
- Invariante: tokenizer, mask, target shift e sampling devono essere coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due sequenze, target spostato di un token e loss calcolata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sampling.
- Prova: SRC-95-003 e sezione pubblica corrispondente.

## Transizione 4. Sampling

- Ultima affermazione stabile: un piccolo language model dalla stringa ai logits.
- Concetto nuovo: Greedy, temperature e top-k mostrano la differenza tra distribuzione e traiettoria.
- Input e shape: corpus, tokenizer, batch di sequenze e target.
- Operazione: embedding, decoder causale, cross-entropy e sampling.
- Output e shape: logits, loss, token generati e checkpoint.
- Che cosa cambia: il passaggio specifico di «Sampling».
- Invariante: tokenizer, mask, target shift e sampling devono essere coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due sequenze, target spostato di un token e loss calcolata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Limiti.
- Prova: SRC-95-004 e sezione pubblica corrispondente.

## Transizione 5. Limiti

- Ultima affermazione stabile: un piccolo language model dalla stringa ai logits.
- Concetto nuovo: Un piccolo LM non rappresenta capacità o sicurezza di modelli su larga scala, ma rende osservabile l'intero contratto.
- Input e shape: corpus, tokenizer, batch di sequenze e target.
- Operazione: embedding, decoder causale, cross-entropy e sampling.
- Output e shape: logits, loss, token generati e checkpoint.
- Che cosa cambia: il passaggio specifico di «Limiti».
- Invariante: tokenizer, mask, target shift e sampling devono essere coerenti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due sequenze, target spostato di un token e loss calcolata; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Progetto di produzione completo.
- Prova: SRC-95-001 e sezione pubblica corrispondente.
