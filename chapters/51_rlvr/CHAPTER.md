<!--
chapter_id: CH-P09-RLVR
part_id: P09
order_key: 510
title: Reinforcement learning con reward verificabili
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 51. Reinforcement learning con reward verificabili

Per entrare in reinforcement learning con reward verificabili, seguiamo il passaggio che unisce «Reward verificabile» a «Verificabilità limitata». L'oggetto osservato è una risposta valutata da una regola verificabile. Il contratto locale dichiara input, prompt, rollout, gruppo di risposte e verifier; operazione, reward verificabile, policy update e gestione di reward sparso; output, reward, vantaggio e nuova policy. Il primo esempio osservabile è Tre rollout ricevono reward 1, 0 e 1; il vantaggio viene centrato sulla media del gruppo. Il limite da non nascondere è: la verificabilità vale solo per il dominio coperto dal verifier.

## Reward verificabile

Problemi con risposta controllabile, come codice o matematica, consentono reward da test, parser o esecutori. [SRC-51-001]

RLVR lega il segnale a una procedura di verifica esplicita e delimitata.

**Caso da seguire.** Tre rollout ricevono reward 1, 0 e 1; il vantaggio viene centrato sulla media del gruppo.

**Controllo.** Per «Reward verificabile», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Reward verificabile», il vincolo da conservare è: Problemi con risposta controllabile, come codice o matematica, consentono reward da test, parser o esecutori.


## Rollout e gruppi

La policy genera più soluzioni per la stessa richiesta. Il reward confronta traiettorie e costruisce advantage o ranking. [SRC-51-001]

**Caso da seguire.** Tre passi in cui lo stato precedente viene consumato prima di produrre il successivo.

**Controllo.** Per «Rollout e gruppi», ricalcola il caso a mano e con lo snippet. Nel caso «Rollout e gruppi», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


La relazione centrale può essere scritta come:

$$
R = verifier(answer)
$$

RLVR lega il segnale a una procedura di verifica esplicita e delimitata. [SRC-51-001]


![Reinforcement learning con reward verificabili: funnel](../../assets/chapters/51_rlvr/RLVR-01/candidate-v48.png)

La prima figura segue il percorso da «Reward verificabile» a «GRPO e policy update».


## GRPO e policy update

Algoritmi group-relative normalizzano reward all'interno di gruppi e aggiornano log-probability con vincoli di stabilità. [SRC-51-002]

**Caso da seguire.** Una traiettoria di due passi in cui l'azione scelta modifica lo stato successivo prima del reward.

**Controllo.** Per «GRPO e policy update», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «GRPO e policy update».


## Sparse reward

Un risultato finale corretto non identifica quali passaggi siano utili. Exploration, curriculum e shaping cambiano la densità del segnale. [SRC-51-003]

**Caso da seguire.** Per «Sparse reward» si mantiene l'input del capitolo e si isola questa condizione: Un risultato finale corretto non identifica quali passaggi siano utili.

**Controllo.** Per «Sparse reward», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Sparse reward», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

La prova locale di reinforcement learning con reward verificabili parte da un esempio minimo, registrato nel repository insieme ai suoi test. Per «Reinforcement learning con reward verificabili», il caso di default usa valori piccoli per isolare il meccanismo. La prova negativa riguarda proprio «reinforcement learning con reward verificabili» e interrompe l'interpretazione prima dell'output.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    rewards = [1.0, 0.0, 1.0]
    mean = sum(rewards) / len(rewards)
    advantages = [round(value - mean, 6) for value in rewards]
    return {"mean_reward": mean, "advantages": advantages, "invariant": "the policy update depends on declared reward and baseline"}
```

Esecuzione con `python snip_51_contract.py`:

```text
{"advantages": [0.333333, -0.666667, 0.333333], "invariant": "the policy update depends on declared reward and baseline", "mean_reward": 0.6666666666666666}
```

Il test associato è [`code/test_51_contract.py`](code/test_51_contract.py); l'output versionato è [`code/outputs/SNIP-51-001.txt`](code/outputs/SNIP-51-001.txt).


## Verificabilità limitata

Un test incompleto può premiare exploit. Il reward verificabile è affidabile soltanto nel perimetro del verificatore. [SRC-51-004]

**Caso da seguire.** Due risposte con log-probabilità diverse producono un margine; il margine può diventare un segnale di training, ma non è una misura assoluta di correttezza.

**Controllo.** Per «Verificabilità limitata», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Verificabilità limitata» non si applica.


![Reinforcement learning con reward verificabili: pipeline](../../assets/chapters/51_rlvr/RLVR-02/candidate-v48.png)

La seconda figura mette a confronto «Sparse reward» e il limite discusso in «Verificabilità limitata».


## Come si collegano i passaggi

- **Da «Reward verificabile» a «Rollout e gruppi».** Problemi con risposta controllabile, come codice o matematica, consentono reward da test, parser o esecutori. La policy genera più soluzioni per la stessa richiesta. Tra «Reward verificabile» e «Rollout e gruppi» l'ingresso viene fissato prima della regola che produce il valore. Da «Reward verificabile» a «Rollout e gruppi» cambia la domanda osservabile. [SRC-51-001; SRC-51-001]

- **Da «Rollout e gruppi» a «GRPO e policy update».** La policy genera più soluzioni per la stessa richiesta. Algoritmi group-relative normalizzano reward all'interno di gruppi e aggiornano log-probability con vincoli di stabilità. Nel caso «GRPO e policy update» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «GRPO e policy update». [SRC-51-001; SRC-51-002]

- **Da «GRPO e policy update» a «Sparse reward».** Algoritmi group-relative normalizzano reward all'interno di gruppi e aggiornano log-probability con vincoli di stabilità. Un risultato finale corretto non identifica quali passaggi siano utili. Dopo «GRPO e policy update», la variante di «Sparse reward» cambia una proprietà alla volta. Da «GRPO e policy update» a «Sparse reward» cambia la domanda osservabile. [SRC-51-002; SRC-51-003]

- **Da «Sparse reward» a «Verificabilità limitata».** Un risultato finale corretto non identifica quali passaggi siano utili. Un test incompleto può premiare exploit. Da «Verificabilità limitata» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «Verificabilità limitata». [SRC-51-003; SRC-51-004]

La catena completa produce reward, vantaggio e nuova policy a partire da prompt, rollout, gruppo di risposte e verifier. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: la verificabilità vale solo per il dominio coperto dal verifier.


## Esercizi sul meccanismo

1. Ricostruisci «Reward verificabile» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Rollout e gruppi», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «GRPO e policy update» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Sparse reward» che produca una failure riconoscibile.
5. Per «Verificabilità limitata», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «prompt, rollout, gruppo di risposte e verifier» e arriva fino a «reward, vantaggio e nuova policy». Il limite da conservare è questo: la verificabilità vale solo per il dominio coperto dal verifier. La formula e il codice collegati a «Verificabilità limitata» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
