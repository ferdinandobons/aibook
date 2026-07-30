# Alt text ATT-02

Diagramma orizzontale in sei passaggi. La query `q=[1,0]` è affiancata a tre coppie key-value: `[1,0]`, `[0,1]` e `[1,1]`. Il prodotto `qK^T` produce il vettore di score `[1,0,1]`, di shape `[1×3]`. La divisione per `sqrt(2)` produce `[0,707,0,000,0,707]`. La softmax produce i pesi `α₁=0,401`, `α₂=0,198`, `α₃=0,401`, che sommano a `1,000`. La somma `0,401·[1,0] + 0,198·[0,1] + 0,401·[1,1]` produce l'output `[0,802; 0,599]`, di shape `[d_v]=[2]`.
