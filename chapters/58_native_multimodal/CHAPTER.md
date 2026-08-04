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

La domanda guida di questa lezione è come collegare «Token interleaved» e «Sincronizzazione» senza perdere il contratto tecnico di modelli multimodali nativi e any-to-any. L'oggetto osservato è token interleaved e output di più modalità. Il contratto locale è: input, sequenza testo-immagine-audio con mask; operazione, backbone condiviso, routing e sincronizzazione; output, token o artefatto nella modalità richiesta. Il caso guida è questo: Una sequenza alterna token testuali e visivi mantenendo la modalità associata a ogni posizione. Il confine da mantenere esplicito è: ordine, durata e maschera della modalità devono essere espliciti.

## Token interleaved

Sequenze possono alternare testo, immagini, audio e marker. Il tokenizer multimodale definisce unità e ordine. [SRC-58-001]

La fusione conserva le dimensioni e le maschere delle modalità.

**Caso da seguire.** Una sequenza alterna token testuali e visivi mantenendo la modalità associata a ogni posizione.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Backbone condiviso

Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici. [SRC-58-002]

**Caso da seguire.** Testo e immagine alternati con due posizioni riservate.

**Controllo.** Ripeti «Backbone condiviso» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![Modelli multimodali nativi e any-to-any: compare](../../assets/chapters/58_native_multimodal/MULTIMODAL-01/candidate-v48.png)

La prima figura segue il percorso da «Token interleaved» a «Output multimodale».


## Output multimodale

La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune. [SRC-58-003]

**Caso da seguire.** Due rappresentazioni di modalità diverse proiettate nella stessa dimensione prima di similarità, fusione o generazione.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Any-to-any

Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate. [SRC-58-004]

**Caso da seguire.** Due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Sincronizzazione

Audio, video e testo possiedono frequenze differenti. Allineamento temporale e turn-taking diventano parte dell'architettura. [SRC-58-001]

**Caso da seguire.** Per «Sincronizzazione» si mantiene l'input del capitolo e si isola questa condizione: Audio, video e testo possiedono frequenze differenti.

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Allineamento temporale e turn-taking diventano parte dell'architettura.


![Modelli multimodali nativi e any-to-any: pipeline](../../assets/chapters/58_native_multimodal/MULTIMODAL-02/candidate-v48.png)

La seconda figura mette a confronto «Any-to-any» e il limite discusso in «Sincronizzazione».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
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

- **Da «Token interleaved» a «Backbone condiviso».** Sequenze possono alternare testo, immagini, audio e marker. Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-58-001; SRC-58-002]

- **Da «Backbone condiviso» a «Output multimodale».** Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici. La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-58-002; SRC-58-003]

- **Da «Output multimodale» a «Any-to-any».** La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune. Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-58-003; SRC-58-004]

- **Da «Any-to-any» a «Sincronizzazione».** Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate. Audio, video e testo possiedono frequenze differenti. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-58-004; SRC-58-001]

La catena completa produce token o artefatto nella modalità richiesta a partire da sequenza testo-immagine-audio con mask. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: ordine, durata e maschera della modalità devono essere espliciti.


## Prove sui confini del sistema

1. Ricostruisci «Token interleaved» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Backbone condiviso», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Output multimodale» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Any-to-any» che produca una failure riconoscibile.
5. Per «Sincronizzazione», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «sequenza testo-immagine-audio con mask» e arriva fino a «token o artefatto nella modalità richiesta». Il limite da conservare è questo: ordine, durata e maschera della modalità devono essere espliciti. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
