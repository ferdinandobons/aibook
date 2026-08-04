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

Qui variational autoencoder e latent discreti viene osservato come un meccanismo: il percorso va da «Inferenza approssimata» a «VQ-VAE». L'oggetto osservato è una variabile osservata e il suo codice latente. Il contratto locale dichiara input, x, media, log-varianza e rumore epsilon; operazione, ELBO e reparameterization trick; output, ricostruzione, KL e codice latente. Il caso di partenza è Un caso minimo con input x, media, log-varianza e rumore epsilon e output «ricostruzione, KL e codice latente». Il limite da non nascondere è: la ricostruzione non elimina il costo KL né dimostra disentanglement.

## Inferenza approssimata

Il VAE introduce un encoder q(z|x) per approssimare il posterior. Il decoder modella p(x|z). [SRC-22-001]

Ricostruzione e regolarizzazione del latent entrano nello stesso obiettivo.

**Caso da seguire.** Un caso minimo con input x, media, log-varianza e rumore epsilon e output «ricostruzione, KL e codice latente».

**Controllo.** Per «Inferenza approssimata», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Inferenza approssimata», il vincolo da conservare è: Il decoder modella p(x|z).


## ELBO

L'evidence lower bound combina ricostruzione e KL verso il prior. Massimizzare l'ELBO non coincide necessariamente con massimizzare qualità percettiva. [SRC-22-002]

**Caso da seguire.** Un dato trasformato e ricostruito con la quantità di probabilità o di errore dichiarata.

**Controllo.** Per «ELBO», ricalcola il caso a mano e con lo snippet. Nel caso «ELBO», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


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

**Controllo.** Per «Reparameterization trick», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Reparameterization trick».


## Posterior collapse

Un decoder molto potente può ignorare z e avvicinare il posterior al prior. KL annealing e architettura possono modificare il fenomeno. [SRC-22-004]

**Caso da seguire.** Un termine di ricostruzione alto e una KL bassa possono descrivere un decoder che ignora il latent; i due termini vanno osservati separatamente.

**Controllo.** Per «Posterior collapse», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Posterior collapse», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Questa sezione apre il contratto Python di variational autoencoder e latent discreti: il lettore può eseguire lo stesso file e confrontare il risultato. Per «Variational Autoencoder e latent discreti», il caso di default usa valori piccoli per isolare il meccanismo. Il caso non supportato viene provato separatamente, così «variational autoencoder e latent discreti» non viene generalizzato oltre l'esempio.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
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

**Controllo.** Per «VQ-VAE», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «VQ-VAE» non si applica.


![Variational Autoencoder e latent discreti: timeline](../../assets/chapters/22_vae_vq/VQ-02/candidate-v48.png)

La seconda figura mette a confronto «Posterior collapse» e il limite discusso in «VQ-VAE».


## Come si collegano i passaggi

- **Da «Inferenza approssimata» a «ELBO».** Il VAE introduce un encoder q(z|x) per approssimare il posterior. L'evidence lower bound combina ricostruzione e KL verso il prior. Tra «Inferenza approssimata» e «ELBO» l'ingresso viene fissato prima della regola che produce il valore. Il passaggio successivo rende misurabile «ELBO». [SRC-22-001; SRC-22-002]

- **Da «ELBO» a «Reparameterization trick».** L'evidence lower bound combina ricostruzione e KL verso il prior. Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Nel caso «Reparameterization trick» il componente diventa il punto in cui localizzare l'errore. Da «ELBO» a «Reparameterization trick» cambia la domanda osservabile. [SRC-22-002; SRC-22-003]

- **Da «Reparameterization trick» a «Posterior collapse».** Un campione gaussiano viene scritto come trasformazione di rumore indipendente. Un decoder molto potente può ignorare z e avvicinare il posterior al prior. Dopo «Reparameterization trick», la variante di «Posterior collapse» cambia una proprietà alla volta. Il passaggio successivo rende misurabile «Posterior collapse». [SRC-22-003; SRC-22-004]

- **Da «Posterior collapse» a «VQ-VAE».** Un decoder molto potente può ignorare z e avvicinare il posterior al prior. La quantizzazione vettoriale sostituisce il latent continuo con indici di un codebook. Da «VQ-VAE» in poi la misura resta distinta dalla correttezza locale del calcolo. Da «Posterior collapse» a «VQ-VAE» cambia la domanda osservabile. [SRC-22-004; SRC-22-001]

La catena completa produce ricostruzione, KL e codice latente a partire da x, media, log-varianza e rumore epsilon. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: la ricostruzione non elimina il costo KL né dimostra disentanglement.


## Esercizi sul meccanismo

1. Ricostruisci «Inferenza approssimata» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «ELBO», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Reparameterization trick» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Posterior collapse» che produca una failure riconoscibile.
5. Per «VQ-VAE», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «x, media, log-varianza e rumore epsilon» e arriva fino a «ricostruzione, KL e codice latente». Il limite da conservare è questo: la ricostruzione non elimina il costo KL né dimostra disentanglement. La formula e il codice collegati a «VQ-VAE» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
