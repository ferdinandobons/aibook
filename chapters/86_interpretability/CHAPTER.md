<!--
chapter_id: CH-P13-INTERPRETABILITY
part_id: P13
order_key: 860
title: Interpretabilità delle rappresentazioni e dei circuiti
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 86. Interpretabilità delle rappresentazioni e dei circuiti

La domanda guida di questa lezione è come collegare «Oggetto dell'interpretazione» e «Circuiti» senza perdere il contratto tecnico di interpretabilità delle rappresentazioni e dei circuiti. L'oggetto osservato è un comportamento del modello e l'intervento che lo modifica. Il contratto locale è: input, attivazioni, probe, attribution e baseline; operazione, probing, attribution, causal intervention e circuit tracing; output, effetto osservato con controllo e confondenti. Il caso guida è questo: Un intervento riduce lo score da 0,60 a 0,25 rispetto alla baseline. Il confine da mantenere esplicito è: correlazione di una feature non prova causalità.

## Oggetto dell'interpretazione

Pesi, attivazioni, feature, head e comportamento sono livelli differenti. Il metodo deve dichiarare quale livello analizza. [SRC-86-001]

Un'interpretazione causale richiede un intervento e un confronto.

**Caso da seguire.** Un intervento riduce lo score da 0,60 a 0,25 rispetto alla baseline.

**Controllo.** Classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Probing

Un probe misura informazione decodificabile da una rappresentazione. Non prova che il modello usi quella informazione causalmente. [SRC-86-002]

**Caso da seguire.** Ablazione di una componente e differenza rispetto alla baseline.

**Controllo.** Cambia la proprietà che distingue «Probing» dalle categorie vicine. Se la classificazione non cambia, la distinzione va formulata meglio.


## Attribution

Gradienti, integrated gradients e perturbazioni assegnano importanza secondo definizioni differenti e possono essere instabili. [SRC-86-003]

**Caso da seguire.** Quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Attribution» e all'output effetto osservato con controllo e confondenti.

**Controllo.** Confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


![Interpretabilità delle rappresentazioni e dei circuiti: compare](../../assets/chapters/86_interpretability/INTERPRETA-01/candidate-v48.png)

La prima figura segue il percorso da «Oggetto dell'interpretazione» a «Attribution».


## Causal intervention

Ablation, activation patching e path patching modificano componenti e misurano effetti sul comportamento. [SRC-86-004]

**Caso da seguire.** Una matrice di visibilità in cui la posizione futura resta esclusa anche se la shape dei tensori è compatibile.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Causal intervention» e quale invece sarebbe irrilevante.


## Circuiti

Un circuito è un insieme di componenti e connessioni sufficienti per un comportamento nel setup studiato. Sufficienza e necessità richiedono test separati. [SRC-86-001]

**Caso da seguire.** Quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Circuiti» e all'output effetto osservato con controllo e confondenti.

**Controllo.** Limita la conclusione alla proprietà dichiarata: Sufficienza e necessità richiedono test separati. Le dimensioni non osservate restano aperte.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    baseline = 0.60
    intervened = 0.25
    effect = intervened - baseline
    return {"baseline": baseline, "intervened": intervened, "effect": effect, "invariant": "an intervention is compared with a baseline before causal language"}
```

Esecuzione con `python snip_86_contract.py`:

```text
{"baseline": 0.6, "effect": -0.35, "intervened": 0.25, "invariant": "an intervention is compared with a baseline before causal language"}
```

Il test associato è [`code/test_86_contract.py`](code/test_86_contract.py); l'output versionato è [`code/outputs/SNIP-86-001.txt`](code/outputs/SNIP-86-001.txt).


![Interpretabilità delle rappresentazioni e dei circuiti: graph](../../assets/chapters/86_interpretability/INTERPRETA-02/candidate-v48.png)

La seconda figura mette a confronto «Causal intervention» e il limite discusso in «Circuiti».


## Come si collegano i passaggi

- **Da «Oggetto dell'interpretazione» a «Probing».** Pesi, attivazioni, feature, head e comportamento sono livelli differenti. Un probe misura informazione decodificabile da una rappresentazione. La definizione iniziale stabilisce l'asse del confronto; la categoria successiva aggiunge una proprietà senza creare una classifica implicita. [SRC-86-001; SRC-86-002]

- **Da «Probing» a «Attribution».** Un probe misura informazione decodificabile da una rappresentazione. Gradienti, integrated gradients e perturbazioni assegnano importanza secondo definizioni differenti e possono essere instabili. Il terzo passaggio verifica se le categorie restano distinguibili sullo stesso caso e impedisce che termini vicini diventino sinonimi. [SRC-86-002; SRC-86-003]

- **Da «Attribution» a «Causal intervention».** Gradienti, integrated gradients e perturbazioni assegnano importanza secondo definizioni differenti e possono essere instabili. Ablation, activation patching e path patching modificano componenti e misurano effetti sul comportamento. La quarta sezione introduce il punto in cui l'asse scelto smette di bastare e richiede una nuova osservazione. [SRC-86-003; SRC-86-004]

- **Da «Causal intervention» a «Circuiti».** Ablation, activation patching e path patching modificano componenti e misurano effetti sul comportamento. Un circuito è un insieme di componenti e connessioni sufficienti per un comportamento nel setup studiato. La sezione finale riunisce le dimensioni della valutazione, ma conserva i limiti di ciascuna invece di fonderle in un unico punteggio. [SRC-86-004; SRC-86-001]

La catena completa produce effetto osservato con controllo e confondenti a partire da attivazioni, probe, attribution e baseline. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: correlazione di una feature non prova causalità.


## Domande per distinguere le categorie

1. Ricostruisci «Oggetto dell'interpretazione» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Probing», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Attribution» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Causal intervention» che produca una failure riconoscibile.
5. Per «Circuiti», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «attivazioni, probe, attribution e baseline» e arriva fino a «effetto osservato con controllo e confondenti». Il limite da conservare è questo: correlazione di una feature non prova causalità. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
