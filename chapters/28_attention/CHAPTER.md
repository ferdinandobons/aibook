<!--
chapter_id: CH-P06-ATTENTION
part_id: P06
order_key: 280
title: Il meccanismo di attention
maturity: CORE
status: revisione editoriale riaperta
version: 0.4.0-rc4
opened: 2026-07-30
last_web_research: 2026-07-30
last_source_check: 2026-07-30
environment: Python 3.13.5, PyTorch 2.10.0+cpu
deferred: informazione posizionale, multi-head attention, varianti KV, KV cache, implementazioni hardware-aware
-->

# Capitolo 28. Il meccanismo di attention

Una sequenza contiene più elementi, ma non tutti sono ugualmente utili in ogni punto del calcolo. Quando aggiorniamo la rappresentazione di un token, potremmo aver bisogno di combinare soprattutto alcune posizioni e quasi ignorarne altre. Un unico riassunto della sequenza, costruito una volta e riutilizzato ovunque, non offre questa flessibilità.

L'attention risolve il problema costruendo una combinazione diversa per ogni posizione. Il calcolo parte da un vettore che rappresenta l'elemento corrente, lo confronta con un insieme di vettori disponibili e trasforma i risultati in coefficienti. Quei coefficienti stabiliscono quanto ciascun vettore contribuisce all'output.

Seguiremo l'intero meccanismo su un esempio numerico molto piccolo. I valori non rappresentano il significato reale di parole specifiche; servono a rendere visibili i passaggi e a permettere il controllo dei conti. Dopo l'esempio passeremo alla forma matriciale, alla causal mask e a un'implementazione PyTorch verificata.

## Perché una combinazione fissa non basta

Consideriamo tre vettori disponibili:

$$
v_1=[1,0],\qquad v_2=[0,1],\qquad v_3=[1,1].
$$

Supponiamo che due posizioni della sequenza debbano costruire la propria rappresentazione usando questi stessi vettori. Se entrambe ricevono un unico riassunto `c`, la combinazione è identica per tutte e due. Una posizione potrebbe invece richiedere

$$
c_1=0{,}10v_1+0{,}60v_2+0{,}30v_3,
$$

mentre l'altra potrebbe richiedere

$$
c_2=0{,}05v_1+0{,}15v_2+0{,}80v_3.
$$

I vettori disponibili non sono cambiati. È cambiato il modo in cui vengono combinati. Il problema consiste quindi nel calcolare, per ogni posizione corrente, una serie di coefficienti specifici.

La figura seguente confronta le due possibilità. Nel pannello sinistro, `v1`, `v2` e `v3` confluiscono in un unico vettore `c`, riutilizzato da entrambe le posizioni di destinazione, indicate nella figura come `consumer 1` e `consumer 2`. Nel pannello destro, gli stessi vettori restano disponibili, ma ogni posizione produce coefficienti propri e ottiene una combinazione diversa.

![Confronto tra contesto fisso e coefficienti dipendenti dalla posizione corrente](../../assets/chapters/28_attention/ATT-01/candidate-v2.png)

La figura non mostra ancora come vengano calcolati i coefficienti. Stabilisce il requisito: la combinazione deve dipendere dall'elemento che sta interrogando la sequenza.

## Query, key e value

Per costruire quei coefficienti servono tre ruoli distinti. Il primo appartiene al vettore della posizione corrente. Il secondo appartiene ai vettori usati per misurare la compatibilità con quella posizione. Il terzo appartiene ai vettori che verranno effettivamente combinati.

Questi ruoli prendono i nomi di **query**, **key** e **value**:

- la query rappresenta l'elemento corrente;
- ogni key viene confrontata con la query;
- ogni value contiene il vettore che può contribuire all'output.

Nel nostro esempio useremo

$$
q=[1,0],
$$

$$
K=
\begin{bmatrix}
1&0\\
0&1\\
1&1
\end{bmatrix},
\qquad
V=
\begin{bmatrix}
1&0\\
0&1\\
1&1
\end{bmatrix}.
$$

La query ha shape `[d_k]=[2]`. Le matrici `K` e `V` hanno shape `[S,d_k]=[3,2]` e `[S,d_v]=[3,2]`, con `S=3` posizioni disponibili.

In questo esempio `K` e `V` contengono gli stessi numeri soltanto per mantenere brevi i calcoli. I due oggetti hanno funzioni diverse: `K` determina i coefficienti, mentre `V` fornisce i vettori da combinare. In un modello reale le key e le value vengono normalmente ottenute attraverso proiezioni differenti e non devono coincidere numericamente.

