# Capitolo 28. Il meccanismo di attention

## Metadati

- `chapter_id`: `CH-P06-ATTENTION`
- Parte: `P06`, Sequenze, linguaggio e contesto
- Maturità: `CORE`
- Stato: **revisione autoriale del capitolo pilota**
- Versione candidata: `0.1.0-rc1`
- Data di apertura: 30 luglio 2026
- Data dell'ultima ricerca web: 30 luglio 2026
- Data dell'ultima verifica delle fonti: 30 luglio 2026
- Data di congelamento editoriale: non assegnata
- Documentazione PyTorch verificata: stable `2.13`
- Ambiente di esecuzione disponibile: Python `3.13.5`, PyTorch `2.10.0+cpu`
- Oggetto continuo: una query e tre coppie key-value di dimensione 2
- Concetti differiti: positional encoding, FlashAttention a livello di kernel, MQA, GQA, MLA e KV cache

> **Stato della candidatura.** Il testo e il codice sono presentati per revisione. Le figure `ATT-01/candidate-v2.png` e `ATT-02/candidate-v2.png` sono validate tecnicamente e attendono l'approvazione autoriale. Nessuna pagina del libro è stata rasterizzata.

## Bussola

- **Stato prima:** disponiamo di una sequenza di vettori, ma non di un'operazione che scelga contributi diversi in funzione della posizione corrente.
- **Problema:** costruire per ogni query una combinazione dei value che dipenda dalla compatibilità con le key.
- **Stato dopo:** sappiamo calcolare scaled dot-product attention per una query e per matrici complete, applicare una causal mask, usare l'API PyTorch e localizzare il passaggio alla multi-head attention.
- **Invariante:** il numero di righe dell'output coincide con il numero di query; la dimensione di ogni riga dell'output coincide con `d_v`.
- **Confine:** il meccanismo non introduce da solo informazione posizionale, memoria esterna o nuove righe di value.

## Obiettivo operativo

Al termine del capitolo il lettore può:

1. spiegare il ruolo distinto di query, key e value;
2. calcolare gli score, lo scaling, la softmax e la somma pesata;
3. verificare le shape di ogni operazione;
4. distinguere self-attention, cross-attention e causal self-attention;
5. implementare il caso base con operazioni tensoriali PyTorch;
6. confrontare l'implementazione diretta con `torch.nn.functional.scaled_dot_product_attention`;
7. riconoscere i limiti del caso base e il motivo della multi-head attention.

## Prerequisiti stabili

Il capitolo assume noti:

- vettori, matrici e prodotto matriciale;
- shape e trasposizione;
- proiezione lineare;
- softmax applicata a un vettore;
- embedding come sequenza di vettori.

## 1. Dove siamo

Consideriamo tre posizioni già trasformate in vettori. Non chiediamo ancora come siano stati prodotti. Per il meccanismo corrente sono input disponibili.

Per una singola posizione corrente usiamo una query:

$$
q = [1, 0] \in \mathbb{R}^{2}.
$$

Le tre posizioni consultabili forniscono una key e una value ciascuna:

$$
K =
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
1 & 1
\end{bmatrix}
\in \mathbb{R}^{3\times2},
\qquad
V =
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
1 & 1
\end{bmatrix}
\in \mathbb{R}^{3\times2}.
$$

I numeri sono **illustrativi**. Sono stati scelti per rendere il calcolo controllabile a mano.

### Stato prima

La query è un vettore. Le key indicano i vettori con cui confrontarla. Le value contengono i vettori da combinare.

### Problema

Manca una regola che produca tre coefficienti dipendenti da `q`. Una media uniforme assegnerebbe sempre `1/3` a ogni value, indipendentemente dalla query.

La figura candidata `ATT-01` confronta queste due situazioni:

![Pesi fissi e pesi dipendenti dalla query](../../assets/chapters/28_attention/ATT-01/candidate-v2.png)

La figura non dimostra la formula. Stabilisce soltanto il requisito: query diverse devono poter produrre coefficienti diversi sulla stessa sorgente.

## 2. Una query confrontata con tutte le key

### Input e shape

- `q`: `[d_k] = [2]`
- `K`: `[S, d_k] = [3, 2]`
- `V`: `[S, d_v] = [3, 2]`

