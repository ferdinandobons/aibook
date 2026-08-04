# Testo alternativo

AUTOREGR-02, Modelli autoregressivi. Quale controllo collega «Sampling e accumulo degli errori» a «Immagini, audio e token discreti» senza superare il limite dichiarato? La composizione sampling tree collega «Sampling e accumulo degli errori», «Immagini, audio e token discreti». L'input è un prefisso di tre token e una mask causale; l'output è logits, token scelto e traiettoria. Il limite esplicito è: nessuna posizione futura entra nella predizione causale.
