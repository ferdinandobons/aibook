<!--
chapter_id: CH-P06-TEXT-DATA
part_id: P06
order_key: 260
title: Il testo come dato
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 26. Il testo come dato

La domanda guida di questa lezione è come collegare «Unicode e byte» e «Lunghezza, lingua e costi» senza perdere il contratto tecnico di il testo come dato. L'oggetto osservato è il testo prima e dopo la tokenizzazione. Il contratto locale è: input, una stringa Unicode con byte e token speciali; operazione, normalizzazione, segmentazione e packing; output, ID, confini, mask e costo in token. Il caso guida è questo: La stessa stringa convertita prima in code point e poi in byte UTF-8, conservando la reversibilità. Il confine da mantenere esplicito è: stringa, encoding e tokenizer devono restare dichiarati.

## Unicode e byte

Il testo è una sequenza di code point codificata in byte. Normalizzazione Unicode e decoding devono essere dichiarati. [SRC-26-001]

Il tokenizer è parte dell'interfaccia del checkpoint, non un dettaglio esterno.

**Caso da seguire.** La stessa stringa convertita prima in code point e poi in byte UTF-8, conservando la reversibilità.

**Controllo.** Conserva record iniziale, regola applicata e record finale; un conteggio aggregato non basta a spiegare la trasformazione.


![Il testo come dato: matrix](../../assets/chapters/26_text_data/DATA-01/candidate-v48.png)

La prima figura segue il percorso da «Unicode e byte» a «Token speciali».


## Tokenizzazione

BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti. Il tokenizer fa parte dell'interfaccia del checkpoint. [SRC-26-002]

**Caso da seguire.** Un prefisso corto con ID, lunghezza, posizione e output del token successivo dichiarati.

**Controllo.** Esegui «Tokenizzazione» due volte sullo stesso manifest e confronta identificatori, ordine, split e checksum.


## Token speciali

BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi. ID uguali richiedono la stessa convenzione. [SRC-26-003]

**Caso da seguire.** Per «Token speciali» si mantiene l'input del capitolo e si isola questa condizione: BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi.

**Controllo.** Aggiungi un record che deve essere escluso e verifica che l'output conservi anche il motivo dell'esclusione.


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
    text = "pacco"
    code_points = list(text)
    token_ids = [ord(char) for char in code_points]
    return {"code_points": code_points, "token_ids": token_ids, "invariant": "tokenization preserves an explicit mapping from text to ids"}
```

Esecuzione con `python snip_26_contract.py`:

```text
{"code_points": ["p", "a", "c", "c", "o"], "invariant": "tokenization preserves an explicit mapping from text to ids", "token_ids": [112, 97, 99, 99, 111]}
```

Il test associato è [`code/test_26_contract.py`](code/test_26_contract.py); l'output versionato è [`code/outputs/SNIP-26-001.txt`](code/outputs/SNIP-26-001.txt).


## Packing e confini

Più documenti possono condividere una sequenza. Attention mask e loss mask devono impedire dipendenze non desiderate. [SRC-26-004]

**Caso da seguire.** Due record con ID, testo, licenza e timestamp che attraversano una sola trasformazione registrata.

**Controllo.** Modifica una sola regola della pipeline e misura quali record cambiano, evitando di confrontare raccolte di origine diversa.


## Lunghezza, lingua e costi

Token per carattere variano tra lingue e formati. La lunghezza in token influenza contesto, costo e valutazione. [SRC-26-001]

**Caso da seguire.** Un confronto tra due prefissi con la stessa stringa, tokenizer dichiarato e mask causale esplicita.

**Controllo.** Descrivi ciò che la pipeline perde oltre a ciò che produce. Il limite locale è: La lunghezza in token influenza contesto, costo e valutazione.


![Il testo come dato: branch](../../assets/chapters/26_text_data/DATA-02/candidate-v48.png)

La seconda figura mette a confronto «Packing e confini» e il limite discusso in «Lunghezza, lingua e costi».


## Come si collegano i passaggi

- **Da «Unicode e byte» a «Tokenizzazione».** Il testo è una sequenza di code point codificata in byte. BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti. Il primo passaggio identifica il record e la sua provenienza; il secondo dichiara la trasformazione che cambia la popolazione osservata. [SRC-26-001; SRC-26-002]

- **Da «Tokenizzazione» a «Token speciali».** BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti. BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi. La trasformazione diventa confrontabile soltanto quando il passaggio successivo conserva configurazione, conteggi e artefatti intermedi. [SRC-26-002; SRC-26-003]

- **Da «Token speciali» a «Packing e confini».** BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi. Più documenti possono condividere una sequenza. Una volta resa tracciabile la pipeline, il quarto passaggio può affrontare selezione o uso senza confondere un cambiamento nei dati con uno nel modello. [SRC-26-003; SRC-26-004]

- **Da «Packing e confini» a «Lunghezza, lingua e costi».** Più documenti possono condividere una sequenza. Token per carattere variano tra lingue e formati. L'ultima sezione porta il risultato alla valutazione e chiede quali record, slice o failure restano fuori dalla media. [SRC-26-004; SRC-26-001]

La catena completa produce ID, confini, mask e costo in token a partire da una stringa Unicode con byte e token speciali. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: stringa, encoding e tokenizer devono restare dichiarati.


## Esercizi sulla tracciabilità

1. Ricostruisci «Unicode e byte» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Tokenizzazione», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Token speciali» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Packing e confini» che produca una failure riconoscibile.
5. Per «Lunghezza, lingua e costi», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## L'artefatto che deve sopravvivere

La lezione parte da «una stringa Unicode con byte e token speciali» e arriva fino a «ID, confini, mask e costo in token». Il limite da conservare è questo: stringa, encoding e tokenizer devono restare dichiarati. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
