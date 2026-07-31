# Alt text `INFO-02`

Diagramma su sfondo bianco. A sinistra il target morbido `q=[0,90; 0,05; 0,05]` è rappresentato con tre barre. A destra la predizione `p=[0,7856; 0,1753; 0,0391]` usa altre tre barre. Entrambe le distribuzioni convergono in un box centrale con la cross-entropy `H(q,p)=0,466311`. Nella fascia inferiore, l'entropia del target `H(q)=0,394398` più la divergenza `KL(q||p)=0,071914` produce la stessa cross-entropy. Un footer indica che, con target one-hot, l'entropia del target è zero e cross-entropy, KL e negative log-likelihood coincidono.
