<!--
chapter_id: CH-P13-PRIVACY-FAIRNESS
part_id: P13
order_key: 910
title: Privacy, fairness e unlearning
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 91. Privacy, fairness e unlearning

La domanda guida di questa lezione è come collegare «Memorizzazione e leakage» e «Machine unlearning» senza perdere il contratto tecnico di privacy, fairness e unlearning. L'oggetto osservato è un dato personale e il comportamento del sistema su gruppi diversi. Il contratto locale è: input, record, membership, gruppo, label e budget privacy; operazione, DP, fairness evaluation e unlearning; output, utility, leakage, disparità e verifica di rimozione. Il caso guida è questo: Due gruppi hanno accuracy pari a 0,75 e 0,50, quindi la media non nasconde il gap. Il confine da mantenere esplicito è: privacy, fairness e utility richiedono metriche e trade-off espliciti.

## Memorizzazione e leakage

Un modello può riprodurre sequenze rare. Membership inference e extraction misurano rischi differenti. [SRC-91-001]

Privacy, equità e utilità entrano in un trade-off da rendere misurabile.

**Caso da seguire.** Due gruppi hanno accuracy pari a 0,75 e 0,50, quindi la media non nasconde il gap.

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Membership inference e extraction misurano rischi differenti.


## Differential privacy

DP limita l'influenza di un record mediante clipping e rumore, con parametri epsilon e delta e un costo di utilità. [SRC-91-002]

**Caso da seguire.** Un input non fidato che raggiunge una policy esterna, con decisione allow/deny e traccia dell'evento conservate separatamente.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


![Privacy, fairness e unlearning: chart](../../assets/chapters/91_privacy_fairness/FAIRNESS-01/candidate-v50.png)

La prima figura segue il percorso da «Memorizzazione e leakage» a «Fairness».


## Fairness

Metriche di parità, equalized odds e calibration possono essere incompatibili sotto distribuzioni differenti. Il contesto decisionale guida la scelta. [SRC-91-003]

**Caso da seguire.** Per «Fairness» si mantiene l'input del capitolo e si isola questa condizione: Metriche di parità, equalized odds e calibration possono essere incompatibili sotto distribuzioni differenti.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Fairness».


## Bias nei dati e nel sistema

Rappresentazione, label, soglie e policy possono produrre disparità anche con lo stesso modello. [SRC-91-004]

**Caso da seguire.** Un input non fidato attraversa una policy esterna. Il controllo deve restare attivo anche se il modello produce una richiesta testuale convincente.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    groups = {"A": {"correct": 3, "total": 4}, "B": {"correct": 2, "total": 4}}
    accuracy = {group: value["correct"] / value["total"] for group, value in groups.items()}
    gap = abs(accuracy["A"] - accuracy["B"])
    return {"accuracy_by_group": accuracy, "gap": gap, "invariant": "aggregate utility does not hide group-specific outcomes"}
```

Esecuzione con `python snip_91_contract.py`:

```text
{"accuracy_by_group": {"A": 0.75, "B": 0.5}, "gap": 0.25, "invariant": "aggregate utility does not hide group-specific outcomes"}
```

Il test associato è [`code/test_91_contract.py`](code/test_91_contract.py); l'output versionato è [`code/outputs/SNIP-91-001.txt`](code/outputs/SNIP-91-001.txt).


## Machine unlearning

Rimuovere l'influenza di dati richiede un criterio e una verifica. Cancellare un record dal corpus non modifica automaticamente il checkpoint. [SRC-91-001]

**Caso da seguire.** Per «Machine unlearning» si mantiene l'input del capitolo e si isola questa condizione: Rimuovere l'influenza di dati richiede un criterio e una verifica.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Machine unlearning» non si applica.


![Privacy, fairness e unlearning: compare](../../assets/chapters/91_privacy_fairness/FAIRNESS-02/candidate-v48.png)

La seconda figura mette a confronto «Bias nei dati e nel sistema» e il limite discusso in «Machine unlearning».


## Come si collegano i passaggi

- **Da «Memorizzazione e leakage» a «Differential privacy».** Un modello può riprodurre sequenze rare. DP limita l'influenza di un record mediante clipping e rumore, con parametri epsilon e delta e un costo di utilità. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-91-001; SRC-91-002]

- **Da «Differential privacy» a «Fairness».** DP limita l'influenza di un record mediante clipping e rumore, con parametri epsilon e delta e un costo di utilità. Metriche di parità, equalized odds e calibration possono essere incompatibili sotto distribuzioni differenti. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-91-002; SRC-91-003]

- **Da «Fairness» a «Bias nei dati e nel sistema».** Metriche di parità, equalized odds e calibration possono essere incompatibili sotto distribuzioni differenti. Rappresentazione, label, soglie e policy possono produrre disparità anche con lo stesso modello. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-91-003; SRC-91-004]

- **Da «Bias nei dati e nel sistema» a «Machine unlearning».** Rappresentazione, label, soglie e policy possono produrre disparità anche con lo stesso modello. Rimuovere l'influenza di dati richiede un criterio e una verifica. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-91-004; SRC-91-001]

La catena completa produce utility, leakage, disparità e verifica di rimozione a partire da record, membership, gruppo, label e budget privacy. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: privacy, fairness e utility richiedono metriche e trade-off espliciti.


## Esercizi sul meccanismo

1. Ricostruisci «Memorizzazione e leakage» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Differential privacy», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Fairness» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Bias nei dati e nel sistema» che produca una failure riconoscibile.
5. Per «Machine unlearning», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «record, membership, gruppo, label e budget privacy» e arriva fino a «utility, leakage, disparità e verifica di rimozione». Il limite da conservare è questo: privacy, fairness e utility richiedono metriche e trade-off espliciti. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
