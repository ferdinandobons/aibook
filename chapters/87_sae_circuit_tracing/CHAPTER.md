<!--
chapter_id: CH-P13-SAE-CIRCUIT-TRACING
part_id: P13
order_key: 870
title: Sparse autoencoder e interpretabilità scalabile
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 87. Sparse autoencoder e interpretabilità scalabile

Per entrare in sparse autoencoder e interpretabilità scalabile, seguiamo il passaggio che unisce «Superposition» a «Valutazione». L'oggetto osservato è un'attivazione scomposta in feature sparse. Il contratto locale dichiara input, attivazione, dizionario, sparsità e ricostruzione; operazione, training SAE, splitting, dead features e tracing; output, feature, errore di ricostruzione e circuito candidato. Il caso di partenza è Due feature sparse ricostruiscono tre coordinate e l'errore viene registrato. Il limite da non nascondere è: interpretabilità di una feature richiede valutazione e controlli indipendenti.

## Superposition

Più feature possono condividere le stesse dimensioni di attivazione. La sparsità offre una ipotesi per separarle. [SRC-87-001]

Un circuito descritto da feature richiede controlli indipendenti sull'attivazione.

**Caso da seguire.** Due feature sparse ricostruiscono tre coordinate e l'errore viene registrato.

**Controllo.** Per «Superposition», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Superposition», il vincolo da conservare è: La sparsità offre una ipotesi per separarle.


## Sparse autoencoder

Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream. Loss e sparsity coefficient determinano il dizionario. [SRC-87-002]

**Caso da seguire.** Due feature attive, una ricostruzione e un intervento.

**Controllo.** Per «Sparse autoencoder», ricalcola il caso a mano e con lo snippet. Nel caso «Sparse autoencoder», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


Per questo capitolo la notazione compatta chiarisce input, trasformazione e risultato.

**Schema concettuale.** `feature = encode(activation)`

Un circuito descritto da feature richiede controlli indipendenti sull'attivazione. [SRC-87-001]


![Sparse autoencoder e interpretabilità scalabile: scatter](../../assets/chapters/87_sae_circuit_tracing/TRACING-01/candidate-v48.png)

La prima figura segue il percorso da «Superposition» a «Dead e splitting features».


## Dead e splitting features

Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità. [SRC-87-003]

**Caso da seguire.** Un manifest che conserva conteggi, checksum, tokenizer e confini dello split prima del training.

**Controllo.** Per «Dead e splitting features», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Dead e splitting features».


## Circuit tracing

Feature e attribution graph possono collegare input, computazione e output. Il grafo resta una approssimazione del calcolo completo. [SRC-87-004]

**Caso da seguire.** Quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Circuit tracing» e all'output feature, errore di ricostruzione e circuito candidato.

**Controllo.** Per «Circuit tracing», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Circuit tracing», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

La prova locale di sparse autoencoder e interpretabilità scalabile parte da un esempio minimo, registrato nel repository insieme ai suoi test. Per «Sparse autoencoder e interpretabilità scalabile», il caso di default usa valori piccoli per isolare il meccanismo. La prova negativa riguarda proprio «sparse autoencoder e interpretabilità scalabile» e interrompe l'interpretazione prima dell'output.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    activation = [1.0, 0.0, 0.5]
    dictionary = [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]
    sparse_codes = [activation[0], activation[2]]
    reconstruction = [
        sum(code * vector[index] for code, vector in zip(sparse_codes, dictionary))
        for index in range(len(activation))
    ]
    error = sum((a - b) ** 2 for a, b in zip(activation, reconstruction))
    return {"active_features": len(sparse_codes), "reconstruction_error": error, "invariant": "sparsity and reconstruction must be evaluated together"}
```

Esecuzione con `python snip_87_contract.py`:

```text
{"active_features": 2, "invariant": "sparsity and reconstruction must be evaluated together", "reconstruction_error": 0.0}
```

Il test associato è [`code/test_87_contract.py`](code/test_87_contract.py); l'output versionato è [`code/outputs/SNIP-87-001.txt`](code/outputs/SNIP-87-001.txt).


## Valutazione

Interpretabilità automatica, causal intervention e coverage devono essere misurate. Una etichetta leggibile non prova monosemanticità universale. [SRC-87-001]

**Caso da seguire.** Su un piccolo insieme, la metrica viene calcolata insieme a una slice e a un caso fallito. La media non sostituisce la diagnosi.

**Controllo.** Per «Valutazione», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Valutazione» non si applica.


![Sparse autoencoder e interpretabilità scalabile: architecture](../../assets/chapters/87_sae_circuit_tracing/TRACING-02/candidate-v48.png)

La seconda figura mette a confronto «Circuit tracing» e il limite discusso in «Valutazione».


## Come si collegano i passaggi

- **Da «Superposition» a «Sparse autoencoder».** Più feature possono condividere le stesse dimensioni di attivazione. Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream. Tra «Superposition» e «Sparse autoencoder» l'ingresso viene fissato prima della regola che produce il valore. Da «Superposition» a «Sparse autoencoder» cambia la domanda osservabile. [SRC-87-001; SRC-87-002]

- **Da «Sparse autoencoder» a «Dead e splitting features».** Un encoder sovracompleto produce attivazioni sparse; un decoder ricostruisce il residual stream. Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità. Nel caso «Dead e splitting features» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «Dead e splitting features». [SRC-87-002; SRC-87-003]

- **Da «Dead e splitting features» a «Circuit tracing».** Feature mai attive, troppo ampie o duplicate indicano problemi di training e granularità. Feature e attribution graph possono collegare input, computazione e output. Dopo «Dead e splitting features», la variante di «Circuit tracing» cambia una proprietà alla volta. Da «Dead e splitting features» a «Circuit tracing» cambia la domanda osservabile. [SRC-87-003; SRC-87-004]

- **Da «Circuit tracing» a «Valutazione».** Feature e attribution graph possono collegare input, computazione e output. Interpretabilità automatica, causal intervention e coverage devono essere misurate. Da «Valutazione» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «Valutazione». [SRC-87-004; SRC-87-001]

La catena completa produce feature, errore di ricostruzione e circuito candidato a partire da attivazione, dizionario, sparsità e ricostruzione. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: interpretabilità di una feature richiede valutazione e controlli indipendenti.


## Esercizi sul meccanismo

1. Ricostruisci «Superposition» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Sparse autoencoder», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Dead e splitting features» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Circuit tracing» che produca una failure riconoscibile.
5. Per «Valutazione», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «attivazione, dizionario, sparsità e ricostruzione» e arriva fino a «feature, errore di ricostruzione e circuito candidato». Il limite da conservare è questo: interpretabilità di una feature richiede valutazione e controlli indipendenti. La formula e il codice collegati a «Valutazione» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
