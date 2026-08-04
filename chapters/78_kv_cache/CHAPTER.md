<!--
chapter_id: CH-P12-KV-CACHE
part_id: P12
order_key: 780
title: KV cache e riuso del contesto
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 78. KV cache e riuso del contesto

Per entrare in kv cache e riuso del contesto, seguiamo il passaggio che unisce «Prefill e decode» a «Compressione ed eviction». L'oggetto osservato è blocchi di KV cache associati a una richiesta. Il contratto locale dichiara input, layer, token, KV dimension, dtype e prefix; operazione, prefill, decode, paging, caching ed eviction; output, cache occupata, hit e latenza. Il primo esempio osservabile è Due richieste condividono un prefisso di due token e divergono al terzo. Il limite da non nascondere è: la cache deve rispettare ownership, posizione e validità del prefisso.

## Prefill e decode

Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache precedente. [SRC-78-001]

La cache cresce con lunghezza, layer, dimensione KV e dtype.

**Caso da seguire.** Due richieste condividono un prefisso di due token e divergono al terzo.

**Controllo.** Per «Prefill e decode», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Prefill e decode», il vincolo da conservare è: Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache precedente.


## Layout

Layer, batch, KV head, token e head dimension determinano shape e byte. Contiguità e paginazione influenzano il kernel. [SRC-78-002]

**Caso da seguire.** Due richieste condividono un prefisso e divergono al terzo token.

**Controllo.** Per «Layout», ricalcola il caso a mano e con lo snippet. Nel caso «Layout», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
memory = layers * tokens * kv_dim * bytes
$$

La cache cresce con lunghezza, layer, dimensione KV e dtype. [SRC-78-001]


![KV cache e riuso del contesto: queue](../../assets/chapters/78_kv_cache/CACHE-01/candidate-v48.png)

La prima figura segue il percorso da «Prefill e decode» a «PagedAttention».


## PagedAttention

Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare sequenze di lunghezza diversa. [SRC-78-003]

**Caso da seguire.** Un caso in cui la cache deve rispettare ownership, posizione e validità del prefisso.

**Controllo.** Per «PagedAttention», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «PagedAttention».


## Prefix caching

Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi sono compatibili. [SRC-78-004]

**Caso da seguire.** Ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo.

**Controllo.** Per «Prefix caching», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Prefix caching», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Questa sezione apre il contratto Python di kv cache e riuso del contesto: il lettore può eseguire lo stesso file e confrontare il risultato. Per «KV cache e riuso del contesto», il caso di default usa valori piccoli per isolare il meccanismo. Il caso non supportato viene provato separatamente, così «kv cache e riuso del contesto» non viene generalizzato oltre l'esempio.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    prefix = ["p0", "p1"]
    requests = {"r1": prefix + ["a"], "r2": prefix + ["b"]}
    shared_tokens = len(set(requests["r1"]) & set(requests["r2"]))
    return {"shared_prefix": shared_tokens, "request_lengths": {key: len(value) for key, value in requests.items()}, "invariant": "cache reuse preserves token position and request ownership"}
```

Esecuzione con `python snip_78_contract.py`:

```text
{"invariant": "cache reuse preserves token position and request ownership", "request_lengths": {"r1": 3, "r2": 3}, "shared_prefix": 2}
```

Il test associato è [`code/test_78_contract.py`](code/test_78_contract.py); l'output versionato è [`code/outputs/SNIP-78-001.txt`](code/outputs/SNIP-78-001.txt).


## Compressione ed eviction

Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano precisione o contesto disponibile. [SRC-78-001]

**Caso da seguire.** Per «Compressione ed eviction» si mantiene l'input del capitolo e si isola questa condizione: Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano precisione o contesto disponibile.

**Controllo.** Per «Compressione ed eviction», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Compressione ed eviction» non si applica.


![KV cache e riuso del contesto: timeline](../../assets/chapters/78_kv_cache/CACHE-02/candidate-v48.png)

La seconda figura mette a confronto «Prefix caching» e il limite discusso in «Compressione ed eviction».


## Come si collegano i passaggi

- **Da «Prefill e decode» a «Layout».** Il prefill calcola K e V per il prompt; il decode aggiunge una posizione e riusa la cache precedente. Layer, batch, KV head, token e head dimension determinano shape e byte. Tra «Prefill e decode» e «Layout» l'ingresso viene fissato prima della regola che produce il valore. Il passaggio successivo rende misurabile «Layout». [SRC-78-001; SRC-78-002]

- **Da «Layout» a «PagedAttention».** Layer, batch, KV head, token e head dimension determinano shape e byte. Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare sequenze di lunghezza diversa. Nel caso «PagedAttention» il componente diventa il punto in cui localizzare l'errore. Da «Layout» a «PagedAttention» cambia la domanda osservabile. [SRC-78-002; SRC-78-003]

- **Da «PagedAttention» a «Prefix caching».** Blocchi logici vengono mappati a pagine fisiche per ridurre frammentazione e supportare sequenze di lunghezza diversa. Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi sono compatibili. Dopo «PagedAttention», la variante di «Prefix caching» cambia una proprietà alla volta. Il passaggio successivo rende misurabile «Prefix caching». [SRC-78-003; SRC-78-004]

- **Da «Prefix caching» a «Compressione ed eviction».** Prefissi identici possono condividere pagine se modello, tokenizer, adapter e messaggi sono compatibili. Quantizzazione, sliding window e selezione dei token riducono memoria, ma modificano precisione o contesto disponibile. Da «Compressione ed eviction» in poi la misura resta distinta dalla correttezza locale del calcolo. Da «Prefix caching» a «Compressione ed eviction» cambia la domanda osservabile. [SRC-78-004; SRC-78-001]

La catena completa produce cache occupata, hit e latenza a partire da layer, token, KV dimension, dtype e prefix. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: la cache deve rispettare ownership, posizione e validità del prefisso.


## Esercizi sul meccanismo

1. Ricostruisci «Prefill e decode» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Layout», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «PagedAttention» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Prefix caching» che produca una failure riconoscibile.
5. Per «Compressione ed eviction», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «layer, token, KV dimension, dtype e prefix» e arriva fino a «cache occupata, hit e latenza». Il limite da conservare è questo: la cache deve rispettare ownership, posizione e validità del prefisso. La formula e il codice collegati a «Compressione ed eviction» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
