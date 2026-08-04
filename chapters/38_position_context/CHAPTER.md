<!--
chapter_id: CH-P08-POSITION-CONTEXT
part_id: P08
order_key: 380
title: Posizione e contesto lungo
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 38. Posizione e contesto lungo

La lezione prende un caso piccolo e lo accompagna da «Posizione assoluta» fino a «Estensione e valutazione», senza saltare i passaggi. L'oggetto osservato è la relazione tra posizione e rappresentazione del token. Il contratto locale dichiara input, query, key e indice di posizione; operazione, posizione assoluta, relativa, RoPE o bias; output, score dipendente dalla posizione. Il caso di partenza è Un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati. Il limite da non nascondere è: estendere il contesto richiede una misura fuori dalla lunghezza addestrata.

## Posizione assoluta

Embedding appresi o sinusoidali aggiungono un segnale legato all'indice. [SRC-38-001]

Una rotazione di query e key rende il prodotto dipendente dalla posizione relativa.

**Caso da seguire.** Un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati.

**Controllo.** Per «Posizione assoluta», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Posizione assoluta», il vincolo da conservare è: Embedding appresi o sinusoidali aggiungono un segnale legato all'indice.


## Posizione relativa

Bias o rappresentazioni relative modificano i confronti in funzione della distanza. [SRC-38-002]

**Caso da seguire.** Per «Posizione relativa» si mantiene l'input del capitolo e si isola questa condizione: Bias o rappresentazioni relative modificano i confronti in funzione della distanza.

**Controllo.** Per «Posizione relativa», ricalcola il caso a mano e con lo snippet. Nel caso «Posizione relativa», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
q'_m = R(theta_m) q_m
$$

Una rotazione di query e key rende il prodotto dipendente dalla posizione relativa. [SRC-38-001]


![Posizione e contesto lungo: matrix](../../assets/chapters/38_position_context/POS-01/candidate-v47.png)

La prima figura segue il percorso da «Posizione assoluta» a «RoPE».


## RoPE

Rotazioni di query e key rendono il prodotto scalare dipendente dall'offset relativo. [SRC-38-003]

**Caso da seguire.** Un caso in cui estendere il contesto richiede una misura fuori dalla lunghezza addestrata.

**Controllo.** Per «RoPE», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «RoPE».


## ALiBi

Bias lineari penalizzano distanze maggiori con slope per head. [SRC-38-004]

**Caso da seguire.** Un blocco viene confrontato a parità di input e shape. Il vantaggio dichiarato resta un'ipotesi finché non viene misurato sullo stesso setup.

**Controllo.** Per «ALiBi», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «ALiBi», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Questa sezione apre il contratto Python di posizione e contesto lungo: il lettore può eseguire lo stesso file e confrontare il risultato. Per «Posizione e contesto lungo», il caso di default usa valori piccoli per isolare il meccanismo. Il caso non supportato viene provato separatamente, così «posizione e contesto lungo» non viene generalizzato oltre l'esempio.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    position = 2
    angle = position * 0.5
    query = [1.0, 0.0]
    rotated = [query[0] * math.cos(angle) - query[1] * math.sin(angle), query[0] * math.sin(angle) + query[1] * math.cos(angle)]
    return {"position": position, "rotated": [round(value, 6) for value in rotated], "invariant": "the positional transform is indexed by position"}
```

Esecuzione con `python snip_38_contract.py`:

```text
{"invariant": "the positional transform is indexed by position", "position": 2, "rotated": [0.540302, 0.841471]}
```

Il test associato è [`code/test_38_contract.py`](code/test_38_contract.py); l'output versionato è [`code/outputs/SNIP-38-001.txt`](code/outputs/SNIP-38-001.txt).


## Estensione e valutazione

Positional interpolation e metodi affini estendono gli indici, ma l'uso effettivo del contesto deve essere misurato. [SRC-38-001]

**Caso da seguire.** Per «Estensione e valutazione» si mantiene l'input del capitolo e si isola questa condizione: Positional interpolation e metodi affini estendono gli indici, ma l'uso effettivo del contesto deve essere misurato.

**Controllo.** Per «Estensione e valutazione», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Estensione e valutazione» non si applica.


![Posizione e contesto lungo: chart](../../assets/chapters/38_position_context/POS-02/candidate-v47.png)

La seconda figura mette a confronto «ALiBi» e il limite discusso in «Estensione e valutazione».


## Come si collegano i passaggi

- **Da «Posizione assoluta» a «Posizione relativa».** Embedding appresi o sinusoidali aggiungono un segnale legato all'indice. Bias o rappresentazioni relative modificano i confronti in funzione della distanza. Tra «Posizione assoluta» e «Posizione relativa» l'ingresso viene fissato prima della regola che produce il valore. Il passaggio successivo rende misurabile «Posizione relativa». [SRC-38-001; SRC-38-002]

- **Da «Posizione relativa» a «RoPE».** Bias o rappresentazioni relative modificano i confronti in funzione della distanza. Rotazioni di query e key rendono il prodotto scalare dipendente dall'offset relativo. Nel caso «RoPE» il componente diventa il punto in cui localizzare l'errore. Da «Posizione relativa» a «RoPE» cambia la domanda osservabile. [SRC-38-002; SRC-38-003]

- **Da «RoPE» a «ALiBi».** Rotazioni di query e key rendono il prodotto scalare dipendente dall'offset relativo. Bias lineari penalizzano distanze maggiori con slope per head. Dopo «RoPE», la variante di «ALiBi» cambia una proprietà alla volta. Il passaggio successivo rende misurabile «ALiBi». [SRC-38-003; SRC-38-004]

- **Da «ALiBi» a «Estensione e valutazione».** Bias lineari penalizzano distanze maggiori con slope per head. Positional interpolation e metodi affini estendono gli indici, ma l'uso effettivo del contesto deve essere misurato. Da «Estensione e valutazione» in poi la misura resta distinta dalla correttezza locale del calcolo. Da «ALiBi» a «Estensione e valutazione» cambia la domanda osservabile. [SRC-38-004; SRC-38-001]

La catena completa produce score dipendente dalla posizione a partire da query, key e indice di posizione. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: estendere il contesto richiede una misura fuori dalla lunghezza addestrata.


## Esercizi sul meccanismo

1. Ricostruisci «Posizione assoluta» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Posizione relativa», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «RoPE» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «ALiBi» che produca una failure riconoscibile.
5. Per «Estensione e valutazione», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «query, key e indice di posizione» e arriva fino a «score dipendente dalla posizione». Il limite da conservare è questo: estendere il contesto richiede una misura fuori dalla lunghezza addestrata. La formula e il codice collegati a «Estensione e valutazione» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
