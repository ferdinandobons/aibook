# Audit visuale ATT-03. Scaled dot-product attention con shape

## Stato

- Versione esaminata: v1
- Esito: **respinta, da rigenerare**
- Immagine finale pubblicabile: non ancora disponibile

## Domanda prevista

Come si generalizza il calcolo di attention a tutte le query attraverso `QK^T`, scaling, mask opzionale, softmax e prodotto con `V`?

## Problemi bloccanti individuati

### 1. Collegamento ambiguo tra mask e percorso di `V`

La linea tratteggiata che scende dal blocco della causal mask termina visivamente sul lungo percorso nero che porta `V` verso `A · V`. Questa composizione può far credere che la mask venga applicata alle value. La mask deve invece modificare gli score, o un attention bias sommato agli score, prima della softmax.

### 2. Valori della softmax non coerenti con gli score mostrati

La matrice degli score illustrativa è:

```text
[ 2.0,  1.0, -1.0]
[ 0.5,  1.5,  0.0]
[-0.5,  0.5,  1.0]
```

La softmax per riga corretta, arrotondata a tre decimali, è:

```text
[0.705, 0.259, 0.035]
[0.231, 0.629, 0.140]
[0.122, 0.331, 0.547]
```

La figura mostra invece valori diversi. L’etichetta `Illustrativo` non autorizza un calcolo internamente incoerente.

### 3. Provenienza dei punteggi non dichiarata nel mini-esempio

Il mini-esempio salta direttamente dagli score alla softmax, mentre il flusso principale introduce scaling e mask. La nuova versione deve specificare se i valori mostrati sono `score già scalati e non mascherati`, oppure deve mostrare anche le operazioni intermedie.

### 4. Uso improprio dell’etichetta “Output verificato”

Il verde e la label `Output verificato` suggeriscono una misurazione riprodotta. L’output è invece concettuale e l’esempio è illustrativo. La legenda deve distinguere `Output` da `Verificato`, riservando quest’ultimo a misure con setup dichiarato.

### 5. Formulazione troppo forte sulla scalatura

La frase `mantenendo stabile la softmax` è meno precisa del meccanismo documentato. La nuova versione userà una formulazione come: `riduce la magnitudine dei logit e il rischio che la softmax entri in regioni con gradienti molto piccoli`.

### 6. Densità eccessiva per una visuale di prima introduzione

La figura riunisce proiezioni, score, scaling, mask, softmax, combinazione con `V`, esempio numerico, invariante, confine e legenda. È adatta, dopo correzione, come visuale di ricostruzione finale. Non è adatta come prima spiegazione del meccanismo. Il capitolo deve prima usare visuali più atomiche, in linea con il gate delle visuali.

### 7. Semantica della mask non completamente esplicita

Le celle colorate della matrice triangolare non dichiarano in modo inequivocabile se rappresentano posizioni bloccate o ammesse. La nuova versione deve includere una label testuale vicina alla matrice e non affidare il significato al solo colore.

## Correzioni richieste per v2

1. Separare completamente il percorso `V -> A · V` dalla callout o dalla linea della mask.
2. Applicare la mask graficamente al tensor degli score prima della softmax.
3. Usare valori di softmax ricalcolati oppure scegliere numeri più semplici e coerenti.
4. Indicare `score già scalati, senza mask` nel mini-esempio, se scaling e mask non vengono mostrati numericamente.
5. Sostituire `Output verificato` con `Output` o `Risultato del calcolo`.
6. Rendere esplicito quali celle della mask sono bloccate.
7. Ridurre le callout e mantenere una sola domanda principale.
8. Valutare due immagini separate: una per il flusso tensoriale, una per l’esempio numerico.

## Nuovo audit richiesto

La v2 dovrà essere ricontrollata integralmente. Non sarà sufficiente verificare soltanto i difetti sopra, perché la rigenerazione può introdurre nuove ambiguità.
