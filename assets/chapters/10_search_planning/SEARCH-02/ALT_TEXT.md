# Alt text previsto `SEARCH-02`

Albero di gioco verticale su sfondo bianco. La radice `MAX` ha valore 4 e tre figli `MIN`: A riceve le foglie 3 e 5 e vale 3; B riceve le foglie 2 e 9 e vale 2; C riceve due foglie di valore 4 e vale 4. Dopo aver valutato A, alpha è 3. Nel ramo B, la prima foglia vale 2, quindi la seconda foglia, 9, è marcata come potata perché non può rendere B preferibile ad A per MAX. Minimax visita sei foglie, alpha-beta cinque, e entrambi restituiscono valore 4.

Stato: da verificare sul raster effettivo.
