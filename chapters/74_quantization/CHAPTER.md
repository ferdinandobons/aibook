<!--
chapter_id: CH-P12-QUANTIZATION
part_id: P12
order_key: 740
title: Quantizzazione
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 74. Quantizzazione

La domanda guida di questa lezione è come collegare «Scala e zero point» e «Metodi per LLM» senza perdere il contratto tecnico di quantizzazione. L'oggetto osservato è un tensore reale e la sua rappresentazione quantizzata. Il contratto locale è: input, valori, scale, zero-point, dtype e calibrazione; operazione, PTQ, QAT, weight-only o activation quantization; output, codici, tensore ricostruito, errore e memoria. Il caso guida è questo: Tre valori con scala 0,25 vengono quantizzati e ricostruiti con errore massimo misurato. Il confine da mantenere esplicito è: scala e dominio di calibrazione fanno parte del risultato.

## Scala e zero point

Una mappa affine converte valori floating point in interi. La granularità per tensor o per channel cambia scale, errore e metadati. [SRC-74-001]

Scale, zero-point e intervallo intero definiscono insieme quantizzazione e ricostruzione.

**Caso da seguire.** Tre valori con scala 0,25 vengono quantizzati e ricostruiti con errore massimo misurato.

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: La granularità per tensor o per channel cambia scale, errore e metadati.


## PTQ

Post-training quantization usa calibration senza riaddestrare completamente. La rappresentatività dei dati di calibration è essenziale. [SRC-74-002]

**Caso da seguire.** Tre valori quantizzati con scala 0,25 e errore massimo.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
q = clamp(round(x / s) + z); \hat{x} = s(q - z)
$$

Scale, zero-point e intervallo intero definiscono insieme quantizzazione e ricostruzione. [SRC-74-001]


![Quantizzazione: chart](../../assets/chapters/74_quantization/QUANTIZATI-01/candidate-v48.png)

La prima figura segue il percorso da «Scala e zero point» a «QAT».


## QAT

Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi. [SRC-74-001]

**Caso da seguire.** Un caso in cui scala e dominio di calibrazione fanno parte del risultato.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «QAT».


## Weight-only e activation quantization

Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo. [SRC-74-003; SRC-74-002]

**Caso da seguire.** Tre valori floating point quantizzati con una scala dichiarata e confrontati con la ricostruzione.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    values = [-0.5, 0.0, 0.5]
    scale = 0.25
    quantized = [round(value / scale) for value in values]
    restored = [code * scale for code in quantized]
    error = max(abs(value - recovered) for value, recovered in zip(values, restored))
    return {"quantized": quantized, "restored": restored, "max_error": error, "invariant": "scale and calibration determine quantization error"}
```

Esecuzione con `python snip_74_contract.py`:

```text
{"invariant": "scale and calibration determine quantization error", "max_error": 0.0, "quantized": [-2, 0, 2], "restored": [-0.5, 0.0, 0.5]}
```

Il test associato è [`code/test_74_contract.py`](code/test_74_contract.py); l'output versionato è [`code/outputs/SNIP-74-001.txt`](code/outputs/SNIP-74-001.txt).


## Metodi per LLM

GPTQ, AWQ e SmoothQuant ottimizzano oggetti differenti: ricostruzione, canali salienti e outlier delle attivazioni. I loro contratti non sono intercambiabili. [SRC-74-004; SRC-74-003; SRC-74-002]

**Caso da seguire.** Ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Metodi per LLM» non si applica.


![Quantizzazione: compare](../../assets/chapters/74_quantization/QUANTIZATI-02/candidate-v48.png)

La seconda figura mette a confronto «Weight-only e activation quantization» e il limite discusso in «Metodi per LLM».


## Come si collegano i passaggi

- **Da «Scala e zero point» a «PTQ».** Una mappa affine converte valori floating point in interi. Post-training quantization usa calibration senza riaddestrare completamente. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-74-001; SRC-74-002]

- **Da «PTQ» a «QAT».** Post-training quantization usa calibration senza riaddestrare completamente. Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-74-002; SRC-74-001]

- **Da «QAT» a «Weight-only e activation quantization».** Quantization-aware training simula arrotondamento e clipping durante il training per adattare i pesi. Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-74-001; SRC-74-003; SRC-74-002]

- **Da «Weight-only e activation quantization» a «Metodi per LLM».** Quantizzare soltanto i pesi riduce memoria; quantizzare attivazioni modifica anche i kernel di calcolo. GPTQ, AWQ e SmoothQuant ottimizzano oggetti differenti: ricostruzione, canali salienti e outlier delle attivazioni. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-74-003; SRC-74-002; SRC-74-004; SRC-74-003; SRC-74-002]

La catena completa produce codici, tensore ricostruito, errore e memoria a partire da valori, scale, zero-point, dtype e calibrazione. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: scala e dominio di calibrazione fanno parte del risultato.


## Esercizi sul meccanismo

1. Ricostruisci «Scala e zero point» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «PTQ», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «QAT» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Weight-only e activation quantization» che produca una failure riconoscibile.
5. Per «Metodi per LLM», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «valori, scale, zero-point, dtype e calibrazione» e arriva fino a «codici, tensore ricostruito, errore e memoria». Il limite da conservare è questo: scala e dominio di calibrazione fanno parte del risultato. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
