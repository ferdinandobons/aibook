# Testo alternativo

SFT-01, Supervised fine-tuning e instruction tuning. Come si passa da «Dal pretraining alle istruzioni» a «Instruction mixture» mantenendo osservabile una coppia prompt-risposta nel formato di instruction tuning? La composizione loss mask collega «Dal pretraining alle istruzioni», «Formati conversazionali», «Instruction mixture». L'input è messaggi, target, mask delle label e mixture; l'output è loss per token e comportamento adattato. Il limite esplicito è: il formato dei dati e le label decidono che cosa viene ottimizzato.
