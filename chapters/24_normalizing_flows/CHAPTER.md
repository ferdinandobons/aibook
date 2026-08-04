<!--
chapter_id: CH-P05-FLOWS
part_id: P05
order_key: 240
title: Normalizing flow e trasformazioni invertibili
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 24. Normalizing flow e trasformazioni invertibili

Per entrare in normalizing flow e trasformazioni invertibili, seguiamo il passaggio che unisce «Cambio di variabile» a «Sampling e costo». L'oggetto osservato è un dato trasformato da una mappa invertibile. Il contratto locale dichiara input, x, log-determinante e variabile latente z; operazione, coupling, cambio di variabile e inversione; output, log-likelihood, z e campione ricostruito. La situazione minima da seguire è Un caso minimo con input x, log-determinante e variabile latente z e output «log-likelihood, z e campione ricostruito». Il limite da non nascondere è: l'inversione richiede una trasformazione e un log-determinante coerenti.

## Cambio di variabile

Una trasformazione invertibile collega una distribuzione semplice ai dati. La densità usa il determinante Jacobiano. [SRC-24-001]

Il cambio di variabile richiede trasformazione invertibile e Jacobiano.

**Caso da seguire.** Un caso minimo con input x, log-determinante e variabile latente z e output «log-likelihood, z e campione ricostruito».

**Controllo.** Per «Cambio di variabile», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Cambio di variabile», il vincolo da conservare è: La densità usa il determinante Jacobiano.


## Coupling layer

RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti. [SRC-24-002]

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Coupling layer».

**Controllo.** Per «Coupling layer», ricalcola il caso a mano e con lo snippet. Nel caso «Coupling layer», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
log p_x(x)=log p_z(f(x))+log|det J_f(x)|
$$

Il cambio di variabile richiede trasformazione invertibile e Jacobiano. [SRC-24-001]


![Normalizing flow e trasformazioni invertibili: pipeline](../../assets/chapters/24_normalizing_flows/FLOWS-01/candidate-v48.png)

La prima figura segue il percorso da «Cambio di variabile» a «Invertibilità e architettura».


## Invertibilità e architettura

L'invertibilità limita operazioni e dimensioni. Squeeze, split e permutazioni riorganizzano l'informazione senza perderla. [SRC-24-003]

**Caso da seguire.** Un caso in cui l'inversione richiede una trasformazione e un log-determinante coerenti.

**Controllo.** Per «Invertibilità e architettura», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Invertibilità e architettura».


## Continuous normalizing flow

Una ODE definisce una trasformazione continua. La likelihood usa la variazione del log-density lungo il flusso. [SRC-24-004]

**Caso da seguire.** Un dato trasformato e ricostruito con la quantità di probabilità o di errore dichiarata.

**Controllo.** Per «Continuous normalizing flow», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Continuous normalizing flow», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Per rendere osservabile normalizing flow e trasformazioni invertibili, il capitolo conserva qui l'artefatto Python eseguito. Per «Normalizing flow e trasformazioni invertibili», il caso di default usa valori piccoli per isolare il meccanismo. Il test rifiuta anche un caso non documentato di «normalizing flow e trasformazioni invertibili».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    scale = [2.0, 0.5]
    log_det = sum(math.log(value) for value in scale)
    inverse = [1.0 / value for value in scale]
    return {"log_det": round(log_det, 6), "inverse_scale": inverse, "invariant": "the transform exposes both an inverse and a log determinant"}
```

Esecuzione con `python snip_24_contract.py`:

```text
{"invariant": "the transform exposes both an inverse and a log determinant", "inverse_scale": [0.5, 2.0], "log_det": 0.0}
```

Il test associato è [`code/test_24_contract.py`](code/test_24_contract.py); l'output versionato è [`code/outputs/SNIP-24-001.txt`](code/outputs/SNIP-24-001.txt).


## Sampling e costo

I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici. [SRC-24-001]

**Caso da seguire.** Un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente.

**Controllo.** Per «Sampling e costo», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Sampling e costo» non si applica.


![Normalizing flow e trasformazioni invertibili: timeline](../../assets/chapters/24_normalizing_flows/FLOWS-02/candidate-v48.png)

La seconda figura mette a confronto «Continuous normalizing flow» e il limite discusso in «Sampling e costo».


## Come si collegano i passaggi

- **Da «Cambio di variabile» a «Coupling layer».** Una trasformazione invertibile collega una distribuzione semplice ai dati. RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti. Tra «Cambio di variabile» e «Coupling layer» l'ingresso viene fissato prima della regola che produce il valore. Il passaggio successivo rende misurabile «Coupling layer». [SRC-24-001; SRC-24-002]

- **Da «Coupling layer» a «Invertibilità e architettura».** RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti. L'invertibilità limita operazioni e dimensioni. Nel caso «Invertibilità e architettura» il componente diventa il punto in cui localizzare l'errore. Da «Coupling layer» a «Invertibilità e architettura» cambia la domanda osservabile. [SRC-24-002; SRC-24-003]

- **Da «Invertibilità e architettura» a «Continuous normalizing flow».** L'invertibilità limita operazioni e dimensioni. Una ODE definisce una trasformazione continua. Dopo «Invertibilità e architettura», la variante di «Continuous normalizing flow» cambia una proprietà alla volta. Il passaggio successivo rende misurabile «Continuous normalizing flow». [SRC-24-003; SRC-24-004]

- **Da «Continuous normalizing flow» a «Sampling e costo».** Una ODE definisce una trasformazione continua. I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici. Da «Sampling e costo» in poi la misura resta distinta dalla correttezza locale del calcolo. Da «Continuous normalizing flow» a «Sampling e costo» cambia la domanda osservabile. [SRC-24-004; SRC-24-001]

La catena completa produce log-likelihood, z e campione ricostruito a partire da x, log-determinante e variabile latente z. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: l'inversione richiede una trasformazione e un log-determinante coerenti.


## Esercizi sul meccanismo

1. Ricostruisci «Cambio di variabile» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Coupling layer», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Invertibilità e architettura» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Continuous normalizing flow» che produca una failure riconoscibile.
5. Per «Sampling e costo», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «x, log-determinante e variabile latente z» e arriva fino a «log-likelihood, z e campione ricostruito». Il limite da conservare è questo: l'inversione richiede una trasformazione e un log-determinante coerenti. La formula e il codice collegati a «Sampling e costo» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
