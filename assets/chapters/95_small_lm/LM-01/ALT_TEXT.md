# Testo alternativo

LM-01, Costruire un piccolo language model. Come si passa da «Corpus e tokenizer» a «Training» mantenendo osservabile un piccolo language model dalla stringa ai logits? La composizione small lm stack collega «Corpus e tokenizer», «Decoder Transformer», «Training». L'input è corpus, tokenizer, batch di sequenze e target; l'output è logits, loss, token generati e checkpoint. Il limite esplicito è: tokenizer, mask, target shift e sampling devono essere coerenti.
