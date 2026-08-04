# Testo alternativo

LM-02, Costruire un piccolo language model. Quale controllo collega «Sampling» a «Limiti» senza superare il limite dichiarato? La composizione training evidence collega «Sampling», «Limiti». L'input è corpus, tokenizer, batch di sequenze e target; l'output è logits, loss, token generati e checkpoint. Il limite esplicito è: tokenizer, mask, target shift e sampling devono essere coerenti.
