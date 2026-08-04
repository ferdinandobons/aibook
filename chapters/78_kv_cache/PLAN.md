# Piano interno. Capitolo 78

- Domanda centrale: quale contratto costruisce KV cache e riuso del contesto?
- Oggetto continuo: blocchi di KV cache associati a una richiesta; input guida: layer, token, KV dimension, dtype e prefix.
- Prerequisito stabile: Capitolo 77, Speculative e parallel decoding.
- Gap: prefill, decode, paging, caching ed eviction.
- Output consegnato: cache occupata, hit e latenza; consumer successivo: Capitolo 79, Serving, batching e scheduling.
- Invariante principale: la cache deve rispettare ownership, posizione e validità del prefisso.
- Visuali: CACHE-01 e CACHE-02, con famiglie compositive variabili.
- Snippet: code/snip_78_contract.py; output: code/outputs/SNIP-78-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Prefill e decode

- Ultima affermazione stabile: blocchi di KV cache associati a una richiesta.
- Concetto nuovo: Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache precedente.
- Input e shape: layer, token, KV dimension, dtype e prefix.
- Operazione: prefill, decode, paging, caching ed eviction.
- Output e shape: cache occupata, hit e latenza.
- Che cosa cambia: il passaggio specifico di «Prefill e decode».
- Invariante: la cache deve rispettare ownership, posizione e validità del prefisso.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due richieste condividono un prefisso e divergono al terzo token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Layout.
- Prova: SRC-78-001 e sezione pubblica corrispondente.

## Transizione 2. Layout

- Ultima affermazione stabile: blocchi di KV cache associati a una richiesta.
- Concetto nuovo: Layer, batch, KV head, token e head dimension determinano shape e byte. Contiguità e paginazione influenzano il kernel.
- Input e shape: layer, token, KV dimension, dtype e prefix.
- Operazione: prefill, decode, paging, caching ed eviction.
- Output e shape: cache occupata, hit e latenza.
- Che cosa cambia: il passaggio specifico di «Layout».
- Invariante: la cache deve rispettare ownership, posizione e validità del prefisso.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due richieste condividono un prefisso e divergono al terzo token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: PagedAttention.
- Prova: SRC-78-002 e sezione pubblica corrispondente.

## Transizione 3. PagedAttention

- Ultima affermazione stabile: blocchi di KV cache associati a una richiesta.
- Concetto nuovo: Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare sequenze di lunghezza diversa.
- Input e shape: layer, token, KV dimension, dtype e prefix.
- Operazione: prefill, decode, paging, caching ed eviction.
- Output e shape: cache occupata, hit e latenza.
- Che cosa cambia: il passaggio specifico di «PagedAttention».
- Invariante: la cache deve rispettare ownership, posizione e validità del prefisso.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due richieste condividono un prefisso e divergono al terzo token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Prefix caching.
- Prova: SRC-78-003 e sezione pubblica corrispondente.

## Transizione 4. Prefix caching

- Ultima affermazione stabile: blocchi di KV cache associati a una richiesta.
- Concetto nuovo: Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi sono compatibili.
- Input e shape: layer, token, KV dimension, dtype e prefix.
- Operazione: prefill, decode, paging, caching ed eviction.
- Output e shape: cache occupata, hit e latenza.
- Che cosa cambia: il passaggio specifico di «Prefix caching».
- Invariante: la cache deve rispettare ownership, posizione e validità del prefisso.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due richieste condividono un prefisso e divergono al terzo token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Compressione ed eviction.
- Prova: SRC-78-004 e sezione pubblica corrispondente.

## Transizione 5. Compressione ed eviction

- Ultima affermazione stabile: blocchi di KV cache associati a una richiesta.
- Concetto nuovo: Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano precisione o contesto disponibile.
- Input e shape: layer, token, KV dimension, dtype e prefix.
- Operazione: prefill, decode, paging, caching ed eviction.
- Output e shape: cache occupata, hit e latenza.
- Che cosa cambia: il passaggio specifico di «Compressione ed eviction».
- Invariante: la cache deve rispettare ownership, posizione e validità del prefisso.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due richieste condividono un prefisso e divergono al terzo token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Serving, batching e scheduling.
- Prova: SRC-78-001 e sezione pubblica corrispondente.
