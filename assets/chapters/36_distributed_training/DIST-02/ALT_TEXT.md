# Testo alternativo

DIST-02, Training distribuito e continued pretraining. Quale controllo collega «Topologia e fault tolerance» a «Continued pretraining» senza superare il limite dichiarato? La composizione communication graph collega «Topologia e fault tolerance», «Continued pretraining». L'input è microbatch, worker, shard e topologia; l'output è gradiente ridotto, stato sincronizzato e fault osservato. Il limite esplicito è: la riduzione e il conteggio del batch devono essere dichiarati.
