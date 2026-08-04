<!--
chapter_id: CH-P11-RAG
part_id: P11
order_key: 640
title: Retrieval-Augmented Generation
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 64. Retrieval-Augmented Generation

La domanda guida di questa lezione è come collegare «Una pipeline in due fasi» e «Valutazione end-to-end» senza perdere il contratto tecnico di retrieval-augmented generation. L'oggetto osservato è la pipeline che collega query, contesto e risposta. Il contratto locale è: input, query, chunk, fonti e prompt; operazione, chunking, retrieval, attribution e generazione; output, risposta con evidenza e score end-to-end. Il caso guida è questo: Due chunk vengono recuperati e una risposta mantiene il documento citato come record distinto. Il confine da mantenere esplicito è: contesto recuperato e testo generato devono restare distinguibili.

## Una pipeline in due fasi

Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati. [SRC-64-001]

Il contesto recuperato deve essere ispezionabile e separato dalla risposta.

**Caso da seguire.** Due chunk vengono recuperati e una risposta mantiene il documento citato come record distinto.

**Controllo.** Conserva record iniziale, regola applicata e record finale; un conteggio aggregato non basta a spiegare la trasformazione.


![Retrieval-Augmented Generation: pipeline](../../assets/chapters/64_rag/RAG-01/candidate-v48.png)

La prima figura segue il percorso da «Una pipeline in due fasi» a «Prompt con fonti».


## Chunking

Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Un chunk non coincide sempre con una unità semantica. [SRC-64-002]

**Caso da seguire.** Due chunk citati e una frase che non compare nelle fonti.

**Controllo.** Esegui «Chunking» due volte sullo stesso manifest e confronta identificatori, ordine, split e checksum.


## Prompt con fonti

Documenti, istruzioni e domanda devono avere confini espliciti. Il modello può ignorare, confondere o citare in modo scorretto il contesto. [SRC-64-003]

**Caso da seguire.** Un caso in cui contesto recuperato e testo generato devono restare distinguibili.

**Controllo.** Aggiungi un record che deve essere escluso e verifica che l'output conservi anche il motivo dell'esclusione.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    retrieved = [("d1", 0.9), ("d2", 0.4)]
    answer = "Il pacco è in transito"
    cited = retrieved[0][0]
    return {"answer": answer, "citation": cited, "invariant": "RAG keeps retrieved evidence and generated answer as separate records"}
```

Esecuzione con `python snip_64_contract.py`:

```text
{"answer": "Il pacco è in transito", "citation": "d1", "invariant": "RAG keeps retrieved evidence and generated answer as separate records"}
```

Il test associato è [`code/test_64_contract.py`](code/test_64_contract.py); l'output versionato è [`code/outputs/SNIP-64-001.txt`](code/outputs/SNIP-64-001.txt).


## Attribution

Una risposta supportata deve essere collegabile a passaggi recuperati. Citazione presente e citazione corretta sono controlli differenti. [SRC-64-004]

**Caso da seguire.** Quattro casi con tre esiti corretti e una failure, riportando la media insieme alla slice e al protocollo per «Attribution» e all'output risposta con evidenza e score end-to-end.

**Controllo.** Modifica una sola regola della pipeline e misura quali record cambiano, evitando di confrontare raccolte di origine diversa.


## Valutazione end-to-end

Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme. [SRC-64-001]

**Caso da seguire.** Una query e tre documenti ricevono punteggi distinti. Prima di generare, controlliamo quale documento è entrato nel contesto e con quale ranking.

**Controllo.** Descrivi ciò che la pipeline perde oltre a ciò che produce. Il limite locale è: Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme.


![Retrieval-Augmented Generation: graph](../../assets/chapters/64_rag/RAG-02/candidate-v48.png)

La seconda figura mette a confronto «Attribution» e il limite discusso in «Valutazione end-to-end».


## Come si collegano i passaggi

- **Da «Una pipeline in due fasi» a «Chunking».** Il retriever seleziona contesto esterno; il generatore produce la risposta condizionata sui documenti recuperati. Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Il primo passaggio identifica il record e la sua provenienza; il secondo dichiara la trasformazione che cambia la popolazione osservata. [SRC-64-001; SRC-64-002]

- **Da «Chunking» a «Prompt con fonti».** Dimensione, overlap e struttura dei chunk modificano recall e quantità di contesto. Documenti, istruzioni e domanda devono avere confini espliciti. La trasformazione diventa confrontabile soltanto quando il passaggio successivo conserva configurazione, conteggi e artefatti intermedi. [SRC-64-002; SRC-64-003]

- **Da «Prompt con fonti» a «Attribution».** Documenti, istruzioni e domanda devono avere confini espliciti. Una risposta supportata deve essere collegabile a passaggi recuperati. Una volta resa tracciabile la pipeline, il quarto passaggio può affrontare selezione o uso senza confondere un cambiamento nei dati con uno nel modello. [SRC-64-003; SRC-64-004]

- **Da «Attribution» a «Valutazione end-to-end».** Una risposta supportata deve essere collegabile a passaggi recuperati. Recall del retriever, precisione del contesto, fedeltà e utilità della risposta devono essere misurate separatamente e insieme. L'ultima sezione porta il risultato alla valutazione e chiede quali record, slice o failure restano fuori dalla media. [SRC-64-004; SRC-64-001]

La catena completa produce risposta con evidenza e score end-to-end a partire da query, chunk, fonti e prompt. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: contesto recuperato e testo generato devono restare distinguibili.


## Esercizi sulla tracciabilità

1. Ricostruisci «Una pipeline in due fasi» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Chunking», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Prompt con fonti» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Attribution» che produca una failure riconoscibile.
5. Per «Valutazione end-to-end», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## L'artefatto che deve sopravvivere

La lezione parte da «query, chunk, fonti e prompt» e arriva fino a «risposta con evidenza e score end-to-end». Il limite da conservare è questo: contesto recuperato e testo generato devono restare distinguibili. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
