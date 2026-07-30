# Registro delle affermazioni. Capitolo 28

| ID | Affermazione portante | Tipo | Fonte o prova | Esito |
|---|---|---|---|---|
| `CLM-ATT-001` | La scaled dot-product attention calcola `softmax(QK^T/sqrt(d_k))V`. | fonte primaria | `SRC-ATT-001`, §3.2.1 | verificata |
| `CLM-ATT-002` | Il fattore `1/sqrt(d_k)` è introdotto per contrastare logit di grande magnitudine e gradienti softmax molto piccoli. | fonte primaria | `SRC-ATT-001`, §3.2.1 | verificata |
| `CLM-ATT-003` | La softmax per riga produce coefficienti non negativi che sommano a 1 se esiste almeno uno score finito e non viene applicato dropout. | derivazione | definizione softmax; test `SNIP-ATT-001/002` | verificata |
| `CLM-ATT-004` | L'output ha una riga per query e dimensione finale `d_v`. | derivazione | algebra delle shape; test `SNIP-ATT-002` | verificata |
| `CLM-ATT-005` | Una mask additiva viene sommata agli score prima della softmax. | fonte primaria/API | `SRC-ATT-001`, `SRC-ATT-004` | verificata |
| `CLM-ATT-006` | In `F.scaled_dot_product_attention`, `True` indica una posizione ammessa. | documentazione ufficiale | `SRC-ATT-004` | verificata |
| `CLM-ATT-007` | In `MultiheadAttention.key_padding_mask`, `True` indica una posizione da ignorare. | documentazione ufficiale | `SRC-ATT-005` | verificata |
| `CLM-ATT-008` | Le head vengono concatenate prima della proiezione `W^O`. | fonte primaria | `SRC-ATT-001`, §3.2.2 | verificata |
| `CLM-ATT-009` | La materializzazione standard degli score/pesi richiede un intermedio `[L,S]`; in self-attention quadrata è `O(n^2)`. | derivazione + fonte | shape; `SRC-ATT-006`, §2.2 | verificata |
| `CLM-ATT-010` | FlashAttention calcola attenzione esatta con un algoritmo IO-aware e riduce la materializzazione degli intermedi in HBM. | fonte primaria | `SRC-ATT-006`, §§1–3 | verificata |
| `CLM-ATT-011` | I valori dell'esempio singola-query sono `[0.40111209, 0.19777581, 0.40111209]` e output `[0.80222418, 0.59888791]`. | risultato eseguito | test `test_single_query_values` | verificata |
| `CLM-ATT-012` | Il codice da zero coincide con `F.scaled_dot_product_attention` nell'ambiente dichiarato e con `dropout_p=0`. | risultato eseguito | `SNIP-ATT-002`, test | verificata |
| `CLM-ATT-013` | La causal mask dell'esempio annulla i pesi delle posizioni future. | risultato eseguito | `SNIP-ATT-003`, test | verificata |
| `CLM-ATT-014` | Con `average_attn_weights=False`, l'esempio MHA produce pesi `[B,H,L,S]`. | documentazione + esecuzione | `SRC-ATT-005`, `SNIP-ATT-004` | verificata |
| `CLM-ATT-015` | L'operatore base non inserisce da solo informazione posizionale. | derivazione | equivarianza a permutazioni coerenti, esposta nel testo | verificata |
| `CLM-ATT-016` | La figura `ATT-01` mostra un requisito concettuale, non una implementazione del calcolo. | confine | `ATT-01/SPEC.md` | verificata |
| `CLM-ATT-017` | La figura `ATT-02` usa numeri illustrativi coerenti con `SNIP-ATT-001`. | illustrativo + esecuzione | immagine e test | verificata |
