# Testo alternativo

PEFT-01, Fine-tuning efficiente. Come si passa da «Parametri congelati e adattamento» a «LoRA» mantenendo osservabile l'aggiornamento adattivo rispetto ai pesi congelati? La composizione low rank update collega «Parametri congelati e adattamento», «Adapter», «LoRA». L'input è peso W, matrice A e B, rank e quantizzazione; l'output è delta W e checkpoint adattatore. Il limite esplicito è: il delta non è il modello completo e va valutato sullo stesso base model.
