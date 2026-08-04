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

Qui distillazione e pruning viene osservato come un meccanismo: il percorso va da «Teacher e student» a «Recovery». L'oggetto osservato è pesi del teacher, student e struttura da comprimere. Il contratto locale dichiara input, logits teacher, target, pruning mask e budget; operazione, distillazione, pruning e recovery; output, student più piccolo con loss e regressioni misurate. Il primo esempio osservabile è Teacher e student hanno due vettori di logits differenti e una mask conserva una connessione. Il limite da non nascondere è: compressione e accuratezza vanno misurate sullo stesso perimetro.

## Teacher e student

La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student. [SRC-73-001]

Compressione e accuratezza vanno misurate nello stesso perimetro.

**Caso da seguire.** Teacher e student hanno due vettori di logits differenti e una mask conserva una connessione.

**Controllo.** Per «Teacher e student», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Teacher e student», il vincolo da conservare è: La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student.


## Temperature e loss

Una temperatura più alta rivela relazioni tra classi o token. Hard target e soft target vengono pesati separatamente. [SRC-73-002]

**Caso da seguire.** Due logits trasferiti e una connessione potata con recovery.

**Controllo.** Per «Temperature e loss», ricalcola il caso a mano e con lo snippet. Nel caso «Temperature e loss», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


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

**Controllo.** Per «Sequence distillation», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Sequence distillation».


## Pruning

Pesi, canali, head o layer possono essere rimossi. Sparsità nominale e accelerazione reale dipendono da kernel e hardware. [SRC-73-004]

**Caso da seguire.** Per «Pruning» si mantiene l'input del capitolo e si isola questa condizione: Pesi, canali, head o layer possono essere rimossi.

**Controllo.** Per «Pruning», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Pruning», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il caso computazionale di distillazione e pruning è riportato senza trasformazioni: il file e l'output sono quelli verificati. Per «Distillazione e pruning», il caso di default usa valori piccoli per isolare il meccanismo. La suite conserva inoltre una failure esplicita per separare il contratto osservato da «distillazione e pruning».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
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

**Controllo.** Per «Recovery», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Recovery» non si applica.


![Distillazione e pruning: compare](../../assets/chapters/73_distillation_pruning/PRUNING-02/candidate-v48.png)

La seconda figura mette a confronto «Pruning» e il limite discusso in «Recovery».


## Come si collegano i passaggi

- **Da «Teacher e student» a «Temperature e loss».** La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student. Una temperatura più alta rivela relazioni tra classi o token. Tra «Teacher e student» e «Temperature e loss» l'ingresso viene fissato prima della regola che produce il valore. Da «Teacher e student» a «Temperature e loss» cambia la domanda osservabile. [SRC-73-001; SRC-73-002]

- **Da «Temperature e loss» a «Sequence distillation».** Una temperatura più alta rivela relazioni tra classi o token. Per modelli generativi, risposte del teacher diventano un nuovo dataset. Nel caso «Sequence distillation» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «Sequence distillation». [SRC-73-002; SRC-73-003]

- **Da «Sequence distillation» a «Pruning».** Per modelli generativi, risposte del teacher diventano un nuovo dataset. Pesi, canali, head o layer possono essere rimossi. Dopo «Sequence distillation», la variante di «Pruning» cambia una proprietà alla volta. Da «Sequence distillation» a «Pruning» cambia la domanda osservabile. [SRC-73-003; SRC-73-004]

- **Da «Pruning» a «Recovery».** Pesi, canali, head o layer possono essere rimossi. Fine-tuning o calibration recuperano qualità dopo compressione. Da «Recovery» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «Recovery». [SRC-73-004; SRC-73-001]

La catena completa produce student più piccolo con loss e regressioni misurate a partire da logits teacher, target, pruning mask e budget. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: compressione e accuratezza vanno misurate sullo stesso perimetro.


## Esercizi sul meccanismo

1. Ricostruisci «Teacher e student» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Temperature e loss», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Sequence distillation» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Pruning» che produca una failure riconoscibile.
5. Per «Recovery», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «logits teacher, target, pruning mask e budget» e arriva fino a «student più piccolo con loss e regressioni misurate». Il limite da conservare è questo: compressione e accuratezza vanno misurate sullo stesso perimetro. La formula e il codice collegati a «Recovery» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
