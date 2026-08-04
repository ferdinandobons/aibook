<!--
chapter_id: CH-P05-VAE-VQ
part_id: P05
order_key: 220
title: Variational Autoencoder e latent discreti
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 22. Variational Autoencoder e latent discreti

La domanda guida di questa lezione è come collegare «Inferenza approssimata» e «VQ-VAE» senza perdere il contratto tecnico di variational autoencoder e latent discreti. L'oggetto osservato è una variabile osservata e il suo codice latente. Il contratto locale è: input, x, media, log-varianza e rumore epsilon; operazione, ELBO e reparameterization trick; output, ricostruzione, KL e codice latente. Il caso guida è questo: Un caso minimo con input x, media, log-varianza e rumore epsilon e output «ricostruzione, KL e codice latente». Il confine da mantenere esplicito è: la ricostruzione non elimina il costo KL né dimostra disentanglement.

## Inferenza approssimata

Il VAE introduce un encoder q(z|x) per approssimare il posterior. Il decoder modella p(x|z). [SRC-22-001]

Ricostruzione e regolarizzazione del latent entrano nello stesso obiettivo.

**Caso da seguire.** Un caso minimo con input x, media, log-varianza e rumore epsilon e output «ricostruzione, KL e codice latente».

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Il decoder modella p(x|z).


## ELBO

L'evidence lower bound combina ricostruzione e KL verso il prior. Massimizzare l'ELBO non coincide necessariamente con massimizzare qualità percettiva. [SRC-22-002]

**Caso da seguire.** Un dato trasformato e ricostruito con la quantità di probabilità o di errore dichiarata.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
ELBO=E_q[log p(x|z)]-KL(q(z|x)||p(z))
$$

Ricostruzione e regolarizzazione del latent entrano nello stesso obiettivo. [SRC-22-001]


![Variational Autoencoder e latent discreti: pipeline](../../assets/chapters/22_vae_vq/VQ-01/candidate-v48.png)

La prima figura segue il percorso da «Inferenza approssimata» a «Reparameterization trick».


## Reparameterization trick

Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Questo consente gradienti pathwise. [SRC-22-003]

**Caso da seguire.** Un caso in cui la ricostruzione non elimina il costo KL né dimostra disentanglement.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Reparameterization trick».


## Posterior collapse

Un decoder molto potente può ignorare z e avvicinare il posterior al prior. KL annealing e architettura possono modificare il fenomeno. [SRC-22-004]

**Caso da seguire.** Un termine di ricostruzione alto e una KL bassa possono descrivere un decoder che ignora il latent; i due termini vanno osservati separatamente.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    reconstruction = 0.40
    kl = 0.10
    beta = 0.5
    objective = reconstruction + beta * kl
    return {"reconstruction": reconstruction, "kl": kl, "objective": round(objective, 6), "invariant": "reconstruction and regularization stay separately observable"}
```

Esecuzione con `python snip_22_contract.py`:

```text
{"invariant": "reconstruction and regularization stay separately observable", "kl": 0.1, "objective": 0.45, "reconstruction": 0.4}
```

Il test associato è [`code/test_22_contract.py`](code/test_22_contract.py); l'output versionato è [`code/outputs/SNIP-22-001.txt`](code/outputs/SNIP-22-001.txt).


## VQ-VAE

La quantizzazione vettoriale sostituisce il latent continuo con indici di un codebook. Commitment loss e aggiornamento del codebook richiedono controlli dedicati. [SRC-22-001]

**Caso da seguire.** Tre probabilità che sommano a 1 prima del campionamento, distinguendo plausibilità del campione e copertura.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «VQ-VAE» non si applica.


![Variational Autoencoder e latent discreti: timeline](../../assets/chapters/22_vae_vq/VQ-02/candidate-v48.png)

La seconda figura mette a confronto «Posterior collapse» e il limite discusso in «VQ-VAE».


## Come si collegano i passaggi

- **Da «Inferenza approssimata» a «ELBO».** Il VAE introduce un encoder q(z|x) per approssimare il posterior. L'evidence lower bound combina ricostruzione e KL verso il prior. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-22-001; SRC-22-002]

- **Da «ELBO» a «Reparameterization trick».** L'evidence lower bound combina ricostruzione e KL verso il prior. Un campione gaussiano viene scritto come trasformazione di rumore indipendente. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-22-002; SRC-22-003]

- **Da «Reparameterization trick» a «Posterior collapse».** Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Un decoder molto potente può ignorare z e avvicinare il posterior al prior. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-22-003; SRC-22-004]

- **Da «Posterior collapse» a «VQ-VAE».** Un decoder molto potente può ignorare z e avvicinare il posterior al prior. La quantizzazione vettoriale sostituisce il latent continuo con indici di un codebook. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-22-004; SRC-22-001]

La catena completa produce ricostruzione, KL e codice latente a partire da x, media, log-varianza e rumore epsilon. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: la ricostruzione non elimina il costo KL né dimostra disentanglement.


## Esercizi sul meccanismo

1. Ricostruisci «Inferenza approssimata» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «ELBO», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Reparameterization trick» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Posterior collapse» che produca una failure riconoscibile.
5. Per «VQ-VAE», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «x, media, log-varianza e rumore epsilon» e arriva fino a «ricostruzione, KL e codice latente». Il limite da conservare è questo: la ricostruzione non elimina il costo KL né dimostra disentanglement. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
