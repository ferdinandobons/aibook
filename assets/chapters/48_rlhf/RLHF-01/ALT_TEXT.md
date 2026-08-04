# Testo alternativo

RLHF-01, Preferenze, reward model e RLHF. Come si passa da «Dalle dimostrazioni alle preferenze» a «Policy optimization» mantenendo osservabile dimostrazioni, preferenze, reward model e policy? La composizione preference pipeline collega «Dalle dimostrazioni alle preferenze», «Reward model», «Policy optimization». L'input è prompt, risposta scelta, rifiutata e score; l'output è reward, log-probability e comportamento aggiornato. Il limite esplicito è: il reward è un proxy e può essere ottimizzato in modo scorretto.
