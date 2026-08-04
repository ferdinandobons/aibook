<!--
chapter_id: CH-P07-DATA-MIXTURE
part_id: P07
order_key: 330
title: Dataset mixture, curriculum e dati sintetici
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 33. Dataset mixture, curriculum e dati sintetici

In dataset mixture, curriculum e dati sintetici il percorso dei record è il filo conduttore: da «Peso effettivo delle sorgenti» a «Dati sintetici» ogni trasformazione lascia una traccia. L'oggetto osservato è la miscela effettiva di sorgenti durante il training. Il contratto locale dichiara input, pesi, temperatura, curriculum e conteggio dei token; operazione, campionamento, ripesatura e generazione controllata; output, probabilità effettive e mix osservato. Il primo esempio osservabile è Due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata. Il limite da non nascondere è: peso nominale e esposizione effettiva non sono la stessa misura.

## Peso effettivo delle sorgenti

Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni. [SRC-33-001]

Il campionamento modifica le esposizioni effettive, non la dimensione grezza delle sorgenti.

**Caso da seguire.** Due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata.

**Controllo.** Per «Peso effettivo delle sorgenti», conserva record iniziale, regola applicata e record finale; un conteggio aggregato non basta a spiegare la trasformazione.


La relazione centrale può essere scritta come:

$$
p_i = w_i^tau / sum_j w_j^tau
$$

Il campionamento modifica le esposizioni effettive, non la dimensione grezza delle sorgenti. [SRC-33-001]


![Dataset mixture, curriculum e dati sintetici: compare](../../assets/chapters/33_data_mixture/MIX-01/candidate-v47.png)

La prima figura segue il percorso da «Peso effettivo delle sorgenti» a «Mixture ottimizzata».


## Temperature sampling

Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli. [SRC-33-002]

**Caso da seguire.** Un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente.

**Controllo.** Esegui «Temperature sampling» due volte sullo stesso manifest e confronta identificatori, ordine, split e checksum.


## Mixture ottimizzata

Pesi appresi con proxy model dipendono da domini, validation e budget. [SRC-33-003]

**Caso da seguire.** Per «Mixture ottimizzata» si mantiene l'input del capitolo e si isola questa condizione: Pesi appresi con proxy model dipendono da domini, validation e budget.

**Controllo.** Per «Mixture ottimizzata», aggiungi un record che deve essere escluso e verifica che l'output conservi anche il motivo dell'esclusione.


## Esempio Python eseguito

Il caso computazionale di dataset mixture, curriculum e dati sintetici è riportato senza trasformazioni: il file e l'output sono quelli verificati. Per «Dataset mixture, curriculum e dati sintetici», il caso di default usa valori piccoli per isolare il meccanismo. La suite conserva inoltre una failure esplicita per separare il contratto osservato da «dataset mixture, curriculum e dati sintetici».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    weights = [0.6, 0.3, 0.1]
    temperature = 0.5
    powered = [weight ** temperature for weight in weights]
    total = sum(powered)
    probabilities = [value / total for value in powered]
    return {"probabilities": [round(value, 6) for value in probabilities], "invariant": "the mixture is normalized after temperature sampling"}
```

Esecuzione con `python snip_33_contract.py`:

```text
{"invariant": "the mixture is normalized after temperature sampling", "probabilities": [0.472734, 0.334273, 0.192993]}
```

Il test associato è [`code/test_33_contract.py`](code/test_33_contract.py); l'output versionato è [`code/outputs/SNIP-33-001.txt`](code/outputs/SNIP-33-001.txt).


## Curriculum

Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione. [SRC-33-004]

**Caso da seguire.** Per «Curriculum» si mantiene l'input del capitolo e si isola questa condizione: Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione.

**Controllo.** Per «Curriculum», modifica una sola regola della pipeline e misura quali record cambiano, evitando di confrontare raccolte di origine diversa.


## Dati sintetici

Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato. [SRC-33-001]

**Caso da seguire.** Per «Dati sintetici» si mantiene l'input del capitolo e si isola questa condizione: Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato.

**Controllo.** Per «Dati sintetici», descrivi ciò che la pipeline perde oltre a ciò che produce. Nel caso «Dati sintetici», il limite locale è: Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato.


![Dataset mixture, curriculum e dati sintetici: chart](../../assets/chapters/33_data_mixture/MIX-02/candidate-v47.png)

La seconda figura mette a confronto «Curriculum» e il limite discusso in «Dati sintetici».


## Come si collegano i passaggi

- **Da «Peso effettivo delle sorgenti» a «Temperature sampling».** Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni. Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli. «Peso effettivo delle sorgenti» identifica il record e «Temperature sampling» dichiara la trasformazione sulla popolazione osservata. Da «Peso effettivo delle sorgenti» a «Temperature sampling» cambia la domanda osservabile. [SRC-33-001; SRC-33-002]

- **Da «Temperature sampling» a «Mixture ottimizzata».** Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli. Pesi appresi con proxy model dipendono da domini, validation e budget. Il passaggio da «Temperature sampling» a «Mixture ottimizzata» conserva configurazione, conteggi e artefatti intermedi. Il passaggio successivo rende misurabile «Mixture ottimizzata». [SRC-33-002; SRC-33-003]

- **Da «Mixture ottimizzata» a «Curriculum».** Pesi appresi con proxy model dipendono da domini, validation e budget. Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione. Con «Curriculum» la pipeline può selezionare o usare dati senza confonderli con una modifica del modello. Da «Mixture ottimizzata» a «Curriculum» cambia la domanda osservabile. [SRC-33-003; SRC-33-004]

- **Da «Curriculum» a «Dati sintetici».** Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione. Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato. «Dati sintetici» porta il risultato alla valutazione e rende visibili record, slice e failure esclusi. Il passaggio successivo rende misurabile «Dati sintetici». [SRC-33-004; SRC-33-001]

La catena completa produce probabilità effettive e mix osservato a partire da pesi, temperatura, curriculum e conteggio dei token. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: peso nominale e esposizione effettiva non sono la stessa misura.


## Esercizi sulla tracciabilità

1. Ricostruisci «Peso effettivo delle sorgenti» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Temperature sampling», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Mixture ottimizzata» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Curriculum» che produca una failure riconoscibile.
5. Per «Dati sintetici», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## L'artefatto che deve sopravvivere

La lezione parte da «pesi, temperatura, curriculum e conteggio dei token» e arriva fino a «probabilità effettive e mix osservato». Il limite da conservare è questo: peso nominale e esposizione effettiva non sono la stessa misura. Per «Dati sintetici», provenienza e trasformazioni sono registrate in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e negli artefatti di `code/`.