Resta invece essenziale la corrispondenza tra le righe. La riga `j` di `K` e la riga `j` di `V` appartengono alla stessa posizione. Se permutassimo una sola delle due matrici, useremmo il coefficiente calcolato per una key sulla value sbagliata.

## Il calcolo completo su una query

Il primo passo confronta la query con ogni key mediante un prodotto scalare:

$$
[1,0]\cdot[1,0]=1,\qquad
[1,0]\cdot[0,1]=0,\qquad
[1,0]\cdot[1,1]=1.
$$

Otteniamo così un vettore di tre score:

$$
qK^T=[1,0,1].
$$

La shape è `[S]=[3]`, perché esiste uno score per ogni key. Le value non sono ancora entrate nel calcolo. Questi score, inoltre, non sono coefficienti: possono essere negativi e non devono sommare a uno.

Nel Transformer originale gli score vengono divisi per la radice della dimensione delle key. Poiché `d_k=2`, il nostro esempio diventa

$$
\frac{[1,0,1]}{\sqrt{2}}
=
[0{,}7071,0,0{,}7071].
$$

La divisione non cambia la shape né l'ordine relativo degli score. Ne modifica soltanto la scala prima della softmax. Vaswani et al. introducono il fattore `1/\sqrt{d_k}` perché prodotti scalari di grande magnitudine possono portare la softmax in regioni con gradienti molto piccoli [Vaswani et al., 2017, §3.2.1].

Il ruolo del fattore si vede anche in un caso idealizzato. Se le componenti di query e key sono indipendenti, con media zero e varianza uno, il prodotto scalare è una somma di `d_k` termini e la sua varianza cresce come `d_k`. La divisione per `\sqrt{d_k}` riporta la varianza a ordine unitario. Questa derivazione spiega il fattore sotto le ipotesi dichiarate; non afferma che le rappresentazioni apprese in un modello reale siano indipendenti o standardizzate.

A questo punto applichiamo la softmax lungo le tre key:

$$
\alpha_j=\frac{e^{s_j}}{\sum_{m=1}^{S}e^{s_m}}.
$$

Con gli score scalati dell'esempio otteniamo, arrotondando a tre decimali,

$$
\alpha=[0{,}401,0{,}198,0{,}401].
$$

I coefficienti sono non negativi e sommano a uno, purché almeno uno score della riga sia finito e non venga applicato dropout dopo la softmax. Ogni coefficiente continua a essere associato alla stessa coppia key-value.

Soltanto ora usiamo `V`. Moltiplichiamo ogni value per il coefficiente corrispondente e sommiamo:

$$
0{,}401[1,0]+0{,}198[0,1]+0{,}401[1,1]
=
[0{,}802,0{,}599].
$$

Il vettore di output ha shape `[d_v]=[2]`. Le righe di `V` non vengono modificate; il calcolo produce una nuova combinazione. La query non viene sommata direttamente alle value: serve a calcolare, attraverso le key, i coefficienti con cui le value vengono combinate.

La figura seguente ripercorre lo stesso calcolo. Da sinistra a destra mostra gli input, i prodotti scalari, la divisione per `\sqrt{d_k}`, la softmax, la somma pesata e l'output finale.

![Esempio numerico completo per una query](../../assets/chapters/28_attention/ATT-02/candidate-v2.png)

Possiamo riassumere l'algoritmo senza usare ancora la formula compatta:

```text
ricevi una query, S key e S value
calcola uno score tra la query e ogni key
dividi gli score per sqrt(d_k)
normalizza gli score con la softmax
moltiplica ogni value per il coefficiente corrispondente
somma i vettori pesati
restituisci un vettore di dimensione d_v
```

Il numero dei coefficienti coincide sempre con il numero di coppie key-value; la dimensione dell'output coincide con quella delle value.

## Dall'esempio alla forma matriciale

La trasformazione appena costruita si chiama **scaled dot-product attention**. Per una sola query si scrive

$$
\mathrm{Attention}(q,K,V)
=
\mathrm{softmax}\left(\frac{qK^T}{\sqrt{d_k}}\right)V.
$$

Quando le query sono più di una, le raccogliamo nelle righe di una matrice `Q`:

- `Q\in\mathbb{R}^{L\times d_k}`;
- `K\in\mathbb{R}^{S\times d_k}`;
- `V\in\mathbb{R}^{S\times d_v}`.

