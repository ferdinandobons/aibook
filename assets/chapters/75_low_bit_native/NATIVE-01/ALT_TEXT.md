# Testo alternativo

NATIVE-01, Modelli low-bit nativi e co-design numerico. Come si passa da «Training nativo» a «Straight-through estimator» mantenendo osservabile un peso low-bit e il suo accumulo numerico? La composizione low bit path collega «Training nativo», «Pesi ternari e 1.58-bit», «Straight-through estimator». L'input è peso reale, codice ternario, scala e attivazione; l'output è peso ricostruito, gradiente e costo hardware. Il limite esplicito è: bit nominali e precisione effettiva dell'accumulo sono distinti.
