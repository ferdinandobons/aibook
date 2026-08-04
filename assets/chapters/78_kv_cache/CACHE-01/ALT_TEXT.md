# Testo alternativo

CACHE-01, KV cache e riuso del contesto. Come si passa da «Prefill e decode» a «PagedAttention» mantenendo osservabile blocchi di KV cache associati a una richiesta? La composizione cache layout collega «Prefill e decode», «Layout», «PagedAttention». L'input è layer, token, KV dimension, dtype e prefix; l'output è cache occupata, hit e latenza. Il limite esplicito è: la cache deve rispettare ownership, posizione e validità del prefisso.
