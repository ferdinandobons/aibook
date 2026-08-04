# Testo alternativo

DECODING-01, Speculative e parallel decoding. Come si passa da «Draft e target» a «Speedup» mantenendo osservabile draft e target durante il decoding speculativo? La composizione draft verify collega «Draft e target», «Acceptance», «Speedup». L'input è token proposti, logits draft e logits target; l'output è token accettati, velocità e distribuzione preservata. Il limite esplicito è: lo speedup richiede verifica senza cambiare il contratto di output.
