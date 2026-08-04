# Piano interno. Capitolo 29

- Domanda centrale: quale contratto costruisce Il Transformer da zero?
- Oggetto continuo: lo stato nascosto che attraversa il blocco Transformer; input guida: tokenizzati di shape [batch, length] e vettori [batch, length, d].
- Prerequisito stabile: Capitolo 28, Il meccanismo di attention.
- Gap: embedding, attention, MLP e residuo.
- Output consegnato: stato contestuale e logits; consumer successivo: Capitolo 30, Famiglie architetturali e obiettivi di pretraining.
- Invariante principale: mask, shape e percorso residuale devono essere compatibili.
- Visuali: TRANSFOR-01 e TRANSFOR-02, con famiglie compositive variabili.
- Snippet: code/snip_29_contract.py; output: code/outputs/SNIP-29-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. La mappa completa

- Ultima affermazione stabile: lo stato nascosto che attraversa il blocco Transformer.
- Concetto nuovo: Il Transformer combina embedding, posizione, attention, feed-forward, residual e normalizzazione. Ogni componente mantiene un contratto di shape.
- Input e shape: tokenizzati di shape [batch, length] e vettori [batch, length, d].
- Operazione: embedding, attention, MLP e residuo.
- Output e shape: stato contestuale e logits.
- Che cosa cambia: il passaggio specifico di «La mappa completa».
- Invariante: mask, shape e percorso residuale devono essere compatibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un blocco con due token e due dimensioni nascoste; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Encoder.
- Prova: SRC-29-001 e sezione pubblica corrispondente.

## Transizione 2. Encoder

- Ultima affermazione stabile: lo stato nascosto che attraversa il blocco Transformer.
- Concetto nuovo: L'encoder usa self-attention bidirezionale e produce rappresentazioni per tutte le posizioni.
- Input e shape: tokenizzati di shape [batch, length] e vettori [batch, length, d].
- Operazione: embedding, attention, MLP e residuo.
- Output e shape: stato contestuale e logits.
- Che cosa cambia: il passaggio specifico di «Encoder».
- Invariante: mask, shape e percorso residuale devono essere compatibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un blocco con due token e due dimensioni nascoste; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Decoder.
- Prova: SRC-29-002 e sezione pubblica corrispondente.

## Transizione 3. Decoder

- Ultima affermazione stabile: lo stato nascosto che attraversa il blocco Transformer.
- Concetto nuovo: Il decoder usa self-attention causale e, nelle architetture encoder-decoder, cross-attention verso l'encoder.
- Input e shape: tokenizzati di shape [batch, length] e vettori [batch, length, d].
- Operazione: embedding, attention, MLP e residuo.
- Output e shape: stato contestuale e logits.
- Che cosa cambia: il passaggio specifico di «Decoder».
- Invariante: mask, shape e percorso residuale devono essere compatibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un blocco con due token e due dimensioni nascoste; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Multi-head attention.
- Prova: SRC-29-003 e sezione pubblica corrispondente.

## Transizione 4. Multi-head attention

- Ultima affermazione stabile: lo stato nascosto che attraversa il blocco Transformer.
- Concetto nuovo: Le head applicano proiezioni differenti e vengono concatenate. La proiezione finale riporta alla dimensione del modello.
- Input e shape: tokenizzati di shape [batch, length] e vettori [batch, length, d].
- Operazione: embedding, attention, MLP e residuo.
- Output e shape: stato contestuale e logits.
- Che cosa cambia: il passaggio specifico di «Multi-head attention».
- Invariante: mask, shape e percorso residuale devono essere compatibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un blocco con due token e due dimensioni nascoste; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Residual stream e output.
- Prova: SRC-29-004 e sezione pubblica corrispondente.

## Transizione 5. Residual stream e output

- Ultima affermazione stabile: lo stato nascosto che attraversa il blocco Transformer.
- Concetto nuovo: Layer ripetuti aggiornano il residual stream. La head di output trasforma la rappresentazione in logits sul vocabolario.
- Input e shape: tokenizzati di shape [batch, length] e vettori [batch, length, d].
- Operazione: embedding, attention, MLP e residuo.
- Output e shape: stato contestuale e logits.
- Che cosa cambia: il passaggio specifico di «Residual stream e output».
- Invariante: mask, shape e percorso residuale devono essere compatibili.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un blocco con due token e due dimensioni nascoste; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Famiglie architetturali e obiettivi di pretraining.
- Prova: SRC-29-001 e sezione pubblica corrispondente.
