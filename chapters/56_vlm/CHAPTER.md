<!--
chapter_id: CH-P10-VLM
part_id: P10
order_key: 560
title: Vision encoder e Vision-Language Model
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 56. Vision encoder e Vision-Language Model

La domanda guida di questa lezione è come collegare «Patch e vision encoder» e «Grounding e hallucination» senza perdere il contratto tecnico di vision encoder e vision-language model. L'oggetto osservato è patch visivi e token linguistici in un VLM. Il contratto locale è: input, immagine, patch, testo e query; operazione, vision encoder, projector e cross-attention; output, token visivi, risposta e grounding. Il caso guida è questo: Una query confronta due patch visive e conserva l'indice della patch con score maggiore. Il confine da mantenere esplicito è: una risposta linguistica non certifica che il dettaglio sia nell'immagine.

## Patch e vision encoder

Una immagine viene trasformata in patch o feature. Risoluzione, positional encoding e pooling definiscono la sequenza visiva. [SRC-56-001]

La similarità misurata non esaurisce la comprensione della scena.

**Caso da seguire.** Una query confronta due patch visive e conserva l'indice della patch con score maggiore.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Dual encoder

CLIP allinea immagine e testo con una loss contrastiva. I due encoder supportano retrieval efficiente ma interagiscono tardi. [SRC-56-002]

**Caso da seguire.** Due patch aggregate e una domanda con riferimento locale.

**Controllo.** Ripeti «Dual encoder» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![Vision encoder e Vision-Language Model: architecture](../../assets/chapters/56_vlm/VLM-01/candidate-v48.png)

La prima figura segue il percorso da «Patch e vision encoder» a «Projector».


## Projector

Architetture modulari proiettano feature visive nella dimensione del language model. Il projector stabilisce capacità e numero di visual token. [SRC-56-003]

**Caso da seguire.** Un caso in cui una risposta linguistica non certifica che il dettaglio sia nell'immagine.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Q-Former e cross-attention

Query apprese possono estrarre un insieme compatto di feature. Altre architetture inseriscono cross-attention dedicata. [SRC-56-004]

**Caso da seguire.** Due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Grounding e hallucination

Descrivere una immagine non garantisce localizzare oggetti o relazioni. Grounding, OCR e affidabilità richiedono test specifici. [SRC-56-001]

**Caso da seguire.** Per «Grounding e hallucination» si mantiene l'input del capitolo e si isola questa condizione: Descrivere una immagine non garantisce localizzare oggetti o relazioni.

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Grounding, OCR e affidabilità richiedono test specifici.


![Vision encoder e Vision-Language Model: pipeline](../../assets/chapters/56_vlm/VLM-02/candidate-v48.png)

La seconda figura mette a confronto «Q-Former e cross-attention» e il limite discusso in «Grounding e hallucination».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    patches = [[0.8, 0.1], [0.2, 0.7]]
    question = [0.5, 0.5]
    scores = [sum(a * b for a, b in zip(patch, question)) for patch in patches]
    selected = max(range(len(scores)), key=scores.__getitem__)
    return {"scores": scores, "selected_patch": selected, "invariant": "visual grounding links a text query to explicit image features"}
```

Esecuzione con `python snip_56_contract.py`:

```text
{"invariant": "visual grounding links a text query to explicit image features", "scores": [0.45, 0.44999999999999996], "selected_patch": 0}
```

Il test associato è [`code/test_56_contract.py`](code/test_56_contract.py); l'output versionato è [`code/outputs/SNIP-56-001.txt`](code/outputs/SNIP-56-001.txt).


## Come si collegano i passaggi

- **Da «Patch e vision encoder» a «Dual encoder».** Una immagine viene trasformata in patch o feature. CLIP allinea immagine e testo con una loss contrastiva. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-56-001; SRC-56-002]

- **Da «Dual encoder» a «Projector».** CLIP allinea immagine e testo con una loss contrastiva. Architetture modulari proiettano feature visive nella dimensione del language model. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-56-002; SRC-56-003]

- **Da «Projector» a «Q-Former e cross-attention».** Architetture modulari proiettano feature visive nella dimensione del language model. Query apprese possono estrarre un insieme compatto di feature. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-56-003; SRC-56-004]

- **Da «Q-Former e cross-attention» a «Grounding e hallucination».** Query apprese possono estrarre un insieme compatto di feature. Descrivere una immagine non garantisce localizzare oggetti o relazioni. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-56-004; SRC-56-001]

La catena completa produce token visivi, risposta e grounding a partire da immagine, patch, testo e query. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: una risposta linguistica non certifica che il dettaglio sia nell'immagine.


## Prove sui confini del sistema

1. Ricostruisci «Patch e vision encoder» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Dual encoder», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Projector» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Q-Former e cross-attention» che produca una failure riconoscibile.
5. Per «Grounding e hallucination», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «immagine, patch, testo e query» e arriva fino a «token visivi, risposta e grounding». Il limite da conservare è questo: una risposta linguistica non certifica che il dettaglio sia nell'immagine. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
