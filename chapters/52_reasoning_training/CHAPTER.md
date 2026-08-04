<!--
chapter_id: CH-P09-REASONING-TRAINING
part_id: P09
order_key: 520
title: Addestrare e distillare il reasoning
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 52. Addestrare e distillare il reasoning

La domanda guida di questa lezione è come collegare «Tracce e risposte» e «Costo e lunghezza» senza perdere il contratto tecnico di addestrare e distillare il reasoning. L'oggetto osservato è una traccia di reasoning e la risposta che la segue. Il contratto locale è: input, prompt, trace del teacher, answer e costo in token; operazione, distillazione, self-consistency e rejection sampling; output, traccia selezionata, risposta e misura di costo. Il caso guida è questo: Tre tracce producono due risposte 4 e una risposta 5; la selezione majority sceglie 4. Il confine da mantenere esplicito è: una traccia leggibile non prova faithfulness causale.

## Tracce e risposte

Una traccia di ragionamento è testo prodotto dal modello. Può aiutare il training senza costituire una prova fedele del processo interno. [SRC-52-001]

La distillazione trasferisce un comportamento osservato, non ogni capacità del teacher.

**Caso da seguire.** Tre tracce producono due risposte 4 e una risposta 5; la selezione majority sceglie 4.

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Può aiutare il training senza costituire una prova fedele del processo interno.


## Distillazione

Un teacher produce soluzioni o distribuzioni che diventano target per uno student. Filtraggio e copertura stabiliscono cosa viene trasferito. [SRC-52-004]

**Caso da seguire.** Un modello teacher e uno student confrontati sullo stesso input, con memoria e regressioni riportate insieme alla loss.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
p_student(y|x) <- p_teacher(y|x)
$$

La distillazione trasferisce un comportamento osservato, non ogni capacità del teacher. [SRC-52-001]


![Addestrare e distillare il reasoning: branch](../../assets/chapters/52_reasoning_training/TRAINING-01/candidate-v48.png)

La prima figura segue il percorso da «Tracce e risposte» a «Self-consistency e rejection sampling».


## Self-consistency e rejection sampling

Più candidate vengono generate e selezionate con voto o verifier. Il dataset risultante dipende dalla procedura di selezione. [SRC-52-002]

**Caso da seguire.** Un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Self-consistency e rejection sampling».


## Faithfulness

Una spiegazione corretta può essere post-hoc. Valutare risposta e fedeltà richiede esperimenti differenti. [SRC-52-003]

**Caso da seguire.** Due risposte con log-probabilità diverse producono un margine; il margine può diventare un segnale di training, ma non è una misura assoluta di correttezza.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    traces = [("4", 0.9), ("4", 0.7), ("5", 0.8)]
    counts = {}
    for answer, _score in traces:
        counts[answer] = counts.get(answer, 0) + 1
    selected = max(counts, key=counts.__getitem__)
    return {"trace_count": len(traces), "selected": selected, "invariant": "self-consistency selects among traces and does not prove their faithfulness"}
```

Esecuzione con `python snip_52_contract.py`:

```text
{"invariant": "self-consistency selects among traces and does not prove their faithfulness", "selected": "4", "trace_count": 3}
```

Il test associato è [`code/test_52_contract.py`](code/test_52_contract.py); l'output versionato è [`code/outputs/SNIP-52-001.txt`](code/outputs/SNIP-52-001.txt).


## Costo e lunghezza

Tracce più lunghe aumentano token e latenza. Il training deve distinguere utilità della risposta e budget del processo. [SRC-52-001]

**Caso da seguire.** Un batch di richieste eterogenee in cui throughput, coda e time-to-first-token vengono misurati separatamente.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Costo e lunghezza» non si applica.


![Addestrare e distillare il reasoning: timeline](../../assets/chapters/52_reasoning_training/TRAINING-02/candidate-v48.png)

La seconda figura mette a confronto «Faithfulness» e il limite discusso in «Costo e lunghezza».


## Come si collegano i passaggi

- **Da «Tracce e risposte» a «Distillazione».** Una traccia di ragionamento è testo prodotto dal modello. Un teacher produce soluzioni o distribuzioni che diventano target per uno student. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-52-001; SRC-52-004]

- **Da «Distillazione» a «Self-consistency e rejection sampling».** Un teacher produce soluzioni o distribuzioni che diventano target per uno student. Più candidate vengono generate e selezionate con voto o verifier. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-52-004; SRC-52-002]

- **Da «Self-consistency e rejection sampling» a «Faithfulness».** Più candidate vengono generate e selezionate con voto o verifier. Una spiegazione corretta può essere post-hoc. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-52-002; SRC-52-003]

- **Da «Faithfulness» a «Costo e lunghezza».** Una spiegazione corretta può essere post-hoc. Tracce più lunghe aumentano token e latenza. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-52-003; SRC-52-001]

La catena completa produce traccia selezionata, risposta e misura di costo a partire da prompt, trace del teacher, answer e costo in token. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: una traccia leggibile non prova faithfulness causale.


## Esercizi sul meccanismo

1. Ricostruisci «Tracce e risposte» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Distillazione», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Self-consistency e rejection sampling» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Faithfulness» che produca una failure riconoscibile.
5. Per «Costo e lunghezza», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «prompt, trace del teacher, answer e costo in token» e arriva fino a «traccia selezionata, risposta e misura di costo». Il limite da conservare è questo: una traccia leggibile non prova faithfulness causale. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
