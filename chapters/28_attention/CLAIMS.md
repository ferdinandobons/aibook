# Registro delle affermazioni. Capitolo 28

| ID | Affermazione portante | Tipo | Fonte o prova | Esito |
|---|---|---|---|---|
| `CLM-ATT-001` | Coefficienti fissi producono la stessa combinazione per posizioni diverse; `ATT-01` usa questo confronto come esempio illustrativo. | illustrativo/confine | `ATT-01/SPEC.md` | verificata |
| `CLM-ATT-002` | La scaled dot-product attention calcola `softmax(QK^T/sqrt(d_k))V`. | fonte primaria | `SRC-ATT-001`, §3.2.1 | verificata |
| `CLM-ATT-003` | Il fattore `1/sqrt(d_k)` è introdotto per contrastare prodotti scalari di grande magnitudine e regioni softmax con gradienti molto piccoli. | fonte primaria | `SRC-ATT-001`, §3.2.1 | verificata |
| `CLM-ATT-004` | La softmax produce coefficienti non negativi che sommano a 1 quando la riga contiene almeno un logit finito e non si considera dropout successivo. | derivazione | definizione softmax; test `SNIP-ATT-001/002` | verificata |
| `CLM-ATT-005` | L'output ha una riga per query e dimensione finale `d_v`. | derivazione | algebra delle shape; test `SNIP-ATT-002` | verificata |
| `CLM-ATT-006` | Una mask additiva viene sommata agli score prima della softmax. | fonte primaria/API | `SRC-ATT-001`, `SRC-ATT-003` | verificata |
| `CLM-ATT-007` | In `F.scaled_dot_product_attention`, `True` indica una posizione ammessa. | documentazione ufficiale | `SRC-ATT-003` | verificata |
| `CLM-ATT-008` | In `MultiheadAttention.key_padding_mask`, `True` indica una posizione da ignorare. | documentazione ufficiale | `SRC-ATT-004` | verificata |
| `CLM-ATT-009` | La realizzazione materializzata conserva score o coefficienti di shape `[L,S]`; con `L=S=n` l'intermedio ha `n^2` elementi. | derivazione | algebra delle shape | verificata |
| `CLM-ATT-010` | L'esempio produce coefficienti `[0.40111209, 0.19777581, 0.40111209]` e output `[0.80222418, 0.59888791]`. | risultato eseguito | `test_single_query_values` | verificata |
| `CLM-ATT-011` | Il codice diretto coincide con `F.scaled_dot_product_attention` nell'ambiente dichiarato con `dropout_p=0.0`. | risultato eseguito | `SNIP-ATT-002`, test | verificata |
| `CLM-ATT-012` | La causal mask dell'esempio annulla i coefficienti delle posizioni future. | risultato eseguito | `SNIP-ATT-003`, test | verificata |
| `CLM-ATT-013` | L'operatore base non inserisce da solo informazione posizionale. | derivazione | equivarianza a permutazioni coerenti esposta nel testo | verificata |
| `CLM-ATT-014` | `ATT-02` usa numeri illustrativi che coincidono con l'esecuzione di `SNIP-ATT-001`. | illustrativo + esecuzione | immagine e test | verificata |
