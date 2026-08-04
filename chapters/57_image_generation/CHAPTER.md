<!--
chapter_id: CH-P10-IMAGE-GENERATION
part_id: P10
order_key: 570
title: Generazione e modifica delle immagini
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 57. Generazione e modifica delle immagini

Generazione e modifica delle immagini viene letto come un sistema: «Latent diffusion» e «Controllo e provenienza» restano collegati da confini e decisioni osservabili. L'oggetto osservato è un contenuto immagine e la condizione che lo modifica. Il contratto locale dichiara input, latent, prompt, mask e rumore; operazione, denoising, guidance, editing o inpainting; output, immagine, score e metadati di provenienza. Per fissare il riferimento usiamo Un singolo passo riduce una coppia di valori rumorosi secondo uno schedule dichiarato. Il limite da non nascondere è: controllo dell'immagine e verità del contenuto sono proprietà diverse.

## Latent diffusion

Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente. Il decoder ricostruisce pixel al termine. [SRC-57-001]

Editing e generazione modificano un contenuto sotto una condizione dichiarata.

**Caso da seguire.** Un singolo passo riduce una coppia di valori rumorosi secondo uno schedule dichiarato.

**Controllo.** Per «Latent diffusion», registra richiesta, decisione, stato e output finale. Nel caso «Latent diffusion», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## Conditioning

Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati. [SRC-57-002]

**Caso da seguire.** Una regione mascherata modificata lasciando il resto fissato.

**Controllo.** Ripeti «Conditioning» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


La relazione centrale può essere scritta come:

$$
x_hat = g(z, condition)
$$

Editing e generazione modificano un contenuto sotto una condizione dichiarata. [SRC-57-001]


![Generazione e modifica delle immagini: timeline](../../assets/chapters/57_image_generation/GENERATION-01/candidate-v48.png)

La prima figura segue il percorso da «Latent diffusion» a «Classifier-free guidance».


## Classifier-free guidance

Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione. [SRC-57-003]

**Caso da seguire.** Un caso in cui controllo dell'immagine e verità del contenuto sono proprietà diverse.

**Controllo.** Per «Classifier-free guidance», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Editing e inpainting

Una mask stabilisce regioni modificabili. La coerenza con le aree conservate dipende da noise schedule e condition. [SRC-57-004]

**Caso da seguire.** Due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito.

**Controllo.** Per «Editing e inpainting», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Controllo e provenienza

ControlNet, adapter e reference image aggiungono vincoli. Dataset, diritti e metadati restano parte del sistema. [SRC-57-001]

**Caso da seguire.** Un payload modificato dopo la firma, con digest e metadati confrontati separatamente.

**Controllo.** Per «Controllo e provenienza», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Controllo e provenienza», il risultato resta limitato da: Dataset, diritti e metadati restano parte del sistema.


![Generazione e modifica delle immagini: pipeline](../../assets/chapters/57_image_generation/GENERATION-02/candidate-v48.png)

La seconda figura mette a confronto «Editing e inpainting» e il limite discusso in «Controllo e provenienza».


## Esempio Python eseguito

Il caso computazionale di generazione e modifica delle immagini è riportato senza trasformazioni: il file e l'output sono quelli verificati. Per «Generazione e modifica delle immagini», il caso di default usa valori piccoli per isolare il meccanismo. La suite conserva inoltre una failure esplicita per separare il contratto osservato da «generazione e modifica delle immagini».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    noisy = [0.9, 0.1]
    denoised = [0.7 * noisy[0] + 0.3 * 0.5, 0.7 * noisy[1] + 0.3 * 0.5]
    return {"denoised": denoised, "steps": 1, "invariant": "a generation step declares its noise level and update"}
```

Esecuzione con `python snip_57_contract.py`:

```text
{"denoised": [0.78, 0.21999999999999997], "invariant": "a generation step declares its noise level and update", "steps": 1}
```

Il test associato è [`code/test_57_contract.py`](code/test_57_contract.py); l'output versionato è [`code/outputs/SNIP-57-001.txt`](code/outputs/SNIP-57-001.txt).


## Come si collegano i passaggi

- **Da «Latent diffusion» a «Conditioning».** Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente. Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati. «Latent diffusion» nomina il confine e «Conditioning» implementa il percorso senza ereditare autorizzazioni implicite. Da «Latent diffusion» a «Conditioning» cambia la domanda osservabile. [SRC-57-001; SRC-57-002]

- **Da «Conditioning» a «Classifier-free guidance».** Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati. Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione. Componendo «Conditioning» e «Classifier-free guidance» diventa necessario conservare stato, identità e decisione. Il passaggio successivo rende misurabile «Classifier-free guidance». [SRC-57-002; SRC-57-003]

- **Da «Classifier-free guidance» a «Editing e inpainting».** Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione. Una mask stabilisce regioni modificabili. «Editing e inpainting» introduce failure e recovery prima di un side effect o di una perdita di stato. Da «Classifier-free guidance» a «Editing e inpainting» cambia la domanda osservabile. [SRC-57-003; SRC-57-004]

- **Da «Editing e inpainting» a «Controllo e provenienza».** Una mask stabilisce regioni modificabili. ControlNet, adapter e reference image aggiungono vincoli. La chiusura su «Controllo e provenienza» valuta il sistema completo, non soltanto il componente iniziale. Il passaggio successivo rende misurabile «Controllo e provenienza». [SRC-57-004; SRC-57-001]

La catena completa produce immagine, score e metadati di provenienza a partire da latent, prompt, mask e rumore. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: controllo dell'immagine e verità del contenuto sono proprietà diverse.


## Prove sui confini del sistema

1. Ricostruisci «Latent diffusion» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Conditioning», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Classifier-free guidance» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Editing e inpainting» che produca una failure riconoscibile.
5. Per «Controllo e provenienza», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «latent, prompt, mask e rumore» e arriva fino a «immagine, score e metadati di provenienza». Il limite da conservare è questo: controllo dell'immagine e verità del contenuto sono proprietà diverse. Il confine di «Controllo e provenienza» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
