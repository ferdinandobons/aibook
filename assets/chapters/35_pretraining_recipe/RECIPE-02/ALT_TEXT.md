# Testo alternativo

RECIPE-02, La ricetta di pretraining. Quale controllo collega «Warmup e schedule» a «Checkpoint e recovery» senza superare il limite dichiarato? La composizione run trace collega «Warmup e schedule», «Checkpoint e recovery». L'input è batch, learning rate, seed, optimizer e checkpoint; l'output è loss, parametri e checkpoint ripristinabile. Il limite esplicito è: un checkpoint deve includere lo stato necessario a continuare il run.
