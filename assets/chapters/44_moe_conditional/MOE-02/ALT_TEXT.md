# Testo alternativo

MOE-02, Mixture of Experts e calcolo condizionale. Quale controllo collega «Expert parallelism» a «Parametri totali e attivi» senza superare il limite dichiarato? La composizione capacity gate collega «Expert parallelism», «Parametri totali e attivi». L'input è logits del router, top-k e capacità per esperto; l'output è carico, token restituiti e costo attivo. Il limite esplicito è: parametri totali e parametri attivi non sono la stessa quantità.
