# Testo alternativo

DIST-01, Training distribuito e continued pretraining. Come si passa da «Data parallelism» a «Tensor e pipeline parallelism» mantenendo osservabile gradienti e stato distribuiti tra worker? La composizione parallel topology collega «Data parallelism», «ZeRO e FSDP», «Tensor e pipeline parallelism». L'input è microbatch, worker, shard e topologia; l'output è gradiente ridotto, stato sincronizzato e fault osservato. Il limite esplicito è: la riduzione e il conteggio del batch devono essere dichiarati.
