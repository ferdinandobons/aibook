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

La lezione prende un caso piccolo e lo accompagna da «Parametri congelati e adattamento» fino a «QLoRA e compatibilità», senza saltare i passaggi. L'oggetto osservato è l'aggiornamento adattivo rispetto ai pesi congelati. Il contratto locale dichiara input, peso W, matrice A e B, rank e quantizzazione; operazione, adapter, LoRA, prefix o QLoRA; output, delta W e checkpoint adattatore. Il caso di partenza è Un peso base e un aggiornamento di rank uno producono un delta misurabile senza riscrivere il checkpoint base. Il limite da non nascondere è: il delta non è il modello completo e va valutato sullo stesso base model.

## Parametri congelati e adattamento

PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint. [SRC-47-001]

Un aggiornamento low-rank cambia pochi gradi di libertà dichiarati.

**Caso da seguire.** Un peso base e un aggiornamento di rank uno producono un delta misurabile senza riscrivere il checkpoint base.

**Controllo.** Per «Parametri congelati e adattamento», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Parametri congelati e adattamento», il vincolo da conservare è: PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint.


## Adapter

Blocchi bottleneck vengono inseriti nel percorso residuale. Posizione, dimensione e inizializzazione determinano l'interfaccia con il modello base. [SRC-47-002]

**Caso da seguire.** Delta W = B A con rank uno su una matrice piccola.

**Controllo.** Per «Adapter», ricalcola il caso a mano e con lo snippet. Nel caso «Adapter», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


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

**Controllo.** Per «LoRA», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «LoRA».


## Prompt, prefix e IA3

Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti. [SRC-47-004]

**Caso da seguire.** Due risposte con log-probabilità diverse producono un margine; il margine può diventare un segnale di training, ma non è una misura assoluta di correttezza.

**Controllo.** Per «Prompt, prefix e IA3», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Prompt, prefix e IA3», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

La prova locale di fine-tuning efficiente parte da un esempio minimo, registrato nel repository insieme ai suoi test. Per «Fine-tuning efficiente», il caso di default usa valori piccoli per isolare il meccanismo. La prova negativa riguarda proprio «fine-tuning efficiente» e interrompe l'interpretazione prima dell'output.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
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

**Controllo.** Per «QLoRA e compatibilità», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «QLoRA e compatibilità» non si applica.


![Fine-tuning efficiente: compare](../../assets/chapters/47_peft/PEFT-02/candidate-v48.png)

La seconda figura mette a confronto «Prompt, prefix e IA3» e il limite discusso in «QLoRA e compatibilità».


## Come si collegano i passaggi

- **Da «Parametri congelati e adattamento» a «Adapter».** PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint. Blocchi bottleneck vengono inseriti nel percorso residuale. Tra «Parametri congelati e adattamento» e «Adapter» l'ingresso viene fissato prima della regola che produce il valore. Da «Parametri congelati e adattamento» a «Adapter» cambia la domanda osservabile. [SRC-47-001; SRC-47-002]

- **Da «Adapter» a «LoRA».** Blocchi bottleneck vengono inseriti nel percorso residuale. Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference. Nel caso «LoRA» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «LoRA». [SRC-47-002; SRC-47-003]

- **Da «LoRA» a «Prompt, prefix e IA3».** Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference. Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti. Dopo «LoRA», la variante di «Prompt, prefix e IA3» cambia una proprietà alla volta. Da «LoRA» a «Prompt, prefix e IA3» cambia la domanda osservabile. [SRC-47-003; SRC-47-004]

- **Da «Prompt, prefix e IA3» a «QLoRA e compatibilità».** Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti. Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili. Da «QLoRA e compatibilità» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «QLoRA e compatibilità». [SRC-47-004; SRC-47-001]

La catena completa produce delta W e checkpoint adattatore a partire da peso W, matrice A e B, rank e quantizzazione. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: il delta non è il modello completo e va valutato sullo stesso base model.


## Esercizi sul meccanismo

1. Ricostruisci «Parametri congelati e adattamento» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Adapter», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «LoRA» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Prompt, prefix e IA3» che produca una failure riconoscibile.
5. Per «QLoRA e compatibilità», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «peso W, matrice A e B, rank e quantizzazione» e arriva fino a «delta W e checkpoint adattatore». Il limite da conservare è questo: il delta non è il modello completo e va valutato sullo stesso base model. La formula e il codice collegati a «QLoRA e compatibilità» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