`S` è il numero di posizioni consultabili. In questo esempio `S = 3`.

### Trasformazione

Calcoliamo un prodotto scalare tra `q` e ogni riga di `K`:

$$
qK^T = [1, 0, 1].
$$

Il risultato contiene uno score per ogni key. La sua shape è `[S]`.

### Cosa è cambiato

Le tre key sono state ridotte a tre numeri di compatibilità rispetto alla query corrente.

### Cosa è rimasto invariato

`V` non è stato ancora letto dal calcolo. Gli score dipendono da `q` e `K`, non dal contenuto di `V`.

### Cosa non fa

Il prodotto scalare non produce ancora coefficienti normalizzati. Gli score possono essere negativi e non devono sommare a 1.

## 3. Perché dividiamo per la radice di `d_k`

La scaled dot-product attention usa:

$$
s = \frac{qK^T}{\sqrt{d_k}}.
$$

Con `d_k = 2` otteniamo:

$$
s = [0{,}7071, 0, 0{,}7071].
$$

Vaswani et al. introducono questa divisione perché, al crescere di `d_k`, prodotti scalari di grande magnitudine possono spingere la softmax verso regioni con gradienti molto piccoli [Vaswani et al., 2017, §3.2.1].

### Derivazione sotto ipotesi esplicite

Supponiamo, soltanto per questa derivazione, che le componenti di `q` e `k` siano indipendenti, abbiano media 0 e varianza 1. Il prodotto scalare è:

$$
q\cdot k = \sum_{r=1}^{d_k} q_r k_r.
$$

Sotto queste ipotesi la varianza della somma cresce come `d_k`. Dividere per `\sqrt{d_k}` riporta la varianza a ordine unitario. Questa derivazione non afferma che le componenti apprese di un modello reale siano indipendenti o standardizzate. Spiega il ruolo del fattore di scala nel caso idealizzato richiamato dal paper.

### Invariante

Lo scaling non cambia la shape. Modifica soltanto la magnitudine degli score prima della softmax.

## 4. Dagli score ai pesi

Applichiamo la softmax lungo le tre key:

$$
\alpha_j = \frac{e^{s_j}}{\sum_{m=1}^{S}e^{s_m}}.
$$

Otteniamo, con arrotondamento a tre decimali:

$$
\alpha = [0{,}401,\ 0{,}198,\ 0{,}401].
$$

Ogni coefficiente è non negativo e la somma è 1, a condizione che la riga contenga almeno uno score finito. Queste proprietà derivano dalla definizione della softmax.

### Output e shape

- input della softmax: `[S]`
- output della softmax: `[S]`

### Errore comune

Gli score e i pesi non sono lo stesso oggetto. Gli score sono i logit prima della normalizzazione. I pesi sono i coefficienti dopo la softmax.

## 5. La somma pesata delle value

Ora usiamo i pesi per combinare le righe di `V`:

$$
o = \sum_{j=1}^{S}\alpha_j v_j = \alpha V.
$$

Nel nostro esempio:

$$
\begin{aligned}
o &= 0{,}401[1,0] + 0{,}198[0,1] + 0{,}401[1,1] \\
  &= [0{,}802,\ 0{,}599].
\end{aligned}
$$

La figura candidata `ATT-02` percorre lo stesso oggetto, dalla query all'output:

![Una query, tre key e tre value](../../assets/chapters/28_attention/ATT-02/candidate-v2.png)

### Cosa è cambiato

Abbiamo prodotto un nuovo vettore che combina informazioni provenienti dalle tre value.

### Cosa è rimasto invariato

Il numero e il contenuto delle righe originali di `V` non vengono modificati. Viene creata una combinazione aggiuntiva.

### Invariante

La dimensione dell'output è `d_v`. Non è obbligatorio che `d_v` coincida con `d_k`.

### Cosa non fa

L'operazione non aggiunge informazione che non sia già contenuta nelle value. Cambia i coefficienti con cui le value vengono combinate.

## 6. Il nome tecnico e il contratto completo

La trasformazione appena eseguita è una **scaled dot-product attention** per una query.

Per più query raccogliamo le query in una matrice:

