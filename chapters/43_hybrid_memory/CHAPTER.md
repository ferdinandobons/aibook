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

La domanda guida di questa lezione è come collegare «Ibridi tra layer» e «Memoria interna ed esterna» senza perdere il contratto tecnico di architetture ibride e memoria interna. L'oggetto osservato è informazione distribuita tra attenzione locale e memoria. Il contratto locale è: input, segmento corrente, stato e memoria persistente; operazione, write, read, routing e fusione; output, stato aggiornato e contenuto recuperato. Il caso guida è questo: Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Ibridi tra layer». Il confine da mantenere esplicito è: durata e provenienza della memoria devono essere separate.

## Ibridi tra layer

Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati. [SRC-43-001]

Memoria locale, stato e memoria esterna hanno letture e durate differenti.

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Ibridi tra layer».

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati.


## Attention locale e stato

Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre la finestra. [SRC-43-002]

**Caso da seguire.** Un fatto stabile e due elementi recenti con letture diverse.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


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

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Memoria segmentale».


## Memoria associativa

Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream. [SRC-43-004]

**Caso da seguire.** Per «Memoria associativa» si mantiene l'input del capitolo e si isola questa condizione: Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
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

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Memoria interna ed esterna» non si applica.


![Architetture ibride e memoria interna: loop](../../assets/chapters/43_hybrid_memory/HYBRID-02/candidate-v47.png)

La seconda figura mette a confronto «Memoria associativa» e il limite discusso in «Memoria interna ed esterna».


## Come si collegano i passaggi

- **Da «Ibridi tra layer» a «Attention locale e stato».** Transformer, SSM e recurrence possono alternarsi con rapporti e interfacce dichiarati. Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre la finestra. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-43-001; SRC-43-002]

- **Da «Attention locale e stato» a «Memoria segmentale».** Una finestra precisa gestisce il vicino; uno stato compatto trasporta informazione oltre la finestra. Stati di segmenti precedenti possono essere riusati o compressi con stop-gradient e capacità limitata. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-43-002; SRC-43-003]

- **Da «Memoria segmentale» a «Memoria associativa».** Stati di segmenti precedenti possono essere riusati o compressi con stop-gradient e capacità limitata. Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-43-003; SRC-43-004]

- **Da «Memoria associativa» a «Memoria interna ed esterna».** Key-value interne o moduli di memoria aggiornati online offrono accesso diverso dal residual stream. Lo stato neurale non coincide con retrieval documentale. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-43-004; SRC-43-001]

La catena completa produce stato aggiornato e contenuto recuperato a partire da segmento corrente, stato e memoria persistente. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: durata e provenienza della memoria devono essere separate.


## Esercizi sul meccanismo

1. Ricostruisci «Ibridi tra layer» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Attention locale e stato», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Memoria segmentale» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Memoria associativa» che produca una failure riconoscibile.
5. Per «Memoria interna ed esterna», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «segmento corrente, stato e memoria persistente» e arriva fino a «stato aggiornato e contenuto recuperato». Il limite da conservare è questo: durata e provenienza della memoria devono essere separate. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
