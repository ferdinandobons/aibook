<!--
chapter_id: CH-P05-GAN
part_id: P05
order_key: 230
title: Generative Adversarial Network
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 23. Generative Adversarial Network

La domanda guida di questa lezione è come collegare «Un gioco tra due modelli» e «Stabilità e valutazione» senza perdere il contratto tecnico di generative adversarial network. L'oggetto osservato è la partita tra generatore e discriminatore. Il contratto locale è: input, un dato reale, un campione e due score; operazione, aggiornamento alternato e segnale di feedback; output, score, gradiente e campione. Il caso guida è questo: Un caso minimo con input un dato reale, un campione e due score e output «score, gradiente e campione». Il confine da mantenere esplicito è: un equilibrio locale non prova copertura né stabilità.

## Un gioco tra due modelli

Il generatore produce campioni; il discriminatore distingue dati reali e generati. L'obiettivo è un gioco, non una loss singola ottimizzata congiuntamente. [SRC-23-001]

Generatore e discriminatore partecipano a un gioco a due obiettivi.

**Caso da seguire.** Un caso minimo con input un dato reale, un campione e due score e output «score, gradiente e campione».

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: L'obiettivo è un gioco, non una loss singola ottimizzata congiuntamente.


## Divergenze e gradienti

La formulazione originale è collegata alla Jensen-Shannon divergence sotto un discriminatore ottimo. I gradienti pratici dipendono dalla loss scelta. [SRC-23-002]

**Caso da seguire.** Due vettori con shape compatibile confrontati prima e dopo il blocco, osservando separatamente scala e percorso residuale in «Divergenze e gradienti».

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
min_G max_D V(D,G)
$$

Generatore e discriminatore partecipano a un gioco a due obiettivi. [SRC-23-001]


![Generative Adversarial Network: timeline](../../assets/chapters/23_gan/GAN-01/candidate-v48.png)

La prima figura segue il percorso da «Un gioco tra due modelli» a «Mode collapse».


## Mode collapse

Il generatore può produrre poche modalità convincenti. Diversità e fedeltà devono essere misurate separatamente. [SRC-23-003]

**Caso da seguire.** Un caso in cui un equilibrio locale non prova copertura né stabilità.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Mode collapse».


## Wasserstein GAN

WGAN usa una distanza legata a funzioni Lipschitz. Weight clipping e gradient penalty sono implementazioni differenti del vincolo. [SRC-23-004]

**Caso da seguire.** Un dato trasformato e ricostruito con la quantità di probabilità o di errore dichiarata.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    real = [0.9, 0.8]
    fake = [0.2, 0.3]
    discriminator_gap = sum(real) / len(real) - sum(fake) / len(fake)
    return {"discriminator_gap": round(discriminator_gap, 6), "invariant": "generator and discriminator signals are not the same loss"}
```

Esecuzione con `python snip_23_contract.py`:

```text
{"discriminator_gap": 0.6, "invariant": "generator and discriminator signals are not the same loss"}
```

Il test associato è [`code/test_23_contract.py`](code/test_23_contract.py); l'output versionato è [`code/outputs/SNIP-23-001.txt`](code/outputs/SNIP-23-001.txt).


## Stabilità e valutazione

Bilanciare update, normalizzazioni e capacità è essenziale. FID è una metrica su feature e non sostituisce l'analisi dei campioni. [SRC-23-001]

**Caso da seguire.** Se il discriminatore diventa perfetto troppo presto, il gradiente utile al generatore può ridursi. La metrica non è soltanto la loss di un singolo update.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Stabilità e valutazione» non si applica.


![Generative Adversarial Network: pipeline](../../assets/chapters/23_gan/GAN-02/candidate-v48.png)

La seconda figura mette a confronto «Wasserstein GAN» e il limite discusso in «Stabilità e valutazione».


## Come si collegano i passaggi

- **Da «Un gioco tra due modelli» a «Divergenze e gradienti».** Il generatore produce campioni; il discriminatore distingue dati reali e generati. La formulazione originale è collegata alla Jensen-Shannon divergence sotto un discriminatore ottimo. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-23-001; SRC-23-002]

- **Da «Divergenze e gradienti» a «Mode collapse».** La formulazione originale è collegata alla Jensen-Shannon divergence sotto un discriminatore ottimo. Il generatore può produrre poche modalità convincenti. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-23-002; SRC-23-003]

- **Da «Mode collapse» a «Wasserstein GAN».** Il generatore può produrre poche modalità convincenti. WGAN usa una distanza legata a funzioni Lipschitz. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-23-003; SRC-23-004]

- **Da «Wasserstein GAN» a «Stabilità e valutazione».** WGAN usa una distanza legata a funzioni Lipschitz. Bilanciare update, normalizzazioni e capacità è essenziale. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-23-004; SRC-23-001]

La catena completa produce score, gradiente e campione a partire da un dato reale, un campione e due score. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: un equilibrio locale non prova copertura né stabilità.


## Esercizi sul meccanismo

1. Ricostruisci «Un gioco tra due modelli» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Divergenze e gradienti», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Mode collapse» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Wasserstein GAN» che produca una failure riconoscibile.
5. Per «Stabilità e valutazione», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «un dato reale, un campione e due score» e arriva fino a «score, gradiente e campione». Il limite da conservare è questo: un equilibrio locale non prova copertura né stabilità. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
