<!--
chapter_id: CH-P04-MLP
part_id: P04
order_key: 150
title: Dal percettrone alle reti multilayer
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 15. Dal percettrone alle reti multilayer

La domanda guida di questa lezione è come collegare «Una decisione lineare» e «Dal forward al training» senza perdere il contratto tecnico di dal percettrone alle reti multilayer. L'oggetto osservato è il vettore di feature x della richiesta. Il contratto locale è: input, x = [1, 2] con shape [2]; operazione, una trasformazione affine seguita da una funzione di attivazione; output, un nuovo vettore h con shape dichiarata. Il caso guida è questo: Un caso minimo con input x = [1, 2] con shape [2] e output «un nuovo vettore h con shape dichiarata». Il confine da mantenere esplicito è: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.

## Una decisione lineare

Il percettrone combina feature con pesi e bias. Il confine risultante è lineare nello spazio delle feature. [SRC-15-001]

La non linearità impedisce di collassare tutti i layer affini in uno solo.

**Caso da seguire.** Un caso minimo con input x = [1, 2] con shape [2] e output «un nuovo vettore h con shape dichiarata».

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Il confine risultante è lineare nello spazio delle feature.


## Strati nascosti

Una MLP alterna trasformazioni affini e funzioni non lineari. Senza non linearità, più layer affini collassano in una sola trasformazione affine. [SRC-15-002]

**Caso da seguire.** W x + b prima di ReLU, con due coordinate osservabili.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
h = \phi(Wx+b)
$$

La non linearità impedisce di collassare tutti i layer affini in uno solo. [SRC-15-001]


![Dal percettrone alle reti multilayer: chart](../../assets/chapters/15_mlp/MLP-01/candidate-v49.png)

La prima figura segue il percorso da «Una decisione lineare» a «Attivazioni».


## Attivazioni

ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. La scelta deve essere letta insieme a inizializzazione e normalizzazione. [SRC-15-003]

**Caso da seguire.** Un caso in cui una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Attivazioni».


## Capacità ed espressività

Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile. [SRC-15-004]

**Caso da seguire.** X=[1,2] passato in una trasformazione affine e poi in una non linearità, con shape e confine espliciti.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    x = [1.0, 2.0]
    weights = [[0.5, -0.25], [0.25, 0.5]]
    bias = [0.0, 0.1]
    hidden = [max(0.0, sum(row[i] * x[i] for i in range(2)) + bias[j]) for j, row in enumerate(weights)]
    return {"output": hidden, "shape": [2], "invariant": "the nonlinearity is after the affine map"}
```

Esecuzione con `python snip_15_contract.py`:

```text
{"invariant": "the nonlinearity is after the affine map", "output": [0.0, 1.35], "shape": [2]}
```

Il test associato è [`code/test_15_contract.py`](code/test_15_contract.py); l'output versionato è [`code/outputs/SNIP-15-001.txt`](code/outputs/SNIP-15-001.txt).


## Dal forward al training

Il forward produce logits e loss. Backpropagation e optimizer trasformano il segnale in aggiornamenti, secondo i contratti costruiti nei capitoli matematici. [SRC-15-001]

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Dal forward al training».

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Dal forward al training» non si applica.


![Dal percettrone alle reti multilayer: architecture](../../assets/chapters/15_mlp/MLP-02/candidate-v49.png)

La seconda figura mette a confronto «Capacità ed espressività» e il limite discusso in «Dal forward al training».


## Come si collegano i passaggi

- **Da «Una decisione lineare» a «Strati nascosti».** Il percettrone combina feature con pesi e bias. Una MLP alterna trasformazioni affini e funzioni non lineari. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-15-001; SRC-15-002]

- **Da «Strati nascosti» a «Attivazioni».** Una MLP alterna trasformazioni affini e funzioni non lineari. ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-15-002; SRC-15-003]

- **Da «Attivazioni» a «Capacità ed espressività».** ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-15-003; SRC-15-004]

- **Da «Capacità ed espressività» a «Dal forward al training».** Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile. Il forward produce logits e loss. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-15-004; SRC-15-001]

La catena completa produce un nuovo vettore h con shape dichiarata a partire da x = [1, 2] con shape [2]. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine.


## Esercizi sul meccanismo

1. Ricostruisci «Una decisione lineare» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Strati nascosti», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Attivazioni» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Capacità ed espressività» che produca una failure riconoscibile.
5. Per «Dal forward al training», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «x = [1, 2] con shape [2]» e arriva fino a «un nuovo vettore h con shape dichiarata». Il limite da conservare è questo: una pila di trasformazioni affini senza non linearità resta una sola trasformazione affine. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
