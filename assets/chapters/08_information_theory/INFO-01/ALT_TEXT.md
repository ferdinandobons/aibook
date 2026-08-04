# Alt text `INFO-01`

Confronto orizzontale tra due predizioni. Nella riga superiore i logits `[2,0]`, `[0,5]`, `[-1,0]` passano da softmax e assegnano alla classe target 0 la probabilità `0,785597`, producendo NLL `0,241311`. Nella riga inferiore i logits sono permutati: la classe target riceve `0,039113` e la NLL cresce a `3,241311`. Le barre mostrano le tre probabilità e il footer chiarisce che le distribuzioni hanno la stessa entropia, mentre la cross-entropy cambia perché il target resta la classe 0.

Stato: verificato su `candidate-v1.png`.

*** Delete File: /Users/ferdinandobons/Desktop/aibook/assets/chapters/08_information_theory/INFO-02/SPEC.md
