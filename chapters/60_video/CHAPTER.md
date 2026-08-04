<!--
chapter_id: CH-P10-VIDEO
part_id: P10
order_key: 600
title: Generazione video
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 60. Generazione video

La domanda guida di questa lezione è come collegare «Spazio e tempo» e «Condizionamento e editing» senza perdere il contratto tecnico di generazione video. L'oggetto osservato è una sequenza di frame condizionata nel tempo. Il contratto locale è: input, frame, latent video, testo e timestamp; operazione, denoising, autoregressione e controllo temporale; output, frame coerenti e misura di flicker. Il caso guida è questo: Tre frame condividono una condizione e conservano l'ordine temporale. Il confine da mantenere esplicito è: qualità del singolo frame non dimostra coerenza tra frame.

## Spazio e tempo

Un video aggiunge una dimensione temporale alle immagini. Token, patch o latent devono conservare movimento e identità. [SRC-60-001]

Una sequenza video aggiunge asse temporale e coerenza tra frame.

**Caso da seguire.** Tre frame condividono una condizione e conservano l'ordine temporale.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Video diffusion

Il denoiser opera su tensori spazio-temporali o latent compressi. Attention fattorizzata e convoluzioni riducono il costo. [SRC-60-002]

**Caso da seguire.** Due rappresentazioni di modalità diverse proiettate nella stessa dimensione prima di similarità, fusione o generazione.

**Controllo.** Ripeti «Video diffusion» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![Generazione video: timeline](../../assets/chapters/60_video/VIDEO-01/candidate-v48.png)

La prima figura segue il percorso da «Spazio e tempo» a «Autoregressione».


## Autoregressione

Frame, patch o token video possono essere generati in ordine. L'ordine scelto modifica dipendenze e cache. [SRC-60-003]

**Caso da seguire.** Un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Coerenza

Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame. [SRC-60-004]

**Caso da seguire.** Due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Condizionamento e editing

Testo, immagine iniziale, traiettoria o maschere guidano il video. Il controllo deve essere valutato nel tempo. [SRC-60-001]

**Caso da seguire.** Per «Condizionamento e editing» si mantiene l'input del capitolo e si isola questa condizione: Testo, immagine iniziale, traiettoria o maschere guidano il video.

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Il controllo deve essere valutato nel tempo.


![Generazione video: pipeline](../../assets/chapters/60_video/VIDEO-02/candidate-v48.png)

La seconda figura mette a confronto «Coerenza» e il limite discusso in «Condizionamento e editing».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    frames = ["f0", "f1", "f2"]
    condition = "prompt"
    generated = [(frame, condition) for frame in frames]
    return {"frame_count": len(generated), "temporal_order": [item[0] for item in generated], "invariant": "video generation keeps an explicit temporal index"}
```

Esecuzione con `python snip_60_contract.py`:

```text
{"frame_count": 3, "invariant": "video generation keeps an explicit temporal index", "temporal_order": ["f0", "f1", "f2"]}
```

Il test associato è [`code/test_60_contract.py`](code/test_60_contract.py); l'output versionato è [`code/outputs/SNIP-60-001.txt`](code/outputs/SNIP-60-001.txt).


## Come si collegano i passaggi

- **Da «Spazio e tempo» a «Video diffusion».** Un video aggiunge una dimensione temporale alle immagini. Il denoiser opera su tensori spazio-temporali o latent compressi. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-60-001; SRC-60-002]

- **Da «Video diffusion» a «Autoregressione».** Il denoiser opera su tensori spazio-temporali o latent compressi. Frame, patch o token video possono essere generati in ordine. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-60-002; SRC-60-003]

- **Da «Autoregressione» a «Coerenza».** Frame, patch o token video possono essere generati in ordine. Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-60-003; SRC-60-004]

- **Da «Coerenza» a «Condizionamento e editing».** Flicker, drift dell'identità e dinamiche impossibili richiedono controlli oltre la qualità di singoli frame. Testo, immagine iniziale, traiettoria o maschere guidano il video. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-60-004; SRC-60-001]

La catena completa produce frame coerenti e misura di flicker a partire da frame, latent video, testo e timestamp. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: qualità del singolo frame non dimostra coerenza tra frame.


## Prove sui confini del sistema

1. Ricostruisci «Spazio e tempo» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Video diffusion», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Autoregressione» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Coerenza» che produca una failure riconoscibile.
5. Per «Condizionamento e editing», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «frame, latent video, testo e timestamp» e arriva fino a «frame coerenti e misura di flicker». Il limite da conservare è questo: qualità del singolo frame non dimostra coerenza tra frame. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
