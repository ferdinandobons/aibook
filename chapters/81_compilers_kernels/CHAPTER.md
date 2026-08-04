<!--
chapter_id: CH-P12-COMPILERS-KERNELS
part_id: P12
order_key: 810
title: Compiler, kernel e runtime
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 81. Compiler, kernel e runtime

La domanda guida di questa lezione è come collegare «Grafo e operatori» e «Autotuning e portabilità» senza perdere il contratto tecnico di compiler, kernel e runtime. L'oggetto osservato è un grafo di operatori trasformato dal compiler. Il contratto locale è: input, grafo, shape, dtype, target e kernel; operazione, lowering, fusion, autotuning e gestione dei graph break; output, kernel eseguito, latenza e fallback. Il caso guida è questo: Tre operatori diventano due gruppi dopo una fusione, con correttezza numerica da confrontare. Il confine da mantenere esplicito è: ottimizzazione del grafo e correttezza numerica devono essere confrontate.

## Grafo e operatori

Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation. [SRC-81-001]

Compiler e runtime trasformano il grafo in operazioni del backend.

**Caso da seguire.** Tre operatori diventano due gruppi dopo una fusione, con correttezza numerica da confrontare.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Kernel fusion

Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso. [SRC-81-002]

**Caso da seguire.** La stessa operazione misurata separando bytes mossi, tempo del kernel e latenza end-to-end.

**Controllo.** Ripeti «Kernel fusion» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![Compiler, kernel e runtime: compare](../../assets/chapters/81_compilers_kernels/KERNELS-01/candidate-v48.png)

La prima figura segue il percorso da «Grafo e operatori» a «Triton e kernel custom».


## Triton e kernel custom

Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA. [SRC-81-003]

**Caso da seguire.** Per «Triton e kernel custom» si mantiene l'input del capitolo e si isola questa condizione: Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## torch.compile e graph break

Tracing e guard permettono specializzazione dinamica. Python side effect o shape non supportate producono graph break. [SRC-81-004]

**Caso da seguire.** Ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Autotuning e portabilità

Tile, num warps e schedule ottimali dipendono dall'hardware. Un kernel corretto richiede test numerici e benchmark separati. [SRC-81-001]

**Caso da seguire.** Per «Autotuning e portabilità» si mantiene l'input del capitolo e si isola questa condizione: Tile, num warps e schedule ottimali dipendono dall'hardware.

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Un kernel corretto richiede test numerici e benchmark separati.


![Compiler, kernel e runtime: pipeline](../../assets/chapters/81_compilers_kernels/KERNELS-02/candidate-v48.png)

La seconda figura mette a confronto «torch.compile e graph break» e il limite discusso in «Autotuning e portabilità».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    graph = ["matmul", "add", "relu"]
    fused = ["matmul_add", "relu"]
    return {"original_ops": len(graph), "fused_ops": len(fused), "invariant": "compiler optimization preserves the declared operator result"}
```

Esecuzione con `python snip_81_contract.py`:

```text
{"fused_ops": 2, "invariant": "compiler optimization preserves the declared operator result", "original_ops": 3}
```

Il test associato è [`code/test_81_contract.py`](code/test_81_contract.py); l'output versionato è [`code/outputs/SNIP-81-001.txt`](code/outputs/SNIP-81-001.txt).


## Come si collegano i passaggi

- **Da «Grafo e operatori» a «Kernel fusion».** Un compiler cattura operazioni e dipendenze, poi applica fusion, scheduling e layout transformation. Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-81-001; SRC-81-002]

- **Da «Kernel fusion» a «Triton e kernel custom».** Combinare operazioni riduce lanci e traffico di memoria, ma può aumentare register pressure e ridurre riuso. Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-81-002; SRC-81-003]

- **Da «Triton e kernel custom» a «torch.compile e graph break».** Un linguaggio di kernel espone tiling e parallelismo mantenendo una astrazione più alta rispetto a CUDA. Tracing e guard permettono specializzazione dinamica. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-81-003; SRC-81-004]

- **Da «torch.compile e graph break» a «Autotuning e portabilità».** Tracing e guard permettono specializzazione dinamica. Tile, num warps e schedule ottimali dipendono dall'hardware. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-81-004; SRC-81-001]

La catena completa produce kernel eseguito, latenza e fallback a partire da grafo, shape, dtype, target e kernel. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: ottimizzazione del grafo e correttezza numerica devono essere confrontate.


## Prove sui confini del sistema

1. Ricostruisci «Grafo e operatori» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Kernel fusion», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Triton e kernel custom» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «torch.compile e graph break» che produca una failure riconoscibile.
5. Per «Autotuning e portabilità», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «grafo, shape, dtype, target e kernel» e arriva fino a «kernel eseguito, latenza e fallback». Il limite da conservare è questo: ottimizzazione del grafo e correttezza numerica devono essere confrontate. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