- `Q \in \mathbb{R}^{L\times d_k}`;
- `K \in \mathbb{R}^{S\times d_k}`;
- `V \in \mathbb{R}^{S\times d_v}`.

`L` è il numero di query. `S` è il numero di coppie key-value.

La forma matriciale è:

$$
\mathrm{Attention}(Q,K,V)
=
\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V.
$$

La softmax è applicata per riga. Ogni riga dell'output corrisponde a una query.

### Contratto delle shape

| Oggetto | Shape | Ruolo |
|---|---:|---|
| `Q` | `[L, d_k]` | una riga per query |
| `K` | `[S, d_k]` | una riga per key |
| `V` | `[S, d_v]` | una riga per value |
| `QK^T` | `[L, S]` | uno score per coppia query-key |
| `A` | `[L, S]` | pesi normalizzati per query |
| `O = AV` | `[L, d_v]` | una riga di output per query |

La definizione e la multi-head generalization sono presentate nel Transformer originale [Vaswani et al., 2017, §§3.2.1–3.2.2].

## 7. Da dove provengono query, key e value

La formula non impone che `Q`, `K` e `V` provengano dallo stesso tensor.

### Self-attention

`Q`, `K` e `V` sono proiezioni della stessa sequenza di input. Nel Transformer originale, ogni head usa proiezioni apprese separate [Vaswani et al., 2017, §3.2.2].

### Cross-attention

Le query provengono da una sequenza, mentre key e value provengono da un'altra sorgente. Questa configurazione è usata, per esempio, tra decoder ed encoder nei modelli encoder-decoder.

### Causal self-attention

`Q`, `K` e `V` provengono dalla stessa sequenza, ma una query in posizione `i` non può usare key in posizioni future. Il vincolo viene applicato agli score prima della softmax.

## 8. La mask modifica gli score, non le value

Introduciamo una mask additiva `M \in \mathbb{R}^{L\times S}`:

$$
A = \mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}} + M\right).
$$

Nel caso causale quadrato:

$$
M_{ij} =
\begin{cases}
0 & \text{se } j \le i,\\
-\infty & \text{se } j > i.
\end{cases}
$$

Dopo la softmax, le posizioni con logit `-\infty` ricevono peso 0.

### Invariante

La mask non cambia `L`, `S` o `d_v`. Cambia quali score possono contribuire.

### Semantica delle mask nelle API PyTorch

La documentazione stabile PyTorch `2.13` specifica che, in `torch.nn.functional.scaled_dot_product_attention`, una mask booleana usa `True` per indicare una posizione che **partecipa** all'attention. Nella `key_padding_mask` di `torch.nn.MultiheadAttention`, `True` indica invece una posizione da ignorare. Le due semantiche booleane non devono essere confuse [PyTorch 2.13 Docs, `scaled_dot_product_attention`; `MultiheadAttention`].

## 9. Implementazione minima: una query

Lo snippet seguente implementa esattamente l'esempio numerico. La riga centrale è il prodotto tra query e key trasposte, seguito dalla divisione per `sqrt(d_k)`.

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

File eseguito: [`code/snip_att_001_single_query.py`](code/snip_att_001_single_query.py).

Output registrato: [`code/outputs/SNIP-ATT-001.txt`](code/outputs/SNIP-ATT-001.txt).

## 10. Implementazione matriciale e confronto con l'API ufficiale

Per batch e head esplicite usiamo le shape documentate dall'API:

- `Q`: `[B, H, L, d_k]`;
- `K`: `[B, H, S, d_k]`;
- `V`: `[B, H, S, d_v]`.

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

Il confronto è stato eseguito nell'ambiente registrato con PyTorch `2.10.0+cpu`. La firma e la semantica correnti dell'API sono state ricontrollate nella documentazione stabile `2.13`. Non viene dichiarata un'esecuzione locale sotto `2.13`.

La documentazione corrente indica che l'operatore può selezionare implementazioni ottimizzate in funzione degli input e del backend. La scelta del kernel può produrre piccole differenze numeriche dovute all'ordine delle operazioni in virgola mobile [PyTorch 2.13 Docs, `scaled_dot_product_attention`].

### Nota sul dropout