La formula diventa

$$
\mathrm{Attention}(Q,K,V)
=
\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V.
$$

La softmax viene applicata riga per riga. Ogni riga di `QK^T` appartiene a una query; ogni colonna appartiene a una key [Vaswani et al., 2017, §3.2.1].

| Oggetto | Shape | Significato |
|---|---:|---|
| `Q` | `[L,d_k]` | una riga per query |
| `K` | `[S,d_k]` | una riga per key |
| `V` | `[S,d_v]` | una riga per value |
| `QK^T` | `[L,S]` | uno score per coppia query-key |
| `A` | `[L,S]` | coefficienti normalizzati |
| `O=AV` | `[L,d_v]` | una riga di output per query |

Con più query, lo stesso calcolo viene eseguito su più righe. Ogni query produce una distribuzione diversa sulle key e quindi una combinazione diversa delle value. Il numero di righe di `K` deve continuare a coincidere con quello di `V`; la dimensione finale di ogni output rimane `d_v`.

La formula non richiede che `Q`, `K` e `V` derivino dalla stessa sequenza. Nella **self-attention** provengono dalla stessa sequenza attraverso proiezioni apprese. Nella **cross-attention**, le query provengono da una sequenza e le coppie key-value da un'altra. Nella **causal self-attention**, i tre gruppi provengono dalla stessa sequenza, ma ogni query può usare soltanto la propria posizione e quelle precedenti.

## Escludere le posizioni future

Nei modelli autoregressivi, il token in posizione `i` non deve usare informazioni provenienti da posizioni successive. Il vincolo viene applicato agli score prima della softmax.

Introduciamo una mask additiva `M\in\mathbb{R}^{L\times S}`:

$$
A=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right).
$$

Nel caso causale quadrato,

$$
M_{ij}=
\begin{cases}
0 & \text{se } j\le i,\\
-\infty & \text{se } j>i.
\end{cases}
$$

Le celle future ricevono quindi un logit pari a `-inf`. Dopo la softmax, i coefficienti corrispondenti sono zero. La mask cambia quali score partecipano alla normalizzazione, ma non modifica `L`, `S`, `d_k`, `d_v` o le righe di `V`.

Applicare la mask direttamente alle value avrebbe un significato diverso: cambierebbe i dati trasportati anziché impedire ad alcune posizioni di ricevere peso. Per implementare il vincolo causale, la mask deve intervenire sugli score prima della softmax.

## Dalla formula a PyTorch

Il seguente snippet ripete l'esempio numerico con le stesse query, key e value. Le righe centrali corrispondono al calcolo già svolto a mano; le asserzioni verificano la somma dei coefficienti e le shape.

```python
from __future__ import annotations

import math
import torch

q = torch.tensor([1.0, 0.0], dtype=torch.float64)
k = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=torch.float64)
v = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=torch.float64)

scores = (q @ k.transpose(0, 1)) / math.sqrt(q.numel())
weights = torch.softmax(scores, dim=-1)
output = weights @ v

assert scores.shape == (3,)
assert output.shape == (2,)
torch.testing.assert_close(weights.sum(), torch.tensor(1.0, dtype=weights.dtype))
```

Il file completo è [`code/snip_att_001_single_query.py`](code/snip_att_001_single_query.py); l'output registrato è in [`code/outputs/SNIP-ATT-001.txt`](code/outputs/SNIP-ATT-001.txt).

Per batch e head esplicite, PyTorch usa shape come `[B,H,L,d_k]`, `[B,H,S,d_k]` e `[B,H,S,d_v]`. Il confronto seguente verifica che l'implementazione diretta coincida con `torch.nn.functional.scaled_dot_product_attention` nell'ambiente eseguito quando `dropout_p=0.0`:

```python
import math
import torch
import torch.nn.functional as F

scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
weights = torch.softmax(scores, dim=-1)
output = weights @ v

api_output = F.scaled_dot_product_attention(q, k, v, dropout_p=0.0)
torch.testing.assert_close(output, api_output, rtol=1e-12, atol=1e-12)
```

Il file completo è [`code/snip_att_002_matrix_api.py`](code/snip_att_002_matrix_api.py). Il codice è stato eseguito con PyTorch `2.10.0+cpu`; la firma e la semantica correnti dell'API sono state ricontrollate nella documentazione stable `2.13`.

Una causal mask booleana può essere costruita con una matrice triangolare inferiore:

