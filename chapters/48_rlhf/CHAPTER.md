<!--
chapter_id: CH-P09-RLHF
part_id: P09
order_key: 480
title: Preferenze, reward model e RLHF
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 48. Preferenze, reward model e RLHF

La domanda guida di questa lezione è come collegare «Dalle dimostrazioni alle preferenze» e «Valutazione e sicurezza» senza perdere il contratto tecnico di preferenze, reward model e rlhf. L'oggetto osservato è dimostrazioni, preferenze, reward model e policy. Il contratto locale è: input, prompt, risposta scelta, rifiutata e score; operazione, fit del reward, KL e aggiornamento della policy; output, reward, log-probability e comportamento aggiornato. Il caso guida è questo: Due risposte per lo stesso prompt ricevono score di reward diversi e una penalità KL separata. Il confine da mantenere esplicito è: il reward è un proxy e può essere ottimizzato in modo scorretto.

## Dalle dimostrazioni alle preferenze

Dati di confronto ordinano risposte alla stessa richiesta. Il protocollo deve registrare istruzioni ai valutatori, accordo e slice. [SRC-48-001]

Il confronto tra policy richiede una policy di riferimento e uno stesso prompt.

**Caso da seguire.** Due risposte per lo stesso prompt ricevono score di reward diversi e una penalità KL separata.

**Controllo.** Scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Il vincolo da conservare è: Il protocollo deve registrare istruzioni ai valutatori, accordo e slice.


## Reward model

Un modello assegna uno score alle risposte e viene addestrato con una loss di ranking. Lo score è una stima del dataset di preferenze, non una misura universale di qualità. [SRC-48-002]

**Caso da seguire.** Una traiettoria di due passi in cui l'azione scelta modifica lo stato successivo prima del reward.

**Controllo.** Ricalcola il caso a mano e con lo snippet. Se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
r_theta = log pi_theta(y|x) - log pi_ref(y|x)
$$

Il confronto tra policy richiede una policy di riferimento e uno stesso prompt. [SRC-48-001]


![Preferenze, reward model e RLHF: pipeline](../../assets/chapters/48_rlhf/RLHF-01/candidate-v48.png)

La prima figura segue il percorso da «Dalle dimostrazioni alle preferenze» a «Policy optimization».


## Policy optimization

PPO o algoritmi affini aggiornano la policy per aumentare reward mantenendo un vincolo rispetto al modello di riferimento. [SRC-48-003]

**Caso da seguire.** Per «Policy optimization» si mantiene l'input del capitolo e si isola questa condizione: PPO o algoritmi affini aggiornano la policy per aumentare reward mantenendo un vincolo rispetto al modello di riferimento.

**Controllo.** Aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Policy optimization».


## KL e reward hacking

Il termine KL limita lo spostamento della policy. Un reward imperfetto può essere sfruttato senza migliorare l'obiettivo umano. [SRC-48-004]

**Caso da seguire.** Per «KL e reward hacking» si mantiene l'input del capitolo e si isola questa condizione: Il termine KL limita lo spostamento della policy.

**Controllo.** Mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    chosen = 0.8
    rejected = 0.2
    reward_margin = chosen - rejected
    return {"reward_margin": round(reward_margin, 6), "invariant": "preference learning compares responses under one prompt"}
```

Esecuzione con `python snip_48_contract.py`:

```text
{"invariant": "preference learning compares responses under one prompt", "reward_margin": 0.6}
```

Il test associato è [`code/test_48_contract.py`](code/test_48_contract.py); l'output versionato è [`code/outputs/SNIP-48-001.txt`](code/outputs/SNIP-48-001.txt).


## Valutazione e sicurezza

Win rate, reward e giudizi automatici devono essere affiancati da controlli indipendenti, red teaming e analisi di regressione. [SRC-48-001]

**Caso da seguire.** Due risposte con log-probabilità diverse producono un margine; il margine può diventare un segnale di training, ma non è una misura assoluta di correttezza.

**Controllo.** Costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Valutazione e sicurezza» non si applica.


![Preferenze, reward model e RLHF: loop](../../assets/chapters/48_rlhf/RLHF-02/candidate-v48.png)

La seconda figura mette a confronto «KL e reward hacking» e il limite discusso in «Valutazione e sicurezza».


## Come si collegano i passaggi

- **Da «Dalle dimostrazioni alle preferenze» a «Reward model».** Dati di confronto ordinano risposte alla stessa richiesta. Un modello assegna uno score alle risposte e viene addestrato con una loss di ranking. Il primo passaggio definisce che cosa entra nel calcolo; il secondo stabilisce la regola che produce il valore osservabile. [SRC-48-001; SRC-48-002]

- **Da «Reward model» a «Policy optimization».** Un modello assegna uno score alle risposte e viene addestrato con una loss di ranking. PPO o algoritmi affini aggiornano la policy per aumentare reward mantenendo un vincolo rispetto al modello di riferimento. La regola generale viene poi letta dentro il componente: questa separazione permette di localizzare un errore prima di attribuirlo all'intero modello. [SRC-48-002; SRC-48-003]

- **Da «Policy optimization» a «KL e reward hacking».** PPO o algoritmi affini aggiornano la policy per aumentare reward mantenendo un vincolo rispetto al modello di riferimento. Il termine KL limita lo spostamento della policy. Dopo avere reso visibile il componente, il percorso introduce la variante o l'ottimizzazione senza cambiare di nascosto il caso di partenza. [SRC-48-003; SRC-48-004]

- **Da «KL e reward hacking» a «Valutazione e sicurezza».** Il termine KL limita lo spostamento della policy. Win rate, reward e giudizi automatici devono essere affiancati da controlli indipendenti, red teaming e analisi di regressione. L'ultimo passaggio sposta l'attenzione dal funzionamento locale alla misura: correttezza del calcolo e qualità applicativa restano domande distinte. [SRC-48-004; SRC-48-001]

La catena completa produce reward, log-probability e comportamento aggiornato a partire da prompt, risposta scelta, rifiutata e score. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: il reward è un proxy e può essere ottimizzato in modo scorretto.


## Esercizi sul meccanismo

1. Ricostruisci «Dalle dimostrazioni alle preferenze» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Reward model», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Policy optimization» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «KL e reward hacking» che produca una failure riconoscibile.
5. Per «Valutazione e sicurezza», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «prompt, risposta scelta, rifiutata e score» e arriva fino a «reward, log-probability e comportamento aggiornato». Il limite da conservare è questo: il reward è un proxy e può essere ottimizzato in modo scorretto. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
