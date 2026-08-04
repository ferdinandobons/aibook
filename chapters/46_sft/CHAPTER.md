<!--
chapter_id: CH-P09-SFT
part_id: P09
order_key: 460
title: Supervised fine-tuning e instruction tuning
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 46. Supervised fine-tuning e instruction tuning

Qui supervised fine-tuning e instruction tuning viene osservato come un meccanismo: il percorso va da «Dal pretraining alle istruzioni» a «Catastrophic forgetting e controllo». L'oggetto osservato è una coppia prompt-risposta nel formato di instruction tuning. Il contratto locale dichiara input, messaggi, target, mask delle label e mixture; operazione, teacher forcing e aggiornamento supervisionato; output, loss per token e comportamento adattato. Per fissare il riferimento usiamo Una conversazione con quattro token assegna la loss soltanto ai due token della risposta. Il limite da non nascondere è: il formato dei dati e le label decidono che cosa viene ottimizzato.

## Dal pretraining alle istruzioni

Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate. [SRC-46-001]

SFT assegna target espliciti, ma la qualità dipende da dati, formato e copertura.

**Caso da seguire.** Una conversazione con quattro token assegna la loss soltanto ai due token della risposta.

**Controllo.** Per «Dal pretraining alle istruzioni», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Dal pretraining alle istruzioni», il vincolo da conservare è: Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate.


## Formati conversazionali

Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente. [SRC-46-002]

**Caso da seguire.** Un messaggio utente e una risposta con loss solo sulla risposta.

**Controllo.** Per «Formati conversazionali», ricalcola il caso a mano e con lo snippet. Nel caso «Formati conversazionali», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
L = -sum_t log p_theta(y_t | x, y_<t)
$$

SFT assegna target espliciti, ma la qualità dipende da dati, formato e copertura. [SRC-46-001]


![Supervised fine-tuning e instruction tuning: pipeline](../../assets/chapters/46_sft/SFT-01/candidate-v48.png)

La prima figura segue il percorso da «Dal pretraining alle istruzioni» a «Instruction mixture».


## Instruction mixture

Compiti e domini vengono mescolati con pesi espliciti. La quantità di esempi non coincide automaticamente con il loro contributo utile. [SRC-46-003]

**Caso da seguire.** Due sorgenti con conteggi diversi confrontate dopo una regola di campionamento dichiarata.

**Controllo.** Per «Instruction mixture», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Instruction mixture».


## Teacher forcing e generalizzazione

Durante il training il modello vede il prefisso corretto. La capacità di seguire istruzioni nuove deve essere valutata su template e domini separati. [SRC-46-004]

**Caso da seguire.** Un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente.

**Controllo.** Per «Teacher forcing e generalizzazione», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Teacher forcing e generalizzazione», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Questa sezione apre il contratto Python di supervised fine-tuning e instruction tuning: il lettore può eseguire lo stesso file e confrontare il risultato. Per «Supervised fine-tuning e instruction tuning», il caso di default usa valori piccoli per isolare il meccanismo. Il caso non supportato viene provato separatamente, così «supervised fine-tuning e instruction tuning» non viene generalizzato oltre l'esempio.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    tokens = ["utente", "domanda", "assistente", "risposta"]
    labels = [False, False, True, True]
    supervised = [token for token, include in zip(tokens, labels) if include]
    return {"supervised_tokens": supervised, "label_count": sum(labels), "invariant": "loss masking distinguishes prompt tokens from target tokens"}
```

Esecuzione con `python snip_46_contract.py`:

```text
{"invariant": "loss masking distinguishes prompt tokens from target tokens", "label_count": 2, "supervised_tokens": ["assistente", "risposta"]}
```

Il test associato è [`code/test_46_contract.py`](code/test_46_contract.py); l'output versionato è [`code/outputs/SNIP-46-001.txt`](code/outputs/SNIP-46-001.txt).


## Catastrophic forgetting e controllo

Learning rate, durata e replay influenzano la perdita di capacità precedenti. Base model, modello SFT e sistema devono restare identificabili. [SRC-46-001]

**Caso da seguire.** Una metrica del compito nuovo confrontata con la stessa metrica sul comportamento precedente.

**Controllo.** Per «Catastrophic forgetting e controllo», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Catastrophic forgetting e controllo» non si applica.


![Supervised fine-tuning e instruction tuning: branch](../../assets/chapters/46_sft/SFT-02/candidate-v48.png)

La seconda figura mette a confronto «Teacher forcing e generalizzazione» e il limite discusso in «Catastrophic forgetting e controllo».


## Come si collegano i passaggi

- **Da «Dal pretraining alle istruzioni» a «Formati conversazionali».** Il modello preaddestrato continua a ottimizzare una loss autoregressiva, ma i dati ora collegano richieste, contesto e risposte desiderate. Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente. Tra «Dal pretraining alle istruzioni» e «Formati conversazionali» l'ingresso viene fissato prima della regola che produce il valore. Il passaggio successivo rende misurabile «Formati conversazionali». [SRC-46-001; SRC-46-002]

- **Da «Formati conversazionali» a «Instruction mixture».** Ruoli, separatori, system message e loss mask definiscono quali token sono input e quali producono gradiente. Compiti e domini vengono mescolati con pesi espliciti. Nel caso «Instruction mixture» il componente diventa il punto in cui localizzare l'errore. Da «Formati conversazionali» a «Instruction mixture» cambia la domanda osservabile. [SRC-46-002; SRC-46-003]

- **Da «Instruction mixture» a «Teacher forcing e generalizzazione».** Compiti e domini vengono mescolati con pesi espliciti. Durante il training il modello vede il prefisso corretto. Dopo «Instruction mixture», la variante di «Teacher forcing e generalizzazione» cambia una proprietà alla volta. Il passaggio successivo rende misurabile «Teacher forcing e generalizzazione». [SRC-46-003; SRC-46-004]

- **Da «Teacher forcing e generalizzazione» a «Catastrophic forgetting e controllo».** Durante il training il modello vede il prefisso corretto. Learning rate, durata e replay influenzano la perdita di capacità precedenti. Da «Catastrophic forgetting e controllo» in poi la misura resta distinta dalla correttezza locale del calcolo. Da «Teacher forcing e generalizzazione» a «Catastrophic forgetting e controllo» cambia la domanda osservabile. [SRC-46-004; SRC-46-001]

La catena completa produce loss per token e comportamento adattato a partire da messaggi, target, mask delle label e mixture. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: il formato dei dati e le label decidono che cosa viene ottimizzato.


## Esercizi sul meccanismo

1. Ricostruisci «Dal pretraining alle istruzioni» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Formati conversazionali», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Instruction mixture» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Teacher forcing e generalizzazione» che produca una failure riconoscibile.
5. Per «Catastrophic forgetting e controllo», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «messaggi, target, mask delle label e mixture» e arriva fino a «loss per token e comportamento adattato». Il limite da conservare è questo: il formato dei dati e le label decidono che cosa viene ottimizzato. La formula e il codice collegati a «Catastrophic forgetting e controllo» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
