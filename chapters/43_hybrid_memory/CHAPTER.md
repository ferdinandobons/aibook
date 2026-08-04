<!--
chapter_id: CH-P08-HYBRID-MEMORY
part_id: P08
order_key: 430
title: Architetture ibride e memoria interna
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 43. Architetture ibride e memoria interna

Qui architetture ibride e memoria interna viene osservato come un meccanismo: il percorso va da «Ibridi tra layer» a «Memoria interna ed esterna». L'oggetto osservato è informazione distribuita tra attenzione locale e memoria. Il contratto locale dichiara input, segmento corrente, stato e memoria persistente; operazione, write, read, routing e fusione; output, stato aggiornato e contenuto recuperato. La situazione minima da seguire è Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Ibridi tra layer». Il limite da non nascondere è: durata e provenienza della memoria devono essere separate.

## Ibridi tra layer

Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati. [SRC-43-001]

Memoria locale, stato e memoria esterna hanno letture e durate differenti.

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Ibridi tra layer».

**Controllo.** Per «Ibridi tra layer», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Ibridi tra layer», il vincolo da conservare è: Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati.


## Attention locale e stato

Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre la finestra. [SRC-43-002]

**Caso da seguire.** Un fatto stabile e due elementi recenti con letture diverse.

**Controllo.** Per «Attention locale e stato», ricalcola il caso a mano e con lo snippet. Nel caso «Attention locale e stato», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
h' = read(write(h, segment))
$$

Memoria locale, stato e memoria esterna hanno letture e durate differenti. [SRC-43-001]


![Architetture ibride e memoria interna: graph](../../assets/chapters/43_hybrid_memory/HYBRID-01/candidate-v47.png)

La prima figura segue il percorso da «Ibridi tra layer» a «Memoria segmentale».


## Memoria segmentale

Stati di segmenti precedenti possono essere riusati o compressi con stop-gradient e capacità limitata. [SRC-43-003]

**Caso da seguire.** Una query confrontata con tre documenti, conservando ranking, chunk entrati nel contesto e risposta finale.

**Controllo.** Per «Memoria segmentale», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Memoria segmentale».


## Memoria associativa

Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream. [SRC-43-004]

**Caso da seguire.** Per «Memoria associativa» si mantiene l'input del capitolo e si isola questa condizione: Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream.

**Controllo.** Per «Memoria associativa», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Memoria associativa», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

La prova locale di architetture ibride e memoria interna parte da un esempio minimo, registrato nel repository insieme ai suoi test. Per «Architetture ibride e memoria interna», il caso di default usa valori piccoli per isolare il meccanismo. La prova negativa riguarda proprio «architetture ibride e memoria interna» e interrompe l'interpretazione prima dell'output.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    local = ["recent-a", "recent-b"]
    long_term = ["stable-fact"]
    read = local[-1] if local else long_term[0]
    return {"local_size": len(local), "long_term_size": len(long_term), "read": read, "invariant": "local and long-term memory have separate lifetimes"}
```

Esecuzione con `python snip_43_contract.py`:

```text
{"invariant": "local and long-term memory have separate lifetimes", "local_size": 2, "long_term_size": 1, "read": "recent-b"}
```

Il test associato è [`code/test_43_contract.py`](code/test_43_contract.py); l'output versionato è [`code/outputs/SNIP-43-001.txt`](code/outputs/SNIP-43-001.txt).


## Memoria interna ed esterna

Lo stato neurale non coincide con retrieval documentale. Reset, isolamento e provenienza hanno contratti differenti. [SRC-43-001]

**Caso da seguire.** Per «Memoria interna ed esterna» si mantiene l'input del capitolo e si isola questa condizione: Lo stato neurale non coincide con retrieval documentale.

**Controllo.** Per «Memoria interna ed esterna», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Memoria interna ed esterna» non si applica.


![Architetture ibride e memoria interna: loop](../../assets/chapters/43_hybrid_memory/HYBRID-02/candidate-v47.png)

La seconda figura mette a confronto «Memoria associativa» e il limite discusso in «Memoria interna ed esterna».


## Come si collegano i passaggi

- **Da «Ibridi tra layer» a «Attention locale e stato».** Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati. Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre la finestra. Tra «Ibridi tra layer» e «Attention locale e stato» l'ingresso viene fissato prima della regola che produce il valore. Da «Ibridi tra layer» a «Attention locale e stato» cambia la domanda osservabile. [SRC-43-001; SRC-43-002]

- **Da «Attention locale e stato» a «Memoria segmentale».** Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre la finestra. Stati di segmenti precedenti possono essere riusati o compressi con stop-gradient e capacità limitata. Nel caso «Memoria segmentale» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «Memoria segmentale». [SRC-43-002; SRC-43-003]

- **Da «Memoria segmentale» a «Memoria associativa».** Stati di segmenti precedenti possono essere riusati o compressi con stop-gradient e capacità limitata. Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream. Dopo «Memoria segmentale», la variante di «Memoria associativa» cambia una proprietà alla volta. Da «Memoria segmentale» a «Memoria associativa» cambia la domanda osservabile. [SRC-43-003; SRC-43-004]

- **Da «Memoria associativa» a «Memoria interna ed esterna».** Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream. Lo stato neurale non coincide con retrieval documentale. Da «Memoria interna ed esterna» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «Memoria interna ed esterna». [SRC-43-004; SRC-43-001]

La catena completa produce stato aggiornato e contenuto recuperato a partire da segmento corrente, stato e memoria persistente. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: durata e provenienza della memoria devono essere separate.


## Esercizi sul meccanismo

1. Ricostruisci «Ibridi tra layer» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Attention locale e stato», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Memoria segmentale» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Memoria associativa» che produca una failure riconoscibile.
5. Per «Memoria interna ed esterna», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «segmento corrente, stato e memoria persistente» e arriva fino a «stato aggiornato e contenuto recuperato». Il limite da conservare è questo: durata e provenienza della memoria devono essere separate. La formula e il codice collegati a «Memoria interna ed esterna» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
