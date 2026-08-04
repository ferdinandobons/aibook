<!--
chapter_id: CH-P10-AUDIO
part_id: P10
order_key: 590
title: Audio, parlato e musica
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 59. Audio, parlato e musica

Per capire audio, parlato e musica, partiamo da «Waveform e spettrogramma» e seguiamo ogni confine fino a «Musica e dialogo». L'oggetto osservato è un segnale audio e la sua rappresentazione discreta. Il contratto locale dichiara input, waveform, sample rate, spettrogramma o codec; operazione, ASR, TTS, codec e generazione; output, testo, waveform o token audio. La situazione minima da seguire è Quattro campioni audio vengono divisi in due frame senza cambiare l'ordine temporale. Il limite da non nascondere è: sample rate e durata fanno parte del contratto.

## Waveform e spettrogramma

Il segnale audio è campionato nel tempo. STFT e mel filterbank producono rappresentazioni tempo-frequenza con parametri espliciti. [SRC-59-001]

Sample rate, token e durata fanno parte del contratto dell'audio.

**Caso da seguire.** Quattro campioni audio vengono divisi in due frame senza cambiare l'ordine temporale.

**Controllo.** Per «Waveform e spettrogramma», registra richiesta, decisione, stato e output finale. Nel caso «Waveform e spettrogramma», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## ASR

Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer. Streaming e offline hanno vincoli diversi. [SRC-59-002]

**Caso da seguire.** Una breve waveform convertita in frame e token.

**Controllo.** Ripeti «ASR» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


La forma compatta aiuta a seguire il flusso senza attribuirgli una garanzia quantitativa.

**Schema concettuale.** `wave = decode(tokens, sample_rate)`

Sample rate, token e durata fanno parte del contratto dell'audio. [SRC-59-001]


![Audio, parlato e musica: timeline](../../assets/chapters/59_audio/AUDIO-01/candidate-v48.png)

La prima figura segue il percorso da «Waveform e spettrogramma» a «TTS».


## TTS

Sintesi vocale trasforma testo in acoustic representation e waveform. Durata, prosodia e vocoder sono componenti distinti. [SRC-59-003]

**Caso da seguire.** Un caso in cui sample rate e durata fanno parte del contratto.

**Controllo.** Per «TTS», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Neural codec

Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model. [SRC-59-004]

**Caso da seguire.** Due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito.

**Controllo.** Per «Neural codec», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Musica e dialogo

Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche. [SRC-59-001]

**Caso da seguire.** Due rappresentazioni di modalità diverse proiettate nella stessa dimensione prima di similarità, fusione o generazione.

**Controllo.** Per «Musica e dialogo», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Musica e dialogo», il risultato resta limitato da: Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche.


![Audio, parlato e musica: pipeline](../../assets/chapters/59_audio/AUDIO-02/candidate-v48.png)

La seconda figura mette a confronto «Neural codec» e il limite discusso in «Musica e dialogo».


## Esempio Python eseguito

La prova locale di audio, parlato e musica parte da un esempio minimo, registrato nel repository insieme ai suoi test. Per «Audio, parlato e musica», il caso di default usa valori piccoli per isolare il meccanismo. La prova negativa riguarda proprio «audio, parlato e musica» e interrompe l'interpretazione prima dell'output.

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    waveform = [0.0, 0.5, -0.5, 0.0]
    frame_size = 2
    frames = [waveform[i:i + frame_size] for i in range(0, len(waveform), frame_size)]
    return {"frames": frames, "sample_count": len(waveform), "invariant": "audio framing preserves sample order and declared frame size"}
```

Esecuzione con `python snip_59_contract.py`:

```text
{"frames": [[0.0, 0.5], [-0.5, 0.0]], "invariant": "audio framing preserves sample order and declared frame size", "sample_count": 4}
```

Il test associato è [`code/test_59_contract.py`](code/test_59_contract.py); l'output versionato è [`code/outputs/SNIP-59-001.txt`](code/outputs/SNIP-59-001.txt).


## Come si collegano i passaggi

- **Da «Waveform e spettrogramma» a «ASR».** Il segnale audio è campionato nel tempo. Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer. «Waveform e spettrogramma» nomina il confine e «ASR» implementa il percorso senza ereditare autorizzazioni implicite. Da «Waveform e spettrogramma» a «ASR» cambia la domanda osservabile. [SRC-59-001; SRC-59-002]

- **Da «ASR» a «TTS».** Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer. Sintesi vocale trasforma testo in acoustic representation e waveform. Componendo «ASR» e «TTS» diventa necessario conservare stato, identità e decisione. Il passaggio successivo rende misurabile «TTS». [SRC-59-002; SRC-59-003]

- **Da «TTS» a «Neural codec».** Sintesi vocale trasforma testo in acoustic representation e waveform. Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model. «Neural codec» introduce failure e recovery prima di un side effect o di una perdita di stato. Da «TTS» a «Neural codec» cambia la domanda osservabile. [SRC-59-003; SRC-59-004]

- **Da «Neural codec» a «Musica e dialogo».** Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model. Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche. La chiusura su «Musica e dialogo» valuta il sistema completo, non soltanto il componente iniziale. Il passaggio successivo rende misurabile «Musica e dialogo». [SRC-59-004; SRC-59-001]

La catena completa produce testo, waveform o token audio a partire da waveform, sample rate, spettrogramma o codec. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: sample rate e durata fanno parte del contratto.


## Prove sui confini del sistema

1. Ricostruisci «Waveform e spettrogramma» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «ASR», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «TTS» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Neural codec» che produca una failure riconoscibile.
5. Per «Musica e dialogo», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «waveform, sample rate, spettrogramma o codec» e arriva fino a «testo, waveform o token audio». Il limite da conservare è questo: sample rate e durata fanno parte del contratto. Il confine di «Musica e dialogo» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
