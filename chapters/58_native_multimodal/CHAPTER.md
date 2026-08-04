<!--
chapter_id: CH-P10-NATIVE-MULTIMODAL
part_id: P10
order_key: 580
title: Modelli multimodali nativi e any-to-any
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 58. Modelli multimodali nativi e any-to-any

Il percorso di modelli multimodali nativi e any-to-any attraversa «Token interleaved» e «Sincronizzazione» senza attribuire al solo modello ciò che dipende dal sistema. L'oggetto osservato è token interleaved e output di più modalità. Il contratto locale dichiara input, sequenza testo-immagine-audio con mask; operazione, backbone condiviso, routing e sincronizzazione; output, token o artefatto nella modalità richiesta. La situazione minima da seguire è Una sequenza alterna token testuali e visivi mantenendo la modalità associata a ogni posizione. Il limite da non nascondere è: ordine, durata e maschera della modalità devono essere espliciti.

## Token interleaved

Sequenze possono alternare testo, immagini, audio e marker. Il tokenizer multimodale definisce unità e ordine. [SRC-58-001]

La fusione conserva le dimensioni e le maschere delle modalità.

**Caso da seguire.** Una sequenza alterna token testuali e visivi mantenendo la modalità associata a ogni posizione.

**Controllo.** Per «Token interleaved», registra richiesta, decisione, stato e output finale. Nel caso «Token interleaved», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Backbone condiviso

Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici. [SRC-58-002]

**Caso da seguire.** Testo e immagine alternati con due posizioni riservate.

**Controllo.** Ripeti «Backbone condiviso» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


Lo schema seguente rende esplicito il confine tra il meccanismo e la sua valutazione.

**Schema concettuale.** `z = fuse(z_text, z_vision, z_audio)`

La fusione conserva le dimensioni e le maschere delle modalità. [SRC-58-001]


![Modelli multimodali nativi e any-to-any: compare](../../assets/chapters/58_native_multimodal/MULTIMODAL-01/candidate-v48.png)

La prima figura segue il percorso da «Token interleaved» a «Output multimodale».


## Output multimodale

La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune. [SRC-58-003]

**Caso da seguire.** Due rappresentazioni di modalità diverse proiettate nella stessa dimensione prima di similarità, fusione o generazione.

**Controllo.** Per «Output multimodale», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Any-to-any

Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate. [SRC-58-004]

**Caso da seguire.** Due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito.

**Controllo.** Per «Any-to-any», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Sincronizzazione

Audio, video e testo possiedono frequenze differenti. Allineamento temporale e turn-taking diventano parte dell'architettura. [SRC-58-001]

**Caso da seguire.** Per «Sincronizzazione» si mantiene l'input del capitolo e si isola questa condizione: Audio, video e testo possiedono frequenze differenti.

**Controllo.** Per «Sincronizzazione», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Sincronizzazione», il risultato resta limitato da: Allineamento temporale e turn-taking diventano parte dell'architettura.


![Modelli multimodali nativi e any-to-any: pipeline](../../assets/chapters/58_native_multimodal/MULTIMODAL-02/candidate-v48.png)

La seconda figura mette a confronto «Any-to-any» e il limite discusso in «Sincronizzazione».


## Esempio Python eseguito

Questa sezione apre il contratto Python di modelli multimodali nativi e any-to-any: il lettore può eseguire lo stesso file e confrontare il risultato. Per «Modelli multimodali nativi e any-to-any», il caso di default usa valori piccoli per isolare il meccanismo. Il caso non supportato viene provato separatamente, così «modelli multimodali nativi e any-to-any» non viene generalizzato oltre l'esempio.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    sequence = [("text", 1), ("image", 7), ("text", 2)]
    vocabulary = {"text": {1, 2}, "image": {7}}
    valid = all(token in vocabulary[modality] for modality, token in sequence)
    return {"valid": valid, "length": len(sequence), "invariant": "native multimodal serialization keeps modality and token identity"}
```

Esecuzione con `python snip_58_contract.py`:

```text
{"invariant": "native multimodal serialization keeps modality and token identity", "length": 3, "valid": true}
```

Il test associato è [`code/test_58_contract.py`](code/test_58_contract.py); l'output versionato è [`code/outputs/SNIP-58-001.txt`](code/outputs/SNIP-58-001.txt).


## Come si collegano i passaggi

- **Da «Token interleaved» a «Backbone condiviso».** Sequenze possono alternare testo, immagini, audio e marker. Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici. «Token interleaved» nomina il confine e «Backbone condiviso» implementa il percorso senza ereditare autorizzazioni implicite. Il passaggio successivo rende misurabile «Backbone condiviso». [SRC-58-001; SRC-58-002]

- **Da «Backbone condiviso» a «Output multimodale».** Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici. La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune. Componendo «Backbone condiviso» e «Output multimodale» diventa necessario conservare stato, identità e decisione. Da «Backbone condiviso» a «Output multimodale» cambia la domanda osservabile. [SRC-58-002; SRC-58-003]

- **Da «Output multimodale» a «Any-to-any».** La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune. Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate. «Any-to-any» introduce failure e recovery prima di un side effect o di una perdita di stato. Il passaggio successivo rende misurabile «Any-to-any». [SRC-58-003; SRC-58-004]

- **Da «Any-to-any» a «Sincronizzazione».** Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate. Audio, video e testo possiedono frequenze differenti. La chiusura su «Sincronizzazione» valuta il sistema completo, non soltanto il componente iniziale. Da «Any-to-any» a «Sincronizzazione» cambia la domanda osservabile. [SRC-58-004; SRC-58-001]

La catena completa produce token o artefatto nella modalità richiesta a partire da sequenza testo-immagine-audio con mask. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: ordine, durata e maschera della modalità devono essere espliciti.


## Prove sui confini del sistema

1. Ricostruisci «Token interleaved» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Backbone condiviso», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Output multimodale» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Any-to-any» che produca una failure riconoscibile.
5. Per «Sincronizzazione», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «sequenza testo-immagine-audio con mask» e arriva fino a «token o artefatto nella modalità richiesta». Il limite da conservare è questo: ordine, durata e maschera della modalità devono essere espliciti. Il confine di «Sincronizzazione» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