```python
allowed = torch.ones(3, 3, dtype=torch.bool).tril()
output = F.scaled_dot_product_attention(
    q,
    k,
    v,
    attn_mask=allowed,
    dropout_p=0.0,
)
```

Nel file [`code/snip_att_003_causal_mask.py`](code/snip_att_003_causal_mask.py), l'output dell'API viene confrontato con un'implementazione diretta che inserisce `-inf` negli score non ammessi.

> **Nota sulle API.** In `F.scaled_dot_product_attention`, `True` indica una posizione ammessa. In `MultiheadAttention.key_padding_mask`, `True` indica invece una posizione da ignorare. Inoltre `scaled_dot_product_attention` applica dropout quando `dropout_p>0`, indipendentemente dallo stato di training del modulo chiamante. Queste convenzioni appartengono alle API e non cambiano la definizione matematica del meccanismo [PyTorch 2.13 Docs].

## Costo, limiti e passaggio alla multi-head attention

Per `Q[L,d_k]`, `K[S,d_k]` e `V[S,d_v]`, il prodotto `QK^T` richiede ordine `O(LSd_k)` operazioni; il prodotto `AV` richiede ordine `O(LSd_v)`. Una realizzazione che conserva score o coefficienti materializza anche un intermedio di shape `[L,S]`. Nella self-attention con `L=S=n`, questo intermedio contiene `n^2` elementi.

Implementazioni hardware-aware possono calcolare lo stesso operatore con strategie diverse di accesso alla memoria e ricomputazione. Il loro funzionamento verrà trattato nella parte dedicata all'efficienza; non è necessario per comprendere l'operatore di base.

L'attention, da sola, non introduce informazione posizionale, non aggiunge dati esterni e non stabilisce se un contenuto sia corretto. Se `Q`, `K` e `V` vengono permutati in modo coerente e non contengono segnali di posizione, anche l'output segue la stessa permutazione. L'ordine deve quindi essere rappresentato nei dati o nel calcolo attraverso un meccanismo aggiuntivo.

Il caso studiato finora usa un solo insieme di proiezioni. La **multi-head attention** ripete lo stesso meccanismo su più proiezioni, mantiene separati i risultati e li ricompone. Concatenazione, proiezione finale e shape per head costituiscono il passo successivo e verranno introdotti insieme al blocco Transformer.

## Riepilogo

Siamo partiti da un limite semplice: un unico vettore di contesto non può offrire combinazioni diverse a posizioni diverse. L'attention sostituisce quel riassunto fisso con un calcolo dipendente dalla query. La query viene confrontata con le key, gli score vengono ridimensionati e normalizzati, poi i coefficienti risultanti combinano le value.

La forma matriciale esegue lo stesso procedimento per più query in parallelo. Una mask può escludere alcune coppie query-key prima della softmax, senza modificare le value. Il risultato è una matrice con una riga per query e dimensione finale `d_v`.

### Verifica della comprensione

1. Ricostruisci l'ordine di prodotto scalare, scaling, mask opzionale, softmax e combinazione delle value.
2. Indica il primo passaggio in cui `V` viene effettivamente usata.
3. Spiega perché la causal mask agisce sugli score e non direttamente sulle value.
4. Sostituisci `q=[1,0]` con `q=[0,1]` e prevedi gli score prima della softmax.
5. Determina la shape dell'output con `L=5`, `S=7`, `d_k=64` e `d_v=32`.

### Esercizi

1. Calcola a mano i coefficienti e l'output per `q=[0,1]` usando le stesse `K` e `V`.
2. Modifica `SNIP-ATT-002` usando `d_v=3` e verifica la nuova shape dell'output.
3. Sostituisci la mask booleana con una mask additiva contenente `0` e `-inf`.
4. Costruisci un caso in cui tutte le key producano lo stesso score e spiega il risultato della softmax.
5. Verifica con un test che una permutazione coerente di query, key e value permuti nello stesso modo l'output quando non è presente informazione posizionale.

## Fonti e materiali verificabili

La definizione portante deriva da Vaswani et al., *Attention Is All You Need* (2017). Il contesto storico comprende Bahdanau, Cho e Bengio (2015) e Luong, Pham e Manning (2015). Le convenzioni implementative sono verificate sulla documentazione ufficiale PyTorch.

Le schede complete e i limiti d'uso sono in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md). Codice, test, output e ambiente sono raccolti nella cartella [`code/`](code/).