`scaled_dot_product_attention` applica dropout quando `dropout_p > 0`, indipendentemente dallo stato di training di un modulo chiamante. La documentazione raccomanda di passare esplicitamente `0.0` quando il dropout non deve essere applicato. Nel capitolo base usiamo `dropout_p=0.0`.

## 11. Causal mask in PyTorch

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

Nel file eseguito, il risultato viene confrontato con una implementazione diretta che applica `-inf` agli score non ammessi.

File: [`code/snip_att_003_causal_mask.py`](code/snip_att_003_causal_mask.py).

Test: le posizioni future hanno peso esattamente zero nell'esempio in `float64`.

## 12. Multi-head attention

Una singola head usa un solo insieme di proiezioni. La multi-head attention calcola più attention in parallelo:

$$
h_i =
\mathrm{Attention}\left(QW_i^Q, KW_i^K, VW_i^V\right),
$$

poi concatena gli output e applica una proiezione finale:

$$
\mathrm{MHA}(Q,K,V)
=
\left[h_1 \mathbin{\|} \cdots \mathbin{\|} h_H\right]W^O.
$$

Le head non vengono sommate direttamente prima di `W^O`. La concatenazione conserva separati i canali prodotti dalle diverse proiezioni fino alla proiezione finale [Vaswani et al., 2017, §3.2.2].

Lo snippet [`code/snip_att_004_multihead_shapes.py`](code/snip_att_004_multihead_shapes.py) esegue `torch.nn.MultiheadAttention` con due head e verifica:

- output `[B, L, E] = [1, 3, 4]`;
- pesi non mediati `[B, H, L, S] = [1, 2, 3, 3]`.

Il capitolo successivo riprenderà il blocco multi-head insieme alle proiezioni, alla concatenazione e a `W^O`.

## 13. Complessità e memoria

Per `Q[L,d_k]`, `K[S,d_k]` e `V[S,d_v]`:

1. `QK^T` richiede ordine `O(LSd_k)` operazioni;
2. `AV` richiede ordine `O(LSd_v)` operazioni;
3. una implementazione che materializza score e pesi conserva tensori intermedi di shape `[L,S]`.

Nel caso di self-attention con `L=S=n`, la dimensione degli intermedi è quadratica in `n`.

Questa descrizione riguarda l'implementazione standard materializzata. FlashAttention riorganizza lo stesso operatore esatto tramite tiling e ricomputazione, riducendo gli accessi alla memoria HBM e senza richiedere la materializzazione completa della matrice `n×n` in HBM [Dao et al., 2022, §§1–3]. Il meccanismo hardware-aware viene differito alla Parte `P12`.

## 14. Proprietà e confini

### Proprietà stabilizzate

- ogni riga di `QK^T` appartiene a una query;
- ogni colonna appartiene a una key;
- la softmax viene applicata lungo le key;
- senza dropout, ogni riga dei pesi è non negativa e somma a 1, se almeno una posizione è ammessa;
- ogni riga di output è una combinazione delle righe di `V`;
- il numero di righe dell'output è `L`;
- la dimensione di ogni riga è `d_v`.

### Cosa non fa il meccanismo base

- non genera da solo informazione posizionale;
- non modifica l'ordine delle righe;
- non introduce dati esterni;
- non decide da solo la correttezza di un contenuto;
- non riduce automaticamente il costo quadratico della matrice degli score;
- non definisce l'intero blocco Transformer.

### Posizione e permutazioni

Se `Q`, `K` e `V` vengono permutati in modo coerente e non contengono segnali posizionali, l'operatore segue la stessa permutazione. Questa proprietà deriva dalle moltiplicazioni matriciali e dalla softmax per riga. Per distinguere l'ordine, il sistema deve inserire informazione posizionale nei dati o nel calcolo.

## 15. Errori comuni

1. **Applicare la softmax sulla dimensione sbagliata.** Per ogni query, la normalizzazione deve avvenire sulle key.
2. **Usare `KQ^T` al posto di `QK^T`.** Le shape e il significato delle righe cambiano.
3. **Applicare la mask a `V`.** La mask modifica gli score o un bias sommato agli score prima della softmax.
4. **Confondere mask booleane tra API diverse.** In PyTorch la semantica di `True` non è uniforme tra `F.scaled_dot_product_attention` e `MultiheadAttention.key_padding_mask`.
5. **Dimenticare il fattore `sqrt(d_k)`.** Si implementa allora dot-product attention non scalata.
6. **Chiamare “pesi” gli score.** I pesi sono il risultato della normalizzazione.
7. **Assumere che i pesi dopo dropout sommino a 1.** Il dropout modifica i coefficienti dopo la softmax.

