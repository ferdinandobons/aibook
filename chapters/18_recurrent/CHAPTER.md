<!--
chapter_id: CH-P04-RECURRENT
part_id: P04
order_key: 180
title: Reti ricorrenti e modelli sequenziali
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 18. Reti ricorrenti e modelli sequenziali

La domanda guida di questa lezione è come collegare «Uno stato che attraversa la sequenza» e «RNN, attention e stato» senza perdere il contratto tecnico di reti ricorrenti e modelli sequenziali. L'oggetto osservato è uno stato nascosto che attraversa una sequenza. Il contratto locale è: input, x_1, x_2, x_3 e h_0 = 0; operazione, ogni passo combina input corrente e stato precedente con gli stessi pesi; output, h_t e, se richiesto, una predizione per il passo. Il caso guida è questo: Tre passi in cui lo stato precedente viene consumato prima di produrre il successivo. Il confine da mantenere esplicito è: lo stato precedente deve essere consumato prima di produrre quello successivo.

## Uno stato che attraversa la sequenza

Una RNN aggiorna uno stato nascosto con input e stato precedente. Lo stesso insieme di parametri viene riutilizzato a ogni passo. [SRC-18-001]

Lo stato corrente dipende dall'input e dallo stato precedente.

**Caso da seguire.** Tre passi in cui lo stato precedente viene consumato prima di produrre il successivo.

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Lo stesso insieme di parametri viene riutilizzato a ogni passo.


## Backpropagation through time

Il grafo ricorrente viene srotolato nel tempo. Gradienti molto lunghi possono svanire o esplodere. [SRC-18-002]

**Caso da seguire.** Tre aggiornamenti tanh con coefficienti fissi e forma scalare.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
h_t=\phi(W_xx_t+W_hh_{t-1}+b)
$$

Lo stato corrente dipende dall'input e dallo stato precedente. [SRC-18-001]


![Reti ricorrenti e modelli sequenziali: timeline](../../assets/chapters/18_recurrent/RECURREN-01/candidate-v49.png)

La prima figura segue il percorso da «Uno stato che attraversa la sequenza» a «LSTM e GRU».


## LSTM e GRU

Gate di input, forget e output controllano il flusso della memoria. GRU usa una parametrizzazione più compatta, con un contratto differente. [SRC-18-003]

**Caso da seguire.** Per «LSTM e GRU» si mantiene l'input del capitolo e si isola questa condizione: Gate di input, forget e output controllano il flusso della memoria.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «LSTM e GRU».


## Bidirezionalità e causalità

Una rete bidirezionale usa anche il futuro ed è adatta a encoding offline. Non può essere usata direttamente per generazione causale streaming. [SRC-18-004]

**Caso da seguire.** Una matrice di visibilità in cui la posizione futura resta esclusa anche se la shape dei tensori è compatibile.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    state = 0.0
    for value in (1.0, 2.0, -1.0):
        state = math.tanh(0.5 * value + 0.8 * state)
    return {"state": round(state, 6), "invariant": "the previous state is consumed before the next step"}
```

Esecuzione con `python snip_18_contract.py`:

```text
{"invariant": "the previous state is consumed before the next step", "state": 0.200159}
```

Il test associato è [`code/test_18_contract.py`](code/test_18_contract.py); l'output versionato è [`code/outputs/SNIP-18-001.txt`](code/outputs/SNIP-18-001.txt).


## RNN, attention e stato

La recurrence mantiene memoria compatta; l'attention accede a rappresentazioni esplicite. I due meccanismi possono essere complementari. [SRC-18-001]

**Caso da seguire.** Per «RNN, attention e stato» si mantiene l'input del capitolo e si isola questa condizione: La recurrence mantiene memoria compatta; l'attention accede a rappresentazioni esplicite.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «RNN, attention e stato» non si applica.


![Reti ricorrenti e modelli sequenziali: loop](../../assets/chapters/18_recurrent/RECURREN-02/candidate-v51.png)

La seconda figura mette a confronto «Bidirezionalità e causalità» e il limite discusso in «RNN, attention e stato».


## Come si collegano i passaggi

- **Da «Uno stato che attraversa la sequenza» a «Backpropagation through time».** Una RNN aggiorna uno stato nascosto con input e stato precedente. Il grafo ricorrente viene srotolato nel tempo. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-18-001; SRC-18-002]

- **Da «Backpropagation through time» a «LSTM e GRU».** Il grafo ricorrente viene srotolato nel tempo. Gate di input, forget e output controllano il flusso della memoria. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-18-002; SRC-18-003]

- **Da «LSTM e GRU» a «Bidirezionalità e causalità».** Gate di input, forget e output controllano il flusso della memoria. Una rete bidirezionale usa anche il futuro ed è adatta a encoding offline. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-18-003; SRC-18-004]

- **Da «Bidirezionalità e causalità» a «RNN, attention e stato».** Una rete bidirezionale usa anche il futuro ed è adatta a encoding offline. La recurrence mantiene memoria compatta; l'attention accede a rappresentazioni esplicite. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-18-004; SRC-18-001]

La catena completa produce h_t e, se richiesto, una predizione per il passo a partire da x_1, x_2, x_3 e h_0 = 0. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: lo stato precedente deve essere consumato prima di produrre quello successivo.


## Esercizi sul meccanismo

1. Ricostruisci «Uno stato che attraversa la sequenza» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Backpropagation through time», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «LSTM e GRU» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Bidirezionalità e causalità» che produca una failure riconoscibile.
5. Per «RNN, attention e stato», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «x_1, x_2, x_3 e h_0 = 0» e arriva fino a «h_t e, se richiesto, una predizione per il passo». Il limite da conservare è questo: lo stato precedente deve essere consumato prima di produrre quello successivo. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
