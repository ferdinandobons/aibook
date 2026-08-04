<!--
chapter_id: CH-P12-DISTILLATION-PRUNING
part_id: P12
order_key: 730
title: Distillazione e pruning
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 73. Distillazione e pruning

La domanda guida di questa lezione è come collegare «Teacher e student» e «Recovery» senza perdere il contratto tecnico di distillazione e pruning. L'oggetto osservato è pesi del teacher, student e struttura da comprimere. Il contratto locale è: input, logits teacher, target, pruning mask e budget; operazione, distillazione, pruning e recovery; output, student più piccolo con loss e regressioni misurate. Il caso guida è questo: Teacher e student hanno due vettori di logits differenti e una mask conserva una connessione. Il confine da mantenere esplicito è: compressione e accuratezza vanno misurate sullo stesso perimetro.

## Teacher e student

La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student. [SRC-73-001]

Compressione e accuratezza vanno misurate nello stesso perimetro.

**Caso da seguire.** Teacher e student hanno due vettori di logits differenti e una mask conserva una connessione.

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student.


## Temperature e loss

Una temperatura più alta rivela relazioni tra classi o token. Hard target e soft target vengono pesati separatamente. [SRC-73-002]

**Caso da seguire.** Due logits trasferiti e una connessione potata con recovery.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
L_student = distill(L_teacher) + lambda R
$$

Compressione e accuratezza vanno misurate nello stesso perimetro. [SRC-73-001]


![Distillazione e pruning: pipeline](../../assets/chapters/73_distillation_pruning/PRUNING-01/candidate-v48.png)

La prima figura segue il percorso da «Teacher e student» a «Sequence distillation».


## Sequence distillation

Per modelli generativi, risposte del teacher diventano un nuovo dataset. Filtri e diversità determinano ciò che lo student vede. [SRC-73-003]

**Caso da seguire.** Un modello teacher e uno student confrontati sullo stesso input, con memoria e regressioni riportate insieme alla loss.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Sequence distillation».


## Pruning

Pesi, canali, head o layer possono essere rimossi. Sparsità nominale e accelerazione reale dipendono da kernel e hardware. [SRC-73-004]

**Caso da seguire.** Per «Pruning» si mantiene l'input del capitolo e si isola questa condizione: Pesi, canali, head o layer possono essere rimossi.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    teacher = [0.8, 0.2]
    student = [0.6, 0.4]
    distillation_error = sum((a - b) ** 2 for a, b in zip(teacher, student))
    mask = [True, False]
    return {"distillation_error": round(distillation_error, 6), "kept_weights": sum(mask), "invariant": "compression quality and structural pruning are measured separately"}
```

Esecuzione con `python snip_73_contract.py`:

```text
{"distillation_error": 0.08, "invariant": "compression quality and structural pruning are measured separately", "kept_weights": 1}
```

Il test associato è [`code/test_73_contract.py`](code/test_73_contract.py); l'output versionato è [`code/outputs/SNIP-73-001.txt`](code/outputs/SNIP-73-001.txt).


## Recovery

Fine-tuning o calibration recuperano qualità dopo compressione. Il confronto deve includere memoria, latency e regressioni per slice. [SRC-73-001]

**Caso da seguire.** Una metrica del compito nuovo confrontata con la stessa metrica sul comportamento precedente.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Recovery» non si applica.


![Distillazione e pruning: compare](../../assets/chapters/73_distillation_pruning/PRUNING-02/candidate-v48.png)

La seconda figura mette a confronto «Pruning» e il limite discusso in «Recovery».


## Come si collegano i passaggi

- **Da «Teacher e student» a «Temperature e loss».** La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student. Una temperatura più alta rivela relazioni tra classi o token. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-73-001; SRC-73-002]

- **Da «Temperature e loss» a «Sequence distillation».** Una temperatura più alta rivela relazioni tra classi o token. Per modelli generativi, risposte del teacher diventano un nuovo dataset. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-73-002; SRC-73-003]

- **Da «Sequence distillation» a «Pruning».** Per modelli generativi, risposte del teacher diventano un nuovo dataset. Pesi, canali, head o layer possono essere rimossi. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-73-003; SRC-73-004]

- **Da «Pruning» a «Recovery».** Pesi, canali, head o layer possono essere rimossi. Fine-tuning o calibration recuperano qualità dopo compressione. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-73-004; SRC-73-001]

La catena completa produce student più piccolo con loss e regressioni misurate a partire da logits teacher, target, pruning mask e budget. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: compressione e accuratezza vanno misurate sullo stesso perimetro.


## Esercizi sul meccanismo

1. Ricostruisci «Teacher e student» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Temperature e loss», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Sequence distillation» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Pruning» che produca una failure riconoscibile.
5. Per «Recovery», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «logits teacher, target, pruning mask e budget» e arriva fino a «student più piccolo con loss e regressioni misurate». Il limite da conservare è questo: compressione e accuratezza vanno misurate sullo stesso perimetro. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
