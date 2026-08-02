# Claim

- `CL-GEOMETRI-001`. Condivisione locale dei pesi: Una convoluzione applica lo stesso kernel in posizioni differenti. Questa condivisione incorpora una ipotesi di regolarità locale.
- `CL-GEOMETRI-002`. Stride, padding e receptive field: Stride e padding determinano la griglia dell'output. Il receptive field cresce con layer, kernel e dilatazione.
- `CL-GEOMETRI-003`. Equivarianza e invariance: La convoluzione è equivariant a traslazioni entro le condizioni del bordo. Pooling e aggregazione possono costruire una maggiore invariance.
- `CL-GEOMETRI-004`. Vision Transformer e ibridi: Patch embedding e attention offrono una geometria diversa. CNN e Transformer possono essere combinati, ma il confronto richiede stesso budget e dati.
- `CL-GEOMETRI-005`. Grafi e message passing: Su un grafo, i vicini non sono disposti in una griglia regolare. Le GNN aggregano messaggi rispettando la struttura degli archi e le simmetrie dichiarate.
