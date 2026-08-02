# Claim

- `CL-DATA-001`. Unicode e byte: Il testo è una sequenza di code point codificata in byte. Normalizzazione Unicode e decoding devono essere dichiarati.
- `CL-DATA-002`. Tokenizzazione: BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti. Il tokenizer fa parte dell'interfaccia del checkpoint.
- `CL-DATA-003`. Token speciali: BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi. ID uguali richiedono la stessa convenzione.
- `CL-DATA-004`. Packing e confini: Più documenti possono condividere una sequenza. Attention mask e loss mask devono impedire dipendenze non desiderate.
- `CL-DATA-005`. Lunghezza, lingua e costi: Token per carattere variano tra lingue e formati. La lunghezza in token influenza contesto, costo e valutazione.
