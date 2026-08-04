<!--
chapter_id: CH-P12-DECODING
part_id: P12
order_key: 760
title: Decoding e generazione vincolata
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 76. Decoding e generazione vincolata

La domanda guida di questa lezione è come collegare «Greedy e beam search» e «Metriche» senza perdere il contratto tecnico di decoding e generazione vincolata. L'oggetto osservato è logits e spazio delle sequenze ammissibili. Il contratto locale è: input, logits, prefisso, temperatura e vincolo; operazione, greedy, beam, sampling, penalty e stop; output, token scelto, sequenza e metrica di costo. Il caso guida è questo: Lo stesso vettore di logits produce un token greedy e un supporto di sampling espliciti. Il confine da mantenere esplicito è: il decoding modifica la traiettoria, non corregge il modello a monte.

## Greedy e beam search

Greedy sceglie il massimo locale; beam mantiene più prefissi secondo score accumulati e criteri di lunghezza. [SRC-76-001]

Vincoli di decoding cambiano lo spazio delle sequenze ammissibili.

**Caso da seguire.** Lo stesso vettore di logits produce un token greedy e un supporto di sampling espliciti.

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Greedy sceglie il massimo locale; beam mantiene più prefissi secondo score accumulati e criteri di lunghezza.


## Sampling

Temperature, top-k e top-p modificano la distribuzione prima dell'estrazione. Seed e backend influenzano la riproducibilità. [SRC-76-002]

**Caso da seguire.** Un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


![Decoding e generazione vincolata: branch](../../assets/chapters/76_decoding/DECODING-01/candidate-v48.png)

La prima figura segue il percorso da «Greedy e beam search» a «Penalità e stop».


## Penalità e stop

Repetition penalty, stop sequence e minimum length intervengono in punti differenti e possono interagire. [SRC-76-003]

**Caso da seguire.** Un caso in cui il decoding modifica la traiettoria, non corregge il modello a monte.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Penalità e stop».


## Constrained decoding

Grammar, automi e schema limitano i token ammessi. Validità strutturale non garantisce argomenti corretti. [SRC-76-004]

**Caso da seguire.** Per «Constrained decoding» si mantiene l'input del capitolo e si isola questa condizione: Grammar, automi e schema limitano i token ammessi.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def normalize(values):
    if not values:
        raise ValueError('values must not be empty')
    maximum = max(values)
    exponentials = [math.exp(value - maximum) for value in values]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def contract():
    logits = [2.0, 1.0, 0.5]
    greedy = max(range(len(logits)), key=logits.__getitem__)
    sampled_support = [index for index, probability in enumerate(normalize(logits)) if probability >= 0.2]
    return {"greedy": greedy, "support": sampled_support, "invariant": "decoding chooses a trajectory from logits without changing model parameters"}
```

Esecuzione con `python snip_76_contract.py`:

```text
{"greedy": 0, "invariant": "decoding chooses a trajectory from logits without changing model parameters", "support": [0, 1]}
```

Il test associato è [`code/test_76_contract.py`](code/test_76_contract.py); l'output versionato è [`code/outputs/SNIP-76-001.txt`](code/outputs/SNIP-76-001.txt).


## Metriche

Qualità, diversità, latency, token per secondo e probabilità della sequenza devono essere letti insieme. [SRC-76-001]

**Caso da seguire.** Quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Metriche» non si applica.


![Decoding e generazione vincolata: chart](../../assets/chapters/76_decoding/DECODING-02/candidate-v48.png)

La seconda figura mette a confronto «Constrained decoding» e il limite discusso in «Metriche».


## Come si collegano i passaggi

- **Da «Greedy e beam search» a «Sampling».** Greedy sceglie il massimo locale; beam mantiene più prefissi secondo score accumulati e criteri di lunghezza. Temperature, top-k e top-p modificano la distribuzione prima dell'estrazione. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-76-001; SRC-76-002]

- **Da «Sampling» a «Penalità e stop».** Temperature, top-k e top-p modificano la distribuzione prima dell'estrazione. Repetition penalty, stop sequence e minimum length intervengono in punti differenti e possono interagire. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-76-002; SRC-76-003]

- **Da «Penalità e stop» a «Constrained decoding».** Repetition penalty, stop sequence e minimum length intervengono in punti differenti e possono interagire. Grammar, automi e schema limitano i token ammessi. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-76-003; SRC-76-004]

- **Da «Constrained decoding» a «Metriche».** Grammar, automi e schema limitano i token ammessi. Qualità, diversità, latency, token per secondo e probabilità della sequenza devono essere letti insieme. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-76-004; SRC-76-001]

La catena completa produce token scelto, sequenza e metrica di costo a partire da logits, prefisso, temperatura e vincolo. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: il decoding modifica la traiettoria, non corregge il modello a monte.


## Esercizi sul meccanismo

1. Ricostruisci «Greedy e beam search» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Sampling», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Penalità e stop» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Constrained decoding» che produca una failure riconoscibile.
5. Per «Metriche», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «logits, prefisso, temperatura e vincolo» e arriva fino a «token scelto, sequenza e metrica di costo». Il limite da conservare è questo: il decoding modifica la traiettoria, non corregge il modello a monte. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
