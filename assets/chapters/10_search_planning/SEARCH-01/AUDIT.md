# Audit visuale `SEARCH-01`

## Stato

- Esito: **aperto**
- PNG nel branch: no
- Approvazione tecnica: no
- Approvazione autoriale: no

## Iterazione image-gen

Respinta perché rappresentava una dashboard sullo stato del libro e inventava capitoli completati. Non rispondeva alla domanda su uniform-cost e A*.

## Renderer raster

`scripts/generate_search_visuals.py` contiene una prima composizione deterministica. Prima della pubblicazione occorre controllare sul raster:

- assenza di archi che attraversano nodi;
- leggibilità dei costi;
- corrispondenza tra grafo e snippet;
- ordine di espansione completo;
- visibilità del cammino ottimo;
- assenza di false gerarchie;
- testo e padding.

## Gate

La figura non può essere referenziata in `CHAPTER.md` finché il raster non viene materializzato, aperto e revisionato almeno due volte in caso di difetti.
