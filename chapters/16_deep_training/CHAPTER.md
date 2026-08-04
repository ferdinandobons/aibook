<!--
chapter_id: CH-P04-DEEP-TRAINING
part_id: P04
order_key: 160
title: Addestrare reti profonde
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 16. Addestrare reti profonde

La domanda guida di questa lezione è come collegare «Segnali che attraversano molti layer» e «Regolarizzazione e diagnostica» senza perdere il contratto tecnico di addestrare reti profonde. L'oggetto osservato è il segnale che attraversa una rete profonda. Il contratto locale è: input, x_l con shape [batch, d] e norma misurata; operazione, un blocco, una normalizzazione o un percorso residuale; output, x_{l+1} con la stessa o con una nuova shape dichiarata. Il caso guida è questo: Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Segnali che attraversano molti layer». Il confine da mantenere esplicito è: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.

## Segnali che attraversano molti layer

Attivazioni e gradienti possono crescere o ridursi lungo la profondità. Inizializzazione, attivazioni e residual determinano la scala osservata. [SRC-16-001]

Il residual path conserva un percorso identità da controllare.

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Segnali che attraversano molti layer».

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Inizializzazione, attivazioni e residual determinano la scala osservata.


## Inizializzazione

Xavier e He initialization collegano la varianza dei pesi al fan-in o fan-out. Le formule presuppongono attivazioni e indipendenze approssimate. [SRC-16-002]

**Caso da seguire.** X + F(x) con due vettori di dimensione 2.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
x_{l+1}=x_l+F(x_l)
$$

Il residual path conserva un percorso identità da controllare. [SRC-16-001]


![Addestrare reti profonde: chart](../../assets/chapters/16_deep_training/TRAINING-01/candidate-v49.png)

La prima figura segue il percorso da «Segnali che attraversano molti layer» a «Normalizzazione».


## Normalizzazione

BatchNorm, LayerNorm e RMSNorm normalizzano assi e statistiche differenti. Non sono sostituibili senza considerare batch, sequenza e architettura. [SRC-16-003]

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Normalizzazione».

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Normalizzazione».


## Residual e profondità

Un residual path conserva un percorso identità e facilita il trasporto di informazione. La somma richiede shape compatibili e una scala controllata. [SRC-16-004]

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Residual e profondità».

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    x = [1.0, -2.0]
    residual = [0.2, 0.3]
    output = [a + b for a, b in zip(x, residual)]
    return {"output": output, "shape": [2], "invariant": "residual operands share shape"}
```

Esecuzione con `python snip_16_contract.py`:

```text
{"invariant": "residual operands share shape", "output": [1.2, -1.7], "shape": [2]}
```

Il test associato è [`code/test_16_contract.py`](code/test_16_contract.py); l'output versionato è [`code/outputs/SNIP-16-001.txt`](code/outputs/SNIP-16-001.txt).


## Regolarizzazione e diagnostica

Dropout, weight decay, data augmentation ed early stopping agiscono in punti diversi. Curve, norme e slice aiutano a distinguere underfitting, overfitting e instabilità. [SRC-16-001]

**Caso da seguire.** Un residual `x + F(x)` richiede shape compatibili. Se `F(x)` ha scala molto maggiore di `x`, la somma resta valida formalmente ma può destabilizzare il percorso.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Regolarizzazione e diagnostica» non si applica.


![Addestrare reti profonde: architecture](../../assets/chapters/16_deep_training/TRAINING-02/candidate-v49.png)

La seconda figura mette a confronto «Residual e profondità» e il limite discusso in «Regolarizzazione e diagnostica».


## Come si collegano i passaggi

- **Da «Segnali che attraversano molti layer» a «Inizializzazione».** Attivazioni e gradienti possono crescere o ridursi lungo la profondità. Xavier e He initialization collegano la varianza dei pesi al fan-in o fan-out. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-16-001; SRC-16-002]

- **Da «Inizializzazione» a «Normalizzazione».** Xavier e He initialization collegano la varianza dei pesi al fan-in o fan-out. BatchNorm, LayerNorm e RMSNorm normalizzano assi e statistiche differenti. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-16-002; SRC-16-003]

- **Da «Normalizzazione» a «Residual e profondità».** BatchNorm, LayerNorm e RMSNorm normalizzano assi e statistiche differenti. Un residual path conserva un percorso identità e facilita il trasporto di informazione. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-16-003; SRC-16-004]

- **Da «Residual e profondità» a «Regolarizzazione e diagnostica».** Un residual path conserva un percorso identità e facilita il trasporto di informazione. Dropout, weight decay, data augmentation ed early stopping agiscono in punti diversi. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-16-004; SRC-16-001]

La catena completa produce x_{l+1} con la stessa o con una nuova shape dichiarata a partire da x_l con shape [batch, d] e norma misurata. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: una somma residuale richiede shape compatibili e non prova da sola stabilità del training.


## Esercizi sul meccanismo

1. Ricostruisci «Segnali che attraversano molti layer» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Inizializzazione», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Normalizzazione» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Residual e profondità» che produca una failure riconoscibile.
5. Per «Regolarizzazione e diagnostica», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «x_l con shape [batch, d] e norma misurata» e arriva fino a «x_{l+1} con la stessa o con una nuova shape dichiarata». Il limite da conservare è questo: una somma residuale richiede shape compatibili e non prova da sola stabilità del training. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
