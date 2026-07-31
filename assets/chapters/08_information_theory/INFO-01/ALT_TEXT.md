# Alt text `INFO-01`

Confronto in due righe su sfondo bianco. In entrambe il target è la classe zero. La riga superiore usa logits `[2,0; 0,5; -1,0]`, produce probabilità `[0,7856; 0,1753; 0,0391]`, assegna `0,785597` alla classe target e ottiene NLL `0,241311`. La riga inferiore permuta i logits in `[-1,0; 0,5; 2,0]`, assegna soltanto `0,039113` alla classe target e ottiene NLL `3,241311`. Un footer chiarisce che le due distribuzioni hanno la stessa entropia, ma cross-entropy diversa perché il target resta la classe zero.
