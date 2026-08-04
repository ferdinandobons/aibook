<!--
chapter_id: CH-P05-AUTOREGRESSIVE
part_id: P05
order_key: 210
title: Modelli autoregressivi
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 21. Modelli autoregressivi

Per entrare in modelli autoregressivi, seguiamo il passaggio che unisce «Fattorizzare una sequenza» a «Immagini, audio e token discreti». L'oggetto osservato è la sequenza di token e la distribuzione del prossimo elemento. Il contratto locale dichiara input, un prefisso di tre token e una mask causale; operazione, fattorizzazione, teacher forcing e decoding; output, logits, token scelto e traiettoria. Il primo esempio osservabile è Tre passi in cui lo stato precedente viene consumato prima di produrre il successivo. Il limite da non nascondere è: nessuna posizione futura entra nella predizione causale.

## Fattorizzare una sequenza

La chain rule scompone la probabilità con un ordine. Ogni fattore condiziona sugli elementi precedenti. [SRC-21-001]

La chain rule rende l'autoregressione una sequenza di predizioni condizionate.

**Caso da seguire.** Tre passi in cui lo stato precedente viene consumato prima di produrre il successivo.

**Controllo.** Per «Fattorizzare una sequenza», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Fattorizzare una sequenza», il vincolo da conservare è: Ogni fattore condiziona sugli elementi precedenti.


## Teacher forcing

Durante il training il modello riceve il prefisso reale e predice il passo successivo. Durante la generazione riceve anche i propri output. [SRC-21-002]

**Caso da seguire.** Un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente.

**Controllo.** Per «Teacher forcing», ricalcola il caso a mano e con lo snippet. Nel caso «Teacher forcing», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
p(x_{1:T})=\prod_t p(x_t|x_{<t})
$$

La chain rule rende l'autoregressione una sequenza di predizioni condizionate. [SRC-21-001]


![Modelli autoregressivi: timeline](../../assets/chapters/21_autoregressive/AUTOREGR-01/candidate-v49.png)

La prima figura segue il percorso da «Fattorizzare una sequenza» a «Maschera causale».


## Maschera causale

La causal mask impedisce a una posizione di usare target futuri. Un errore nella maschera produce leakage pur con loss numericamente valida. [SRC-21-003]

**Caso da seguire.** Una matrice di visibilità in cui la posizione futura resta esclusa anche se la shape dei tensori è compatibile.

**Controllo.** Per «Maschera causale», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Maschera causale».


## Sampling e accumulo degli errori

Ogni scelta modifica il contesto successivo. Errori iniziali possono spostare la traiettoria verso regioni poco viste nel training. [SRC-21-004]

**Caso da seguire.** Per «Sampling e accumulo degli errori» si mantiene l'input del capitolo e si isola questa condizione: Ogni scelta modifica il contesto successivo.

**Controllo.** Per «Sampling e accumulo degli errori», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Sampling e accumulo degli errori», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il caso computazionale di modelli autoregressivi è riportato senza trasformazioni: il file e l'output sono quelli verificati. Per «Modelli autoregressivi», il caso di default usa valori piccoli per isolare il meccanismo. La suite conserva inoltre una failure esplicita per separare il contratto osservato da «modelli autoregressivi».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    logits = [[2.0, 1.0, 0.0], [4.0, 3.0, 2.0]]
    causal = [[True, False, False], [True, True, False]]
    visible = [[row[j] for j in range(len(row)) if causal[i][j]] for i, row in enumerate(logits)]
    return {"visible_lengths": [len(row) for row in visible], "invariant": "a causal position cannot read a future token"}
```

Esecuzione con `python snip_21_contract.py`:

```text
{"invariant": "a causal position cannot read a future token", "visible_lengths": [1, 2]}
```

Il test associato è [`code/test_21_contract.py`](code/test_21_contract.py); l'output versionato è [`code/outputs/SNIP-21-001.txt`](code/outputs/SNIP-21-001.txt).


## Immagini, audio e token discreti

L'autoregressione non è limitata al testo. Una sequenza può rappresentare pixel, code audio o latent discreti. [SRC-21-001]

**Caso da seguire.** Un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati.

**Controllo.** Per «Immagini, audio e token discreti», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Immagini, audio e token discreti» non si applica.


![Modelli autoregressivi: pipeline](../../assets/chapters/21_autoregressive/AUTOREGR-02/candidate-v49.png)

La seconda figura mette a confronto «Sampling e accumulo degli errori» e il limite discusso in «Immagini, audio e token discreti».


## Come si collegano i passaggi

- **Da «Fattorizzare una sequenza» a «Teacher forcing».** La chain rule scompone la probabilità con un ordine. Durante il training il modello riceve il prefisso reale e predice il passo successivo. Tra «Fattorizzare una sequenza» e «Teacher forcing» l'ingresso viene fissato prima della regola che produce il valore. Da «Fattorizzare una sequenza» a «Teacher forcing» cambia la domanda osservabile. [SRC-21-001; SRC-21-002]

- **Da «Teacher forcing» a «Maschera causale».** Durante il training il modello riceve il prefisso reale e predice il passo successivo. La causal mask impedisce a una posizione di usare target futuri. Nel caso «Maschera causale» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «Maschera causale». [SRC-21-002; SRC-21-003]

- **Da «Maschera causale» a «Sampling e accumulo degli errori».** La causal mask impedisce a una posizione di usare target futuri. Ogni scelta modifica il contesto successivo. Dopo «Maschera causale», la variante di «Sampling e accumulo degli errori» cambia una proprietà alla volta. Da «Maschera causale» a «Sampling e accumulo degli errori» cambia la domanda osservabile. [SRC-21-003; SRC-21-004]

- **Da «Sampling e accumulo degli errori» a «Immagini, audio e token discreti».** Ogni scelta modifica il contesto successivo. L'autoregressione non è limitata al testo. Da «Immagini, audio e token discreti» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «Immagini, audio e token discreti». [SRC-21-004; SRC-21-001]

La catena completa produce logits, token scelto e traiettoria a partire da un prefisso di tre token e una mask causale. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: nessuna posizione futura entra nella predizione causale.


## Esercizi sul meccanismo

1. Ricostruisci «Fattorizzare una sequenza» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Teacher forcing», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Maschera causale» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Sampling e accumulo degli errori» che produca una failure riconoscibile.
5. Per «Immagini, audio e token discreti», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «un prefisso di tre token e una mask causale» e arriva fino a «logits, token scelto e traiettoria». Il limite da conservare è questo: nessuna posizione futura entra nella predizione causale. La formula e il codice collegati a «Immagini, audio e token discreti» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
