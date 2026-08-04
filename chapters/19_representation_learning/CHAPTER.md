<!--
chapter_id: CH-P04-REPRESENTATION
part_id: P04
order_key: 190
title: Representation learning
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 19. Representation learning

La domanda guida di questa lezione è come collegare «Che cosa rappresenta un vettore» e «Valutare una rappresentazione» senza perdere il contratto tecnico di representation learning. L'oggetto osservato è un vettore prodotto per un compito successivo. Il contratto locale è: input, u = [1, 2, 0] e v = [2, 1, 0]; operazione, una proiezione, una ricostruzione o una metrica tra rappresentazioni; output, un vettore, una similarità o una predizione downstream. Il caso guida è questo: Un caso minimo con input u = [1, 2, 0] e v = [2, 1, 0] e output «un vettore, una similarità o una predizione downstream». Il confine da mantenere esplicito è: la geometria dipende da dati, obiettivo e normalizzazione.

## Che cosa rappresenta un vettore

Una rappresentazione è un insieme di quantità prodotte dal modello e usate da un calcolo successivo. Il significato dipende da obiettivo e dati. [SRC-19-001]

La similarità coseno confronta direzioni dopo una scelta di normalizzazione.

**Caso da seguire.** Un caso minimo con input u = [1, 2, 0] e v = [2, 1, 0] e output «un vettore, una similarità o una predizione downstream».

**Controllo.** Classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Bottleneck e autoencoder

Un autoencoder comprime e ricostruisce. Un bottleneck limita la capacità, ma non garantisce che le coordinate corrispondano a fattori interpretabili. [SRC-19-002]

**Caso da seguire.** Similarità coseno calcolata dopo la normalizzazione delle norme.

**Controllo.** Cambia la proprietà che distingue «Bottleneck e autoencoder» dalle categorie vicine. Se la classificazione non cambia, la distinzione va formulata meglio.


## Metric e contrastive learning

Obiettivi contrastivi avvicinano coppie positive e separano alternative. La definizione delle coppie e delle augmentazioni stabilisce le invarianti apprese. [SRC-19-003]

**Caso da seguire.** Quattro casi con protocollo, una failure e una slice conservati insieme al valore aggregato.

**Controllo.** Confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


![Representation learning: compare](../../assets/chapters/19_representation_learning/REPRESEN-01/candidate-v49.png)

La prima figura segue il percorso da «Che cosa rappresenta un vettore» a «Metric e contrastive learning».


## Disentanglement e identifiability

Separare fattori latenti richiede ipotesi. Senza supervision o bias aggiuntivi, molte rappresentazioni equivalenti possono spiegare gli stessi dati. [SRC-19-004]

**Caso da seguire.** Due vettori con prodotto scalare positivo possono avere similarità diversa dopo normalizzazione. La metrica va scelta insieme al compito.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Disentanglement e identifiability» e quale invece sarebbe irrilevante.


## Valutare una rappresentazione

Linear probe, retrieval e fine-tuning misurano proprietà diverse. Una buona metrica downstream non dimostra interpretabilità globale. [SRC-19-001]

**Caso da seguire.** Per «Valutare una rappresentazione» si mantiene l'input del capitolo e si isola questa condizione: Linear probe, retrieval e fine-tuning misurano proprietà diverse.

**Controllo.** Limita la conclusione alla proprietà dichiarata: Una buona metrica downstream non dimostra interpretabilità globale. Le dimensioni non osservate restano aperte.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    left = [1.0, 2.0, 0.0]
    right = [2.0, 1.0, 0.0]
    dot = sum(a * b for a, b in zip(left, right))
    score = dot / (math.sqrt(sum(a * a for a in left)) * math.sqrt(sum(b * b for b in right)))
    return {"cosine": round(score, 6), "invariant": "the denominator normalizes both vectors"}
```

Esecuzione con `python snip_19_contract.py`:

```text
{"cosine": 0.8, "invariant": "the denominator normalizes both vectors"}
```

Il test associato è [`code/test_19_contract.py`](code/test_19_contract.py); l'output versionato è [`code/outputs/SNIP-19-001.txt`](code/outputs/SNIP-19-001.txt).


![Representation learning: scatter](../../assets/chapters/19_representation_learning/REPRESEN-02/candidate-v49.png)

La seconda figura mette a confronto «Disentanglement e identifiability» e il limite discusso in «Valutare una rappresentazione».


## Come si collegano i passaggi

- **Da «Che cosa rappresenta un vettore» a «Bottleneck e autoencoder».** Una rappresentazione è un insieme di quantità prodotte dal modello e usate da un calcolo successivo. Un autoencoder comprime e ricostruisce. La definizione iniziale stabilisce l'asse del confronto; la categoria successiva aggiunge una proprietà senza creare una classifica implicita. [SRC-19-001; SRC-19-002]

- **Da «Bottleneck e autoencoder» a «Metric e contrastive learning».** Un autoencoder comprime e ricostruisce. Obiettivi contrastivi avvicinano coppie positive e separano alternative. Il terzo passaggio verifica se le categorie restano distinguibili sullo stesso caso e impedisce che termini vicini diventino sinonimi. [SRC-19-002; SRC-19-003]

- **Da «Metric e contrastive learning» a «Disentanglement e identifiability».** Obiettivi contrastivi avvicinano coppie positive e separano alternative. Separare fattori latenti richiede ipotesi. La quarta sezione introduce il punto in cui l'asse scelto smette di bastare e richiede una nuova osservazione. [SRC-19-003; SRC-19-004]

- **Da «Disentanglement e identifiability» a «Valutare una rappresentazione».** Separare fattori latenti richiede ipotesi. Linear probe, retrieval e fine-tuning misurano proprietà diverse. La sezione finale riunisce le dimensioni della valutazione, ma conserva i limiti di ciascuna invece di fonderle in un unico punteggio. [SRC-19-004; SRC-19-001]

La catena completa produce un vettore, una similarità o una predizione downstream a partire da u = [1, 2, 0] e v = [2, 1, 0]. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: la geometria dipende da dati, obiettivo e normalizzazione.


## Domande per distinguere le categorie

1. Ricostruisci «Che cosa rappresenta un vettore» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Bottleneck e autoencoder», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Metric e contrastive learning» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Disentanglement e identifiability» che produca una failure riconoscibile.
5. Per «Valutare una rappresentazione», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «u = [1, 2, 0] e v = [2, 1, 0]» e arriva fino a «un vettore, una similarità o una predizione downstream». Il limite da conservare è questo: la geometria dipende da dati, obiettivo e normalizzazione. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
