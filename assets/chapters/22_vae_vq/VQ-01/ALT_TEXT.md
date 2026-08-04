# Testo alternativo

VQ-01, Variational Autoencoder e latent discreti. Come si passa da «Inferenza approssimata» a «Reparameterization trick» mantenendo osservabile una variabile osservata e il suo codice latente? La composizione latent bottleneck collega «Inferenza approssimata», «ELBO», «Reparameterization trick». L'input è x, media, log-varianza e rumore epsilon; l'output è ricostruzione, KL e codice latente. Il limite esplicito è: la ricostruzione non elimina il costo KL né dimostra disentanglement.
