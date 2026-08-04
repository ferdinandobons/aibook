# Testo alternativo

OPT-01, Ottimizzazione diretta delle preferenze. Come si passa da «Evitare un reward model esplicito» a «Temperatura beta» mantenendo osservabile una coppia chosen-rejected per l'ottimizzazione diretta? La composizione pairwise objective collega «Evitare un reward model esplicito», «Coppie chosen e rejected», «Temperatura beta». L'input è prompt, log-probability della policy e riferimento; l'output è loss di preferenza e policy aggiornata. Il limite esplicito è: la preferenza osservata non è una verità assoluta.
