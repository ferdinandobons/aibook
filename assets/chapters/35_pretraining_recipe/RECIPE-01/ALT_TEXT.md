# Testo alternativo

RECIPE-01, La ricetta di pretraining. Come si passa da «Batch di token» a «AdamW» mantenendo osservabile lo stato completo di una ricetta di pretraining? La composizione recipe pipeline collega «Batch di token», «Inizializzazione», «AdamW». L'input è batch, learning rate, seed, optimizer e checkpoint; l'output è loss, parametri e checkpoint ripristinabile. Il limite esplicito è: un checkpoint deve includere lo stato necessario a continuare il run.
