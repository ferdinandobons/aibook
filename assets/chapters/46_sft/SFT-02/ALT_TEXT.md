# Testo alternativo

SFT-02, Supervised fine-tuning e instruction tuning. Quale controllo collega «Teacher forcing e generalizzazione» a «Catastrophic forgetting e controllo» senza superare il limite dichiarato? La composizione supervision pipeline collega «Teacher forcing e generalizzazione», «Catastrophic forgetting e controllo». L'input è messaggi, target, mask delle label e mixture; l'output è loss per token e comportamento adattato. Il limite esplicito è: il formato dei dati e le label decidono che cosa viene ottimizzato.
