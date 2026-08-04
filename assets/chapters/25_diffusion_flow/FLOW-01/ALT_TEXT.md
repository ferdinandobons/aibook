# Testo alternativo

FLOW-01, Diffusione, score matching e flow matching. Come si passa da «Corrompere e ricostruire» a «Parametrizzazioni epsilon, x0 e v» mantenendo osservabile un dato corrotto e il percorso di denoising? La composizione noise path collega «Corrompere e ricostruire», «Score matching», «Parametrizzazioni epsilon, x0 e v». L'input è x_0, rumore epsilon e timestep t; l'output è stima del rumore e campione ricostruito. Il limite esplicito è: parametrizzazione e scheduler fanno parte del contratto.