## 16. Ricostruzione completa

Partiamo da una query `q`, tre key e tre value.

1. `qK^T` produce uno score per key.
2. La divisione per `sqrt(d_k)` ridimensiona i logit.
3. La mask, se presente, rende non ammesse alcune posizioni.
4. La softmax produce coefficienti per la query corrente.
5. I coefficienti combinano le righe di `V`.
6. Ripetendo il calcolo per `L` query otteniamo `O[L,d_v]`.
7. Con più head ripetiamo il meccanismo su proiezioni separate, concateniamo e applichiamo `W^O`.

Ora che abbiamo ottenuto rappresentazioni dipendenti dal contesto, il componente successivo può combinare più head e reintegrare l'output nel blocco Transformer.

## 17. Controlli di comprensione

### Ricostruzione

Partendo da `q`, `K` e `V`, ricostruire l'ordine esatto di score, scaling, mask, softmax e prodotto con `V`.

### Localizzazione

Indicare quale operazione usa `V` per la prima volta.

### Confine

Spiegare perché la mask non deve essere applicata direttamente alle righe di `V`.

### Trasferimento

Ripetere l'esempio sostituendo `q=[0,1]` e prevedere quali key ricevono score maggiore prima di calcolare la softmax.

### Variazione

Prevedere la shape dell'output quando `L=5`, `S=7`, `d_k=64` e `d_v=32`.

## 18. Esercizi

1. Calcolare a mano la seconda riga dei pesi per `q=[0,1]`.
2. Modificare `SNIP-ATT-002` usando `d_v=3` e verificare la nuova shape dell'output.
3. Sostituire la causal mask booleana con una mask additiva contenente `0` e `-inf`.
4. Creare un caso in cui tutte le key producano lo stesso score e spiegare il risultato della softmax.
5. Verificare con un test che una permutazione coerente delle righe permuti coerentemente l'output nel caso senza posizione.

## 19. Fonti primarie

Le schede complete, le sezioni consultate e i limiti sono in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md).

- Vaswani et al., *Attention Is All You Need*, NeurIPS 2017.
- Bahdanau, Cho e Bengio, *Neural Machine Translation by Jointly Learning to Align and Translate*, ICLR 2015 / arXiv.
- Luong, Pham e Manning, *Effective Approaches to Attention-based Neural Machine Translation*, EMNLP 2015.
- Dao et al., *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness*, 2022.

## 20. Documentazione ufficiale

- PyTorch stable `2.13`, `torch.nn.functional.scaled_dot_product_attention`.
- PyTorch stable `2.13`, `torch.nn.MultiheadAttention`.
- PyTorch stable `2.13`, `torch.nn.attention`.

## 21. Artefatti di riproduzione

- ambiente: [`code/environments/python-pytorch.txt`](code/environments/python-pytorch.txt);
- test: [`code/test_attention_snippets.py`](code/test_attention_snippets.py);
- output: [`code/outputs/`](code/outputs/);
- audit codice: [`code/CODE_AUDIT.md`](code/CODE_AUDIT.md);
- audit testo: [`TEXT_AUDIT.md`](TEXT_AUDIT.md);
- claim: [`CLAIMS.md`](CLAIMS.md);
- visuale `ATT-01`: [`candidate-v2.png`](../../assets/chapters/28_attention/ATT-01/candidate-v2.png);
- visuale `ATT-02`: [`candidate-v2.png`](../../assets/chapters/28_attention/ATT-02/candidate-v2.png).

## 22. Registro finale di approvazione

- Review fattuale: completata per la candidatura `0.1.0-rc1`
- Review matematica: completata per la candidatura `0.1.0-rc1`
- Review codice: test locali superati
- Review visuale: `ATT-01` e `ATT-02` validate tecnicamente; approvazione autoriale aperta
- Review didattica: completata internamente, aperta alla revisione dell'autore
- Review autoriale: **aperta**
- Commit congelato: non assegnato
