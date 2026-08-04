<!--
chapter_id: CH-P05-DIFFUSION-FLOW
part_id: P05
order_key: 250
title: Diffusione, score matching e flow matching
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 25. Diffusione, score matching e flow matching

Qui diffusione, score matching e flow matching viene osservato come un meccanismo: il percorso va da «Corrompere e ricostruire» a «Flow matching e rectified flow». L'oggetto osservato è un dato corrotto e il percorso di denoising. Il contratto locale dichiara input, x_0, rumore epsilon e timestep t; operazione, forward noising, score o velocity e sampler; output, stima del rumore e campione ricostruito. Per fissare il riferimento usiamo Un caso minimo con input x_0, rumore epsilon e timestep t e output «stima del rumore e campione ricostruito». Il limite da non nascondere è: parametrizzazione e scheduler fanno parte del contratto.

## Corrompere e ricostruire

La diffusione forward aggiunge rumore secondo uno schedule. Il modello impara a invertire o a stimare una quantità equivalente. [SRC-25-001]

Il forward process rende osservabile il livello di rumore.

**Caso da seguire.** Un caso minimo con input x_0, rumore epsilon e timestep t e output «stima del rumore e campione ricostruito».

**Controllo.** Per «Corrompere e ricostruire», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Corrompere e ricostruire», il vincolo da conservare è: Il modello impara a invertire o a stimare una quantità equivalente.


## Score matching

Lo score è il gradiente del log-density rispetto ai dati perturbati. Denoising score matching evita di conoscere la densità normale completa. [SRC-25-002]

**Caso da seguire.** Un dato trasformato e ricostruito con la quantità di probabilità o di errore dichiarata.

**Controllo.** Per «Score matching», ricalcola il caso a mano e con lo snippet. Nel caso «Score matching», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
$$

Il forward process rende osservabile il livello di rumore. [SRC-25-001]


![Diffusione, score matching e flow matching: timeline](../../assets/chapters/25_diffusion_flow/FLOW-01/candidate-v48.png)

La prima figura segue il percorso da «Corrompere e ricostruire» a «Parametrizzazioni epsilon, x0 e v».


## Parametrizzazioni epsilon, x0 e v

Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambiano scala e weighting del training. [SRC-25-003]

**Caso da seguire.** Un caso in cui parametrizzazione e scheduler fanno parte del contratto.

**Controllo.** Per «Parametrizzazioni epsilon, x0 e v», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Parametrizzazioni epsilon, x0 e v».


## Sampler

DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti. Meno step non garantiscono stessa distribuzione o qualità. [SRC-25-004]

**Caso da seguire.** Aumentando `t`, il coefficiente del dato diminuisce e quello del rumore cresce secondo lo schedule. Il sampler deve rispettare lo stesso contratto.

**Controllo.** Per «Sampler», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Sampler», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il caso computazionale di diffusione, score matching e flow matching è riportato senza trasformazioni: il file e l'output sono quelli verificati. Per «Diffusione, score matching e flow matching», il caso di default usa valori piccoli per isolare il meccanismo. La suite conserva inoltre una failure esplicita per separare il contratto osservato da «diffusione, score matching e flow matching».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    alpha_bar = [0.9, 0.5, 0.1]
    signal = [math.sqrt(value) for value in alpha_bar]
    noise = [math.sqrt(1.0 - value) for value in alpha_bar]
    return {"signal": [round(value, 6) for value in signal], "noise": [round(value, 6) for value in noise], "invariant": "the sampler uses the same noise schedule as the forward process"}
```

Esecuzione con `python snip_25_contract.py`:

```text
{"invariant": "the sampler uses the same noise schedule as the forward process", "noise": [0.316228, 0.707107, 0.948683], "signal": [0.948683, 0.707107, 0.316228]}
```

Il test associato è [`code/test_25_contract.py`](code/test_25_contract.py); l'output versionato è [`code/outputs/SNIP-25-001.txt`](code/outputs/SNIP-25-001.txt).


## Flow matching e rectified flow

Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni. Rectified flow cerca traiettorie più rettilinee in setup specifici. [SRC-25-001]

**Caso da seguire.** Per «Flow matching e rectified flow» si mantiene l'input del capitolo e si isola questa condizione: Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni.

**Controllo.** Per «Flow matching e rectified flow», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Flow matching e rectified flow» non si applica.


![Diffusione, score matching e flow matching: pipeline](../../assets/chapters/25_diffusion_flow/FLOW-02/candidate-v48.png)

La seconda figura mette a confronto «Sampler» e il limite discusso in «Flow matching e rectified flow».


## Come si collegano i passaggi

- **Da «Corrompere e ricostruire» a «Score matching».** La diffusione forward aggiunge rumore secondo uno schedule. Lo score è il gradiente del log-density rispetto ai dati perturbati. Tra «Corrompere e ricostruire» e «Score matching» l'ingresso viene fissato prima della regola che produce il valore. Da «Corrompere e ricostruire» a «Score matching» cambia la domanda osservabile. [SRC-25-001; SRC-25-002]

- **Da «Score matching» a «Parametrizzazioni epsilon, x0 e v».** Lo score è il gradiente del log-density rispetto ai dati perturbati. Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambiano scala e weighting del training. Nel caso «Parametrizzazioni epsilon, x0 e v» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «Parametrizzazioni epsilon, x0 e v». [SRC-25-002; SRC-25-003]

- **Da «Parametrizzazioni epsilon, x0 e v» a «Sampler».** Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambiano scala e weighting del training. DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti. Dopo «Parametrizzazioni epsilon, x0 e v», la variante di «Sampler» cambia una proprietà alla volta. Da «Parametrizzazioni epsilon, x0 e v» a «Sampler» cambia la domanda osservabile. [SRC-25-003; SRC-25-004]

- **Da «Sampler» a «Flow matching e rectified flow».** DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti. Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni. Da «Flow matching e rectified flow» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «Flow matching e rectified flow». [SRC-25-004; SRC-25-001]

La catena completa produce stima del rumore e campione ricostruito a partire da x_0, rumore epsilon e timestep t. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: parametrizzazione e scheduler fanno parte del contratto.


## Esercizi sul meccanismo

1. Ricostruisci «Corrompere e ricostruire» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Score matching», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Parametrizzazioni epsilon, x0 e v» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Sampler» che produca una failure riconoscibile.
5. Per «Flow matching e rectified flow», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «x_0, rumore epsilon e timestep t» e arriva fino a «stima del rumore e campione ricostruito». Il limite da conservare è questo: parametrizzazione e scheduler fanno parte del contratto. La formula e il codice collegati a «Flow matching e rectified flow» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
