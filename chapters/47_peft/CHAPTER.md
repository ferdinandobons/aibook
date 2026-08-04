<!--
chapter_id: CH-P09-PEFT
part_id: P09
order_key: 470
title: Fine-tuning efficiente
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 47. Fine-tuning efficiente

La domanda guida di questa lezione è come collegare «Parametri congelati e adattamento» e «QLoRA e compatibilità» senza perdere il contratto tecnico di fine-tuning efficiente. L'oggetto osservato è l'aggiornamento adattivo rispetto ai pesi congelati. Il contratto locale è: input, peso W, matrice A e B, rank e quantizzazione; operazione, adapter, LoRA, prefix o QLoRA; output, delta W e checkpoint adattatore. Il caso guida è questo: Un peso base e un aggiornamento di rank uno producono un delta misurabile senza riscrivere il checkpoint base. Il confine da mantenere esplicito è: il delta non è il modello completo e va valutato sullo stesso base model.

## Parametri congelati e adattamento

PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint. [SRC-47-001]

Un aggiornamento low-rank cambia pochi gradi di libertà dichiarati.

**Caso da seguire.** Un peso base e un aggiornamento di rank uno producono un delta misurabile senza riscrivere il checkpoint base.

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint.


## Adapter

Blocchi bottleneck vengono inseriti nel percorso residuale. Posizione, dimensione e inizializzazione determinano l'interfaccia con il modello base. [SRC-47-002]

**Caso da seguire.** Delta W = B A con rank uno su una matrice piccola.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
Delta W = B A
$$

Un aggiornamento low-rank cambia pochi gradi di libertà dichiarati. [SRC-47-001]


![Fine-tuning efficiente: architecture](../../assets/chapters/47_peft/PEFT-01/candidate-v48.png)

La prima figura segue il percorso da «Parametri congelati e adattamento» a «LoRA».


## LoRA

Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference. [SRC-47-003]

**Caso da seguire.** Un caso in cui il delta non è il modello completo e va valutato sullo stesso base model.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «LoRA».


## Prompt, prefix e IA3

Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti. [SRC-47-004]

**Caso da seguire.** Due risposte con log-probabilità diverse producono un margine; il margine può diventare un segnale di training, ma non è una misura assoluta di correttezza.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    base = [1.0, 2.0]
    direction_a = [0.5, 0.0]
    direction_b = [0.0, -0.25]
    scale = 0.4
    delta = [scale * (a + b) for a, b in zip(direction_a, direction_b)]
    adapted = [value + change for value, change in zip(base, delta)]
    return {"delta": delta, "adapted": adapted, "invariant": "the low-rank update is separated from frozen base weights"}
```

Esecuzione con `python snip_47_contract.py`:

```text
{"adapted": [1.2, 1.9], "delta": [0.2, -0.1], "invariant": "the low-rank update is separated from frozen base weights"}
```

Il test associato è [`code/test_47_contract.py`](code/test_47_contract.py); l'output versionato è [`code/outputs/SNIP-47-001.txt`](code/outputs/SNIP-47-001.txt).


## QLoRA e compatibilità

Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili. Formato, tokenizer e architettura devono corrispondere. [SRC-47-001]

**Caso da seguire.** Per «QLoRA e compatibilità» si mantiene l'input del capitolo e si isola questa condizione: Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «QLoRA e compatibilità» non si applica.


![Fine-tuning efficiente: compare](../../assets/chapters/47_peft/PEFT-02/candidate-v48.png)

La seconda figura mette a confronto «Prompt, prefix e IA3» e il limite discusso in «QLoRA e compatibilità».


## Come si collegano i passaggi

- **Da «Parametri congelati e adattamento» a «Adapter».** PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint. Blocchi bottleneck vengono inseriti nel percorso residuale. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-47-001; SRC-47-002]

- **Da «Adapter» a «LoRA».** Blocchi bottleneck vengono inseriti nel percorso residuale. Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-47-002; SRC-47-003]

- **Da «LoRA» a «Prompt, prefix e IA3».** Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference. Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-47-003; SRC-47-004]

- **Da «Prompt, prefix e IA3» a «QLoRA e compatibilità».** Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti. Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-47-004; SRC-47-001]

La catena completa produce delta W e checkpoint adattatore a partire da peso W, matrice A e B, rank e quantizzazione. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: il delta non è il modello completo e va valutato sullo stesso base model.


## Esercizi sul meccanismo

1. Ricostruisci «Parametri congelati e adattamento» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Adapter», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «LoRA» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Prompt, prefix e IA3» che produca una failure riconoscibile.
5. Per «QLoRA e compatibilità», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «peso W, matrice A e B, rank e quantizzazione» e arriva fino a «delta W e checkpoint adattatore». Il limite da conservare è questo: il delta non è il modello completo e va valutato sullo stesso base model. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
