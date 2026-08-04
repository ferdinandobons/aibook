# Testo alternativo

MOE-01, Mixture of Experts e calcolo condizionale. Come si passa da «Router top-k» a «Load balancing» mantenendo osservabile token e assegnazioni del router agli esperti? La composizione expert router collega «Router top-k», «Capacità», «Load balancing». L'input è logits del router, top-k e capacità per esperto; l'output è carico, token restituiti e costo attivo. Il limite esplicito è: parametri totali e parametri attivi non sono la stessa quantità.
