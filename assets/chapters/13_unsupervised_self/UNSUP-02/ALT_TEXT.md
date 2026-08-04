# Alt text `UNSUP-02`

Pipeline orizzontale su sfondo bianco. Il dato originale `x=[a,b,c,d]` passa attraverso la maschera `m=[0,1,0,1]`, che nasconde `b` e `d`; l'input corrotto entra nell'encoder e nel decoder. La loss MSE è calcolata solo sulle posizioni mascherate, usando come target i valori originali. Un box inferiore precisa che la maschera costruisce il segnale di training ma non assegna un significato umano all'esempio.

Stato: verificato su `candidate-v1.png`.
